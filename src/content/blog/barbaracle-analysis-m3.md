---
title: '【ポケモンチャンピオンズ】ガメノデス考察 M-3 使用率79位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率79位のガメノデス。からをやぶる採用率98.1%、インファイト96.0%のメガ進化型アタッカー。ようきメガ型・いじっぱりメガ型の2パターンを型別採用率・技構成・環境ポケモンとの相性を交えて解説。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-barbaracle-m3.png'
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
  <img src="/images/pokemon/pokemon-0689-00.webp" alt="ガメノデス" />
  <div>
    <h2 style="margin:0 0 8px">ガメノデス（メガガメノデス）</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-05-rock.png" alt="いわ" style="width:44px;height:44px" />
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <span style="font-size:0.85rem;color:#666">→ メガ後</span>
      <img src="/images/types/type-05-rock.png" alt="いわ" style="width:44px;height:44px" />
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">79位</strong>　特性: <strong>かたいツメ 92.8%（メガ後も継続）</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/25）時点の集計です

---

## なぜ今ガメノデスが使用率79位なのか

### 理由① からをやぶる採用率98.1%が示す爆発力

ガメノデスの採用理由の最大の柱は、メガ進化と「からをやぶる」の組み合わせによる一撃突破力にあります。メガ進化後のこうげき140・すばやさ88という水準は決して高くありませんが、からをやぶり後はこうげきが実質280相当、すばやさも2段階上昇します。特殊耐久が下がるリスクを負いつつも、相手のタスキやきのみを突破するロックブラスト（66.8%採用）と組み合わせることで、上振れ時の圧倒的な制圧力が環境に刺さっています。

### 理由② メガ後かくとうタイプが生む技範囲の広さ

通常時はいわ/みずタイプですが、メガ進化でいわ/かくとうに変化します。これによりインファイト（96.0%採用）がタイプ一致になり、はがね・いわ・こおり・あく・ノーマルを等倍以上で叩けます。じしん（46.2%）やアクアブレイク（30.2%）を組み合わせると、1体で幅広い範囲をカバーでき、選出段階から相手に圧力をかけられます。

### 理由③ 特性かたいツメ×ガメノデスナイトほぼ固定の読みやすさと安定感

持ち物はガメノデスナイトが大多数（DBに他の持ち物の合計記録が約2.8%にとどまるため、残差の大部分がガメノデスナイト使用と推定）、特性はかたいツメ92.8%と採用率がほぼ集中しています。型の読みやすさはデメリットにも見えますが、逆に言えばプレイヤーが迷わず最適択を選べる安定感の高さを示しています。型が絞られているため立ち回りの再現性が高く、構築に組み込みやすいのがランクマッチで一定の使用率を確保する理由となっています。

---

## 基本スペック

### 種族値（メガ進化後）

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">72</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:70%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">140</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+35</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+15</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">64</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:53%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">106</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:44%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">88</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

（メガ前: HP72 / A105 / B115 / C54 / D86 / S68 / 合計500）

### タイプ・弱点（メガ進化後: いわ/かくとう）

<div class="type-row">
  <strong>タイプ（メガ後）：</strong>
  <img src="/images/types/type-05-rock.png" alt="いわ" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="いわ" />
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="かくとう" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なし</td>
</tr>
</tbody>
</table>
</div>

メガ進化後はいわ/かくとうの複合となり弱点が7タイプと多い点が最大のネック。特にくさ（×2）・みず（×2）・じめん（×2）・エスパー（×2）・フェアリー（×2）は環境上位ポケモンが広く持つ技タイプで、からをやぶり前に削られると役割を果たせません。一方、ノーマル・いわ・あく・むし・ほのお・どくへの耐性は立ち回りで活かせる場面もあります。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center;width:40px">順位</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>からをやぶる</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">98.1%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>インファイト</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">96.0%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ロックブラスト</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">25</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">66.8%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じしん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">100</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">46.2%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>アクアブレイク</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">85</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">30.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>シャドークロー</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">70</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">15.9%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>いわなだれ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10.6%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ストーンエッジ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">100</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10.2%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくづき</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>つじぎり</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">70</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4.4%</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

