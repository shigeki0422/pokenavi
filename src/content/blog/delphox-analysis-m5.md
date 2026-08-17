---
title: '【ポケモンチャンピオンズ】マフォクシー 考察 M-5 シーズン わるだくみ採用増と型の変化'
description: 'M-5シーズン使用率10位（2026-08-15時点、M-4は9位・2026-07-13時点）のメガマフォクシーを考察。かえんほうしゃが84.2%→65.4%に下落する一方、わるだくみが39.6%→55.4%に上昇。マフォクシナイト採用率99.2%、特性ふゆうを軸にした型構成の変化をデータで分析します。'
pubDate: '2026-08-17'
updatedDate: '2026-08-17'
heroImage: '../../assets/hero-delphox-m5.png'
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
  <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" />
  <div>
    <h2 style="margin:0 0 8px">メガマフォクシー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">10位</strong>（2026-08-15時点、M-4: 9位）　持ち物: <strong>マフォクシナイト 99.2%</strong>
    </div>
  </div>
</div>

M-5シーズン、マフォクシーは使用率10位（2026-08-15時点）で環境に定着しています（M-4は9位。2026-07-13時点のデータ）。ほのお/エスパーの複合タイプに、メガ進化後はとくこう159という高い一致打点と、とくぼう125の特殊耐久を両立する特殊アタッカーで、かえんほうしゃ（65.4%）を軸にサイコキネシス・わるだくみ・マジカルシャインを組み合わせる構成が主流です。M-4からはわるだくみの採用率が大きく伸びており、殴り合いから積みを重視する方向へ型の重心が動いています。

※本記事のM-4データは2026-07-13時点の1日分のクロールデータに基づきます。

---

## メガマフォクシーの基本スペック

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
      <div style="width:38%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">75</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">69</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">72</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:79%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">114</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+45</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:63%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+25</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:84%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">104</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">534</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でとくこう159（+45）・とくぼう125（+25）・すばやさ134（+30）が伸び、特性は**ふゆう**に変わります。ふゆうは地面にいないことになる特性で、じめん技（じしん・じならし等）・まきびし・どくびし・ねばねばネットを無効化します。EV H2-C32-S32・おくびょう（性格採用率79.7%）想定の実数値は **H152 / A80 / B92 / C211 / D145 / S204** です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">特性による無効（メガ後・ふゆう）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

メガ進化後は特性がふゆうに変わりじめん技を無効化するため、実戦では**いわ・ゴースト・みず・あくの4タイプが実質の弱点**です（ミミッキュのかげうち・アシレーヌのうたかたのアリアが代表例）。ただし特性かたやぶりを持つ相手（ギャラドスナイト採用時のギャラドス等）はふゆうを無視するため、じしんが通常どおり×2で通ります。

### 特性

メガ進化前は**もうか（91.8%）**が最多です。HPが最大HPの1/3以下になるとほのおタイプの技の威力が1.5倍になります。もう一つの選択肢である**マジシャン（8.2%）**は道具を持っていない時に技を当てた相手の道具を奪う特性です。メガ進化後は**ふゆう**に変わります（効果は前節参照）。マフォクシナイト採用率99.2%の環境では、実戦で機能するのはほぼ常にふゆうです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">65.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技のメインウェポン。10%でやけど付与。はがね・くさタイプに一致補正で通す（いわタイプには半減）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコキネシス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">56.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10%で相手の特防を1段階下げる。かくとう・どくへの一致打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わるだくみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">55.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自身のとくこうを2段階上昇。積んだ後の打点は大きく伸びるが隙を晒す</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マジカルシャイン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>46.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう・ドラゴンへの打点。使用率1位ガブリアスに×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みがわり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>43.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分のHP1/4を消費し設置。先制技・状態異常を透かしながら安全にターンを進める</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコショック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>34.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のぼうぎょ実数値で計算。とくぼうが高い受け寄りの相手に効果的</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を直前の技に固定。積み技・補助技を封じてみがわりを安全に張り直す1ターンを作れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オーバーヒート</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃより高威力だが自分の特攻が2段階下がる一発性の打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マジカルフレイム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の特攻を1段階下げる。かえんほうしゃより低威力だが特殊アタッカーの後続を弱体化できる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさむすび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20-120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の体重が重いほど高威力。体重300kgのカバルドンには最大威力120</td>
</tr>
</tbody>
</table>
</div>

