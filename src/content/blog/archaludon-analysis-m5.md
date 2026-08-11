---
title: '【ポケモンチャンピオンズ】ブリジュラス 考察 M-5 シーズン 使用率3位・ずぶとい耐久型の増加'
description: 'M-5シングルバトルで使用率3位に浮上したブリジュラスを分析。M-4（2026-07-13時点）と比べてずぶとい性格が15.7%→17.6%、ピントレンズが5.1%→7.1%へ増加する一方、こだわりスカーフ型はやや減少。技・持ち物・性格・EV分布のM-4比較と型別解説、主要ポケモンとの相性をデータで解説。'
pubDate: '2026-08-10'
updatedDate: '2026-08-10'
heroImage: '../../assets/hero-archaludon-m5.png'
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
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス（M-5）" />
  <div>
    <h2 style="margin:0 0 8px">ブリジュラス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">3位</strong>（M-4は5位）　特性: <strong>じきゅうりょく 69.7%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-5シーズン時点の集計です

M-5シングルバトルでブリジュラスは**使用率3位**まで順位を上げました。技構成の中心（ラスターカノン・りゅうせいぐん・10まんボルト）はM-4（2026-07-13時点）から変わらず安定していますが、性格・持ち物の分布には動きがあります。ずぶとい性格が15.7%→17.6%へ、ピントレンズが5.1%→7.1%へ増加する一方、こだわりスカーフ・おくびょうの速度補強型はやや減少しており、耐久寄りの構築がわずかに勢力を伸ばしています（詳細はデータ分析①）。

---

## なぜブリジュラスが環境上位に定着しているのか

### 1. はがね/ドラゴンは弱点が2タイプのみで、多くの技に耐性を持つ

はがね/ドラゴン複合の弱点はかくとう・じめんの2タイプのみ。環境上位のマスカーニャ（くさ/あく）のくさ技は×0.25で通りにくく、でんき技・みず技・ひこう技・ノーマル技もいずれも半減（×0.5）です。マスカーニャの最大打点ははたきおとす（あく技・採用率65.1%）で、あく技はブリジュラスに等倍（×1）で通るうえ、相手が道具を持っていると威力が1.5倍（65×1.5）になり道具も失わせます。ブリジュラスは主流の持ち物（オボンのみ・たべのこし・しろいハーブ）を必ず何か持っているため、この威力上昇に加え、持ち物を落とされる不利もあります。トリプルアクセル（こおり技・採用率87.3%）も等倍で通りますが、はたきおとすの方が実効打点は上です。一方でじめん弱点（×2）はガブリアス（環境1位・じしん採用率99.5%）が直撃するため、ガブリアスへの受け出しは基本的にできません。耐性の広さとじめん弱点は常にセットで評価する必要があります。

### 2. C種族値125からの3方向特殊打点

ラスターカノン（はがね）・りゅうせいぐん（ドラゴン）・でんき技（10まんボルト/エレクトロビーム）の3タイプで打点を確保します。単体で完結した特殊アタッカーとして機能し、M-5でもこの3枠の採用率はいずれも58%以上を維持しています（詳細は「主要な技と採用率」）。

### 3. 特性で物理被弾への耐性を作る

採用率69.7%のじきゅうりょくは、技のダメージを受けるたびに防御が1段階上昇します。物理アタッカーに対して被弾しながらB上昇を積み上げ、C125の特殊技でカウンターを取り続けられます。もう一つの主要特性がんじょう（採用率30.2%）は、HP満タン時に一撃で瀕死になるダメージを受けてもHP1で耐える効果です。じめん弱点を突かれて一撃で落とされる展開を防ぐ役割があり、M-2以降おおむね2〜3割の採用を保っています（M-2は21.9〜23.5%、M-3は18.8〜31.4%で2割を下回る時点もあります。なおM-4の2026-07-13時点のデータにはがんじょうのレコード自体がありません）。

---

## 基本スペック

### 種族値

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:62.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">125</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
  </div>
</div>

最多EV構成「H2 C32 S32 ひかえめ」では**H167・B150・C194・S137**となります。S137はメガメタグロス（最速S178）・ガブリアス（最速S169）・ミミッキュ（ようきS162）・マスカーニャ（ようきS192）に後手となります。こだわりスカーフを持たせたおくびょう型ではS225となり、これらを上回ります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

---