### 型1: ようきメガ型（採用率53.7%）

**性格採用率: ようき 53.7%**（S重視型の指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0689-00.webp" alt="ガメノデス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ようきメガガメノデス</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かたいツメ（92.8%）※メガ後も継続<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（採用率43.2%）<br>
<strong>持ち物:</strong> ガメノデスナイト
</div>
<div>
<strong>技構成:</strong><br>
・からをやぶる（98.1%）<br>
・インファイト（96.0%）<br>
・ロックブラスト（66.8%）<br>
・じしん（46.2%）
</div>
</div>
</div>

**強み:**

いじっぱり型と比べてからをやぶり前の素すばやさが高く、メガ進化時点で抜ける相手の範囲が広がります。メガ後S実数値はようき（EV32）で154、いじっぱり（EV32）で140。S実数値149のおくびょうS32サーフゴー（23位）はようき154なら上から動けますが、いじっぱり140では先手を取れません。からをやぶり前に行動を許される確率が下がるため、いじっぱり型では先に動かれて崩されるケースを減らせます。

**弱み:**

こうげき補正がないため、いじっぱり型と比較してインファイトの最大火力がやや落ちます。ぼうぎょの高い相手（ブリジュラス等のはがね）に対しては確定数がずれるケースがあり、からをやぶり1回では押し切れない場面が出ます。

---

### 型2: いじっぱりメガ型（採用率44.2%）

**性格採用率: いじっぱり 44.2%**（火力重視型の指標）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0689-00.webp" alt="ガメノデス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いじっぱりメガガメノデス</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かたいツメ（92.8%）※メガ後も継続<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H10-A32-S24（採用率18.5%）<br>
<strong>持ち物:</strong> ガメノデスナイト
</div>
<div>
<strong>技構成:</strong><br>
・からをやぶる（98.1%）<br>
・インファイト（96.0%）<br>
・ロックブラスト（66.8%）<br>
・<span style="color:#1d4ed8">じしん46.2% / アクアブレイク30.2%</span>
</div>
</div>
</div>

**強み:**

ようき型よりこうげき実数値が約10%高く、ようき型では2発になる耐久ラインの相手をからをやぶり後の一致技で1発圏内に入れられます。ロックブラストはタスキやきのみを貫通し、上振れ時は一掃を狙えます。S24止まりでもからをやぶり後の上昇で多くの相手を抜けるため、火力を取りつつ最低限の素早さを確保する構成です。

**弱み:**

からをやぶり前の素早さがようき型より低いぶん、メガ進化直後に相手に先制される機会が増え、からをやぶりを通す前に削られるリスクが高くなります。

---