---

## M-5の採用型

### 型1：特殊アタッカー型（かえんほうしゃ・サイコキネシス軸）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0655-00.webp" alt="メガマフォクシー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（91.8%）→メガ後ふゆう<br>
<strong>性格:</strong> おくびょう（79.7%）／ひかえめ（18.6%）<br>
<strong>EV:</strong> H2-C32-S32（最多EV分布）<br>
<strong>持ち物:</strong> マフォクシナイト（99.2%）
</div>
<div>
<strong>技構成:</strong><br>
・かえんほうしゃ<br>
・サイコキネシス<br>
・わるだくみ（マジカルシャイン）<br>
・みがわり（サイコショック）
</div>
</div>
</div>

かえんほうしゃ（ほのお・威力90）とサイコキネシス（エスパー・威力90）が主軸の一致技。わるだくみ（55.4%）とマジカルシャイン（46.7%）は採用率が拮抗し、積みで打点を伸ばすか、かくとう・ドラゴンへの打点（マジカルシャインはかくとう×2・ドラゴン×2）を確保するかの選択です。みがわり（43.8%）は先制技・状態異常を透かす選択肢、サイコショック（34.2%）は相手のとくぼうが高い受け寄りの相手に効果的です。性格はおくびょう（79.7%）とひかえめ（18.6%）に割れますが、この差が主要な対面（サザンドラ・アシレーヌ）の結果を左右しない理由はデータ分析②で扱います。

**強み:** マジカルシャイン採用時はかくとう・ドラゴンへの弱点打点を、サイコショック採用時は特殊耐久が高い受け寄りの相手への打点を確保でき、一致2本だけでは崩せない相手にも第3の打点で対応できます。

**弱み:** マジカルシャインとサイコショックは同一構成に両立できない択のため、選ばなかった側の打点（かくとう・ドラゴン、あるいは高とくぼう受け）には他の型2択（アンコール等）に頼る必要があり、この型だけでは全対応できません。

---

### 型2：アンコール型（19.2%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0655-00.webp" alt="メガマフォクシー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">アンコール型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（91.8%）→メガ後ふゆう<br>
<strong>性格:</strong> おくびょう（79.7%）<br>
<strong>EV:</strong> H2-C32-S32（最多EV分布）<br>
<strong>持ち物:</strong> マフォクシナイト（99.2%）
</div>
<div>
<strong>技構成:</strong><br>
・かえんほうしゃ<br>
・サイコキネシス<br>
・アンコール<br>
・みがわり（わるだくみ）
</div>
</div>
</div>

わるだくみ・マジカルシャインいずれかの枠をアンコール（19.2%、M-4は17.0%）に替えた構成です。カバルドンのあくびやギャラドスのりゅうのまいといった変化技を封じ、その隙にわるだくみを積む、あるいはみがわりを張り直す1ターンを作れます。型1が一致技で押し切る「殴り合い」型なのに対し、型2は行動を縛って立て直す「対面操作」型という位置づけです。

**強み:** 変化技を1ターン縛れるため、積みポケモンや状態異常付与を狙う相手に対して主導権を握りやすく、みがわりの張り直しで安全に立て直せます。

**弱み:** 打点面は型1（マジカルシャイン採用）に劣り、アンコールが機能しない攻撃技一辺倒の相手には行動を縛る利点を活かせません。

---

## データ分析①：M-4→M-5 技構成の変化

