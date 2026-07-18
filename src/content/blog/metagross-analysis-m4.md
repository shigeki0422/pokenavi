---
title: 'メガメタグロス 考察 M-4 シーズン 採用型と立ち回り'
description: 'チャンピオンズM-4使用率4位メガメタグロス考察。M-3から継続する攻撃型に加え、てっぺき・ボディプレス型がM-4で台頭。わんぱく型の採用率20.5%・ボディプレス27.8%のデータを分析します。'
pubDate: '2026-07-14'
updatedDate: '2026-07-18'
heroImage: '../../assets/hero-metagross-m4.png'
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
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" />
  <div>
    <h2 style="margin:0 0 8px">メガメタグロス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">4位</strong>（M-3: 4位）　持ち物: <strong>メタグロスナイト 98.4%</strong>
    </div>
  </div>
</div>

M-4シーズン、メタグロスは使用率4位を維持しています。M-3から継続するいじっぱり・ようき攻撃型が主流である一方、M-4で新たにわんぱく性格が20.5%に達し、てっぺき（27.1%）とボディプレス（27.8%）がともにランク圏外から上位10技に浮上しました。てっぺき・ボディプレス型はメガ後B150という種族値の高さを積み技で増幅させ、ボディプレスの攻撃値に変換する仕組みで、M-3の上位構築での実績がM-4での数値上昇につながった形です。

---

## メガメタグロスの基本スペック

### 種族値（通常→メガ後）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:40px;text-align:right">メガ後</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:72%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">135</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:75%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">130</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">90</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">600</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でぼうぎょ150・すばやさ110（+40）と全ステータスが上昇し、特性も**かたいツメ**（接触技の威力×1.3）に変わります。ぼうぎょ150はてっぺき・ボディプレス型の土台となる数値です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

弱点はじめん・ゴースト・ほのお・あくの4タイプ（いずれも×2）。耐性が8タイプと広く、特にドラゴン・フェアリーへの耐性とどく無効がパーティ内での役割につながります。ただし環境1位のガブリアスがじしん（じめん）を99.5%採用しており、2位のミミッキュはかげうち（ゴースト）97.5%と、上位ポケモンが弱点タイプの技を持ちやすい点は立ち回りの制約になります。

### 特性

メガ進化前は**クリアボディ（99.3%）**が固定。相手の能力ダウン技を無効にし、どくどくやにらみつける等のデバフに左右されない対面の安定性があります。メガ進化後は**かたいツメ**に変わり、サイコファング・バレットパンチ・れいとうパンチなどの接触技に×1.3の補正がかかります（じしんは非接触のため対象外）。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコファング</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">94.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかりのかべ・リフレクター・オーロラベールを解除して攻撃するメインウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バレットパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">92.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1で必ず先制。ミミッキュ（ゴースト/フェアリー）へはがね×2打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">46.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラス（はがね/ドラゴン）へ×2。はがねタイプへの主力打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">41.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カイリュー（ドラゴン/ひこう）へ×4。10%の確率でこおり状態にする追加効果</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボディプレス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">27.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげきではなくぼうぎょの実数値でダメージが決まる技。てっぺきで積んだB値をそのまま攻撃力に変換</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっぺき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">27.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分のぼうぎょを2段階上昇。ボディプレスの攻撃値と被物理ダメージ半減を同時に得る積み技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かみなりパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドス（みず/ひこう）等のみず・ひこう複合への打点。10%の確率でまひ状態にする追加効果</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アームハンマー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン（じめん単）等の高耐久へ高威力。自分のすばやさが1段階下がる代償あり</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさむすび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">重さ依存</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン等の重い相手ほど高威力。じめん・みず複合の高耐久に対する採用</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20%の確率でひるませる追加効果を持つバレットパンチの代替枠</td>
</tr>
</tbody>
</table>
</div>

サイコファング（94.7%）・バレットパンチ（92.4%）はほぼ確定枠で、この2技に加えてじしん・れいとうパンチをどう組み合わせるかが攻撃型の技構成の軸になります。てっぺき（27.1%）・ボディプレス（27.8%）はM-4で新たに台頭した組み合わせで、わんぱく型でのみ採用される専用パーツです。

---

## M-4の採用型

### 型1：物理アタッカー型（いじっぱり 42.2% / ようき 35.4%）

**性格採用率: いじっぱり 42.2% / ようき 35.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">物理アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> クリアボディ（99.3%）→メガ後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）またはようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（全体最多EV分布・性格別の内訳は非公開）<br>
<strong>持ち物:</strong> メタグロスナイト（98.4%）
</div>
<div>
<strong>技構成:</strong><br>
・サイコファング<br>
・バレットパンチ<br>
・じしん<br>
・れいとうパンチ（かみなりパンチ）
</div>
</div>
</div>