## 環境ポケモンへの相性分析

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
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ドラゴンにインファイト・じしんがともに×2。からをやぶりを通せれば一致技で押し切れます。ぼうぎょが高いためいじっぱり型のほうが確定数で勝りやすいです</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく/はがねにインファイト×4。S実数値は最多型（H32-A32-S2）で71にとどまり、こちらのいじっぱり140を大きく下回るため、からをやぶり前でも両型で先手を取れます。ふいうち（あく×0.5）・ドゲザン（あく×0.5）は半減できますが、アイアンヘッド（はがね）はメガ後のこちらに×2の弱点を突かれます。先手インファイトで倒し切れるかが勝負の分かれ目です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト・じしんともガブリアスに等倍。からをやぶり後なら上から押せますが、ガブリアス側のじしんはメガ後に×2弱点で、先に動かれると大ダメージを受けます。対面性能は拮抗しています</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう技はゴースト/フェアリーに無効でインファイトが通りません。じゃれつく（95.4%）がメガ後の×2弱点を突き、化けの皮でからをやぶりも凌がれます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ技がメガ後の×2弱点。トリックフラワー（98.2%）・トリプルアクセル（89.1%）を高い素早さから先に通され、からをやぶり前に崩されやすいです</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0398-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ムクホーク（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いかく（96.8%）でこうげきを1段階下げられ、ブレイブバード（91.4%）で高い打点を受けます。かくとう技はノーマル/ひこうに等倍止まりで、有効打に欠けます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0260-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ラグラージ（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト・じしん・アクアブレイクいずれもみず/じめんに等倍止まりで決定打に乏しいです。ラグラージのじしんはメガ後の×2弱点を突くため、撃ち合いで不利です</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ガメノデスが苦手なミミッキュ・マスカーニャにじしん・げきりんで対応でき、ガメノデスのくさ弱点を別軸で補完します。物理2枚で先発択を散らせます</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0861-00.webp" alt="オーロンゲ">
    <div class="name">オーロンゲ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">いたずらごころによるおいかぜやでんじは等のサポートで、ガメノデスがからをやぶりを安全に展開できる状況を作れます。うそなき等のサポートも相性が良いです</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0660-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">あくびや砂あらしでゲームテンポを落としながら展開する役割を担います。砂ダメージで相手のきあいのタスキを削れるため、ガメノデスのからをやぶり後の攻撃が通りやすくなります</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="キュウコン">
    <div class="name">アローラキュウコン</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">オーロラベールやおいかぜでガメノデスがからをやぶりを通しやすい状況を整えます。こおり・フェアリー技でガメノデスが苦手なマスカーニャに圧力をかけられます</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき技でガメノデスが重いみず・ひこうを牽制し、はがねの高耐久で受け回しを担います。ガメノデスの×2弱点であるくさをブリジュラスは半減で受けられる補完関係です</div>
  </div>
</div>

**パーティ構成の基本方針:**

ガメノデスは「からをやぶる」を通す前提で動くため、展開サポートをしてくれるポケモンとの相性が特に重要になります。

---

## データ分析①：からをやぶる採用率と性格分布から読む最適解

M-3データでからをやぶる採用率は98.1%に達しており、実質ほぼ全ての個体で採用されています。性格はようき53.7%・いじっぱり44.2%と拮抗しつつもようきがわずかに多数派で、プレイヤーの間でも「素早さ重視か火力重視か」の議論が続いていることが数値にも表れています。

EV振りで最も多い「H2-A32-S32」（43.2%）は、こうげきとすばやさに最大投資しつつHPに2を割くパターンです。からをやぶり前後の素早さラインを最大化する構成で、多数派のようき性格と組み合わせて採用される傾向があります。次点の「H10-A32-S24」（18.5%）は、すばやさを少し削ってHP耐久を厚くした配分で、火力を確保するいじっぱり型と相性が良いです。

特性かたいツメ（92.8%）の圧倒的な採用率は、ロックブラスト・インファイト等の接触技の火力を上乗せする目的が主で、スナイパー（5.0%）は連続技の急所狙いを重視する少数派にとどまります。

---

**総評:**

ガメノデスはメガ進化後のからをやぶりを通せるかどうかがすべての鍵になります。多数派のようき型（53.7%）はからをやぶり前後の素早さを最大化して行動保証を優先し、いじっぱり型（44.2%）はこうげき実数値で約10%上回り、ようき型では2発の相手を1発圏内に入れる火力で勝負します。どちらも技構成はからをやぶる・インファイト・ロックブラストがほぼ固定で、4枠目のじしん（46.2%）かアクアブレイク（30.2%）の選択で対応範囲が変わります。

苦手なミミッキュ（かくとう無効）・マスカーニャ（くさ×2）には選出段階で割り切り、ガブリアスやブリジュラスといった同居率上位のサポート役でからをやぶりを安全に展開できる構築に組み込むことで、使用率79位のポテンシャルを引き出せるポケモンといえます。

---

## 関連記事

- [【ポケモンチャンピオンズ】ムクホーク考察 M-3 使用率7位](/blog/staraptor-analysis-m3/)
- [【ポケモンチャンピオンズ】メガメタグロス考察 M-3 使用率6位](/blog/metagross-analysis-m3/)