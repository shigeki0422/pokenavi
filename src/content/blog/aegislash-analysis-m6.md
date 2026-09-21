---
title: '【ポケモンチャンピオンズ】ギルガルド 考察 M-6 シーズン バトルスイッチとフォルムチェンジの立ち回り'
description: 'M-6シーズン使用率13位のギルガルドを考察。はがね/ゴーストの複合タイプとバトルスイッチによるフォルムチェンジの仕組み、シャドーボール採用率+20.2pp・れいせい採用率+17.0ppなどM-5からの分布変化、型を問わず結果が一致した得意/苦手をデータで解説します。'
pubDate: '2026-09-21'
updatedDate: '2026-09-21'
heroImage: '../../assets/hero-aegislash-m6.png'
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
  <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" />
  <div>
    <h2 style="margin:0 0 8px">ギルガルド</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">13位</strong>（M-5: 23位）　特性: <strong>バトルスイッチ 100.0%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位・技/持ち物/性格/EV/同居率の詳細データは2026-09-17時点のスナップショットを使用しています。

※本記事の苦手/得意な相手の確定数分析は、対戦エンジン上でバトルスイッチによるフォルムチェンジ（攻撃技を出すとブレードフォルム、キングシールドでシールドフォルムに戻る）をターン進行に沿ってそのまま計算した結果を使用しています。

M-6シーズンのギルガルドは使用率13位。M-5終盤の23位から順位を上げています。はがね/ゴーストの複合タイプに、特性バトルスイッチによるフォルムチェンジ（攻撃技でブレードフォルム、キングシールドでシールドフォルムに切り替わる）を軸に、攻めと守りを1体で使い分ける立ち回りが特徴です。使用率上昇の背景にある技・持ち物・性格の分布変化は後述のデータ分析で詳しく扱います。

---

## ギルガルドの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:23%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:19%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong style="color:#dc2626">140</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:19%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong style="color:#dc2626">140</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:23%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">500</span>
  </div>
</div>

上記はシールドフォルム（デフォルト状態）の種族値です。B140・D140と防御面が突出する一方、A50・C50と攻撃面は低く見えますが、バトルスイッチによってフォルムごとにA/CとB/Dが入れ替わります。詳細は次表のとおりです。

### 種族値（ブレードフォルム）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:23%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong style="color:#dc2626">140</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:19%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong style="color:#dc2626">140</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:19%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:23%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">500</span>
  </div>
</div>

バトルスイッチで攻撃技を選択した際のブレードフォルムの種族値です。合計種族値500自体はフォルムを問わず変わりません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はじめん・ゴースト・ほのお・あくの4タイプ（いずれも×2）。ひこう・いわ・はがね・くさ・エスパー・こおり・ドラゴン・フェアリーの8タイプが×0.5、さらにむしは×0.25、ノーマル・かくとう・どくは無効です。ノーマル・かくとう・どくの3タイプを無効化できるのは、はがね/ゴースト複合ならではの受けの強みです。使用率5位のメガグソクムシャの採用率29.4%のドリルライナー（じめん・威力80）はこの弱点じめんを突く技で、後述の苦手表のとおり実際にギルガルドが押し負ける相手のひとつです。

### 特性

<strong>バトルスイッチ（100.0%）</strong>が唯一の特性です。攻撃技を選択するとブレードフォルムに変化し（こうげき・とくこうが140、ぼうぎょ・とくぼうが50になります）、キングシールドを使うとシールドフォルムに戻ります（ぼうぎょ・とくぼう140、こうげき・とくこう50）。攻撃した直後はぼうぎょ・とくぼうが50まで下がるため、キングシールドで守りに戻すまでの間は脆さを抱えます。逆にキングシールドを使ったターンはこうげき・とくこうが50まで下がり打点を失う点も、物理型・特殊型を問わず共通です。攻めるターンと守るターンの選択が立ち回りの軸になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かげうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。物理技のためブレードフォルムのこうげきを参照する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>キングシールド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">82.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+4。相手の攻撃を防ぎシールドフォルムに戻る。接触技を防いだ場合は相手の攻撃を1段階下げる。連続使用で成功率が1/3に低下</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ポルターガイスト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">52.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト一致の高火力技。命中率90%で、相手が道具を持っていないと失敗する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">44.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊のゴースト一致技。ポルターガイストの失敗リスクを避けたい場面の主力</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>せいなるつるぎ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>35.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の能力変化を無視してダメージを与える。積み技を透かす際の保険</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>25.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげきを2段階上昇。積んだ後のかげうち・ポルターガイストが大幅に高火力化</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラスターカノン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね一致の特殊技。フェアリー等はがね耐性の薄い相手への打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">高威力だが使用後ぼうぎょ・とくぼうが1段階下がる。せいなるつるぎより選択率は低い</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：物理アタッカー型