## 主要な技と採用率（M-5）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center;width:40px">順位</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ラスターカノン</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">75.0%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:left">一致技。ミミッキュ（ゴースト/フェアリー）に×2。10%で相手の特防を下げる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>りゅうせいぐん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">72.7%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:left">一致技。使用後は自分のC2段階低下</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>10まんボルト</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">58.8%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:left">みず/フェアリー複合（アシレーヌ等）に×2</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ステルスロック</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">37.9%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:left">相手の場に設置し、繰り出しごとに固定割合のダメージを与える</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>あくのはどう</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">21.2%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:left">ゴースト複合（ゲンガー等）に×2、20%でひるみ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ほえる</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">17.8%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:left">優先度-6。相手を強制交代させステルスロックを踏ませる</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はどうだん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">17.7%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:left">必中技。かくとう技が弱点の相手への打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ミラーコート</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">15.4%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:left">優先度-5。受けた特殊ダメージを2倍で返す</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ドラゴンテール</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">60</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">14.4%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:left">優先度-6。ダメージを与えつつ相手を強制交代させステルスロックを踏ませる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>エレクトロビーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">13.0%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:left">通常2ターン技（あめ状態では1ターンで発動）。溜めターンでC1段階上昇</td>
</tr>
</tbody>
</table>
</div>

---

## 主な型

性格はひかえめ42.5%・ずぶとい17.6%・おくびょう16.8%・おだやか13.9%。持ち物はオボンのみ30.8%・たべのこし20.3%・しろいハーブ19.3%・こだわりスカーフ13.8%が主流です。

### 型1: ひかえめ 回復持ち型（最多採用）

**性格採用率: ひかえめ 42.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ひかえめ 回復持ち型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（69.7%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）42.5%<br>
<strong>EV:</strong> H2 C32 S32（採用率23.4%）<br>
<strong>持ち物:</strong> オボンのみ（30.8%）／たべのこし（20.3%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（75.0%）<br>
・りゅうせいぐん（72.7%）<br>
・10まんボルト（58.8%）<br>
・ステルスロック（37.9%）またはあくのはどう（21.2%）またはほえる（17.8%）
</div>
</div>
</div>

**強み:**

ひかえめC32でC実数値194。ラスターカノン・りゅうせいぐん・10まんボルトの3枠がM-5でも固定を維持しており、4枠目のステルスロック・あくのはどう・ほえるのいずれかで役割を追加できる汎用性が型1の特徴です。M-4から採用率・実数値ともほぼ変化がなく、ブリジュラスの主力型として定着しています。

**弱み:**

4枠目を1つしか選べないため、設置技（ステルスロック）・打点追加（あくのはどう）・流し技（ほえる）を同時には満たせません。持ち物を耐久・回復系（オボンのみ・たべのこし）に割いているため、型3（こだわりスカーフ）が持つ素早さ面のアドバンテージ（S実数値225）はありません。

---

### 型2: しろいハーブ りゅうせいぐん連射型

**持ち物採用率: しろいハーブ 19.3%（性格はひかえめが中心）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">しろいハーブ りゅうせいぐん連射型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（69.7%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H2 C32 S32<br>
<strong>持ち物:</strong> しろいハーブ（19.3%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（75.0%）<br>
・りゅうせいぐん（72.7%）<br>
・10まんボルト（58.8%）<br>
・ステルスロック（37.9%）またはあくのはどう（21.2%）
</div>
</div>
</div>

**強み:**

りゅうせいぐん（ドラゴン・威力130・命中90・使用後C2段階低下）の弱点を、しろいハーブ（能力低下を1度だけ自動回復）で補います。1発目使用後にCが2段階下がった直後、しろいハーブが自動発動してC低下分を回復するため、2発目のりゅうせいぐんもC低下前の火力で撃てます（回復は1度きり）。しろいハーブを持たない型1がりゅうせいぐんを連続で使う場合、2発目はC2段階低下（実質C97相当・0.5倍）を背負って撃つことになりますが、型2はしろいハーブでC194を維持したまま撃てるため、2発目の与ダメージがおよそ2倍になり、確定数が1つ縮まる相手も生まれます。

**弱み:**

しろいハーブはHPを回復する持ち物ではなく能力低下の打ち消しのみで、型1のオボンのみ・たべのこしのようなHP回復手段は持ちません。3発目以降のりゅうせいぐん使用でCが落ちるため、中盤以降はラスターカノン・10まんボルトへの切り替えが必要になります。

---

### 型3: おくびょうスカーフ型