以下は、M-4・M-5いずれかのシーズンで上位10位以内に入った技を対象にした比較です。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4（2026-07-13時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">84.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-18.8pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコキネシス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">56.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">56.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">±0.0pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わるだくみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>55.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+15.8pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マジカルシャイン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">63.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">46.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-17.0pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みがわり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">42.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">43.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+1.5pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコショック</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アンコール</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.2pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マジカルフレイム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オーバーヒート</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">上位10位外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>16.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">上位10位外→16.8%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさむすび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.8pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おにび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">上位10位外へ</td>
</tr>
</tbody>
</table>
</div>

M-5の最大変化は**わるだくみの+15.8pp（39.6%→55.4%）とマジカルシャインの-17.0pp（63.7%→46.7%）**です。かえんほうしゃも-18.8pp下落しており、一致技2本で殴り合う構成から、わるだくみで積んでから一撃を通す構成へと重心が動いたことがうかがえます。加えて、M-4では上位10位外だった威力130のオーバーヒートが16.8%まで伸びており、一発の高火力技として存在感を増しています。オーバーヒートは技を出すたびに自分のとくこうが2段階下がるため、わるだくみで積んだ後に使う技ではなく、積まずに一撃で押し切る択として別枠で採用される技です。両者は同じ構成に共存させるものではなく、積んでから殴るか、積まずに一撃で仕留めるかという択の分岐を示しています。一方で状態異常技のおにびは上位10位から姿を消しており、削り役よりアタッカーとしての運用が優先される傾向です。マジカルフレイム（10.3%→13.4%）とくさむすび（9.9%→10.7%）は両シーズンとも上位10位内を維持しています。マジカルフレイムはほのお技（かえんほうしゃと同じくいわタイプに半減）で威力自体はかえんほうしゃに劣りますが、命中した相手の特攻を1段階下げる追加効果を持ち、後続の特殊アタッカーを弱体化させる目的で採用されます。くさむすびは体重が重い相手ほど高威力になる技で、体重の重いじめんタイプなどへの一致以外の打点として一定の需要があります。

---

## データ分析②：S204は主要な対面相手にも上から動けるか

すばやさ種族値がマフォクシー（104）以下でスカーフ非採用が多数派のミミッキュ・カバルドン・アシレーヌ・ギャラドス・ウォッシュロトムの5体について、実際の持ち物採用率とすばやさ種族値からスカーフ非採用時の最速実数値を確認しました。このうちウォッシュロトムは後述のとおり打点面の再検証で「型によって有利不利が入れ替わる相手」に、アシレーヌ・カバルドンは互角に近い対面として区分しています。

残るサザンドラ・ゲッコウガ・イダイトウの3体は事情が異なります。種族値だけで見ればサザンドラ（98）・イダイトウ（オス78）はマフォクシー（104・メガ後134）より遅いものの、こだわりスカーフの採用率がサザンドラ82.9%と最多持ち物になっており、多数派に対しては上を取られます。イダイトウ（オス）はこだわりスカーフ採用率32.6%とスカーフ自体は最多持ち物ですが、性格はS上昇補正のないひかえめが40.3%で最多のため、この型のスカーフはS実数値195にとどまりマフォクシー（S204）に上から動かれます。ようき（18.4%）・おくびょう（11.5%）などS上昇補正の性格（合計約30%）のスカーフ個体はS214でこちらが後手に回るため、性格まで踏まえると型によって先手・後手が入れ替わる相手です。

ゲッコウガはメガ後S142で、おくびょう個体（採用率53.0%）はS213となりマフォクシー（メガ後おくびょうS204）から上を取ってきます。ひかえめ個体（41.0%）はS194にとどまりマフォクシーが上を取れるため、性格次第で先手・後手が入れ替わる相手です。この3体は5体とは別に「苦手なポケモン」表の各行で個別に速度関係を記載しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ種族値</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">理論上限S（最速おくびょう換算・参考値）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ミミッキュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">96</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">0.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">162</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">カバルドン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">47</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">データ上ごく少数（上位10位圏外）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">108</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">0.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">123</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">81</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">0.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">146</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ウォッシュロトム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">86</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>26.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">151</td>
</tr>
</tbody>
</table>
</div>

