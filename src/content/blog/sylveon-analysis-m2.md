---
title: '【ポケモンチャンピオンズ】ニンフィア考察 M-2 使用率40位 ハイパーボイス型の採用率と立ち回り'
description: 'M-2シングルバトルで使用率40位のニンフィアを徹底分析。フェアリースキンで実質威力108になるハイパーボイス、あくび＋まもるの起点作り、HB/HC耐久型の構築を解説。とくぼう130を活かした特殊受けの立ち回りと苦手なはがね対策まで実データで紹介します。'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-sylveon-m2.png'
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
  <img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" />
  <div>
    <h2 style="margin:0 0 8px">ニンフィア</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">40位</strong>　特性: <strong>フェアリースキン 98.6%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ニンフィアは**使用率40位**を記録しました。特性は**フェアリースキン**が98.6%を占め、ほぼ全ての個体がこれを採用しています。

ニンフィアの核は、特性**フェアリースキン**で強化したハイパーボイス（採用率96.9%）です。フェアリースキンはノーマル技をフェアリータイプに変え、さらに威力を1.2倍します。とくこう110と合わせ、ドラゴンを無効化しつつ高威力の一致技を毎ターン安定して撃てるのが持ち味です。さらにとくぼう130という高い特殊耐久を背景に、あくび・ねがいごとで起点を作る耐久型として運用されます。

---

## なぜM-2でニンフィアが使われるのか

### 1. フェアリースキンのハイパーボイスが主力

ニンフィアの最大の特徴は**特性フェアリースキン**です。ノーマル技がフェアリータイプに変化し、威力が1.2倍になります。ハイパーボイス（基礎威力90）はフェアリー技として扱われ、タイプ一致補正×1.5とフェアリースキンの×1.2が乗って**実質威力162相当**になります。

フェアリー技はドラゴン・かくとう・あくに×2で通ります。M-2で使用率1位のガブリアス（ドラゴン/じめん）、16位カイリュー（ドラゴン/ひこう）、21位サザンドラ（あく/ドラゴン）はいずれもドラゴン複合で、ニンフィアのドラゴン無効と合わせて相性面で優位を取りやすい相手です。

ハイパーボイスは音技のため、まもる・みがわりを貫通する点も安定打点として機能します。

### 2. とくぼう130を活かした特殊受け

ニンフィアのとくぼう種族値は**130**で、HP95と合わせて特殊方面の耐久が高水準です。性格はひかえめ54.6%に次いでずぶとい23.3%が採用され、EVもHB（HP・ぼうぎょ）振りが上位を占めます。これは、ひかえめでハイパーボイスの火力を確保する攻撃型と、ずぶといで物理にも厚くする耐久型に運用が分かれていることを示します。

あくび（採用率67.5%）で相手に眠りを迫って交代を誘い、ねがいごと（25.8%）で自身や後続を回復する、起点作り兼クッションの動きが基本になります。

### 3. ドラゴンを無効化できる安定した受け先

フェアリー単タイプはドラゴン技を無効化します。ガブリアスのげきりん（採用率47.9%）、サザンドラのりゅうせいぐん（90.2%）、ブリジュラスのりゅうせいぐん（64.8%）といった環境上位のドラゴン技を受け切れるため、ドラゴンアタッカーへの後出しが利きます。ただし後述の通り、これらの相手はドラゴン以外の技でニンフィアを攻撃できるため、無効化＝完封ではない点に注意が必要です。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
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
      <div style="width:65%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">525</span>
  </div>
</div>

とくこう110・とくぼう130に種族値が集中した特殊耐久型です。すばやさ60は低く、環境上位の大半より遅いため、上から殴る役割ではなく**受けて起点を作る**のが基本になります。ぼうぎょ65は低めですが、ずぶとい＋HB振りで補強する型が23.3%採用されています。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="フェアリー" />
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
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン
  </td>
</tr>
</tbody>
</table>
</div>

