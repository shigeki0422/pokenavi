---
title: '【ポケモンチャンピオンズ】メガマフォクシー 考察 M-4 シーズン 特殊アタッカーの型と立ち回り'
description: 'M-4シーズン使用率9位（M-3は16位）のメガマフォクシーを考察。メガ石マフォクシナイト採用率99.1%、特性ふゆうでじめん技を無効化する立ち回りと、かえんほうしゃ84.2%を軸にした型構成をデータで分析します。'
pubDate: '2026-07-15'
updatedDate: '2026-07-15'
heroImage: '../../assets/hero-delphox-m3.png'
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
  <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" />
  <div>
    <h2 style="margin:0 0 8px">メガマフォクシー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">9位</strong>（M-3: 16位）　持ち物: <strong>マフォクシナイト 99.1%</strong>
    </div>
  </div>
</div>

M-4シーズン、マフォクシーは使用率9位に浮上しました（M-3は16位）。ほのお/エスパーの複合タイプに、メガ進化後はとくこう159・とくぼう125という高い水準の特殊耐久を得る特殊アタッカーで、かえんほうしゃ（84.2%）とマジカルシャイン（63.7%）を軸に、サイコキネシス・サイコショックのエスパー技で打点を広げる構成が主流です。

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

メガ進化でとくこう159（+45）・とくぼう125（+25）・すばやさ134（+30）が伸び、特性は**ふゆう**に変わります。ふゆうは地面にいないことになる特性で、じめん技（じしん・じならし等）を無効化します。EV H2-C32-S32・おくびょう（性格採用率80.9%）想定の実数値は **H152 / A80 / B92 / C211 / D145 / S204** です。

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

タイプ相性上の弱点はじめん・いわ・ゴースト・みず・あくの5タイプ（いずれも×2）。ただしメガ進化後は特性がふゆうに変わり、じめん技を無効化するため、マフォクシナイト採用率99.1%の実戦では**じめん以外の4タイプ（いわ・ゴースト・みず・あく）が実質の弱点**になります。上位ではミミッキュ（2位）のかげうち（ゴースト）97.5%、カバルドン（3位）のじしん（じめん、ふゆうで無効）98.4%、ギャラドス（8位）のたきのぼり（みず）80.1%が代表的な脅威です。

### 特性

メガ進化前は**もうか（90.3%）**が固定。HPが最大HPの1/3以下になるとほのおタイプの技の威力が1.5倍になります。もう一つの選択肢である**マジシャン（9.7%）**は道具を持っていない時に技を当てた相手の道具を奪う特性です。メガ進化後は**ふゆう**に変わり、じめん技・まきびし・どくびし・ねばねばネットが効かなくなります。マフォクシナイト採用率99.1%の環境では、実戦で機能するのはほぼ常にふゆうです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">84.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技のメインウェポン。10%でやけど付与。はがね・くさタイプに一致補正で通す（いわタイプには半減）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マジカルシャイン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">63.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう・ドラゴンへの打点。カバルドン・ギャラドス等ほのお・エスパーが通らない相手を補完</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコキネシス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">56.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10%で相手の特防を1段階下げる。かくとう・どくへの一致打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みがわり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>42.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分のHP1/4を消費し設置。先制技・状態異常を透かしながら安全にターンを進める</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコショック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>39.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のぼうぎょ実数値で計算。とくぼうが高い受け寄りの相手に効果的</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わるだくみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>39.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自身のとくこうを2段階上昇。積んだ後の打点は大きく伸びるが隙を晒す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を直前の技に固定。積み技・補助技を封じてみがわりを安全に張り直す起点になる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マジカルフレイム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の特攻を1段階下げる。かえんほうしゃより低威力だが特殊アタッカーの後続を弱体化できる</td>
</tr>
</tbody>
</table>
</div>

---

## M-4の採用型

### 型1：特殊アタッカー型（おくびょう 80.9%）