**性格採用率: いじっぱり（全体の性格採用率42.7%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:48px;height:48px">
  <strong style="font-size:1.05em">物理アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> バトルスイッチ（100.0%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32-A32-B1-D1<br>
<strong>持ち物:</strong> たべのこし（49.5%）
</div>
<div>
<strong>技構成:</strong><br>
・かげうち<br>
・キングシールド<br>
・ポルターガイスト<br>
・つるぎのまい
</div>
</div>
</div>

つるぎのまいでこうげきを2段階上げてから、優先度+1のかげうち（ゴースト・威力40）と高火力のポルターガイスト（ゴースト・威力110、相手が道具を持っていないと失敗）で押し切る構成です。キングシールドで相手の攻撃を防ぎつつシールドフォルムに戻し、ぼうぎょ・とくぼう140の高耐久を活かして立て直す場面も作れます。

**強み:**

いじっぱり・EV H32-A32-B1-D1のブレードフォルム時のこうげき実数値は**211**（HP167・ぼうぎょ161〈シールドフォルム時〉）。型2（れいせい採用時のこうげき実数値160）の物理打点より51高いため、かげうち・ポルターガイストの確定数を縮められる場面が多くなります。

**弱み:**

ポルターガイストは相手が道具を持っていないと不発になる点に注意が必要です。技範囲を広げる選択肢としてインファイト（採用率14.5%、かくとう技）やアイアンヘッド（採用率14.2%、はがね技）がありますが、これらはいずれも優先度0の通常技で、優先度+1のかげうちと入れ替える形になるため、採用すると先制で削る手段を失います。

---

### 型2：特殊アタッカー型

**性格採用率: れいせい（全体の性格採用率34.9%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:48px;height:48px">
  <strong style="font-size:1.05em">特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> バトルスイッチ（100.0%）<br>
<strong>性格:</strong> れいせい（C↑ S↓）<br>
<strong>EV:</strong> H32-B1-C32-D1<br>
<strong>持ち物:</strong> たべのこし（49.5%）
</div>
<div>
<strong>技構成:</strong><br>
・かげうち<br>
・キングシールド<br>
・シャドーボール<br>
・せいなるつるぎ
</div>
</div>
</div>

シャドーボール（特殊・威力80）をメインに据えつつ、道具を持たない相手にも通るかげうち・せいなるつるぎを併用する構成です。ブレードフォルムではこうげき・とくこうが同時に140まで上がるため、れいせい補正でとくこうを伸ばしても、無振り・無補正のこうげきは実数値160残り、せいなるつるぎ（かくとう・威力90）を実戦的な打点として運用できます。

**強み:**

れいせい・EV H32-B1-C32-D1のブレードフォルム時のとくこう実数値は**211**（型1のこうげき211と同水準）。ポルターガイストが失敗する（道具を持たない）相手にもシャドーボールで確実にダメージを与えられる点が型1にはない利点です。

**弱み:**

こうげき実数値は160で型1の211より51低く、かげうちの一致技打点とせいなるつるぎの打点はいずれも型1に劣ります。またれいせい補正でS実数値が80→72に低下するため、S実数値72〜79の相手に対しては型1なら先手を取れる場面でも先手を取れなくなります。

---

## データ分析：M-5→M-6 採用データの変化

※M-5列のデータはM-5シーズン最終スナップショット（2026-09-09時点）、M-6列のデータは2026-09-17時点を使用しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-6</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>13位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">上昇</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>44.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+20.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラスターカノン採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>22.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+13.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">67.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">52.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-15.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいせい採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>34.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+17.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">58.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">42.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-15.9pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たべのこし採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+13.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いのちのたま採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-10.6pp</td>
</tr>
</tbody>
</table>
</div>

