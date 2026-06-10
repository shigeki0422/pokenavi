---
title: '【ポケモンチャンピオンズ】メガフシギバナ考察 M-2 使用率27位 耐久型の技採用率と立ち回り'
description: 'M-2シングルバトルで使用率27位のメガフシギバナを徹底分析。あついしぼうでほのお・こおりを等倍化し、こうごうせい＋ギガドレインで居座る耐久アタッカー。だいちのちから88%・こうごうせい73%など実データから型と苦手な相手、相性の良いパートナーを解説します。'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-venusaur-m2.png'
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
  <img src="/images/pokemon/pokemon-0003-00.webp" alt="メガフシギバナ" />
  <div>
    <h2 style="margin:0 0 8px">メガフシギバナ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">27位</strong>　メガ石採用率: <strong>フシギバナイト 93.2%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、フシギバナは**使用率27位**。そのうち**93.2%がフシギバナイトを採用**しており、ほぼメガ進化前提の構成です。

メガフシギバナの核は特性**あついしぼう**。本来×2で弱点を突かれるほのお・こおりが等倍まで軽減され、くさ/どくの数少ない弱点を大幅に減らせます。こうげき以外の全ステータスが100以上の高い総合耐久に、こうごうせい（HP回復）とギガドレイン（吸収）を重ねた**居座り型のアタッカー**として運用されます。

---

## メガフシギバナがM-2で機能する理由

### 1. あついしぼうでくさ/どくの弱点を2つに絞る

くさ/どくは素のままだとほのお・こおり・エスパー・ひこうの4弱点を持ちますが、**あついしぼうがほのお・こおりを等倍化**するため、残る弱点はエスパーとひこうの2つだけになります。本来×2のほのお技が等倍で済むことで、特殊ほのお技に一撃で落とされず、こうごうせい・ギガドレインで回復しながら居座る土台になります（ただしほのおにひこうを併せ持つリザードンはエアスラッシュで弱点×2を突いてくるため受けは成立しません。後述の苦手な相手を参照）。

### 2. こうごうせい＋ギガドレインで居座って削る

メガ後のとくぼう120・ぼうぎょ123という高耐久に、**こうごうせい（採用率72.7%）**でHPを最大1/2回復し、さらに**ギガドレイン（56.9%）**で与ダメージの半分を吸収します。みず・じめん・でんきの多い相手に受け出してギガドレインで体力を回復しながら居座る運用が成立し、削り合いで優位に立てます。

### 3. やどりぎのタネ・どくどくで受けに強い

**やどりぎのタネ（58.5%）**や**どくどく（13.1%）**で定数ダメージを入れる選択肢を持ち、こうごうせいの回復と合わせて高耐久ポケモンを時間をかけて崩せます。攻撃技だけで落としにくいアーマーガア・カバルドンのような相手にも、定数ダメージで対抗できるのが耐久型ならではの強みです。

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:61.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">123</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:61%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">122</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">120</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">625</span>
  </div>
</div>

ぼうぎょ123・とくぼう120・HP80と耐久が高く、とくこう122で攻撃も両立します。一方すばやさ80は環境の主要アタッカー（ガブリアスS102・マスカーニャS123・ゲッコウガS122等）に軒並み先手を取られる速度で、**先手で殴る型ではなく、受けて回復しながら削る耐久型**として運用するのが基本です。

### メガ前→メガ後ステータス変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ前</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ後</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">82</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+18</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">83</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#2563eb">123</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+40</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">122</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+22</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#2563eb">120</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+20</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
</tbody>
</table>
</div>

メガ進化でぼうぎょ+40・とくぼう+20と耐久が大きく伸び、特性も非メガのようりょくそ（採用率69.8%）から**あついしぼう**に変わります。素早さは80のまま据え置きで、メガ後も後手から動く前提は変わりません。

### タイプ・弱点（あついしぼう適用）

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="くさ" />
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="どく" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なし</td>
</tr>
</tbody>
</table>
</div>