**性格採用率: おくびょう 80.9%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0655-00.webp" alt="メガマフォクシー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（90.3%）→メガ後ふゆう<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（最多EV分布）<br>
<strong>持ち物:</strong> マフォクシナイト（99.1%）
</div>
<div>
<strong>技構成:</strong><br>
・かえんほうしゃ<br>
・マジカルシャイン<br>
・サイコキネシス（サイコショック）<br>
・みがわり（わるだくみ）
</div>
</div>
</div>

かえんほうしゃ（ほのお・威力90）とマジカルシャイン（フェアリー・威力80）が主軸の一致技。サイコキネシス（エスパー・威力90）とサイコショック（エスパー・相手のぼうぎょ実数値でダメージ計算）は採用率が拮抗しており、相手の特殊耐久が高い相手にはサイコショックが刺さります。みがわり（42.3%）は先制技やこおり技を透かしながら、わるだくみ（39.6%）採用時はとくこうを2段階上げて後続の打点を伸ばす選択です。

**強み:**

おくびょうはH152 / A80 / B92 / C211 / D145 / S204。S204は環境上位のスカーフ非採用勢の多くより高い数値で、みがわりを安全に設置しやすい速度です。

**弱み:**

C211は最速に振った代償として、ひかえめ型のC232と比べ確定数がやや伸びにくい場面があります。

---

### 型2：高火力型（ひかえめ 18.0%）

**性格採用率: ひかえめ 18.0%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0655-00.webp" alt="メガマフォクシー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ひかえめ 高火力型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（90.3%）→メガ後ふゆう<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（代表例）<br>
<strong>持ち物:</strong> マフォクシナイト
</div>
<div>
<strong>技構成:</strong><br>
・かえんほうしゃ<br>
・マジカルシャイン<br>
・サイコキネシス<br>
・わるだくみ
</div>
</div>
</div>

技構成はおくびょう型と共通で、性格による実数値の違いだけが型の差になります。

**強み:**

ひかえめはH152 / A80 / B92 / C232 / D145 / S186。C232はおくびょう型のC211より約10%高く、乱数で1発多く削れる場面が生まれます。

**弱み:**

S186はおくびょう型のS204より低く、上から動ける相手の範囲が狭まります。みがわりを安全に置ける対面が減る点がトレードオフです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">81.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>84.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.8pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マジカルシャイン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">42.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>63.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+21.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコキネシス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">52.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">56.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+4.2pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みがわり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>42.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+12.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコショック</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">44.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.1pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">51.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-11.8pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アンコール</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-7.8pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさむすび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-7.2pp</td>
</tr>
</tbody>
</table>
</div>

M-4の最大変化は**マジカルシャインの+21.6pp（42.1%→63.7%）**です。M-3上位でカバルドン（じめん/採用率3位）・ギャラドス（みず/8位）が上位に定着し、これらへの一致打点にならないほのお・エスパーを補う打点としてフェアリー技の需要が高まった動きと一致します。一方でわるだくみは-11.8ppと下落しており、積みよりみがわり（+12.1pp）を優先して対面操作を安定させる構築思考へのシフトがうかがえます。

---

## データ分析②：S204は「苦手なポケモン」相手にも上から動けるか

苦手なポケモンとして挙げたミミッキュ・ガブリアス・カバルドン・アシレーヌ・ギャラドスについて、実際の持ち物採用率とすばやさ種族値からスカーフ非採用時の最速実数値を確認しました。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ種族値</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">最速おくびょう想定S</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ミミッキュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">96</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">データ上ごく少数（上位5枠外）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">162</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">102</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">169</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">カバルドン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">47</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">0.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">108</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">データ上ごく少数（上位5枠外）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">123</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">81</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">データ上ごく少数（上位5枠外）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">146</td>
</tr>
</tbody>
</table>
</div>

