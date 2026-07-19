---
title: '【ポケモンチャンピオンズ】アーマーガア 考察 M-4 シーズン てっぺき・ボディプレス型の受け性能'
description: 'M-4シーズン使用率14位のアーマーガア考察。てっぺき64.2%・ボディプレス66.8%の受け型を中心に、EV H32-B32わんぱく72.7%の実数値とほのお・でんき弱点への対策を分析します。'
pubDate: '2026-07-18'
updatedDate: '2026-07-18'
heroImage: '../../assets/hero-corviknight-m4.png'
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
  <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" />
  <div>
    <h2 style="margin:0 0 8px">アーマーガア</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">14位</strong>　特性: <strong>プレッシャー 66.8%</strong>
    </div>
  </div>
</div>

M-4シーズン、アーマーガアは使用率14位につけています。ひこう/はがねの複合タイプで、B105・H98の耐久を土台にてっぺき（64.2%）とボディプレス（66.8%）を組み合わせた受け型が主流です。はねやすめ（98.4%）ととんぼがえり（67.0%）を軸に、長期戦での回復と対面操作を両立させる構築が中心になっています。

---

## アーマーガアの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:49%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">98</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:44%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">87</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:53%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:27%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">53</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:34%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">67</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">495</span>
  </div>
</div>

H98・B105・D85と、物理・特殊の両面である程度の耐久を持つバランス型の種族値です。A87はてっぺきで補うボディプレス運用を前提にした数値で、素の攻撃力はさほど高くありません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はほのお・でんきの2タイプ（いずれも×2）のみに絞られており、耐性は6タイプ・無効2タイプと広く受けやすい配分です。特にじめん無効は環境1位のガブリアスのじしんを完全に無効化できる強みです。一方でこおり・かくとうはいずれも等倍（弱点でも耐性でもない）で、こおり技を持つ相手には打点を通されます。

### 特性

<strong>プレッシャー</strong>（66.8%）は相手の技のPP消費を通常の1から2に増やす特性で、はねやすめによる長期戦でPP切れを誘発しやすくします。次点の<strong>ミラーアーマー</strong>（31.8%）は自分が受ける能力ダウン効果を相手に跳ね返す特性で、なきごえ等の能力ダウン技を撃たれた場合に相手の能力を下げ返せます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの1/2回復。使用ターンはひこうタイプでなくなり、じめん技を受けられる点に注意</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">67.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代。対面操作しながら後続に負担をかける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボディプレス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">66.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげきでなくぼうぎょ実数値でダメージ計算。てっぺきと組み合わせて打点にする物理技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっぺき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">64.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分のぼうぎょを2段階上昇。ボディプレスの打点を伸ばす積み技。とくぼうは強化しない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>45.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20%でひるみ。ビルドアップ型のA基準打点。フェアリー・こおりへの一致技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ビルドアップ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分のこうげき・ぼうぎょを各1段階上昇。アイアンヘッドの物理打点を底上げ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ブレイブバード</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">与ダメージの1/3を反動で受ける高火力ひこう技。かくとう・むしへの一致打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きりばらい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の回避率を下げつつ、リフレクター等の設置技を解除する補助技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を変化技封じ状態にする。てっぺき・積み技持ちの相手を機能停止させる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つけあがる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20+</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の能力上昇段階に応じて威力上昇。てっぺき後に撃つと威力が伸びる高火力技になる（アーマーガアはあくタイプを持たずタイプ一致は乗らない）</td>
</tr>
</tbody>
</table>
</div>

---

## M-4の採用型

### 型1：てっぺき・ボディプレスの受け型（わんぱく 72.7%）

**性格採用率: わんぱく 72.7%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:48px;height:48px">
  <strong style="font-size:1.05em">てっぺき・ボディプレスの受け型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> プレッシャー（66.8%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32-B32（最多EV分布43.5%）<br>