弱点はどく・はがねの2タイプのみで、かくとう・むし・あくを半減し、ドラゴンを無効化します。受けやすいタイプが多い一方、環境に多いはがねアタッカー（ブリジュラス2位・アーマーガア6位・ハッサム14位・ギルガルド11位・ドドゲザン24位）には弱点を突かれるため、はがね対面が明確な弱点になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ハイパーボイス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90→108（フェアリー）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリースキンでフェアリー化＋威力1.2倍。音技でまもる・みがわり貫通</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">67.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">次のターン終了時に眠らせる。交代を誘う起点作り（変化技のためフェアリースキンの対象外）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>でんこうせっか</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40→48（フェアリー）先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>57.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリースキンでフェアリー化。優先度+1で相手のSに関わらず先制。低耐久の削り残し処理に</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マジカルフレイム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>57.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のCを1段階下げる。弱点のはがね（ハッサム・ギルガルド等）への打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくびの眠り誘発・たべのこし回復との相性が良い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねがいごと</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">次のターン終了時に最大HPの半分回復。自身や後続の継戦サポート</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>めいそう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">C・Dを1段階アップ。とくぼう130をさらに伸ばし特殊受け＋積みアタッカー化</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はかいこうせん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">150→180（フェアリー）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリースキンでフェアリー化＋威力1.2倍。撃った次ターンは行動不可</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリーが半減のソウブレイズ・ラウドボーン等ほのお/ゴーストに、ゴースト×2で刺さる打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ミストフィールド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">地上の味方を状態異常から守り、ドラゴン技の威力を半減</td>
</tr>
</tbody>
</table>
</div>

ハイパーボイス・あくび・マジカルフレイムが採用率上位で、これにまもる／ねがいごと／でんこうせっかを組み合わせる構成が主流です。マジカルフレイム（採用率57.0%）は弱点のはがねへの貴重な打点で、相手のCを下げる効果も特殊受けと噛み合います。

---

## 主要型の解説

型①・型②のEV配分は実データのEVスプレッド（HB／HC）を指標としています。

### 型1: HB特殊受け型（最多構成）

**EV採用率: HB系 合計約45%**（HB無振り23.8%＋HB調整型の合算。EVスプレッド上位を占める）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HBずぶとい受け型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> フェアリースキン（98.6%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32 B32（HB振り。余りをDかSに2）<br>
<strong>持ち物:</strong> たべのこし / ようせいのハネ
</div>
<div>
<strong>技構成:</strong><br>
・ハイパーボイス<br>
・あくび<br>
・まもる / ねがいごと<br>
・マジカルフレイム
</div>
</div>
</div>

**強み:**

ずぶとい＋HB振りで物理方面の隙を埋め、元々高いとくぼう130と合わせて両受けを成立させます。あくびで相手の交代を誘い、まもる＋たべのこしで居座りながら数的アドバンテージを取るのがこの型の主眼です。ハイパーボイスはまもる・みがわりを貫通するため、起点回避の交代先にも安定して打点を残せます。

ひかえめ型と比べてハイパーボイスの火力は落ちますが、物理アタッカーの的にならず、ガブリアスのげきりん・スケイルショット（物理ドラゴン技）を無効化しながら居座れる安定性が上回ります。

**弱み:**

A65のためあくびで居座っても削りが甘く、まもる・あくびのループ中にステルスロック（ガブリアス採用率50.7%）やこだわり技で押し切られると突破されます。とくにはがねアタッカーには弱点を突かれて受けが成立しません。

---

### 型2: HC攻撃型（火力重視）

**EV採用率: HC系 合計約24%**（HC無振り15.9%＋HCS振り8.5%等の合算。性格はひかえめ54.6%が指標）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HCひかえめ攻撃型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> フェアリースキン（98.6%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H32 C32（HC振り。余りをSに2）<br>
<strong>持ち物:</strong> たべのこし / オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・ハイパーボイス<br>
・マジカルフレイム<br>
・でんこうせっか / シャドーボール<br>
・あくび / めいそう
</div>
</div>
</div>

**強み:**

ひかえめC32でとくこう110を最大化し、フェアリースキン＋一致補正で実質威力162相当になるハイパーボイスの火力を上げる型です。HB型がA65で削り不足になりやすいのに対し、こちらはドラゴン・あく・かくとうの環境上位を一致技で大きく削れます。マジカルフレイムで弱点のはがねにも打点を持てるため、受けに回らず攻撃でアドバンテージを取りに行けます。

すばやさ60と遅いため、削り残しはでんこうせっか（フェアリースキンでフェアリー化・優先度+1）で先制処理でき、相手のすばやさに関わらず詰められます。