使用率23位から13位への上昇と同時に、技・性格・持ち物の分布が明確に「特殊型シフト」しています。シャドーボール（+20.2pp）とラスターカノン（+13.6pp）がともに増加し、性格もれいせい（+17.0pp）が伸びていじっぱり（-15.9pp）から一部が移行しました。ポルターガイストは依然として単独最多の物理技（52.7%）ですが、67.8%からは大きく減少しており、「道具を持たない相手には失敗する」というポルターガイストの弱点を、確実に通るシャドーボールで補う構築が増えたことが読み取れます。持ち物はたべのこし（+13.6pp）が一貫して伸び、いのちのたま（-10.6pp）は減少しており、反動を負う高火力運用よりも、キングシールドで場をつなぎながら長期戦を見据える運用が増加したと言えます。使用率の上昇は特定の1要素ではなく、これら複数の分布変化が重なった結果です。

持ち物採用率2位ののろいのおふだ（21.7%）は、ゴースト技の威力を1.2倍にするアイテムです。この1.2倍はかげうち・ポルターガイスト・シャドーボールなどゴースト技に限ってかかるもので、せいなるつるぎ（採用率35.9%、かくとう技）やラスターカノン（採用率22.3%、はがね技）、インファイト（採用率14.5%、かくとう技）といった非ゴースト技には乗りません。例えばウォッシュロトム（たべのこし想定）にはポルターガイストがたべのこし採用時で確定3発ですが、のろいのおふだ採用時は確定2発に縮まります。ギャラドス（ゴツゴツメット想定）も同様にたべのこし採用時の確定4発が、のろいのおふだ採用時は確定3発に縮まります。反面、先述のとおりブレードフォルムで被弾しやすい展開では採用にリスクも伴います。

---

## 苦手なポケモン

使用率TOP30の全ポケモンを対象に、対戦エンジンで自分・相手ともに採用率20%以上の主力技だけを使った1v1判定を行い、代表的な型を通じて結果が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は表に含めません）。持ち物はギルガルドがたべのこし、相手は最多採用の持ち物を前提としています。技名・採用率・確定数は判定結果をそのまま転記しています。データ基準日は2026-09-17です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位（ボーマンダナイト採用率97.7%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力技はポルターガイスト（採用率52.7%、確定2発）。メガボーマンダの主力じしん（採用率71.1%、じめん×2弱点）も確定2発と互角の発数ですが、S実数値172のメガボーマンダに対しS実数値80のギルガルドは後攻になるため先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力技はポルターガイスト（採用率52.7%、確定4発）。カバルドンの主力じしん（採用率97.7%、じめん×2弱点）は確定2発です。ギルガルド（S実数値80）はカバルドン（S実数値67）より速いものの、必要な発数自体で大きく劣るため先手を取っても倒し切れません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位（グソクムシャナイト採用率98.5%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力技はポルターガイスト（採用率52.7%、確定3発）。メガグソクムシャの主力ドリルライナー（採用率29.4%、じめん×2弱点）は確定2発で発数を上回ります。メガグソクムシャはであいがしら（採用率71.2%、優先度+2、登場ターンに最初に出す技でないと失敗）・ふいうち（採用率58.0%、優先度+1、相手が攻撃技を選んでいないと失敗）も持ち、素の速さ（S実数値60）でギルガルドに劣っても発動条件が揃えば先制技で行動順を覆すため、確定数・先制技の両面で押し切られる展開があります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力技はポルターガイスト（採用率52.7%、確定2発）。ゴリランダーの主力はたきおとす（採用率67.5%、あく×2弱点）も確定2発と互角ですが、S実数値107のゴリランダーに対しS実数値80のギルガルドは後攻になるため先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力技はポルターガイスト（採用率52.7%、確定4発）。ギャラドスの主力じしん（採用率44.8%、じめん×2弱点）は確定3発で発数を上回ります。S実数値101のギャラドスに対しS実数値80のギルガルドは後攻にもなり、発数・速度の両面で不利です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位（リザードナイトX採用率25.8%）<sup>※</sup></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力技はポルターガイスト（採用率52.7%、確定2発）。メガリザードンXの主力フレアドライブ（採用率24.6%、ほのお×2弱点）は確定1発で上回ります。S実数値167のメガリザードンXに対しS実数値80のギルガルドは先手を取れず、そのまま1発で沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位（リザードナイトY採用率72.8%）<sup>※</sup></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力技はポルターガイスト（採用率52.7%、確定2発）。メガリザードンYの主力かえんほうしゃ（採用率50.8%、ほのお×2弱点）も確定1発で上回ります。S実数値152のメガリザードンYに対しS実数値80のギルガルドは先手を取れず、そのまま1発で沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0009-00.webp" alt="メガカメックス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガカメックス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位（カメックスナイト採用率96.7%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力技はポルターガイスト（採用率52.7%、確定2発）。メガカメックスの主力あくのはどう（採用率81.3%、あく×2弱点）も確定2発と互角ですが、S実数値128のメガカメックスに対しS実数値80のギルガルドは後攻になるため先に沈められます</td>
</tr>
</tbody>
</table>
</div>