サイコファング（エスパー・威力85）とバレットパンチ（はがね・威力40・優先度+1）が主軸。サイコファングはひかりのかべ・リフレクター・オーロラベール展開を貫通する効果を持ちます。バレットパンチはメガ後でも先制技として機能し、ミミッキュ（ゴースト/フェアリー）へのはがね×2の打点になります。じしん（じめん・威力100）はブリジュラス（はがね/ドラゴン）へ×2、れいとうパンチ（こおり・威力75）はカイリュー（ドラゴン/ひこう）へ×4と幅広いカバレッジを持ちます。

**強み:**

いじっぱりはH157 / A216 / B170 / C112 / D130 / S162。A216は1発の打点が高く、S振りなしでもぼうぎょ150と合わせて物理アタッカーの攻撃を受けながら殴り返せます。

**弱み:**

ようきはH157 / A197 / B170 / C112 / D130 / S178。S178で上から動ける相手が広がる一方、A197といじっぱりよりやや火力を落とすトレードオフになります。

---

### 型2：てっぺき・ボディプレス型（わんぱく 20.5%）

**性格採用率: わんぱく 20.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">わんぱく てっぺき・ボディプレス型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> クリアボディ（99.3%）→メガ後かたいツメ<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32-B32（代表例）<br>
<strong>持ち物:</strong> メタグロスナイト
</div>
<div>
<strong>技構成:</strong><br>
・てっぺき<br>
・ボディプレス<br>
・サイコファング<br>
・バレットパンチ
</div>
</div>
</div>

てっぺきでぼうぎょを2段階上げ（B222→実質444相当）、その数値をボディプレスの攻撃値に変換する型。ボディプレス（かくとう・威力80）はこうげきではなくぼうぎょの実数値でダメージが決まる技です。積み後のぼうぎょ値をそのまま攻撃値として使うため、メガ後B150という種族値の高さが積み技効果を乗算する形で活きます。てっぺき後は被物理ダメージも同時に半減するため、相手の物理打点を抑えながら高火力を出せます。

H187 / A165 / B222 / C112 / D130 / S130（EV: H32-B32）。

---

## データ分析①：M-3→M-4 技構成の変化

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコファング</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">91.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>94.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バレットパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">87.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>92.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+4.9pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">46.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">41.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-18.4pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボディプレス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">27.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっぺき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">27.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かみなりパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-7.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アームハンマー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+11.9pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-9.9pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさむすび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
</tbody>
</table>
</div>

M-4の最大変化は**ボディプレス（+27.8%）・てっぺき（+27.1%）の新台頭**です。M-3では圏外だったこれら2技がセットで27%台に達したことは、わんぱく性格20.5%という性格分布と整合しています。一方でれいとうパンチが-18.4ppに落ちていますが、依然41.6%と採用率は高く、カイリュー（ドラゴン/ひこう）への×4打点として攻撃型には残ります。

じしん（46.0%）はM-3の技採用データには掲載がありませんでしたが、M-4で半数近くが採用しています。ブリジュラス（はがね/ドラゴン）への×2打点として機能します。

---

## データ分析②：てっぺき・ボディプレス型の仕組み

ボディプレス（かくとう・威力80）はこうげきではなくぼうぎょの実数値を攻撃値として使う物理技です。わんぱく（B↑）H32-B32のてっぺき・ボディプレス型の実数値は以下のとおりです。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">EV</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">実数値（てっぺき前）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">てっぺき1積み後</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">187</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">こうげき（無補正）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">165</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ぼうぎょ（わんぱく↑）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>222</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>444</strong>（実質）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">とくこう（わんぱく↓）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">112</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
</tbody>
</table>
</div>

てっぺき1積み後にボディプレスはぼうぎょ444を攻撃値として使います。かたいツメ（×1.3）の補正込みで（かくとう技はじめん単タイプに等倍）、カバルドン（わんぱく H32-B32想定 H215/B187）への計算結果は以下のとおりです（メタグロスはかくとうタイプでないためSTABなし）。

- てっぺき前B222でのボディプレス → **48〜56ダメ（H215の22〜26%）** → 乱数4発以上（3発圏外）
- てっぺき後B444でのボディプレス → **94〜111ダメ（H215の44〜52%）** → 乱数2発

このわんぱく型のサイコファング（A165・エスパー一致1.5倍）がカバルドンへ56〜67ダメ（H215の26〜31%）にとどまるのに対し、てっぺき1積み後のボディプレスは約1.4〜1.9倍の打点になり、乱数2発圏まで打点が伸びます。

