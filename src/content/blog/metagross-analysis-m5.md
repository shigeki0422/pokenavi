---
title: '【ポケモンチャンピオンズ】メタグロス 考察 M-5 シーズン バレットパンチが最多採用技に浮上'
description: 'チャンピオンズM-5使用率9位メタグロス考察。いじっぱり52.4%への性格偏重とバレットパンチ92.6%がサイコファング87.5%を上回った採用率変化、わんぱく型（17.7%）のてっぺき・ボディプレスのデータを分析します。'
pubDate: '2026-08-16'
updatedDate: '2026-08-16'
heroImage: '../../assets/hero-metagross-m5.png'
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
      使用率: <strong style="color:#e67e22">9位</strong>（M-4: 7位※2026-08-04時点）　持ち物: <strong>メタグロスナイト 98.3%</strong>
    </div>
  </div>
</div>

M-5シーズン、メタグロスは使用率9位に位置しています（M-4最終日2026-08-04時点は7位）。技構成の主軸自体は変わっていませんが、採用率の順位に変化があり、バレットパンチ（92.6%）がサイコファング（87.5%）を上回って最多採用技になりました。性格分布もいじっぱりが52.4%まで伸び、M-4の42.2%から偏重が進んでいます。

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

メガ進化でHP以外の5ステータスが上昇し、ぼうぎょ150・すばやさ110（+40）に到達します。特性も**かたいツメ**（接触技の威力×1.3）に変わります。ぼうぎょ150はてっぺき・ボディプレス型の土台となる数値です。

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

弱点はじめん・ゴースト・ほのお・あくの4タイプ（いずれも×2）です。耐性は8タイプと広く、ドラゴン・フェアリーへの耐性とどく無効がパーティ内での役割につながります。ただし環境1位のガブリアスがじしん（じめん）を99.5%採用しており、5位のミミッキュはかげうち（ゴースト）96.6%と、上位ポケモンが弱点タイプの技を持ちやすい点は立ち回りの制約になります。

### 特性

メガ進化前は**クリアボディ（99.5%）**がほぼ固定です（残り0.5%はライトメタルの個体）。相手の技・特性による能力ランクダウンを無効化し、いかく（こうげき低下）・がんせきふうじ（すばやさ低下）・こわいかお（すばやさ低下）等のランクダウン技/特性に左右されない対面の安定性があります（どくどくのような状態異常はクリアボディの対象外です）。メガ進化後は**かたいツメ**に変わり、サイコファング・バレットパンチ・れいとうパンチなどの接触技に×1.3の補正がかかります（じしんは非接触のため対象外）。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バレットパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">92.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1で通常技より先に動ける。ミミッキュ（ゴースト/フェアリー）へはがね×2打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコファング</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">87.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかりのかべ・リフレクター・オーロラベールを解除して攻撃するメインウェポン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラス（はがね/ドラゴン）へ×2。はがねタイプへの主力打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">38.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス（ドラゴン/じめん）・カイリュー（ドラゴン/ひこう）へいずれも×4。10%の確率で相手を凍り状態にする追加効果</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かみなりパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドス（メガストーン採用率77.8%・メガ後みず/あく）へ×2。10%の確率でまひ状態にする追加効果</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アームハンマー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン（じめん単）等の高耐久へ高威力。自分のすばやさが1段階下がる代償あり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボディプレス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">24.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげきではなくぼうぎょの実数値でダメージが決まる技。てっぺきで積んだB値をそのまま攻撃力に変換</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっぺき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">23.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分のぼうぎょを2段階上昇。ボディプレスの攻撃値と被物理ダメージ半減を同時に得る積み技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20%の確率でひるませる追加効果を持つバレットパンチの代替枠</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">コメットパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20%の確率で自分のこうげきを1段階上げる追加効果。アイアンヘッドより高威力な選択肢</td>
</tr>
</tbody>
</table>
</div>

バレットパンチ（92.6%）とサイコファング（87.5%）はほぼ確定枠で、残り2枠をじしん（39.6%）・れいとうパンチ（38.0%）・かみなりパンチ（32.3%）・アームハンマー（25.2%）から選ぶのが攻撃型の軸です。れいとうパンチはガブリアス（1位）・カイリュー（8位）へいずれも×4が入る打点で、じしんに次ぐ採用率を確保しています。てっぺき（23.1%）・ボディプレス（24.5%）は主にわんぱく型（17.7%）が採用する専用パーツです。