「理論上限S」は各ポケモンがおくびょうS32振りだった場合の仮想値で、実際の主流性格ではありません（実測の主流性格はミミッキュ＝いじっぱり82.2%、カバルドン＝わんぱく64.1%、アシレーヌ＝ひかえめ70.0%、ギャラドス＝いじっぱり47.5%／ようき45.3%、ウォッシュロトム＝ずぶとい47.5%で、いずれも実戦のSはこの理論値以下です）。ウォッシュロトムのスカーフ採用率26.5%を除けば、いずれもスカーフ採用は少数派で、非スカーフの理論上限SはすべておくびょうS204のマフォクシーを下回ります。つまりマフォクシーは、これらの相手の多数派の型に対しては先に動いてみがわりを設置する、あるいはわるだくみを積む1ターンを確保できる立場にあります。ただしウォッシュロトムは約4分の1がスカーフを採用するため、この相手に限っては後手に回る可能性を常に考慮する必要があります。

**速度面では影響しないが、打点面では差が出る**：環境上位のサザンドラ（使用率15位）はこだわりスカーフ採用率82.9%が多数派で、サザンドラのS225に対しては、マフォクシーがおくびょう・ひかえめどちらの性格でも先手を取られます。非スカーフのサザンドラ（S150）にはどちらの性格でも先手を取れるため、先手・後手の結果は性格差で変わりません。一方、アシレーヌ（最多EVはH32-C32-S2・採用率5.8%、HP実数値187、D実数値136）への打点には性格差が出ます。採用率56.7%のサイコキネシス（エスパー・威力90）はみず/フェアリー複合に等倍で通り、おくびょうC211（ダメージ79〜94）は2発とも最大乱数でようやくHP187に届く水準で乱数2発の確率は約1.2%にとどまり実質確定3発ですが、ひかえめC232（同87〜103）は乱数2発の確率が実測67.6%と過半数を占め、1ターン速く沈められます。つまりサイコキネシスはどちらの性格でも確定3発ですが、ひかえめは高確率で乱数2発に入る点で、おくびょうより打点面で優れています。半減となるかえんほうしゃに限れば、おくびょうC211（最大47）は4発合計の最大値が188でHP187をわずかに上回るものの、4発とも高乱数を引かなければ届かない低確率のため実質確定5発、ひかえめC232（最大51、乱数4発に入る）でも同様の差が出ます。

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
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち（ゴースト・威力40・優先度+1・採用率96.6%）が×2弱点で先制。こちらの一致技は等倍止まりで決定打を欠きます。いのちのたま込み（採用率80.5%、いじっぱりA156）のかげうちは101〜119。採用率57.9%のシャドークロー（威力70）は同条件で174〜210に達し、HP152を確定1発で落とす最大打点です。特性ばけのかわで初撃を無効化される点も厄介です。マフォクシーはS204で、ミミッキュ（S種族値96・いじっぱりS32振りでもS実数値148）に先手を取れますが、かげうちは優先度+1の先制技のため素早さ勝負自体が意味を持ちません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ後（採用率77.8%）は特性かたやぶりでふゆうを無視し、じしん・たきのぼりが×2で通ります。りゅうのまいで積まれると重く、こちらのほのお技は半減。エスパー技はみず/あく複合に無効化されますが、マジカルシャイン（46.7%）はあく複合に×2で打点になります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（あく・採用率99.2%）が×2弱点。こだわりスカーフ82.9%が多数派でS225、こちらは先手を取られます。あくのはどう（ひかえめC194）は122〜146でHP152を確定耐え。返しのマジカルシャイン（×4、おくびょうC211）は232〜276で確定1発ですが、この打点はマジカルシャイン採用型（46.7%）限定です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（あく・採用率86.4%）が×2弱点。ゲッコウガナイト65.4%が多数派で、おくびょう（53.0%、S213）は先手、ひかえめ（41.0%、S194）はこちらが先手と性格で分かれます。先制のみずしゅりけん（49.5%）は×2で追い打ちになります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/ゴースト複合で、シャドーボール（72.4%）・なみのり（55.3%）・先制のアクアジェット（70.8%）がいずれも×2弱点。こだわりスカーフ32.6%が最多持ち物ですが、最多性格のひかえめ（40.3%）はS195でこちらが先手。ようき・おくびょうのスカーフ個体（計約30%）はS214で先手を取られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カイリュナイト採用率80.4%でメガ前提。特性マルチスケイルでかえんほうしゃ（半減）はさらに減衰し初撃18〜22しか通りません。最大打点のマジカルシャイン（46.7%、×2）も初撃45〜53、削った後は90〜106で2発。りゅうせいぐん（54.4%）は109〜130とHP152の大半を持っていく一撃で、打点勝負で押し切られやすい相手です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">リザードン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">少数派のリザードナイトX（41.1%）はかえんほうしゃは×0.25でほぼ通らず、特性かたいツメで強化されたげきりん（採用率23.1%）の一撃が確定1発と致命的です。多数派のリザードナイトY（57.9%）にはメガマフォクシーがS204でメガY（S152〜167）より先手を取り、サイコキネシスで確定2発と有利を取れます（詳細は表下段落）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ/あく複合で、はたきおとす（65.1%）・先制ふいうち（30.9%）が×2で通ります。いじっぱり（32.8%）のスカーフ個体のはたきおとすは144〜170でOHKO率11/16（68.8%）、ようき（61.1%）のスカーフ個体は132〜156で乱数1発12.5%（2/16）です。ふいうちは攻撃技選択時のみ成功する技で、こちらのわるだくみ・みがわり選択時は不発になります。返しのかえんほうしゃ（×2、おくびょうC211）は236〜282でHP153の相手を確定1発で落とせます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0503-01.webp" alt="ダイケンキ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ダイケンキ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">環境のダイケンキはみず/あく複合のヒスイダイケンキ。ひけん・ちえなみ（99.4%、きれあじで実効威力97）、先制ふいうち（84.8%、×2弱点）が主力で、くろいメガネ込みいじっぱり（48.6%・86.4%）だとどちらも確定1発です。マフォクシーのかえんほうしゃ・サイコキネシスは半減/無効で決定打を欠きますが、マジカルシャイン（46.7%、×2）は150〜178で乱数1発37.5%・確定2発。ふいうちは攻撃技選択時のみ成功するため、わるだくみ・みがわり選択時は不発になります。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" alt="ドドゲザン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ドドゲザン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく/はがね複合で、ドゲザン（96.7%）・先制ふいうち（98.9%）がいずれも×2。くろいメガネ込みいじっぱり（50.5%・91.9%）だとドゲザン259〜304、ふいうち211〜252で確定1発です。種族値S50でマフォクシーが先手を取れ、かえんほうしゃ（×2、おくびょうC211）は204〜242でOHKO率87.5%。外した場合や後出し・つるぎのまい後の先制ふいうちを許すと一方的に落とされます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のパワージェム（採用率80.3%）はいわタイプで×2弱点。ひかえめC200（最多EV分布H1-B1-C32-S32、採用率46.7%）で126〜150、単発ではHP152を落とし切れませんが確定2発です。持ち物はきあいのタスキ63.6%が最多で、これを持つ相手は先制の一撃を耐えてからパワージェムを返してくるため決着に時間がかかり、こだわりスカーフ（15.7%）の個体には素早さでも上を取られます</td>
</tr>
</tbody>
</table>
</div>