ただし、てっぺきを積む時間を作るには相手の交代や補助技のターンを利用する必要があります。ガブリアス（1位）・ミミッキュ（2位）の弱点技（じしん・かげうち）を引かずにてっぺきを積める局面を選ぶことが、この型の運用上の条件になります。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率99.5%）が×2弱点。てっぺき型は積んだぼうぎょでじしんを耐えやすくなりますが、攻撃型は受け出しできません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち（ゴースト・採用率97.5%）が×2弱点。バレットパンチ（はがね×2）でミミッキュに打点を持ちますが、ばけのかわ消費後にかげうちを受けると大ダメージになります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率98.4%）が×2弱点。なお、てっぺき・ボディプレス型ではてっぺき1積み後のボディプレスで乱数2発圏に入ります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（あく・採用率64.5%）・ふいうち（あく・採用率18.5%）があく×2弱点を突きます。サイコファングはマスカーニャ（くさ/あく）に無効です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">リザードン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（ほのお・採用率42.5%）・フレアドライブ（ほのお・採用率32.6%）がほのお×2弱点。持ち物はリザードナイトY65.3%・リザードナイトX33.5%で、メガYのほのお特殊打点に注意が必要です</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でメタグロスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" loading="lazy">
    <div class="name">サザンドラ</div>
    <div class="rate">5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">10位</div>
  </div>
</div>

**アシレーヌ**（1位）はみず/フェアリーで、メタグロスが持つほのお弱点に対してみず打点でリザードンを牽制し、メタグロスはアシレーヌのどく弱点をどく無効特性でカバーします。アシレーヌのフェアリー打点がドラゴン・あくタイプを抑え、メタグロスの物理打点と打点範囲が補い合う組み合わせです。

**ミミッキュ**（2位）はゴースト/フェアリーで、ばけのかわによる先制かげうちがメタグロスの苦手なゴースト・じめん技を強いてくる相手への圧力になります。メタグロスのバレットパンチ（はがね×2）でミミッキュへの打点を補い合う選出が多い構成です。

**ガブリアス**（3位）はドラゴン/じめんで、メタグロスのドラゴン耐性（×0.5）がドラゴン技を受けやすくします。一方でじしん弱点がパーティで重なる点は共通の弱みであり、ひこう・ふゆうタイプとのセットが安定します。

**カバルドン**（4位）はあくびとステルスロックのサポート役として機能します。カバルドンのあくびで相手の交代を強制し、メタグロスの対面を安全に作る運用に向きます。

**サザンドラ**（5位）はあく/ドラゴンで、タイプ相性の補完性が高い組み合わせです。サザンドラの最大弱点であるフェアリー（×4）をメタグロスが耐性（×0.5）でカバーする一方、メタグロスの弱点であるゴースト・ほのおはサザンドラ側が耐性（いずれも×0.5）を持ち、互いの弱点を打ち消し合う関係になっています。あくのはどう（99.3%）・りゅうせいぐん（93.3%）で特殊方面の打点を担い、メタグロスの物理打点と役割を分担します。

**ブリジュラス**（6位）ははがね/ドラゴンで、メタグロスと同じはがねタイプを共有し弱点分散にはなりませんが、ブリジュラスのラスターカノン（はがね一致）とメタグロスのバレットパンチで打点方向が異なる相手を分担できます。

---

## まとめ

M-4のメタグロスは使用率4位を維持しながら、わんぱく性格の台頭という新しい潮流が見られたシーズンです。

- **てっぺき（27.1%）・ボディプレス（27.8%）が圏外から上位10技へ浮上**：メガ後B150の高種族値を積み技で増幅させる「てっぺき・ボディプレス型」がM-3の実績を踏まえてM-4で数値上昇
- **いじっぱり・ようきの物理アタッカー型が引き続き主流**（合計77.6%）：EVは全体最多分布のH2-A32-S32が代表的で、性格ごとの内訳は非公開
- **同居率はアシレーヌがM-3の6位から1位へ上昇**：メタグロスの弱点であるほのお・どくをアシレーヌのみず打点・どく無効特性で補完する組み合わせが定着

はがね/エスパーの多耐性（半減8タイプ＋どく無効）と、かたいツメによる接触技強化を備えた物理アタッカーという基本性能は不変です。攻撃型・耐久型のどちらを選ぶかは、パーティ内での役割（先制フィニッシャーか、受けて殴り返す役か）に応じた判断が求められます。

---

*関連記事：[アシレーヌ考察 M-3](/blog/primarina-analysis-m3/)*