**性格採用率: おくびょう 16.8%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">おくびょうスカーフ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（69.7%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）16.8%<br>
<strong>EV:</strong> B1 C32 D1 S32（2.8%）またはB2 C32 S32（2.3%）<br>
<strong>持ち物:</strong> こだわりスカーフ（13.8%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（75.0%）<br>
・りゅうせいぐん（72.7%）<br>
・10まんボルト（58.8%）<br>
・あくのはどう（21.2%）またはステルスロック（37.9%）
</div>
</div>
</div>

**強み:**

おくびょうS32のS実数値150にスカーフを持たせることでS225となり、ガブリアス最速S169・メガメタグロス最速S178・ミミッキュようきS162を超えられます。おくびょうC32のC実数値177は型1のひかえめC194より17低くなります。速度と火力のどちらに比重を置くかが、ひかえめ型との選択軸です。

**弱み:**

スカーフを持つため技が固定され、対面ごとに最適な技を選べません。またCがひかえめ型より低い（C177対C194）ため、確定数が1増える相手が存在します。持ち物がスカーフに固定されるため回復手段が加わらず、物理被弾を積み上げてもB上昇だけで耐える展開となります。M-4（こだわりスカーフ15.3%・おくびょう18.4%）と比べるとM-5は13.8%・16.8%へやや減少しており、後述の耐久型へ一部が流れています（データ分析①）。

---

### 型4: 耐久振り型

**性格採用率: ずぶとい 17.6% / おだやか 13.9%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">耐久振り型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（69.7%）またはがんじょう（30.2%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）17.6% またはおだやか（D↑ A↓）13.9%<br>
<strong>EV:</strong> H32 B2 D32（8.0%）またはH32 D32 S2（4.0%）<br>
<strong>持ち物:</strong> たべのこし（20.3%）またはオボンのみ（30.8%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（75.0%）<br>
・10まんボルト（58.8%）<br>
・ステルスロック（37.9%）<br>
・ほえる（17.8%）またはドラゴンテール（14.4%）
</div>
</div>
</div>

**強み:**

ずぶとい型（H32 B2 D32）は**H197・B167・D117**で、EVはHとDに最大まで振り、種族値65と低いとくぼうを補って特殊耐久を重視した配分になっています。じきゅうりょくのB上昇と合わせ、物理・特殊いずれの継続攻撃にも粘れる構成です。おだやか型（H32 D32 S2）ではD128とさらに特殊耐久を伸ばします。特性をがんじょうに切り替えた場合、HP満タンから一撃で瀕死になるダメージ（ガブリアス・カバルドンのじしんなど）を受けてもHP1で耐えられます。じきゅうりょくがB上昇による持久戦向けなのに対し、がんじょうは1回限りの確定生存を保証する点が異なり、じめん弱点を突かれる展開への保険として選べます。

**弱み:**

Cは無補正・EV0のため（ずぶとい・おだやかはC無補正、C実数値145）、型1のひかえめC194と比較してC49低く、1発確定が2発になる相手が増えます。がんじょうはHP満タン時のみ発動するため、一度でも被弾した後の一撃耐性は保証されません。火力を出す場面が少ないため、アタッカーとして採用する価値は薄く、展開補助後に後続に依存する構成です。

---

## データ分析①：M-4（07-13時点）→M-5 性格・持ち物の変化——耐久型のわずかな増加

技構成の主力3枠（ラスターカノン・りゅうせいぐん・10まんボルト）はM-4（2026-07-13時点）からほぼ変化していません。一方で性格・持ち物の分布には小さな変化があります。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">指標</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-4（07-13）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">特性：じきゅうりょく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">68.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">69.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+0.8pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格：ずぶとい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">15.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>17.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+1.9pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格：おくびょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">18.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-1.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物：こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">15.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-1.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物：ピントレンズ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">7.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+2.0pp</td>
</tr>
</tbody>
</table>
</div>

最も動いているのは性格・持ち物です。ずぶとい（+1.9pp）が伸びる一方、おくびょう（-1.6pp）・こだわりスカーフ（-1.5pp）の速度補強型はともに微減しており、「速度で上から動く」型よりも「一撃に耐えて長く戦う」型へわずかに需要がシフトしています。急所ランクを+1する持ち物ピントレンズの採用も5.1%→7.1%へ増加していますが、確定数を縮める効果であり、耐久型のB上昇・回復手段を代替するものではありません。なお特性はじきゅうりょくが69.7%と主流で、もう一つの主要特性がんじょう（30.2%）もM-2シーズン（21.9〜23.5%）からおおむね2〜3割の採用があり（M-3は18.8〜31.4%で2割を下回る時点もあり）、M-5で新たに登場した特性ではありません。