**弱み:**

HB型と比べてぼうぎょに振らないため物理を受けにくく、A65・S60と攻撃性能と素早さは中途半端です。上から殴る役割は担えず、低耐久を上から叩かれると一方的に倒されます。S60のまま運用するのが基本で、削り残しはでんこうせっかの先制に頼る点が攻撃型としての上限になります。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位（TOP30目安）のうち、ニンフィアと相性がはっきり出るポケモンを有利・不利の両面から挙げます。フェアリー単タイプはドラゴン無効・かくとう/あく/むし半減で受けが利く一方、どく・はがねが×2弱点で、すばやさ60の低さから上から殴られやすい点に注意してください。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">げきりん（48%）・スケイルショット（34%）を無効化、ハイパーボイスが×2。ただしじしん（99%）は等倍で通り、低Bでは2発耐えが厳しいため受けっぱなしは不可。どくづき（19%）を持つ個体にはどく×2弱点を突かれる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく・ドラゴン複合にハイパーボイスが×4（あく2×ドラゴン2）。主力のあくのはどう（99%）は半減、りゅうせいぐん（90%）は無効。ただしS98でこちらが後手、かえんほうしゃ（67%）は等倍で通る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン技を無効化、ハイパーボイスが×2（ドラゴン2×ひこう1）。ただしS80でこちらが後手、しんそく（46%・先制）やじしん（15%）等の非ドラゴン技での削りには注意</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利（先手に注意）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ/あくにハイパーボイスが×2（くさ1×あく2）。あく技は半減で受けやすい。ただしS123で先手を取られ、トリックフラワー等で先に削られる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト/どくで、ヘドロウェーブ（82%）がどく×2弱点。S110で先手を取られ、こちらのフェアリーはどく半減で½止まり（フェアリー0.5×ゴースト1）と決定打にならない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ドラゴンでハイパーボイスは等倍止まり（はがね0.5×ドラゴン2）。ラスターカノン（56%）がはがね×2弱点で、りゅうせいぐんは無効だがはがね・でんき技で受け負ける</td>
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
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく/はがねでハイパーボイスは等倍止まり（あく2×はがね0.5）。アイアンヘッド（87%）がはがね×2弱点で、A65のニンフィアでは等倍打点では落とし切れない。先制技ふいうち（99%・あく半減）で削られながら起点にされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マジカルフレイム（ほのお×2）で弱点を突くか、じめん・かくとう技を持つポケモンを同伴して後出しで処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">むし/はがねでハイパーボイス半減、バレットパンチ（100%）がはがね×2の先制技でA65の削り合いに勝てない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マジカルフレイム（ほのお×4：むし2×はがね2）で確実に弱点を突く。落とせない個体には、ほのお・ひこうタイプを同伴して後続から処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト/どくでヘドロウェーブ（82%）がどく×2弱点。S110で先手を取られ、こちらの一致技はどく半減で½止まり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんこうせっか（先制）で削った後に処理するか、ドドゲザン等のあくタイプ（ゴースト技を半減）を同伴してシャドーボールを受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ドラゴンでハイパーボイスは等倍止まり（はがね0.5×ドラゴン2）。ラスターカノン（56%）・10まんボルト（67%）で削られ、ラスターカノンははがね×2弱点</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ニンフィアの技は等倍以下しか入らない（マジカルフレイムもほのお×ドラゴンで等倍）。じめん・かくとう技を持つアタッカーを後出しで合わせて処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガY（ほのお/ひこう）にはフェアリー½止まり、メガX（ほのお/ドラゴン）でも等倍止まり。S100で先手を取られ、ほのお技で上から撃ち返されて火力負けする</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ・みず・でんきタイプを同伴してリザードンに後出しし、弱点を突いて処理する</td>
</tr>
</tbody>
</table>
</div>