<strong>持ち物:</strong> たべのこし（50.8%）
</div>
<div>
<strong>技構成:</strong><br>
・てっぺき<br>
・ボディプレス<br>
・とんぼがえり<br>
・はねやすめ
</div>
</div>
</div>

てっぺき（はがね・積み技）でぼうぎょを2段階上げ、その実数値をそのまま攻撃値として使うボディプレス（かくとう・威力80）で打点に変換する型です。実数値はH205 / A107 / B172 / C65 / D107 / S87（EV H32-B32・わんぱく）で、てっぺき使用後のBは実質344まで伸びます。かくとうタイプはアーマーガアの一致技ではないため、ボディプレスに一致補正はかかりません。

わんぱく（B↑C↓）のEV配分でもD85は種族値のまま強化されないため、ほのお・でんきの特殊技への耐性は変わりません。とんぼがえり（むし・威力70）で後続に負担をかけつつ交代し、はねやすめで積んだ耐久を維持する運用が中心です。

**強み:**

てっぺき1回でボディプレスの打点がB172→344相当まで伸び、乱数の発数を大きく縮められます。カバルドン（H215・B187、EV H32-B32わんぱく想定）へのボディプレスは、てっぺき前が28〜34ダメ（H215の13〜16%）にとどまるのに対し、てっぺき後は56〜66ダメ（26〜31%）まで伸びます。

**弱み:**

てっぺきは自分の物理防御しか上げないため、ほのお・でんきの特殊技には無防備なままです。かえんほうしゃ等の特殊ほのお技を持つ相手には、積む前後でダメージ量が変わりません。

---

### 型2：ビルドアップ・アイアンヘッド型（わんぱく 72.7%）

**性格採用率: わんぱく 72.7%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ビルドアップ・アイアンヘッド型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> プレッシャー（66.8%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32-B32（最多EV分布43.5%）<br>
<strong>持ち物:</strong> オボンのみ（43.2%）
</div>
<div>
<strong>技構成:</strong><br>
・ビルドアップ<br>
・アイアンヘッド<br>
・とんぼがえり<br>
・はねやすめ
</div>
</div>
</div>

ビルドアップ（かくとう・積み技、A・Bを各1段階上昇）でアイアンヘッド（はがね・威力80・怯み効果）の打点を伸ばす型です。てっぺき型がボディプレス1本にBを全振りするのに対し、ビルドアップはAとBを同時に強化するため、アイアンヘッドという通常の物理技（攻撃側はA基準）で火力を出せる点が異なります。

**強み:**

ビルドアップはA・Bを同時に1段階ずつ上げるため、てっぺき型では使えないアイアンヘッドを主力打点にできます。アイアンヘッドの追加効果（怯み30%）は、てっぺき型のボディプレスにはない交代誘導の圧力になります。

**弱み:**

てっぺき（B+2段階）に対しビルドアップはB+1段階にとどまるため、1回の積みで到達する耐久値はてっぺき型より低くなります。

---

## データ分析①：M-3→M-4 技採用率の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">96.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>98.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">≒同</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボディプレス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">82.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>66.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626"><strong>-15.8pp</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっぺき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">72.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>64.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626"><strong>-8.6pp</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>67.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+6.8pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>45.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a"><strong>+17.9pp</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ビルドアップ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>26.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a"><strong>+17.6pp</strong></td>
</tr>
</tbody>
</table>
</div>

M-3の時点で既にてっぺき（72.8%）・とんぼがえり（60.2%）は主流技として定着しており、M-4で新たに現れた技ではありません。M-4での変化は「てっぺき・ボディプレスの受け型」の中の配分交代と、対抗型の台頭の2つです。ボディプレス（82.6%→66.8%、-15.8pp）とてっぺき（72.8%→64.2%、-8.6pp）がともに下げた一方、**アイアンヘッド（27.3%→45.2%、+17.9pp）とビルドアップ（8.4%→26.0%、+17.6pp）が大きく伸び**、てっぺき・ボディプレス型と並ぶビルドアップ・アイアンヘッド型（型2）が二番手として明確に定着しています。性格はわんぱく採用率66.0%→72.7%（+6.7pp）で、受け型としての方向性自体はM-3から変わっていません。