**リザードンの型別詳細**：多数派のリザードナイトY（57.9%）はメガリザードンYのひでりで場のほのお技が双方1.5倍になりますが、こちらのかえんほうしゃは半減のため打ち勝てません。メガリザードンYはメガ進化で素早さが上昇せず、リザードン全体の最多EV分布（H2-C32-S32、24.4%）を前提にすると実数値はひかえめ/いじっぱりでS152、おくびょう/ようき（性格別採用率合計34.2%）でもS167にとどまり、メガマフォクシーはS204でどちらの性格に対しても確実に先手を取れます。サイコキネシス（採用率56.7%、C211）は79〜94でメガYのHP155に確定2発。返しの最大打点は採用率19.2%のオーバーヒート（晴れ下、ひかえめC232）で88〜104、次点のエアスラッシュ（採用率39.2%、同C232）は67〜81で、いずれもメガマフォクシーのHP152を1発で落とせません。オーバーヒートは最低ロールの88でも2発で152を上回るため確定2発です。確定数が同じ2発で先手も取れるため、マフォクシーが1ターン早く倒し切れます。少数派のリザードナイトX（41.1%）はほのお/ドラゴン複合で、かえんほうしゃは×0.25、サイコキネシスも決定打を欠きます。X型に対する最大打点はマジカルシャイン（46.7%）で等倍。おくびょうC211で61〜72、メガXのHP155に対し確定3発です。一方でメガリザードンXの特性はかたいツメ（接触技の威力を1.3倍）で、リザードン全体で2番目に多い性格のいじっぱり（29.9%）・A32振り個体のげきりん（採用率23.1%）は、STAB1.5倍とかたいツメ1.3倍が重なり191〜226。メガマフォクシーのHP152に対し確定1発（16/16）です。メガリザードンXのS（いじっぱりA32振りでS152）はメガマフォクシーのS204を下回るため、こちらが先手を取れますが、マジカルシャイン1発ではメガXのHP155を落とし切れず、返り討ちのげきりんが確定1発で通るため、先手を取っても打点で押し切れないX型が実質的な脅威です。