くさ/どくは本来ほのお・こおり・エスパー・ひこうの4弱点を持ちますが、あついしぼうでほのお・こおりが等倍になり、実質的な弱点はエスパー・ひこうの2つに絞られます。みず・でんき・かくとう・フェアリーを半減、くさを4分の1まで軽減し、受け出しできる範囲が広いのが特徴です。残るエスパー・ひこうは環境にメガマフォクシー（サイコショック・サイコキネシス、S134）・メガスターミー（しねんのずつき、S120）といった速いエスパー使いや、リザードン（エアスラッシュ、S100）・アーマーガア（ブレイブバード）といったひこう技持ちがいるため、この2タイプの相手には注意が必要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>だいちのちから</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">88.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最多採用。一致技を半減するはがね・どく・ほのおに×2の貫通打点。低確率でDダウン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こうごうせい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">72.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP回復技。晴れ下では回復量が2/3に増える。居座りの軸</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>やどりぎのタネ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>58.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">毎ターン相手HPを吸収。くさ無効の相手には入らない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ギガドレイン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>56.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">与ダメージの半分を回復。みず・じめん・いわに刺さる一致技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロばくだん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>55.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どく一致技。くさ・フェアリーに刺さる。30%毒</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロウェーブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロばくだんの代替どく技。10%とくこうダウン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくどく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">猛毒で高耐久を崩す。攻撃技で落としにくい相手用</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねむりごな</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中75で相手を眠らせる。くさ無効の相手には入らない</td>
</tr>
</tbody>
</table>
</div>

採用率の上位を**だいちのちから（88.4%）・こうごうせい（72.7%）・ギガドレイン（56.9%）・ヘドロばくだん（55.0%）**が占め、攻撃2枠＋回復＋どく技という耐久アタッカーの構成がほぼ固定化しています。やどりぎのタネ・どくどく・ねむりごなは、攻撃枠を1つ削って起点作り・崩しに寄せたい場合の選択肢です。

---

## 主要型の解説

性格はおだやか（D↑）・ずぶとい（B↑）・ひかえめ（C↑）の3種が大半を占め、どの耐久に寄せるかで型が分かれます。いずれもすばやさを伸ばさず、HPを最大まで振る耐久型です。

### 型1: HD特殊受け型（最多採用）

**性格採用率: おだやか 39.9%**（D↑。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0003-00.webp" alt="メガフシギバナ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HD特殊受けおだやか型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ようりょくそ（69.8%）<br>
<strong>性格:</strong> おだやか（D↑ A↓）<br>
<strong>EV:</strong> H32 D32（最多型。余り2はBに）<br>
<strong>持ち物:</strong> フシギバナイト
</div>
<div>
<strong>技構成:</strong><br>
・だいちのちから<br>
・ギガドレイン<br>
・こうごうせい<br>
・やどりぎのタネ / ヘドロばくだん
</div>
</div>
</div>

**強み:**

あついしぼうでほのおを等倍にしつつ、おだやかでとくぼうをさらに伸ばすことで、ラウドボーンのフレアソングやウルガモスのほのおのまいといった特殊ほのお技を受けやすくなります。みず・でんきの特殊アタッカー（アシレーヌ・ウォッシュロトム等）にも受け出しでき、ギガドレインとこうごうせいで回復しながら居座れます。

**弱み:**

ぼうぎょに振らないため、HB型に比べてガブリアスのじしん（等倍）など物理打点をやや受けにくくなります。物理アタッカーの多い相手には次のHB型が向きます。

---

### 型2: HB物理受け型（2番目に多い構成）

**性格採用率: ずぶとい 32.9%**（B↑。おだやかに次ぐ2番手）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0003-00.webp" alt="メガフシギバナ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HB物理受けずぶとい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ようりょくそ（69.8%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32 B32（余り2はDに）<br>
<strong>持ち物:</strong> フシギバナイト
</div>
<div>
<strong>技構成:</strong><br>
・だいちのちから<br>
・ギガドレイン<br>
・こうごうせい<br>
・やどりぎのタネ / どくどく
</div>
</div>
</div>

**強み:**

ずぶといでぼうぎょを伸ばし、ガブリアス・カバルドンなど物理じめん・物理アタッカーを受けやすくなります。じめん技はくさ/どくに等倍ですが、ぼうぎょ実数値を上げてギガドレイン（みず・じめん・いわに×2）とこうごうせいで撃ち合えば、削り合いで優位に立てます。

**HD型との使い分け:**

HD型が特殊ほのお・みず・でんきの受け出しに強いのに対し、HB型はガブリアスのじしんやマスカーニャのトリプルアクセル（物理こおり、あついしぼうで等倍）など**物理アタッカーへの受け出し**に寄せた型です。環境にどちらのアタッカーが多いかで選びます。

**弱み:**