ガブリアスのスカーフ採用率19.8%を除けば、いずれもスカーフ採用は少数派で、非スカーフの最速実数値はすべておくびょう型マフォクシーのS204を下回ります。つまりマフォクシーは「決定打を欠く」相手であっても、多数派の型に対しては先に動いてみがわりを張る、あるいは弱点を突かれる前に交代を選ぶ、といった主導権を握れる立場にあります。ただしガブリアスは約2割がスカーフを採用するため、この相手に限っては後手に回る可能性を常に考慮する必要があります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち（ゴースト・採用率97.5%）が×2弱点。こちらのほのお・エスパー・フェアリー技はいずれもミミッキュに等倍止まりで、ばけのかわを剥がしても決定打に欠けます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率98.4%）はふゆうで無効化できますが、こちらの技もカバルドンに等倍止まりで、あくび（94.0%）による交代圧力とH・B両方の高い耐久を崩し切れません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア（みず・採用率88.2%）・先制のアクアジェット（みず・74.6%）がいずれも×2弱点。こちらのほのお技はみず/フェアリー複合に半減、エスパー・フェアリー技は等倍止まりで押し切れません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼり（みず・採用率80.1%）が×2弱点。じしん（77.8%）はふゆうで無効化できますが、りゅうのまい後のたきのぼりは一撃が重く、こちらのほのお技はみず/ひこう複合に半減で、決定打を欠きます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハイドロポンプ（みず・採用率99.0%）が×2弱点。おにび（75.5%）でやけどを負うと物理方面の火力がさらに落ち、こちらのほのお技もでんき/みず複合には半減です</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でマフォクシーと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" loading="lazy">
    <div class="name">アローラキュウコン</div>
    <div class="rate">9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" loading="lazy">
    <div class="name">ウォッシュロトム</div>
    <div class="rate">10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、マフォクシーの弱点であるいわ・みずをじしん・げきりん等の打点で牽制します。ガブリアスの弱点はフェアリー（×2）とこおり（×4）ですが、マフォクシーがカバーできるのはマジカルシャイン（フェアリー）のみで、こおり技は持たないため×4弱点は補えません。フェアリー方面に限った補完関係です。

**ミミッキュ**（2位）はゴースト/フェアリーで、つるぎのまいで積んだかげうちが、マフォクシーが決定打を欠く高耐久の相手を押し切る役割を担います。ただしマフォクシーのほのお・エスパー・フェアリー技はいずれもミミッキュに等倍止まりで、ミミッキュの弱点を突く打点はマフォクシー側にありません。役割分担は「ミミッキュの一致打点で押し切る／マフォクシーが別の相手を処理する」という住み分けです。

**マスカーニャ**（3位）はくさ/あくで、マフォクシーが苦手なあくタイプの相手をはたきおとす・ふいうちで処理できる役割分担です。

**ブリジュラス**（4位）ははがね/ドラゴンで、マフォクシーのかえんほうしゃ・マジカルシャインはいずれもブリジュラスに等倍です。ブリジュラスのラスターカノン（はがね一致）・りゅうせいぐん（ドラゴン一致）がマフォクシーの打点範囲外の相手を処理する役割分担で、タイプ相性で互いを補い合う関係ではありません。

**アシレーヌ**（5位）はみず/フェアリーで、マフォクシーの弱点であるみずタイプの相手をアシレーヌが受け持つ役割分担です。

---

## まとめ

M-4のマフォクシーは使用率9位へ浮上し、M-3の16位から大きく順位を上げたシーズンです。

- **マジカルシャインが+21.6pp（42.1%→63.7%）で最大の技採用率の変化**：カバルドン・ギャラドスなど上位に定着したじめん・みずタイプへの打点として需要が高まった
- **みがわりが+12.1pp（30.2%→42.3%）で対面操作を重視する構築思考へシフト**：わるだくみは-11.8ppと下落
- **メガ進化後の特性ふゆうがじめん技を無効化**：使用率1位のガブリアス・3位のカバルドンが持つじしん（採用率99.5%・98.4%）を実質無効にできる、タイプ相性表だけでは見えない安定感がある

ほのお/エスパーの一致技に加えマジカルシャインで打点を広げつつ、ふゆうでじめん技を無効化する立ち回りが基本線です。一方でいわ・ゴースト・みず・あくの4タイプは弱点のまま残るため、ミミッキュ・アシレーヌ・ギャラドスといった上位のみず・ゴーストタイプには決定打を欠く場面がある点は変わりません。

---

*関連記事：[メガメタグロス考察 M-4](/blog/metagross-analysis-m4/)*