---

## 相性が問題になる主要ポケモン

タイプ相性だけでは「苦手」に見えても、無効化特性・弱点技・素早さを踏まえた実打点の再検証で見え方が変わる相手がいます。メタグロス・アーマーガアは一致技（かえんほうしゃ）が弱点を突く一方、相手の主力打点は半減以下が中心です（メタグロスのかみなりパンチ32.3%は例外で等倍）。ガブリアスは非一致のマジカルシャイン（×2）が唯一の弱点打点で、多数派のタスキ型には先手を取れますが、スカーフ型（20.0%）には先手を取られます。ゲンガーはメガ後の素早さでマフォクシーが上回るため、サイコキネシス採用型（56.7%）に限りシャドーボールを受ける前に先制して倒し切れる相手です。非採用型（43.3%）はかえんほうしゃが等倍止まりで決定打を欠きます。ウォッシュロトムは型によって有利不利が入れ替わる相手、アシレーヌ・カバルドンは決定打も限定的な互角対面として掲載します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">相性分析</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のじしん（採用率99.5%）はふゆうで完全無効。げきりん・スケイルショットは等倍止まりで、×2のいわ技（がんせきふうじ26.8%・いわなだれ14.4%）の合計採用率は約4割（重複含む）です。マフォクシーの一致技は弱点を突けず、非一致のマジカルシャイン（46.7%、×2）がおくびょうC211で122〜144、HP185に確定2発です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（92.6%）・サイコファング（87.5%）は半減、じしん（39.6%）もふゆうで無効。かえんほうしゃ（×2、おくびょうC211）は168〜198、メガ後個体（HP157）に確定1発です。かみなりパンチ（32.3%）は等倍で通る例外です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ハッサム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハッサムナイト59.6%が多数派で、むし/はがね複合。かえんほうしゃ（×4、おくびょうC211）は360〜424で確定1発です。はたきおとす（47.2%）は×2で、最多EV分布H32-A2-B32（17.5%）基準では102〜120とHP152を落とし切れませんが、A32振り個体なら120〜142まで伸びます。いずれもバレットパンチ（半減）は軽微です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲンガー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゲンガナイト採用率80.6%が多数派。主力のシャドーボール（88.3%）は×2弱点ですが、おくびょうS200のメガゲンガーに対しマフォクシーはメガ後S204で上回るため先に動けます。サイコキネシス（採用率56.7%、×2、おくびょうC211）は186〜222でHP137のメガゲンガーを確定1発でき、サイコキネシス採用型に限り先に動いてシャドーボールを受ける前に倒し切れます。非採用型（43.3%）はかえんほうしゃ（等倍）が93〜111にとどまりHP137を落とし切れず、返しのシャドーボールはおくびょう（76.3%）で138〜164＝OHKO率50%、ひかえめ（22.3%）で152〜182＝確定1発を受けるため、五分〜不利な対面です。加えてメガゲンガーの特性かげふみは相手の交代自体を封じるため、この非採用型に対しては倒し切れないまま逃げて仕切り直すこともできません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ボディプレス（55.6%）・アイアンヘッド（35.6%）は半減（ブレイブバード26.0%は等倍）。かえんほうしゃ（×2、おくびょうC211）は204〜240、HP205の相手にOHKO率87.5%です。とんぼがえり（71.8%）で被弾前に交代されがちで、落とし損ねた場合ははねやすめで巻き戻される点は注意が必要です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん単タイプで、じしん（98.5%）はふゆうで完全無効。有効な物理打点はがんせきふうじ（採用率0.9%）のみでほぼありません。一方かえんほうしゃ・サイコキネシスも等倍で確定3発以上、なまける（49.5%）で回復されます。決定打はくさむすび（10.7%・×2）のみで154〜182×2発。互角に近い対面で、あくびの交代圧力・ステルスロックは別の脅威として残ります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">種族値S60・スカーフ0.3%で先手は取れますが、うたかたのアリア（90.8%、×2弱点）はD145に対し138〜164でOHKO率50%と返り討ちのリスクがあります。こちらの最大打点サイコショック（34.2%）は102〜121で確定2発必要。先制アクアジェット（71.7%、×2）の削りもあり、オボンのみ（46.1%）も絡む五分五分の対面です。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2番手のEV分布の耐久型（H32-B32-D2、9.5%）はC無振りのためハイドロポンプ（99.1%、×2）が108〜128で確定2発と互角以上ですが、最多EV分布のCS型（H2-C32-S32、14.4%）はひかえめでOHKO率87.5%、スカーフ（26.5%）を持てば速度でも上を取られ、型によって有利不利が入れ替わります（詳細は表下段落）</td>
</tr>
</tbody>
</table>
</div>