とくぼうに振らないため、メガマフォクシーのサイコショック（特殊だが防御で受ける技）以外の特殊エスパー技や、特殊ほのおの集中をHD型ほど受けきれません。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位（TOP30目安）のうち、メガフシギバナと相性がはっきり出るポケモンを有利・不利の両面から挙げます。攻撃面の倍率はだいちのちから（じめん）・ギガドレイン（くさ）・ヘドロばくだん（どく）を基準に、防御面はあついしぼう適用後の倍率で判定しています。

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
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロばくだんがフェアリーに×2。主力のうたかたのアリア（みず・79%）・ムーンフォース（フェアリー・97%）はどちらも×0.5半減で、ギガドレインで回復しつつ撃ち合える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0009-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カメックス（30位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギガドレインがみずに×2、みずのはどう（78%）は×0.5半減で受け出ししやすい。ただしあくのはどう（79%）は等倍特殊、からをやぶる（68%）で積まれると突破され得るため、積む前に削るのが前提</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギガドレインが×2（じめん）で刺さり、低速のため受け出ししやすい。じしんは等倍止まりで耐え、やどりぎ・どくどくで高耐久も崩せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギガドレインは等倍（くさ→ドラゴン0.5×じめん2）だが吸収で居座れる。じしん（99%）も等倍で耐え、いわなだれ・がんせきふうじも等倍。S102で先手を取られるため、HB型で受けつつ削る形になる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちからが×2（あく1×はがね2）。あく技は等倍、先制技ふいうち（99%）も等倍で大打撃にならず、低速のため受けやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちからはひこう無効で×0、ギガドレイン×0.5・ヘドロばくだん×0（はがね）と打点が皆無。ブレイブバード（ひこう・19%）は弱点×2。どくどくも入らず崩せない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あついしぼうでほのおは等倍だが、エアスラッシュ（ひこう・33%）は弱点×2。S100で先手を取られ、こちらの打点はギガドレイン×0.25・ヘドロばくだん×1止まりで決め手に欠ける</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

エスパー・ひこうで弱点を突けるアタッカー、または攻撃打点が乏しく崩しきれない相手を中心に挙げます。

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
    <img src="/images/pokemon/pokemon-0655-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガマフォクシー（25位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S134で先手を取られ、サイコショック（50%）・サイコキネシス（38%）など一致エスパー技が×2弱点。わるだくみ（40%）で積まれると回復が追いつかない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくタイプ（ドドゲザン・ブラッキー等）を同伴し、エスパー技を無効化できる枠で受けて処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3つの攻撃技すべてが半減以下（だいちのちからは無効）で有効打がなく、はねやすめ（98%）で回復され崩せない。ブレイブバードは弱点×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおタイプ（ソウブレイズのむねんのつるぎ等。はがねの弱点を×2で突ける）を同伴し、後出しして処理する。どくどくも入らないため自力では落とせない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こちらの攻撃技はギガドレイン×0.25・ヘドロばくだん等倍・だいちのちから等倍と決定打がなく、あさのひざし（64%）で回復されて崩せない。ちょうのまい（97%）で積まれるとほのおのまい（80%）で押し切られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みずタイプ（ギャラドスのたきのぼり・カメックスのみずのはどう等。ほのおに×2）を同伴し、ちょうのまいで積む前に弱点を突いて落とす</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エアスラッシュ（ひこう・33%）が×2弱点でS100から先制される。こちらの打点はギガドレイン×0.25・ヘドロばくだん等倍で押し切れない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ・でんき・みずタイプ（ウォッシュロトム等）を同伴し、リザードンに後出しして弱点を突いて処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ラウドボーン（29位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから×2が通るがHP104・高耐久で一撃が遠く、なまける（96%）で回復され、どくどくを入れても回復で押し返される。ほのお技フレアソング（99.6%）を等倍で撃たれ続け、ギガドレイン×0.5の吸収では削り負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわ・じめんタイプ（カメックス・ガブリアス等）を同伴し、ほのお/ゴーストの弱点を突いて処理を任せる</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0937-00.webp" alt="ソウブレイズ">
    <div class="name">ソウブレイズ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお/ゴースト。ポルターガイスト・かげうちがエスパーに×2。フシギバナが苦手なメガマフォクシーのエスパー枠を後続から処理</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ">
    <div class="name">ゲッコウガ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S122の高速アタッカー。フシギバナが受けで止めた相手を上から削る速攻枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">いわ技でフシギバナが苦手なリザードン・ウルガモスのほのお枠に×4打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでひこう・エスパーを半減し、フシギバナの弱点を後続で補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー">
    <div class="name">ブラッキー</div>
    <div class="rate">同居率8位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高耐久あく枠。フシギバナが苦手なメガマフォクシーのエスパー技を無効化して受ける</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガフシギバナは弱点がエスパー・ひこうの2つに絞られる代わりに、その2タイプを速い使い手に突かれると脆く、アーマーガアのような打点皆無の相手も自力では崩せません。残り5体で以下を補います。