---

## M-5の採用型

### 型1：物理アタッカー型（いじっぱり 52.4% / ようき 28.4%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">物理アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> クリアボディ（99.5%）→メガ後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）またはようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（全体最多EV分布・性格別の内訳は非公開）<br>
<strong>持ち物:</strong> メタグロスナイト（98.3%）
</div>
<div>
<strong>技構成:</strong><br>
・バレットパンチ<br>
・サイコファング<br>
・じしん<br>
・れいとうパンチ／かみなりパンチ／アームハンマー
</div>
</div>
</div>

バレットパンチとサイコファングが主軸で、じしん・れいとうパンチ・かみなりパンチ・アームハンマーの中から2枠を選び補完打点を確保します（各技の詳細は上記の技採用率表を参照）。

**性格差：Sの違いが決めるガブリアスとの先手争い**

ようき型（S178）は非スカーフのガブリアス（S169）に先手を取れますが、いじっぱり型（S162）は下回ります。詳細な速度比較はデータ分析③を参照してください。

---

### 型2：てっぺき・ボディプレス型（わんぱく 17.7%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">わんぱく てっぺき・ボディプレス型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> クリアボディ（99.5%）→メガ後かたいツメ<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H20-B20-S26（わんぱく型で想定される分布・全体4.9%）<br>
<strong>持ち物:</strong> メタグロスナイト
</div>
<div>
<strong>技構成:</strong><br>
・てっぺき<br>
・ボディプレス<br>
・バレットパンチ<br>
・サイコファング
</div>
</div>
</div>

てっぺきで積んだぼうぎょをボディプレスの攻撃値に変換し、被物理ダメージ半減も同時に得る積み技です（仕組みの詳細はデータ分析②を参照）。

実数値: H175 / A165 / B209 / C112 / D130 / S156（EV: H20-B20-S26）。

---

## データ分析①：M-4→M-5 技構成の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4（07-13時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バレットパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">92.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>92.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+0.2pp（首位交代）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコファング</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">94.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>87.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-7.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">46.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-6.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">41.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>38.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かみなりパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>32.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+6.9pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アームハンマー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>25.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+11.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボディプレス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>24.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.3pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっぺき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>23.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-4.0pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+10.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">コメットパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">記録なし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">M-4は10技のみ記録（最小はアイアンヘッド7.5%）、コメットパンチはそもそも記録に含まれていません</td>
</tr>
</tbody>
</table>
</div>

M-5の最大変化は**バレットパンチとサイコファングの採用率順位の入れ替わり**です。ただしこれはバレットパンチ自体が伸びたためではなく（+0.2ppでほぼ横ばい）、サイコファングが-7.2ppと大きく下落したことによる順位交代です。サイコファングで空いた枠は特定のタイプに偏らず、でんき技のかみなりパンチ（+6.9pp）・かくとう技のアームハンマー（+11.5pp）・はがね技のアイアンヘッド（+10.0pp）の3方向に分散しており、補完打点を増やす方向に技選択が動いています。

れいとうパンチはM-4の41.6%からM-5は38.0%へ-3.6ppとやや減少しましたが、じしん（39.6%）に次ぐ4位を維持しており、じしんとほぼ同格の補完打点として扱われ続けています。ガブリアス（ドラゴン/じめん）・カイリュー（ドラゴン/ひこう）へいずれも×4が入り、地面技が効かないひこうタイプ・ふゆう特性の相手にも通る点でじしんとは異なる用途を持ちます。コメットパンチ（M-5で7.2%）はM-4データが10技のみの記録（最小はアイアンヘッド7.5%）で採用率一覧に含まれていないため、M-4時点での採用率は不明です。てっぺき・ボディプレス型の2技はいずれも数pp下がっていますが、23〜25%台を維持しており依然として一定数のプレイヤーに選ばれています。

---

## データ分析②：てっぺき・ボディプレス型の仕組み

ボディプレス（かくとう・威力80）はこうげきではなくぼうぎょの実数値を攻撃値として使う物理技です。わんぱく（B↑）H20-B20-S26（わんぱく型で想定される分布・全体4.9%）のてっぺき・ボディプレス型の実数値は以下のとおりです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">175</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>209</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>418</strong>（実質）</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">26</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">156</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
</tbody>
</table>
</div>