<p style="font-size:0.85em;color:#666;margin-top:8px">※ 使用率データはリザードンを1体として集計しており、メガリザードンXとYを個別に区別していません。両者とも母種としての使用率順位は17位です。</p>

8体は3パターンに分かれます。メガボーマンダ・ゴリランダー・メガカメックスの3体は「確定数は互角だが後攻になる」ケース、カバルドン・メガグソクムシャ・ギャラドスの3体は確定数自体で上回られるケース、メガリザードンX・Yの2体は速さ・確定数の両方で上回られるケースです。S実数値72〜80のギルガルドは環境上位の多くに素早さで劣るため、発数を縮められない相手には撃ち合い負けしやすい構造です。特にメガリザードンX・Yのような一致技で確定1発を取れる相手には、後出しした時点で崩されます。

---

## 得意なポケモン

使用率TOP30の全ポケモンを対象に、対戦エンジンで自分・相手ともに採用率20%以上の主力技だけを使った1v1判定を行い、代表的な型を通じて結果が一致した相手のみを掲載します（型によって結果が分かれる相手は表に含めません）。持ち物はギルガルドがたべのこし、相手は最多採用の持ち物を前提としています。技名・採用率・確定数は判定結果をそのまま転記しています。データ基準日は2026-09-17です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（採用率44.3%、確定4発）。アシレーヌの主力うたかたのアリア（採用率92.0%、確定4発）と互角の発数ですが、双方が持つ優先度+1の先制技（かげうち／アクアジェット66.9%）の撃ち合いをギルガルドが制して押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガルカリオ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（ルカリオナイトZ採用率90.5%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト（採用率52.7%、確定2発）。メガルカリオの主力あくのはどう（採用率76.2%、あく×2弱点）は確定3発にとどまり、S実数値223のメガルカリオに先手を取られても、発数差でギルガルドが先に沈めます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">せいなるつるぎ（採用率35.9%、確定3発）。ブリジュラスの主力りゅうせいぐん（採用率69.8%）は確定圏外にとどまり、決め手を欠いて先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト（採用率52.7%、確定1発）。サーフゴーの主力シャドーボール（採用率99.0%）は確定2発にとどまり、S実数値136のサーフゴーに先手を取られてもギルガルドが1発で沈めます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト（採用率52.7%、確定3発）。アーマーガアの主力ブレイブバード（採用率30.5%、ひこう×0.5耐性）は確定圏外で、着実に押し切れます<sup>※</sup></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラスターカノン（採用率22.3%、確定2発）。キラフロルの主力だいちのちから（採用率61.3%、じめん×2弱点）は確定3発にとどまり、S実数値151のキラフロルに先手を取られても発数差でギルガルドが先に沈めます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト（採用率52.7%、確定1発）。イダイトウ(オス)の主力ウェーブタックル（採用率96.7%）は確定2発にとどまり、こだわりスカーフでS実数値214まで上げてギルガルド（S実数値80）より先制されても、後手からでも1発で沈められます（相手のウェーブタックルは確定2発のため、先制1発は耐えます）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト（採用率52.7%、確定1発）。オオニューラの主力じごくづき（採用率50.9%、あく×2弱点）は確定3発にとどまり、S実数値172のオオニューラに先手を取られてもギルガルドが1発で沈めます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">せいなるつるぎ（採用率35.9%、確定2発）。イエッサン(オス)の主力マジカルフレイム（採用率90.4%）は確定4発にとどまり、S実数値147のイエッサン(オス)に先手を取られても発数差でギルガルドが先に沈めます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラスターカノン（採用率22.3%、確定1発）。アローラキュウコンの主力ふぶき（採用率61.2%、こおり×0.5耐性）は確定圏外で、着実に押し切れます<sup>※</sup></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト（採用率52.7%、確定3発）。ウォッシュロトムの主力ハイドロポンプ（採用率98.2%）は確定5発にとどまり、決め手を欠いて先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト（採用率52.7%、確定2発）。パーモット（S実数値172）はギルガルドより大幅に速く先手を取られますが、主力でんこうそうげき（採用率93.4%）は確定圏外にとどまり、後手からでも2発で沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガメタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位（メタグロスナイト採用率94.2%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト（採用率52.7%、確定2発）。メガメタグロスの主力じしん（採用率51.0%）も確定2発と互角のため、S実数値162のメガメタグロスに先手を取られると通常はポルターガイスト2発が間に合いません。ただしギルガルドは優先度+1のかげうち（採用率96.3%）を持ち、ポルターガイストで大きく削った後にかげうちで先制フィニッシュできるため、優先度技で押し切れます</td>
</tr>
</tbody>
</table>
</div>