1. **エスパー対策**: あくタイプのブラッキーでメガマフォクシー・メガスターミーのエスパー技を無効化して受け、ソウブレイズのゴースト技（ポルターガイスト等は×2）で上から削る枠
2. **ひこう対策**: でんき技でリザードンを処理（ウォッシュロトムの10まんボルトはほのお/ひこうのリザードンに×2、いわ×4の打点も刺さる）。アーマーガアははがねが弱点のほのおタイプ（ソウブレイズ等）で処理する
3. **崩し性能の補完**: ゲッコウガ等の高速アタッカーで、受けで止めた相手を上から落とす速攻枠

---

## データ分析①：技採用率に表れる「攻撃型ではなく耐久型」という設計

メガフシギバナの技採用率は、攻撃技より**回復・搦め手の比率が高い**点に特徴があります。

| 役割 | 技 | 採用率 |
|---|---|---|
| 攻撃（一致以外の主軸） | だいちのちから | 88.4% |
| 回復 | こうごうせい | 72.7% |
| 定数ダメージ | やどりぎのタネ | 58.5% |
| 攻撃＋回復 | ギガドレイン | 56.9% |
| 攻撃（一致どく） | ヘドロばくだん | 55.0% |

攻撃技で最も高いのはだいちのちから（88.4%）ですが、次点にこうごうせい（72.7%）が入り、3番目のやどりぎのタネ（58.5%）と4番目のギガドレイン（56.9%）は**いずれもHPを回復しながら戦う技**です。つまり技スロットの過半が「居座って回復し続ける」ことに割かれており、攻撃を一致技2枠（くさ・どく）に絞ってもなお回復・搦め手を優先する構成が主流だと分かります。

これはとくこう122という決して低くない攻撃力を持ちながら、すばやさ80では先手で殴り切れないため、**回復で受けのターンを稼ぎ、定数ダメージとギガドレインで時間をかけて削る**という設計を選んだ結果です。だいちのちからの高採用率（88.4%）も、はがね・どく・ほのおといった一致技を半減してくる相手に対し、回復で居座る間の数少ない貫通打点を確保する意味合いが大きいといえます。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">採用率（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HD特殊受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">おだやか 39.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おだやか</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">だいちのちから・ギガドレイン・こうごうせい・やどりぎ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊ほのお・みず・でんきの受け出しに強い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理打点をHB型ほど受けきれない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HB物理受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい 32.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">だいちのちから・ギガドレイン・こうごうせい・どくどく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ガブリアス等の物理アタッカーを受けやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊ほのおの集中をHD型ほど受けきれない</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガフシギバナはあついしぼうでくさ/どくの弱点をエスパー・ひこうの2つに絞り、ぼうぎょ123・とくぼう120の高耐久にこうごうせい・ギガドレインの回復を重ねた居座り耐久アタッカーです。みず・でんき・かくとう・フェアリーを半減できる受け範囲の広さから、アシレーヌ・カメックス・カバルドンといった水・地面の相手に強く出られます。

一方、すばやさ80では環境上位のアタッカーに軒並み先手を取られ、エスパー・ひこうで弱点を突くメガマフォクシー・リザードン・アーマーガアには受けが成立しません。特にアーマーガアは3つの攻撃技がすべて半減以下で崩しようがないため、エスパー対策のあく枠、リザードンを落とすでんき/いわ枠、アーマーガアのはがねを突くほのお枠での弱点補完が前提になります。受けの広さを活かしつつ、突破できない相手をパーティ全体でケアできるかが、27位という使用率での評価を分けるポイントです。

---

## 関連記事

- [天敵となる飛行はがね アーマーガアのM-2考察](/blog/corviknight-analysis-m2/)
- [同じ高速水アタッカー ウォッシュロトムのM-2考察](/blog/rotom-wash-analysis-m2/)
- [受けにくい使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
</content>
</invoke>
