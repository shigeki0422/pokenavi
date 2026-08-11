---
title: '【ポケモンチャンピオンズ】ガブリアス 考察 M-5 シーズン つるぎのまい台頭・オボンのみ急減の変化点を解説'
description: 'M-5シングルバトルで使用率1位を継続するガブリアスを分析。つるぎのまい29.2%→37.3%（+8.1pp）・オボンのみ23.2%→13.8%（-9.4pp）などM-4（2026-07-13時点）からの採用率変化を検算データで解説。型別実数値・苦手な相手・パーティ構成まで紹介。'
pubDate: '2026-08-10'
updatedDate: '2026-08-10'
heroImage: '../../assets/hero-garchomp-m5.png'
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
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" />
  <div>
    <h2 style="margin:0 0 8px">ガブリアス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">1位</strong>（M-2から4シーズン連続）　特性: <strong>さめはだ 99.3%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事はM-5シーズンのデータです。M-4版は[ガブリアス考察 M-4](/blog/garchomp-analysis-m4/)をご覧ください。

シーズンM-5でも、ガブリアスは使用率1位を維持しています。ドラゴン/じめん複合と種族値合計600の高いステータスを持ち、一致技じしん（威力100・命中100）とS169（スカーフ時S253）の速度を武器にする、チャンピオンズを代表するアタッカーです。M-4（2026-07-13時点）からの主な変化はつるぎのまい・スケイルショットの上昇とオボンのみ・わんぱく性格の減少で、詳細は後述のデータ分析で解説します。

---

## ガブリアスの基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">108</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:51%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">102</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
  </div>
</div>

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき
  </td>
</tr>
</tbody>
</table>
</div>

こおり×4が最大の弱点です。M-5の使用率圏内ではアローラキュウコン（36位、フリーズドライ80.7%・ふぶき67.8%）・ゲッコウガ（17位、れいとうビーム91.1%）・マスカーニャ（4位、トリプルアクセル87.3%）・イダイトウ（オス）（15位、れいとうビーム57.2%）・ギャラドス（7位、こおりのキバ49.0%）が主なこおり脅威です。フェアリー×2ではミミッキュ（5位、じゃれつく97.3%）・アシレーヌ（2位、ムーンフォース98.2%）が該当します。ドラゴン×2ではブリジュラス（3位、りゅうせいぐん72.7%）・サザンドラ（16位、りゅうせいぐん93.0%）・カイリュー（8位、りゅうせいぐん54.4%）が該当します。

---

## 特性

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">特性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>さめはだ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.3%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すながくれ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.7%</td>
</tr>
</tbody>
</table>
</div>

**さめはだ**は接触技を受けたとき、攻撃してきた相手のHPを最大HPの1/8削る特性です。こうげき130の高火力に加えて接触技を受けるたびに相手を1/8削る効果があり、物理アタッカーとの削り合いを有利に進められます。採用率は99.3%で実質固定です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技・命中100でほぼ全員が採用するメインウェポン。ひこうタイプには無効</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>スケイルショット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25×2〜5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">49.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">連続ヒット技。最後にS+1・B-1がつき混乱リスクなし。M-4（7/13時点）から+9.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">47.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">場に設置し交代のたびにダメージ。タスキ型・わんぱく型の主力</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">37.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき2段階上昇。いじっぱり増加と連動しM-4（7/13時点）から+8.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>げきりん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>29.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">単発最高打点だが使用後に混乱が確定。M-4（7/13時点）から-5.5pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドラゴンテール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を強制的に交代させる。設置技との併用でダメージを蓄積</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がんせきふうじ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S-1効果。じしんが無効なひこうタイプへの打点が主目的で、それ以外の相手には一致技じしんの方が実効打点で上回ることが多い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくづき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー単タイプ・複合タイプに広く×2（例: アシレーヌ）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>いわなだれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひるみ判定つき</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほのおのキバ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがねタイプへの打点。M-5で圏内に新登場</td>
</tr>
</tbody>
</table>
</div>

---

## 主な型

### 型1：きあいのタスキ型（持ち物採用率40.2%）

**性格採用率（ガブリアス全体）: ようき50.9% / いじっぱり31.6%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">タスキ型（ようき / 設置+スケイルショット）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.3%）<br>
<strong>性格:</strong> ようき（すばやさ↑ とくこう↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・ステルスロック<br>
・スケイルショット<br>
・がんせきふうじ（げきりん）
</div>
</div>
</div>