選定基準：使用率TOP30から、ニンフィアの一致技が等倍以下に抑えられる相手、または弱点（どく・はがね）を突いてくる主力技を採用率上位で持つ相手を抽出しています。

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0571-01.webp" alt="ゾロアーク(ヒスイ)">
    <div class="name">ゾロアーク(ヒスイ)</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ノーマル/ゴーストの高速特殊アタッカー。ニンフィアが遅い分の上からの打点を補う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0752-00.webp" alt="オニシズクモ">
    <div class="name">オニシズクモ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/むしの高耐久。ニンフィアが苦手なほのお・はがねに後出ししやすい</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じしんでニンフィアの弱点どく・はがねに上から打点。ステロ展開で起点作りを補強</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ひこうでほのお・じめんを呼びにくく、ニンフィアの苦手な物理にいかくで対応</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお打点でニンフィアが苦手なはがね（ハッサム等）を上から処理</div>
  </div>
</div>

**パーティ構成の基本方針:**

ニンフィアはすばやさ60と低く、はがね・どくに弱点を持つため、残り5体で以下を補います。

1. **はがね対策**: ほのお・じめん・かくとう技を持つアタッカー（リザードン・ガブリアス等）で、ハッサム・ブリジュラス等を上から処理する枠
2. **どく対策**: じめん技でゲンガー等を上から叩く枠
3. **高速アタッカー**: ゾロアーク(ヒスイ)等でニンフィアの遅さを補い、削り残しを処理する枠
4. **起点活用**: あくびで誘った交代に合わせて積みや展開を通すエース

---

## データ分析①：フェアリースキン補正で変わる実質威力

ニンフィアが採用するノーマル技を、フェアリースキン1.2倍×一致補正1.5倍を乗せた実質威力で横並びにすると、どの技がどの役割を担うかが見えてきます。

| 技 | 基本威力 | スキン1.2倍後 | 一致補正×1.5込み | 通常フェアリー技との差 |
|---|---|---|---|---|
| ハイパーボイス | 90 | 108 | **162相当** | ムーンフォース（95）一致補正142相当より+14% |
| でんこうせっか | 40 | 48 | **72相当** | — |
| はかいこうせん | 150 | 180 | **270相当** | — |

ニンフィアはフェアリー専用技を覚えにくいため、フェアリースキンは「ノーマル技を高威力のフェアリー一致技に変換する」役割を担います。注目すべきは**でんこうせっか**で、本来威力40の先制技がフェアリー化＋1.2倍で実質威力72相当になり、しかもドラゴン・あく・かくとうに×2で通ります。ただしでんこうせっかは物理技でA65依存のため、C110で撃つハイパーボイスと同じ威力値でも実ダメージははるかに小さく、役割は「相手のすばやさに関わらず通る削り残しの処理・低耐久アタッカーへの先制点」に限られます（採用率57.5%）。

主力のハイパーボイス（実質162相当・採用率96.9%）に目が行きますが、フェアリースキンの本質は「フェアリー技を覚えにくいニンフィアに、音技かつ先制技という別軸の打点を一致技として与える」点にあります。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">EV指標</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HB特殊受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">HB系 約45%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ハイパーボイス・あくび・まもる・マジカルフレイム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">両受け＋起点作り。ドラゴン無効で居座れる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A65で削り不足。はがね対面は不成立</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HC攻撃型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HC系 約24%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ハイパーボイス・マジカルフレイム・でんこうせっか・あくび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C110で一致技の火力最大。先制技で詰め可</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理を受けにくい。S60で上から殴られる</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ニンフィアはフェアリースキンのハイパーボイスと、とくぼう130・ドラゴン無効を軸にした特殊受け兼起点作りのポケモンです。ガブリアス・サザンドラ・カイリューといったドラゴン複合の環境上位に強く、あくびで交代を誘って数的有利を作る動きが持ち味です。

一方、すばやさ60の遅さとはがね・どくの弱点が明確な課題で、ブリジュラス・ハッサム・ドドゲザン等のはがねアタッカーやゲンガーには受けが成立しません。マジカルフレイム（採用率57.0%）で弱点のはがねに最低限の打点を持ちつつ、はがね・どくを処理できるアタッカーをパーティに添えて弱点を補完するのが、使用率40位のニンフィアを活かす鍵になります。

---

## 関連記事

- [天敵となるはがね/ドラゴン ブリジュラスのM-2考察](/blog/archaludon-analysis-m2/)
- [同じフェアリーアタッカー フラエッテのM-2考察](/blog/florette-analysis-m2/)
- [ドラゴン無効で受けやすい使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