---

## データ分析②：M-4（07-13時点）との型比較——3枠固定の中での役割分化

M-4（2026-07-13時点）ではひかえめ耐久火力型（型1）・しろいハーブ りゅうせいぐん連射型（型2）・おくびょうスカーフ型（型3）・ずぶとい/おだやか耐久型（型4）の4型が確認されていました（M-4記事）。M-5でもこの4型の骨格は維持されており、内訳もほぼ変化していません。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-4（07-13）の特徴</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-5の特徴</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">型1（ひかえめ）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">性格採用率42.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">性格採用率42.5%・変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">型2（しろいハーブ）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物採用率18.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物採用率19.3%・微増</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">型3（スカーフ）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物採用率15.3%・速度補強の主力</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物採用率13.8%・微減</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">型4（耐久振り）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">性格採用率 ずぶとい15.7%・おだやか14.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">性格採用率 ずぶとい17.6%・おだやか13.9%</td>
</tr>
</tbody>
</table>
</div>

型1〜3はM-4の技・持ち物構成をほぼそのまま維持しています。型4はずぶといがやや伸びる一方でおだやかはやや減っており、物理面の粘りを重視する構成が相対的に選ばれる傾向にあります。ブリジュラスの型構造は3枠固定＋4枠目選択＋性格選択という骨格が固まっていると言えます。

---

## 主要ポケモンとの相性

以下の相性はひかえめH2 C32 S32型（H167・B150・C194・S137）を基準とします。**選定基準は使用率TOP10のうち、タイプ相性・速度関係から相性がはっきり示せる相手**です（使用率10位のリザードンはメガストーン採用データが欠損しており明確な判定ができないため除外）。○＝有利、△＝五分、×＝不利です。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン（使用率順位）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">相性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="ガブリアス">ガブリアス（使用率1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">×</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率99.5%でほぼ確実にじめん×2弱点を突かれます。でんき技はじめん複合に無効です。最速S169に後手なので引く択が必要です。がんじょう型なら満タンからの一撃は耐えられますが、以降の追撃には対応できません。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="アシレーヌ">アシレーヌ（使用率2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/フェアリー複合に10まんボルトは×2です。速度種族値60のアシレーヌにはS137のブリジュラスが先手を取れます。ムーンフォース（フェアリー）はブリジュラスに等倍です。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="マスカーニャ">マスカーニャ（使用率4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#888;font-weight:bold">△</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ/あく複合。こだわりスカーフ採用率55.2%が過半数でS実数値288、非スカーフでも最速S192とブリジュラスS137を上回り先手を取られます。ブリジュラスへの最大打点ははたきおとす（あく・採用率65.1%）で等倍。ブリジュラスは必ず道具を持っているため威力1.5倍（65×1.5＝97.5相当）まで伸び、ブリジュラスの主流持ち物（オボンのみ・たべのこし・しろいハーブ）を落としながら先手で削ってきます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="ミミッキュ">ミミッキュ（使用率5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#888;font-weight:bold">△</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特性ばけのかわは技のダメージを最大HPの1/8消費に置き換えるため、初撃のラスターカノン（ゴースト/フェアリーに×2）はダメージ0でばけのかわを剥がすだけに終わります。ミミッキュはようきS162でブリジュラスS137に先手を取り、つるぎのまい（82.7%）・じゃれつく（97.3%）を持つため、+2状態のじゃれつくを受けると大きく削られます。じゃれつくはフェアリー→はがね/ドラゴンで等倍止まりのため一撃で崩されるわけではなく、B150の耐久でラスターカノン2発圏に収める展開も見込めますが、実質2ターン目でようやく本来のダメージが通る、後手を強いられる相手です。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="カバルドン">カバルドン（使用率6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">×</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん単タイプのためでんき技は無効です。最大打点はドラゴン・はがね技ですがいずれも等倍にとどまります。カバルドンのじしんはブリジュラスのじめん弱点を×2で突きます。有効打に乏しくじめん技を受けるリスクが高い相手です。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="ギャラドス">ギャラドス（使用率7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#888;font-weight:bold">△</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ率77.8%でメガ後はみず/あく・最速S146です。ブリジュラスS137は後手になります。10まんボルトはみず/あく複合に×2で有効打ですが、ギャラドスのじしんはブリジュラスに×2で通るため、先手を取られると大きく削られる五分の対面です。さらにギャラドスはりゅうのまい（採用率82.3%）を持ち、1回積まれるとS219まで上昇して確実に先手を取られるようになるため、積みを許した後は一方的に押し切られやすくなります。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="カイリュー">カイリュー（使用率8位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#888;font-weight:bold">△</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ率80.4%。メガ後はドラゴン/ひこう・最速S167（ひかえめ・EV32時はS152）で、多くはブリジュラスS137より先に動きます。主力のかえんほうしゃ（66.7%）・りゅうせいぐん（54.4%）はいずれもブリジュラスに等倍にとどまり、じしん（16.5%）採用時のみじめん×2弱点を突かれます。一方でブリジュラスのりゅうせいぐんはカイリューに×2で通ります。速度で先手を取られても大半の型では大ダメージに繋がらない五分の対面です。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="メタグロス">メガメタグロス（使用率9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#888;font-weight:bold">△</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ率98.3%でメガ後ははがね/エスパー・最速S178です。ブリジュラスS137は後手になります。りゅうせいぐんはドラゴン技がはがねに半減（×0.5）で有効打に乏しく、じしん（採用率39.6%）を持たれるとじめん×2弱点を突かれ先手も取れません。一方でメタグロス側の主力技バレットパンチ（採用率92.6%）・サイコファング（採用率87.5%）はいずれもはがね/エスパー→ドラゴンで半減となり、双方が決定打を欠く展開になりやすい点で五分です。</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 同居率上位パートナー（M-5）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位（M-4：2位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じしんで幅広い相手に等倍以上の打点を持つ物理アタッカー枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位（M-4：5位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ムーンフォース（フェアリー）はドラゴン複合の相手に×2で通る打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率3位（M-4：1位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ガブリアスへじゃれつく（フェアリー×2）。物理アタッカー枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率4位（M-4：6位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">物理アタッカー枠。ブリジュラスと打点を分担</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率5位（M-4：3位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ステルスロック設置役。ブリジュラスがアタッカーに集中できる展開を作る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率6位（M-4：7位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">物理アタッカーとしてブリジュラスと打点を分担</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率7位（M-4：8位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">わるだくみ55.4%からのかえんほうしゃ65.4%で、ブリジュラスの技が半減されるはがねタイプ、および等倍止まりのくさタイプを焼く役割</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率8位（M-5新）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひかえめ主体の特殊アタッカー（シャドーボール72.4%・れいとうビーム57.2%）。アクアジェットで削り残しを詰める</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率9位（M-5新）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">メガ石採用データはM-5で欠損。M-4（07-13）はリザードナイトY 65.3%/X 33.5%が中心</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス">
    <div class="name">メタグロス</div>
    <div class="rate">同居率10位（M-4：4位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">物理アタッカー枠。共通弱点はじめんのみで、かくとうはメタグロス側が等倍で受けられる</div>
  </div>