タスキ込みで最低でも2ターン確保できる立ち位置から、設置技＋スケイルショットで動く構成です。スケイルショットは使用後の混乱が発生しないため、げきりんより後続の行動を縛られにくい点が採用率49.1%まで伸びた理由です。

**強み:**

H185 / A182 / B115 / D105 / S169。S169で多くの環境ポケモンに先手を確保できます。初手はメガゲッコウガ（おくびょうS213）に後手を取られますが、きあいのタスキでHP1を残して1発を耐えられ、さらにスケイルショットは2〜5回の連続技で最後にS+1段階が付くため、撃ち切った時点でS169×1.5=253相当まで上昇し、次ターン以降はメガゲッコウガにも上から動けるようになります。

**弱み:**

きあいのタスキはHP満タン時にしか発動せず、一度消費すると以降は耐久の裏付けがありません。ステルスロック等の設置ダメージが先に入っていると発動条件が崩れ、素のS169のまま後手を取り続けることになります。またマスカーニャのトリプルアクセル（87.3%）は3連続攻撃技のため、タスキで耐えられるのは1発目のみで残り2発で処理されてしまい、こだわりスカーフ採用時（55.2%・S288）はスケイルショット後のS253でも上を取れません。

---

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">タスキ型（いじっぱり / つるぎのまい）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.3%）<br>
<strong>性格:</strong> いじっぱり（こうげき↑ とくこう↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・つるぎのまい<br>
・スケイルショット<br>
・ステルスロック
</div>
</div>
</div>

タスキで1発保証しつつつるぎのまいを積む狙いの構成です。いじっぱり31.6%・つるぎのまい37.3%はいずれもM-4（7/13時点）から大きく増加しており、この型がタスキ型内での比率を高めています。

**強み:**

H185 / A200 / B115 / D105 / S154。つるぎのまいを1積みした場合、いじっぱり型のこうげきは実質A400相当、ようき型は実質A364相当となり、いじっぱり型はようき型より積み後の打点が約10%高くなります。

**弱み:**

S154はようき型（S169）と比べてS155〜169の速度帯のポケモンに先手を取れません。メガカイリュー（おくびょう採用率35.4%、メガ後S167）はようき型のS169には後手ですが、いじっぱり型のS154には先手を取り、りゅうせいぐんで打点を通してきます。

---

### 型2：こだわりスカーフ型（持ち物採用率20.0%）

S169にスカーフ補正（×1.5）がかかりS253となる、最速アタッカー志向の型です。

**性格採用率: ようき 50.9%（ガブリアス全体）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">スカーフ型（ようき・最速アタッカー）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.3%）<br>
<strong>性格:</strong> ようき（すばやさ↑ とくこう↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・スケイルショット<br>
・げきりん<br>
・がんせきふうじ
</div>
</div>
</div>

じしんを固定して先手で削る動きが主軸です。

**強み:**

H185 / A182 / S169（スカーフ補正後 S253）。素のS169では上から動けなかった相手のうち、メガゲッコウガ（S213）・マスカーニャ非スカーフ（S192）はもちろん、**相手がスカーフを持っていても**ブリジュラス（多数派ひかえめ・スカーフでS205）・サザンドラ（スカーフ多数派S225、少数派S247）・キラフロル（多数派ひかえめ・スカーフでS207）まで上から動けるようになります。素のS169の段階ではスカーフ勢に一方的に後手を取られていたのが、この型ではスカーフ同士の速度勝負でも優位に立てる点が最大の強みです。ただしスカーフマスカーニャ（採用率55.2%・S288）には届きません。

**弱み:**

技が1種固定になるため設置技や積み技と組み合わせできません。こだわりスカーフの持ち物採用率は20.0%と少数派ですが、その2割のミラー戦では双方S253の同速勝負（乱数）にもつれます。

---

### 型3：わんぱく型（性格採用率14.5%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">わんぱく型（H32-B32 / ステロ設置）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.3%）<br>
<strong>性格:</strong> わんぱく（ぼうぎょ↑ とくこう↓）<br>
<strong>EV:</strong> H32-B32-S2<br>
<strong>持ち物:</strong> オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・ステルスロック<br>
・ドラゴンテール<br>
・がんせきふうじ
</div>
</div>
</div>