**ウォッシュロトムの型別詳細**：持ち物はたべのこし34.0%・オボンのみ29.2%・スカーフ26.5%に分散、性格は最多がずぶとい47.5%（とくこうに補正がかからない）です。2番手のEV分布H32-B32-D2（9.5%）の耐久型はこのEV分布自体がとくこうに振っていないためC無振りとなり、ハイドロポンプ（99.1%、×2）は108〜128でHP152に確定2発、サイコキネシス（56.7%、等倍）は84〜99で確定2発とこちらが優位です。一方、最多EV分布H2-C32-S32（14.4%）のCS型では話が変わります。ひかえめ個体（性格別採用率22.3%）はC172でハイドロポンプが150〜176、OHKO率87.5%（14/16）。おくびょう個体（17.8%）でもC157で134〜162、OHKO率37.5%（6/16）と無視できない打点になります。さらにこのCS型がスカーフ（26.5%）を持つ場合はS実数値でマフォクシーより先手を取られるため、耐久型には有利でもCS型には打点・速度の両面で分が悪く、型によって有利不利が入れ替わる相手です。

---

## 同居率上位の分析

M-5でマフォクシーと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。M-4からアーマーガア（7位）・ダイケンキ（9位）・ドヒドイデ（10位）が新たに上位入りし、メタグロス・アローラキュウコン・ウォッシュロトム（M-4は10位）は10位圏外となりました。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0503-01.webp" alt="ダイケンキ（ヒスイ）" loading="lazy">
    <div class="name">ダイケンキ（ヒスイ）</div>
    <div class="rate">9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0748-00.webp" alt="ドヒドイデ" loading="lazy">
    <div class="name">ドヒドイデ</div>
    <div class="rate">10位</div>
  </div>
</div>