---

## 苦手なポケモン

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
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY（Yナイト65.3%）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（ほのお・特殊・採用率42.5%）が×2弱点。メガ後種族値C159・ひかえめ想定でC実数値232となり、D107に確定1発が入ります。てっぺきで積んでも耐性は変わりません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">バシャーモ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（ほのお・物理・採用率84.7%）が×2弱点。物理技のためてっぺき型はある程度耐えられますが、反動を受けてもバシャーモ側が押し切れる火力です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんじほう（でんき・特殊・威力120・採用率96.6%）が×2弱点。特殊技のためてっぺき・ビルドアップのどちらの積みも防御に寄与しません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき・特殊・採用率55.3%）が×2弱点。ボルトチェンジ（採用率90.6%）で打点を出しながら後続に交代できるため、対面で押し込まれやすい相手です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアソング（ほのお・特殊・採用率99.1%）が×2弱点でほぼ確定採用。おにび（採用率85.1%）でやけどを負わされると物理型の打点まで落ちます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でアーマーガアと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0939-00.webp" alt="ハラバリー" loading="lazy">
    <div class="name">ハラバリー</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0121-00.webp" alt="スターミー" loading="lazy">
    <div class="name">スターミー</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" loading="lazy">
    <div class="name">ゲンガー</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0503-00.webp" alt="ダイケンキ" loading="lazy">
    <div class="name">ダイケンキ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0547-00.webp" alt="エルフーン" loading="lazy">
    <div class="name">エルフーン</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" loading="lazy">
    <div class="name">バシャーモ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

同居率上位10体のうち、スターミー（3位）・ダイケンキ（5位）・アシレーヌ（9位）の3体がみずタイプです。みずタイプはほのお技を半減で受けられるため、アーマーガアの弱点であるほのおをこれらのパートナーが処理し、アーマーガアはみずタイプが苦手とするくさを耐性（×0.25）でカバーする役割分担になっています。

ガブリアス（1位）はドラゴン/じめんで、でんきタイプを無効化できます。アーマーガアのでんき弱点をガブリアスが受け持つ一方、ガブリアスの弱点であるフェアリー・ドラゴンはアーマーガアが耐性（いずれも×0.5）で受けられ、互いの弱点を補い合う関係です。

ゲンガー（4位）はゴースト/どくで、アーマーガアのとんぼがえりによる対面操作からゴーストタイプの特殊技を通す運用に向きます。ミミッキュ（6位）も同様にゴースト/フェアリーの打点をとんぼがえりの後続として運用しやすい組み合わせです。

---

## まとめ

M-4のアーマーガアは使用率14位で、てっぺき・ボディプレスの受け型を中心に採用されています。

- **てっぺき（64.2%）・ボディプレス（66.8%）の組み合わせが主流です**：Bを2段階積み、その実数値をそのままボディプレスの攻撃値に変換する物理アタッカー兼受けの型です
- **ビルドアップ（26.0%）・アイアンヘッド（45.2%）型も一定数存在します**：A・Bを同時に強化し、通常の物理技であるアイアンヘッドで打点を出す型です
- **てっぺきはD（種族値85）を強化しません**：環境上位のほのお・でんき技の多くは特殊技のため、積んでも被ダメージは変わりません

はねやすめ（98.4%）とんぼがえり（67.0%）を軸にした対面操作と回復の安定感が基本性能である一方、ほのお・でんきの2弱点はいずれも特殊技として撃たれることが多く、B特化の受け型では根本的な対策にならない点は運用上の制約になります。

---

*関連記事：[ガブリアス考察 M-4](/blog/garchomp-analysis-m4/)*

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/corviknight/)**