H215・B161の耐久ラインでステルスロックを設置しつつ、ドラゴンテールで相手を強制交代させながら設置ダメージを蓄積する動きが主軸です。M-4（7/13時点）18.2%から14.5%へ縮小しており、後述のデータ分析②のとおりオボンのみ・わんぱくの採用率低下と連動しています。

**強み:**

H215 / A150 / B161 / D105 / S124。B161の高い物理耐久で、物理等倍〜半減技を受けながらステルスロック・ドラゴンテールで消耗させる立ち回りに向きます。

**弱み:**

A150（ようき型A182から32減）と火力は劣ります。加えてこおり×4弱点のふぶき（採用率67.8%）は確定1発、フリーズドライ（80.7%）も高乱数1発になるため、物理方面の耐久を積んでも特殊のこおり技にはほとんど耐えられません。

---

## データ分析①：M-4（7/13時点）→M-5 採用率変化

### 技採用率（M-4（7/13時点）比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4（7/13時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">99.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>99.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">±0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>スケイルショット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">49.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+9.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">49.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>47.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-2.5pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">37.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+8.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>げきりん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>29.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.5pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドラゴンテール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>27.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">-1.4pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がんせきふうじ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>26.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.2pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくづき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>15.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+1.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわなだれ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-1.8pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">まきびし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">圏外へ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほのおのキバ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">13.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新登場</td>
</tr>
</tbody>
</table>
</div>

最大の変化は**つるぎのまい（+8.1pp）とスケイルショット（+9.2pp）の同時上昇**、およびその裏返しとしての**げきりん（-5.5pp）・がんせきふうじ（-3.2pp）・まきびし（圏外へ）の低下**です。設置技（ステルスロック・まきびし）を重ねて受け出しを軸にする型より、混乱リスクのないスケイルショットで削りつつ、つるぎのまいで一気に押し切る型への比重が高まっています。

### 持ち物採用率（M-4（7/13時点）比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4（7/13時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きあいのタスキ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">40.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+1.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こだわりスカーフ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>20.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オボンのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">13.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-9.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラムのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>9.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カゴのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新登場</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たつじんのおび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新登場</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いのちのたま</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">-0.2pp</td>
</tr>
</tbody>
</table>
</div>

**オボンのみ（-9.4pp）**が最大の下落です。オボンのみは後述のわんぱく型（受け出し・耐久重視）の主力持ち物のため、この下落はわんぱく採用率（-3.7pp、後述）の低下と直接連動しています。一方で**きあいのタスキ**は40.2%とタスキ型全体の比率は微増しており、耐久で受けるより1発保証から積極的に攻める構成へ重心が移った形です。

### 性格分布（M-4（7/13時点）比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4（7/13時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">補正</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ようき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">50.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">50.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.7pp</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ↑ とくこう↓</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>いじっぱり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">31.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.6pp</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき↑ とくこう↓</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わんぱく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">14.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.7pp</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ とくこう↓</td>
</tr>
</tbody>
</table>
</div>

いじっぱりが31.6%まで拡大した一方、わんぱくは14.5%まで縮小しました。いじっぱり採用時のこうげき実数値は200（ようき時182）で約10%高く、つるぎのまいを積んでも比率はそのまま保たれます。一方でS実数値はようき169に対しいじっぱり154と15下がるため、先手の有無が変わる相手がいる点は前述の型カードのとおりです。

### EV分布（M-4（7/13時点）比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">EV配分</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4（7/13時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">概要</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H2-A32-S32</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">49.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">48.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・すばやさ全振り+HP最小調整</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>A32-B2-S32</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">10.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・すばやさ全振り+ぼうぎょ微調整</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B32-S2（わんぱく）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">1.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・ぼうぎょ全振り（ステロ型）</td>
</tr>
</tbody>
</table>
</div>

最多EV配分**H2-A32-S32（48.9%）**が引き続き主流です。**H32-B32-S2（1.9%）**の縮小は、性格分布のわんぱく低下（-3.7pp）・持ち物のオボンのみ低下（-9.4pp）と同じ流れで、耐久型からアタッカー型への構築シフトが複数の指標で一貫して確認できます。

---

## データ分析②：つるぎのまい台頭とオボンのみ急減の読み方

M-4（7/13時点）からM-5にかけて最も注目される変化は①つるぎのまい+8.1pp・スケイルショット+9.2ppの同時上昇、②オボンのみ-9.4pp・わんぱく-3.7ppの同時下落、③まきびしの圏外落ちの3点です。