<p style="font-size:0.85em;color:#666;margin-top:8px">※ アーマーガア（はねやすめ採用率99.1%）・アローラキュウコン（アンコール採用率73.8%）は、上記の主力攻撃技だけを使った検証結果です。これらの補助技を絡めて使われた場合は結論が変わりうる点に注意してください。</p>

なお、使用率上位のガブリアス（2位）・セグレイブ（7位）・ミミッキュ（11位）・マスカーニャ（12位）・エースバーン（20位）・ゲッコウガ（22位）・ウルガモス（25位）・カイリュー（30位）・ラウドボーン（28位）は、ギルガルドの型（物理アタッカー型／特殊アタッカー型）によって勝敗が入れ替わるため、苦手・得意いずれの表にも含めていません。

---

## 同居率上位の分析

M-6でギルガルドと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" loading="lazy">
    <div class="name">ゴリランダー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ボーマンダ**（1位）はドラゴン/ひこうで、じめん技を無効化できます。逆にボーマンダの弱点であるこおり（×4）はギルガルドが半減で受けられるため、じめん・こおりを持つ相手への受け出し先を分担できる組み合わせです。

**カバルドン**（2位）はじめん単タイプで、ギルガルドが等倍でしか受けられないでんき技を無効化できます。逆にカバルドンの弱点であるこおり・くさはギルガルドが半減で受けられるため、でんき・こおり・くさを持つ相手への受け出し先を分担できます。

**ガブリアス**（4位）はドラゴン/じめんで、弱点であるこおり（×4）とドラゴン（×2）の技をギルガルドが半減で受けられます。逆にギルガルドの弱点であるほのおをガブリアスは半減で受けられるため、こおり・ドラゴン・ほのおを持つ相手への受け出し先を分担できる組み合わせです。

**グソクムシャ**（5位）は通常個体はむし/みずですが、グソクムシャナイトの採用率が98.5%とほぼ全個体がメガ進化し、メガ後はむし/はがねに変化します。メガ後のいわは弱点（×2）から等倍に改善し、じめんも半減ではなく等倍で、ギルガルドとの弱点分担は限定的です（じめんの受け出し先はカバルドンやボーマンダが担当）。一方でメガ後のグソクムシャはどくが無効、ノーマル・エスパー・フェアリーが半減と複数タイプに耐性を持ち、ギルガルドが0.25倍で強く受けるむしをメガグソクムシャも0.5倍で半減できるなど、互いに得意分野が異なるタイプ構成です。

**マスカーニャ**（7位）はくさ/あくで、弱点であるこおりをギルガルドが半減で受けられます。逆にギルガルドの弱点であるあくをマスカーニャは半減で受けられるため、こおり・あくを持つ相手への受け出し先を分担できます。

---

## まとめ

M-6のギルガルドはM-5終盤の23位から13位へ使用率を伸ばしました。バトルスイッチによるフォルムチェンジ（攻撃でブレードフォルム、キングシールドでシールドフォルム）を軸にした基本構造は変わっていませんが、技・性格・持ち物の分布は明確に変化しています。

- **使用率23位→13位**：M-5終盤からの上昇が続き、使用率上位圏に到達しています
- **シャドーボール+20.2pp・ラスターカノン+13.6pp・れいせい+17.0pp**：ポルターガイストの失敗リスク（相手が道具を持たない場合に不発）を避けられる特殊型が増加しています
- **たべのこし+13.6pp・いのちのたま-10.6pp**：反動を負う高火力運用より、キングシールドで場をつなぐ長期戦志向が強まっています

物理型・特殊型いずれもブレードフォルムのこうげき・とくこうが同時に140まで上がる特性のため、一致技以外にせいなるつるぎのような補完技も実用的な打点になります。じめん・ゴースト・ほのお・あくの4弱点は環境上位に広く存在するため、選出段階でのケアは引き続き必要です。

---

関連記事：[アシレーヌ M-6考察](/blog/primarina-analysis-m6/)