てっぺき1回使用後（+2段階）にボディプレスはぼうぎょ418を攻撃値として使います。かたいツメ（×1.3、ボディプレスは接触技）の補正込みで（かくとう技はじめん単タイプに等倍）、カバルドン（わんぱく H32-B2-D32・最多EV分布、実数値H215/ぼうぎょ154）への計算結果は以下のとおりです（メタグロスはかくとうタイプでないためタイプ一致補正なし）。

- てっぺき前ぼうぎょ209でのボディプレス → **53〜63ダメ（H215の24.7〜29.3%）** → 最低ダメ53×4=212はH215に届かず乱数4発では倒しきれない目が残り、乱数5発の可能性もあります
- てっぺき後ぼうぎょ418でのボディプレス → **106〜126ダメ（H215の49.3〜58.6%）** → 乱数2発（低乱数では3発）

このわんぱく型のサイコファング（A165・エスパー一致1.5倍・かたいツメ×1.3）はカバルドンへ67〜81ダメ（H215の31.2〜37.7%）です。てっぺき前のボディプレスはサイコファングの打点を下回りますが、てっぺきを1回積むとボディプレスはサイコファングの約1.5倍まで伸びます。

ただし、てっぺきを積む時間を作るには相手の交代や補助技のターンを利用する必要があります。ガブリアス（1位）・カバルドン（6位）の弱点技（じしん）を引かずにてっぺきを積める局面を選ぶことが、この型の運用上の条件になります。

---

## データ分析③：物理型の性格差とガブリアスとの先手争い

いじっぱりはH157 / A216 / B170 / C112 / D130 / S162、ようきはH157 / A197 / B170 / C112 / D130 / S178です。ガブリアスの性格分布はようき50.9%・いじっぱり31.6%・わんぱく14.5%（M-5データ）で、性格によって速度が大きく異なります。ようき個体（実数値S169・EV32想定）にはメタグロスのようき型（S178）のみが先手を取れ、いじっぱり型（S162）は下回り後手に回ります。一方、いじっぱり・わんぱく個体（実数値S154・EV32想定、計約46%）に対してはメタグロスのいじっぱり型（S162）でも先手を取れます。ただしガブリアスはこだわりスカーフも20.0%採用しており、ようき個体なら実数値S253、いじっぱり・わんぱく個体でも実数値S231に達するため、この個体にはメタグロスのどちらの性格型でも後手になります。まとめると、メタグロスいじっぱり型が後手に回るのはようき個体（50.9%）と性格を問わずスカーフを持つ個体（20.0%、性格分布の内数）に対してで、非スカーフのいじっぱり・わんぱく個体（計約46%のうちスカーフを除いた個体）には先手を取れます。後手の場面ではA216の打点でどこまで削り返せるかが分かれ目になります。

---

## 得意なポケモン