**つるぎのまい・スケイルショットの同時上昇**：スケイルショット（威力25×2〜5回）は最後にS+1・B-1が付き、混乱を伴わずにこうげき技を継続できます。げきりん（威力120・単発）は使用後に混乱が確定するため、つるぎのまいを積んだ後の連続行動を縛ってしまいます。積んだ打点を安定して出し切りたいいじっぱり+つるぎのまい構成にとって、スケイルショットは「積み後も止まらない」相性の良い技であり、この組み合わせが同時に伸びたと考えられます。

**オボンのみ・わんぱくの同時下落**：オボンのみはH215・B161の耐久を活かして相手の攻撃を受け、ステルスロックとドラゴンテールで消耗させるわんぱく型の主力持ち物です。わんぱく（-3.7pp）とオボンのみ（-9.4pp）が同時に下がっていることは、受け出しでダメージを蓄積させる立ち回りより、タスキで1発を保証しつつ積んで押し切る立ち回りへの支持が強まったことを示しています。

**まきびしの圏外落ち**：まきびし（M-4（7/13時点）18.4%→M-5圏外）はステルスロックと合わせて設置ダメージを重ねる技でしたが、ステルスロック自体も47.1%（-2.5pp）とわずかに減少しています。設置技を2種併用する構成の減少は、上記の「受け出し型からアタッカー型へ」という流れと整合しています。

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
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（98.2%）でフェアリー×2。特殊技のためさめはだ効果なし。こちらのじしんはアシレーヌ（みず/フェアリー）に等倍止まりで確定数が伸びず、どくづきも15.6%にとどまり打点が限られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（97.3%）でフェアリー×2。こちらのじしんは等倍止まりのうえ、ばけのかわで初弾を無効化されるため2発の確保が必要な場面が多くなります（ドラゴン技はゴースト/フェアリー複合のミミッキュに無効で打点になりません）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（87.3%）でこおり×4。ようき最速でS実数値192、こだわりスカーフ採用時（55.2%）はS288となり、ようきガブリアス169・いじっぱりガブリアス154のいずれに対しても先手を取ります。こちらのじしんはくさ/あく複合に半減止まりで打点が伸びません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（72.7%）でドラゴン×2。特殊技のためさめはだ効果なし。ブリジュラスはS EV振り無補正でS137程度（こだわりスカーフ13.8%ならS205）でガブリアス（S169）より遅く、こちらが先手でじしん（×2）を当てても確定1発は取れません。生き残られるとりゅうせいぐんで返り討ちに遭います</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム（91.1%）でこおり×4。メガストーン採用率65.4%でメガ後S142→おくびょう主流（53.0%）でS実数値213（ひかえめでも194）となり、ようきガブリアス169・いじっぱりガブリアス154のいずれに対しても先手を取ります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（93.0%）でドラゴン×2。特殊技のためさめはだ効果なし。こだわりスカーフ採用率82.9%でS実数値225に達し、多くの個体はガブリアス（S169）より先に動いてりゅうせいぐんを撃ってきます。先手を取れてもじしん（等倍）は2発必要で1発は取り切れません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ（オス）" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ（オス）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム（57.2%）でこおり×4。特殊技のためさめはだ効果なし。イダイトウはひかえめ主流でS実数値130、ガブリアス（S169）より遅いものの、こだわりスカーフ32.6%の個体はS195で先手を取ります。先手を取れてもじしん（等倍）は2発必要で1発は取り切れず、生き残られるとれいとうビームで返り討ちに遭います</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ（49.0%）でこおり×4。メガストーン採用率77.8%でメガ後（みず/あく）はようきでS146・いじっぱりでS133と、いずれもガブリアス（S169）より遅く、こちらが先手でじしん（等倍）を当てても半分程度しか削れません。ただしりゅうのまい（採用率82.3%・最多技）を1回許すとようき型はS219まで上昇しガブリアス（S169）を逆転するため、初手で削り切れないとりゅうのまい後のこおりのキバでほぼ確定1発を取られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（54.4%）・りゅうのはどう（25.0%）でドラゴン×2。カイリューは素の時点でドラゴン/ひこう複合のため、じしんはメガ前後を問わず無効化されます。がんせきふうじ（いわ・×2）で代替してもメガカイリュー（S152〜167）には打点が乏しく、りゅうせいぐんでほぼ確定1発を取られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マフォクシー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マジカルシャイン（46.7%）でフェアリー×2。マフォクシナイト採用率99.2%でメガ後の特性はふゆうに変わり、主力のじしんが無効化されます。おくびょう採用率79.7%を想定するとメガ後S実数値204でガブリアス（S169）より速く、わるだくみ（55.4%）で積んだマジカルシャインは確定圏に入ります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">36位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フリーズドライ（80.7%）・ふぶき（67.8%）がこおり×4。性格はおくびょう86.5%が主流でS実数値177とガブリアス（S169）より速く、先にこおり技を通されます。オーロラベール（95.5%）で味方の物理・特殊ダメージを軽減する構築が中心です</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-5でガブリアスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" loading="lazy">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" loading="lazy">
    <div class="name">ハッサム</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