**ガブリアス**（1位）はマフォクシーがこおり技を半減で受けられるため、ガブリアスの弱点であるこおり×4を受け出しで肩代わりできる関係です。同じくガブリアスが弱点とするフェアリー技もマフォクシーは半減で受けられるため、こおり・フェアリーの両弱点をカバーできる組み合わせです。

**ブリジュラス**（2位）はマフォクシーの打点範囲外の相手をラスターカノン・りゅうせいぐんで処理する住み分けで、タイプ相性による補完ではありません。

**アシレーヌ**（3位）はマフォクシーの弱点であるみずタイプの相手を受け持つ役割分担です。

**マスカーニャ**（4位）は一致技トリックフラワー（採用率96.9%）でマフォクシーの弱点であるいわ・みずタイプに×2が通り、決定打を欠く相手を処理します。

**ミミッキュ**（5位）はじゃれつく（採用率97.3%）・つるぎのまい（82.7%）で積んでから押し切る役割を持ち、マフォクシーが決定打を欠く高耐久の相手を処理する住み分けです。

---

## まとめ

M-5のマフォクシーは使用率10位（2026-08-15時点）で環境上位に定着しています（M-4は9位。2026-07-13時点のデータ）。以下のM-4比較データは2026-07-13時点の1日分のクロールデータに基づきます。

- **わるだくみが+15.8pp（39.6%→55.4%）で最大の技採用率の増加です**：かえんほうしゃ・マジカルシャインはそれぞれ-18.8pp・-17.0ppと下落し、殴り合いから積みを重視する型へ重心が移動しました
- **威力130のオーバーヒートは上位10位外→16.8%に伸びる一方、おにびは上位10位から消えました**：わるだくみで積んだ後の追撃ではなく、積まずに一撃で仕留める択として、削りより一発火力を優先する運用が広がっています
- **メガ進化後の特性ふゆうがじめん技を無効化します**：使用率1位のガブリアス・6位のカバルドンが持つじしん（採用率99.5%・98.5%）を実質無効にでき、タイプ相性表だけでは見えない安定感があります。ただしメガギャラドス（同7位、特性かたやぶり）のじしんはこの無効化を無視して通ります

ほのお/エスパーの一致技にわるだくみ・マジカルシャインで打点を広げつつ、ふゆうでじめん技を無効化する立ち回りが基本線です。一方でいわ・ゴースト・みず・あくの4タイプは弱点のまま残るため、ミミッキュ・ギャラドスといった上位のゴースト・みずタイプには決定打を欠く場面がある点は変わりません。加えてメガカイリュー（マルチスケイル）やメガリザードンX（げきりん）のように、タイプ相性表だけでは見えない特性・技構成で打点勝負に不利を背負う相手もいます。反対にメタグロス・アーマーガアは一致技（かえんほうしゃ）が弱点を突きつつ相手の主力打点の多くが半減以下に収まる有利対面です。ガブリアスは一致技では弱点を突けず、非一致のマジカルシャイン（フェアリー、×2）が唯一の弱点打点になる相手で、こだわりスカーフ20.0%（S実数値253）で先手を取られ、がんせきふうじ（26.8%）が×2で通る型がある点も踏まえると無条件の有利ではありません。ウォッシュロトムは、2番手のEV分布である耐久型（H32-B32-D2、9.5%）にはC無振り実数値でハイドロポンプが確定2発と有利ですが、最多EV分布のCS型（H2-C32-S32、14.4%）にはひかえめでOHKO率87.5%、スカーフ持ち（26.5%）なら先手も取られる、型によって有利不利が入れ替わる相手です。アシレーヌは先手を取れるものの被弾すれば50%でOHKOされる分の悪い五分対面、カバルドンはじしん無効による安定感はあるものの決定打はくさむすび採用型（10.7%）に限られ、いずれも無条件の得意ではなく互角に近い対面です。

---

*関連記事：[メガマフォクシー考察 M-4](/blog/delphox-analysis-m4/)*

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/mega-delphox/)**