</div>

**M-4との最大の違いはガブリアス・アシレーヌが上位に浮上した点**です。M-4は同居率1位ミミッキュ・2位ガブリアスでしたが、M-5では1位ガブリアス・2位アシレーヌへ入れ替わりました。M-4上位で見られたカバルドン（3位→5位）・メタグロス（4位→10位）は順位を落としつつも10位圏内を維持しています。新たにイダイトウ(オス)・リザードンが同居率圏内に加わりました。

---

## 総評

ブリジュラスはM-5で使用率3位まで浮上しました。ラスターカノン・りゅうせいぐん・10まんボルトの3枠固定という技構成の骨格はM-4（2026-07-13時点）から変わっていませんが、性格・持ち物の分布には小さな変化があります。ずぶといの微増（+1.9pp）は、速度補強型（おくびょう・こだわりスカーフ）の微減と対になっており、「一撃に耐えて長く戦う」耐久寄りの構築へわずかに需要がシフトしていると読めます。特性はじきゅうりょく（69.7%）が主流で、がんじょう（30.2%）もM-2以降おおむね2〜3割の採用を保つ選択肢です。じめん弱点（ガブリアス・カバルドン）とでんき無効（じめん複合全般）は構造上解消されないため、アシレーヌ・ミミッキュなどのパートナーで対面補完することが選出を組む前提となる点はM-4から変わりません。

---

*関連記事：[ブリジュラス考察 M-4](/blog/archaludon-analysis-m4/) / [ブリジュラス考察 M-3](/blog/archaludon-analysis-m3/) / [使用率1位 ガブリアス考察 M-3](/blog/garchomp-analysis-m3/)*

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/archaludon/)**