M-4（7/13時点）からの変化として注目されるのは**アシレーヌが2位→1位**、**マスカーニャが4位→2位**、**ミミッキュが1位→3位**とトップ3の顔ぶれは維持しつつ順位が入れ替わった点です。M-4（7/13時点）上位だった**バシャーモ・アローラキュウコンが圏外へ**去り、代わって**アーマーガア・ハッサムが新たに9・10位へ**入りました。メタグロス（3位→8位）・ブリジュラス（5位→4位）・ギャラドス（6位→6位）・リザードン（8位→7位）・マフォクシー（7位→5位）は10位圏内を維持しています。

以下では役割分担が明確な上位3種＋新規参入のアーマーガアに絞って解説します（ブリジュラス・マフォクシー・ギャラドス・リザードン・メタグロス・ハッサムは特筆すべき噛み合わせが確認できないため順位のみ掲載）。

**アシレーヌ（1位）**はみず/フェアリーで、ガブリアスの弱点であるドラゴン技をタイプ相性で無効化でき、ムーンフォースでフェアリータイプの相手に打点を持ちます。アシレーヌが苦手などくタイプの相手（キラフロル等）は、ガブリアスのじしんが処理する役割分担です。

**マスカーニャ（2位）**はくさ/あくで、あく技はガブリアスのドラゴン技と打点が重ならず攻撃範囲を補い合えます。マスカーニャが苦手などくタイプの相手は、ガブリアスのじしんが処理する役割分担です。

**ミミッキュ（3位）**はゴースト/フェアリーで、ガブリアスの弱点であるドラゴン技を無効化して受けられます（フェアリー技は等倍で通ります）。ガブリアスが弱点を突かれやすいドラゴンタイプの相手には、じゃれつくで×2の打点も持ちます。一方でミミッキュ自身が苦手なはがねタイプは、ガブリアスのじしんが処理する役割分担です。

**アーマーガア（9位）**ははがね/ひこうで、ガブリアスの弱点であるフェアリータイプを半減で受けられ、主力のアイアンヘッド（35.6%採用のはがね技）はガブリアスの弱点であるこおりタイプの一部（アローラキュウコン等）にも通ります。アーマーガア自身はじめんタイプをひこう複合で無効化できる一方、弱点とするほのお・でんきタイプの相手は、ガブリアスのじしんが処理する役割分担です。

---

## まとめ

M-5のガブリアスは使用率1位を維持しながら、以下の3点で技・型の構成が変化したシーズンです。

- **スケイルショット（+9.2pp）+ つるぎのまい（+8.1pp）の同時上昇**：混乱リスクのない連続技で積んだ打点を出し切る「一撃狙い」構成がさらに強化されています
- **オボンのみ（-9.4pp）+ わんぱく（-3.7pp）の同時下落**：受け出し重視の耐久型からアタッカー型への構築シフトが複数指標で確認できます
- **まきびしの圏外落ち**：ステルスロックとの二重設置構成が縮小し、設置技依存の立ち回りが後退しています

じしん99.5%の一致技とようきS169（スカーフ時S253）の速度は不変で、環境中心であり続ける基本性能は変わっていません。こおり×4・フェアリー×2の弱点に対して、パーティ全体でカバーを用意するか、タスキで1ターン保証する構成を選ぶかが採用時の主な検討事項です。

---

*関連記事：[ガブリアス考察 M-4](/blog/garchomp-analysis-m4/) / [メタグロス考察 M-4](/blog/metagross-analysis-m4/)*

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/garchomp/)**