使用率上位（目安TOP50）のうち、メタグロスの弱点（じめん・ゴースト・ほのお・あく）を突く技の採用率が20%未満（またはそもそも不採用）で、かつメガ進化・特性・実数値まで検算しても優位が崩れないポケモンを絞り込んだ結果は以下のとおりです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力技（ムーンフォース・うたかたのアリア・アクアジェット）はメタグロスの弱点を突きません。逆にメタグロスがかみなりパンチ採用個体（32.3%）であれば、でんき技はアシレーヌ（みず/フェアリー）へ×2で通ります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ニンフィア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最多採用技のハイパーボイス（技表記はノーマル・98.8%）は、ニンフィアの特性フェアリースキン（99.4%採用）によって実際にはフェアリー技として飛び、威力も1.2倍に補正されます。フェアリー技としてもメタグロス（はがね/エスパー）へは半減（結果自体はノーマル技のときと同じ倍率）で、メタグロスの主力打点はいずれも等倍以上で通ります。ただし弱点を突くマジカルフレイム（ほのお）採用個体（19.4%）には不利になる点に注意が必要です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のフリーズドライ（こおり・80.7%）・ふぶき（こおり・67.8%）・ムーンフォース（フェアリー・47.9%）はいずれもメタグロスに半減で、弱点技は不採用です。逆にメタグロスの主力バレットパンチ（はがね・92.6%）はこおり/フェアリー複合へ×4の大打点です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0670-05.webp" alt="フラエッテ(永遠)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">フラエッテ（永遠）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガストーン採用率97.2%のメガフラエッテはフェアリー単タイプで、メタグロスへの弱点技を持ちません。最多採用のムーンフォース（フェアリー・93.5%）は半減、サイコキネシス（エスパー・21.3%）は0.25倍にとどまります。ただしはめつのひかり（フェアリー・威力140・採用率40.2%）は無視できない脅威技です。多数派の性格おくびょう（73.6%）・EV最多分布H22-B11-C1-S32（30.5%、C1＝ほぼ無振り）の個体では、フェアリーオーラ（威力1.33倍）込みで71〜84ダメ（メガメタグロスH157の45.2〜53.5%）＝乱数2〜3発です。EV分布2位のH2-C32-S32（12.3%、性格は問わない集計値）にひかえめを組み合わせた個体まで想定すると91〜108ダメ（58.0〜68.8%）＝確定2発まで伸びます。それでもメタグロス側は優先度+1・かたいツメ補正込みのバレットパンチ（はがね一致×2）で、フラエッテ多数派個体（B118・H171）へ109〜132ダメ（63.7〜77.2%）・確定2発を先に決められるため、有利判定自体は維持できます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0279-00.webp" alt="ペリッパー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ペリッパー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">49位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のぼうふう（ひこう・98.7%）・れいとうビーム（こおり・56.6%）はメタグロスに半減、とんぼがえり（むし・86.5%）・なみのり（みず・50.7%）は等倍で、採用率上位に弱点技（ほのお・じめん・ゴースト）は見られません。メタグロスがかみなりパンチ採用個体（32.3%）であれば、でんき技はみず/ひこう複合へ×4で通ります</td>
</tr>
</tbody>
</table>
</div>

打点面の優位に加え、被弾面でも有利が取れる相手はアシレーヌ・アローラキュウコン・ペリッパー・ニンフィア・フラエッテ（永遠）の5体です。ただし採用率50%を超える相手であるガブリアス（じしん99.5%）・マスカーニャ（はたきおとす65.1%）・ミミッキュ（かげうち96.6%）のように、メタグロスの弱点を高採用率の技で突いてくる相手も上位に多く、上記の「得意」は限定的な範囲にとどまる点は変わりません。

---

## 苦手なポケモン

以下は弱点技（メタグロスの弱点であるじめん・ゴースト・ほのお・あく）の採用率を基準に選定しており、後述のサイト内1v1シミュレーションの平均判定（技構成を確率的に扱う）とは選定基準が異なります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率99.5%）が×2弱点で、攻撃型は受け出しできません。一方でメタグロス側もれいとうパンチ採用個体（38.0%）であればガブリアスへ×4が入るため、先制できれば打点で押し返せる相手でもあります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（あく・採用率65.1%）・ふいうち（あく・採用率30.9%）があく×2弱点を突きます。サイコファングはマスカーニャ（くさ/あく）に無効です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち（ゴースト・採用率96.6%）が×2弱点で優先度+1のため避けにくく、ばけのかわ消費後の一撃も大ダメージになります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率98.5%）が×2弱点で、高い耐久から長期戦になりやすい相手です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率76.8%）が×2弱点、かみくだく（あく・採用率25.0%）も×2弱点を突きます。メガストーン採用率77.8%と高く、メガ後はA155の高打点に加えみず/あく複合になるため、メタグロスの主力技サイコファング（エスパー）が無効になり打点で崩せません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（ほのお・採用率66.7%）が×2弱点を突きます。メタグロス側もれいとうパンチ採用個体（38.0%）であればカイリューへ×4が入り、打点面では有利を取り返せます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マフォクシー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（ほのお・採用率65.4%）が×2弱点で、特殊アタッカーのため物理耐久の高いてっぺき型でも受けにくい相手です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">リザードン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（ほのお・採用率40.6%）・フレアドライブ（ほのお・採用率40.1%）がほのお×2弱点を突きます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ハッサム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（あく・採用率47.2%）が×2弱点を突きます。メタグロス側は同じはがね一致技のバレットパンチがむし/はがね複合へ半減にとどまり、打点で押し返しにくい相手です（じしん採用個体39.6%・アームハンマー採用個体25.2%は等倍で通りますが、いずれもタイプ一致はありません）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ（オス）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（ゴースト・採用率72.4%）が×2弱点を突きます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（あく・採用率99.2%）がほぼ確定で採用され×2弱点を突きます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから（じめん・採用率68.9%）が×2弱点を突きます。キラフロル（いわ/どく）へはメタグロスのバレットパンチ・サイコファングもいずれも×2で通り、サイト内1v1シミュレーション（技構成を確率的に扱う）では平均的にメタグロス有利判定が出ますが、これはだいちのちからを持たない個体（約31%）を含めた平均であるためです。だいちのちからを採用する多数派（68.9%）との対面では弱点を突かれる側になるため、苦手なポケモンに残しています</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（あく・採用率86.4%）が×2弱点を突きます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲンガー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（ゴースト・採用率88.3%）がほぼ確定で採用され×2弱点を突きます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0503-00.webp" alt="ダイケンキ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ダイケンキ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">技名にみずを連想させるひけん・ちえなみ（採用率99.4%）・ふいうち（採用率84.8%）はいずれも実際にはあくタイプで、×2弱点をほぼ確実に突かれます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-5でメタグロスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" loading="lazy">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" loading="lazy">
    <div class="name">ゲンガー</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**アシレーヌ**（1位）はみず/フェアリーで、メタグロスが持つほのお弱点に対してみず打点でリザードンやマフォクシーを牽制し、メタグロスははがね/エスパータイプの相性上どくタイプの技が無効になるため、アシレーヌのどく弱点をカバーします。アシレーヌのフェアリー打点がドラゴン・あくタイプを抑え、メタグロスの物理打点と打点範囲が補い合う組み合わせです。

**ガブリアス**（2位、M-4の3位から上昇）はドラゴン/じめんで、ガブリアスのドラゴン技を相手のはがねタイプが半減してくる場面を、メタグロスのはがね打点（バレットパンチ等）で分担できる役割分担の組み合わせです。一方でじしん弱点がパーティで重なる点は共通の弱みであり、ひこうタイプやふゆう特性のポケモンとのセットが安定します。

**カバルドン**（3位）はあくびとステルスロックのサポート役として機能します。カバルドンのあくびで相手の交代を強制し、メタグロスの対面を安全に作る運用に向きます。

**サザンドラ**（4位）はあく/ドラゴンで、タイプ相性の補完性が高い組み合わせです。サザンドラの最大弱点であるフェアリー（×4）をメタグロスが耐性（×0.5）でカバーする一方、メタグロスの弱点であるゴースト・ほのおはサザンドラ側が耐性（いずれも×0.5）を持ち、互いの弱点を打ち消し合う関係になっています。あくのはどう（99.2%）・りゅうせいぐん（93.0%）で特殊方面の打点を担い、メタグロスの物理打点と役割を分担します。

**ブリジュラス**（5位）ははがね/ドラゴンで、メタグロスと同じはがねタイプを共有し弱点分散にはなりませんが、ブリジュラスのラスターカノン（はがね一致）とメタグロスのバレットパンチで打点方向が異なる相手を分担できます。

**ミミッキュ**（7位、M-4の2位から下降）はゴースト/フェアリーで、ばけのかわを盾に優先度+1のかげうちで相手を削る先制枠です。メタグロスは高い攻撃力と耐久を持つ物理アタッカーとして、ミミッキュが削った後の相手を押し切る役割を分担します。

---

## まとめ

M-5のメタグロスは使用率9位となり（M-4最終日は7位）、採用技の内訳に細かな変化が見られたシーズンです。

- **バレットパンチ（92.6%）がサイコファング（87.5%）を上回り最多採用技に交代しました**：M-4の07-13時点データではサイコファングが上回っていましたが、これはサイコファングが-7.2pp下落した結果の順位交代で、空いた枠はでんき・かくとう・はがねの補完打点に分散して採用されています
- **性格分布はいじっぱりが52.4%（M-4比+10.2pp）へ偏重しています**：ようき28.4%・わんぱく17.7%はいずれも減少しました
- **同居率はガブリアスが3位→2位、ミミッキュが2位→7位へ変動しました**：ゲンガーが新たに同居率上位10入りしました

はがね/エスパーの多耐性（半減8タイプ＋タイプ相性上どく技が無効）と、かたいツメによる接触技強化を備えた物理アタッカーという基本性能は不変です。攻撃型・耐久型のどちらを選ぶかは、パーティ内での役割（先制フィニッシャーか、受けて殴り返す役か）に応じた判断が求められます。

---

*関連記事：[メガメタグロス考察 M-4](/blog/metagross-analysis-m4/)*
