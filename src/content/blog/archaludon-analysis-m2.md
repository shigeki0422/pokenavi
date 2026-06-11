---
title: '【ポケモンチャンピオンズ】ブリジュラス考察 M-2 使用率2位 型別採用率と立ち回り'
description: 'M-2シングルバトルで使用率2位のブリジュラスを徹底分析。10まんボルト採用率66.9%・りゅうせいぐん64.8%の特殊アタッカー型と、じきゅうりょく78.0%＋ステルスロック49.8%の耐久型を実データで解説。環境上位への相性とパーティ構成まで紹介します。'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-archaludon-m2.png'
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
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" />
  <div>
    <h2 style="margin:0 0 8px">ブリジュラス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">2位</strong>　特性: <strong>じきゅうりょく 78.0%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ブリジュラスは**使用率2位**を記録。はがね/ドラゴンという弱点が**かくとう・じめんの2タイプのみ**という優秀な複合タイプに、とくこう125・ぼうぎょ130を併せ持ち、攻守両面で器用に立ち回れるのが上位定着の理由です。

特性は**じきゅうりょく**が78.0%と主流で、物理技を受けるたびにぼうぎょが1段階上がります。攻撃を受けながら硬くなる性質が、ステルスロック設置や起点作りといった耐久型の動きと噛み合っています。

---

## なぜ今ブリジュラスが使用率2位なのか

### 1. 弱点がかくとう・じめんの2タイプのみ

はがね/ドラゴンは、はがねの豊富な耐性とドラゴンの組み合わせで、**弱点がかくとう・じめんの2タイプだけ**に絞られます。ほのお（はがね×2・ドラゴン×0.5＝等倍）・ドラゴン（はがね×0.5・ドラゴン×2＝等倍）・フェアリー（はがね×0.5・ドラゴン×2＝等倍）はいずれも等倍止まりで、本来これらに弱いはずのタイプを軽減できます。一方で残るかくとう・じめんはともに×2で通るため、後述のとおりこの2タイプを持つ環境上位が明確な弱点になります。

### 2. とくこう125からの広い攻撃範囲

とくこう種族値は125。10まんボルト（採用率66.9%）・りゅうせいぐん（64.8%）・ラスターカノン（55.7%）と特殊技の採用率が高く、でんき・ドラゴン・はがねの3タイプで広い範囲に等倍以上の打点を持ちます。とくにでんき技はみず・ひこうタイプへ刺さり、使用率上位のアシレーヌ（みず/フェアリー・4位）やギャラドス（みず/ひこう・12位）に有効です。

### 3. じきゅうりょく＋ステルスロックで起点を作れる

特性じきゅうりょく（78.0%）は物理攻撃を受けるたびにぼうぎょが1段階上がるため、物理アタッカーと撃ち合うほど硬くなります。ステルスロック（採用率49.8%）・ほえる（23.4%）・ドラゴンテール（18.8%）を併せ持つ個体は、ステルスロックを撒いて相手を流し、交代ダメージを蓄積させる起点役として機能します。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:62.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">125</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
  </div>
</div>

ぼうぎょ130・とくこう125に対し、とくぼう65・すばやさ85は控えめ。物理方向には硬いがとくぼうは低く、すばやさも環境の高速勢には及ばないため、特殊アタッカーとの撃ち合いや上から殴られる展開には弱いというステータス配分です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ドラゴン" />
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
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

はがねがどくを無効化し、くさは2タイプとも半減して×0.25に抑えます。ほのお・ドラゴン・フェアリーは2タイプの倍率が打ち消し合って等倍止まりで、これらを軸とする相手に被弾しても致命傷になりにくいのが利点です。一方、**弱点はかくとう・じめんの2タイプのみ**ですが、いずれも×2かつ環境の物理アタッカーが採用する主力技（ガブリアスのじしん採用率99.2%等）に多く、被弾耐性とは裏腹に物理地面・かくとうへの後出しはできません。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんボルト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">66.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・ひこうへの主力打点。10%マヒ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうせいぐん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">64.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致最大火力。使用後C2段階ダウン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラスターカノン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">55.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー・いわ・こおりへの安定一致技。10%Cダウン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">起点作り。交代読みで撒いて削りを蓄積</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はどうだん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">必中。あく・はがねへの補完打点。ドドゲザン等に刺さる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほえる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">強制交代。積み相手を流しつつステロ削りを稼ぐ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドラゴンテール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度-1。ダメージを与えつつ強制交代</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ミラーコート</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">受けた特殊ダメージを2倍で反射。低いとくぼうを逆手に取る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっていこうせん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね最大火力。使用後C2段階ダウンで使い切り向き</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>エレクトロビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">溜め技だがあめ下では即発動＋C1段階上昇。でんき最大火力</td>
</tr>
</tbody>
</table>
</div>

特性は**じきゅうりょく78.0%・がんじょう21.9%**の2択。がんじょうはHP満タンから一撃で倒されないため、上から弱点を突かれても1回は行動を残せます。じきゅうりょくは物理を受けてBを上げる耐久型、がんじょうはタスキ的な保険を持つアタッカー寄りと、特性で立ち回りの方向性が分かれます。

---

## 主要型の解説

性格分布はひかえめ40.9%・ずぶとい27.5%・おだやか13.7%で、攻撃に寄せた特殊型と、ぼうぎょ・とくぼうに振った耐久型に二分されます。

### 型1: ひかえめ特殊アタッカー型（最多採用）

**性格採用率: ひかえめ 40.9%**（特殊AT型の指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">CSひかえめ特殊型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> がんじょう（21.9%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> C32 S32（最多配分・採用率18.0%。余りはHへ）<br>
<strong>持ち物:</strong> しろいハーブ / こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・りゅうせいぐん<br>
・10まんボルト<br>
・ラスターカノン<br>
・はどうだん / ステルスロック
</div>
</div>
</div>

**強み:**

とくこう125をCS最大振りで活かす型です。最多のステータス振りはC32 S32（採用率18.0%）で、すばやさを確保しつつ最大火力を出します。りゅうせいぐんはアシレーヌ・ギャラドスといったでんき・ドラゴンが等倍以上で通る相手に高い一撃を入れられ、しろいハーブを持てばりゅうせいぐんのCダウンを1度だけ即リセットできるため、火力を落とさず連発に近い運用ができます。耐久型（ずぶとい・おだやか）と異なり、初手から能動的に上位の高耐久を削れるのが利点です。

**弱み:**

すばやさ85のため、後述するガブリアス（S102）やマスカーニャ（S123）など環境上位の高速勢には先手を取られます。とくぼう65と低く、こだわりスカーフを持たない限り上から特殊技を浴びると一撃が重い点も、Bに振る耐久型にはない弱みです。

---

### 型2: じきゅうりょく耐久型（2番目に多い構成）

**性格採用率: ずぶとい 27.5%＋おだやか 13.7%**（耐久型の指標。物理受けのずぶとい・特殊受けのおだやかの合計）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HBずぶとい耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（78.0%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32 B32（ずぶといはHB寄せ、おだやかはHD寄せが主流）<br>
<strong>持ち物:</strong> オボンのみ / たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・ステルスロック<br>
・ほえる / ドラゴンテール<br>
・10まんボルト / ラスターカノン<br>
・りゅうせいぐん
</div>
</div>
</div>

**強み:**

特性じきゅうりょくで物理を受けるたびにBが上がり、ずぶとい＋H振りと合わせて物理アタッカーを起点にステルスロックを撒けます。ほえる・ドラゴンテールで積みアタッカーを流しながら交代ダメージを稼げるため、特殊型のように一撃で削るのではなく、ステルスロックと強制交代で盤面を削り続ける役割です。オボンのみ・たべのこしによる回復を絡め、特殊型では持続しにくい長期戦を支えられます。

**弱み:**

攻撃に振らないぶん突破力が低く、特殊型のように上位を能動的に削れません。とくぼう65は据え置きで、おだやか型に振らない限り特殊アタッカーには受け出しが難しく、攻撃役を別途用意する前提の型です。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

使用率上位のうち、ブリジュラスと相性がはっきり出るポケモンを有利・不利の両面から挙げます。はがね/ドラゴンは弱点がかくとう・じめんの2タイプのみで多くの攻撃を等倍以下に抑えますが、すばやさ85・とくぼう65と先手と特殊耐久には欠けるため、上から殴る高速勢・かくとう/じめんの物理打点を持つ相手が苦手という構図です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルトが×2（みず2×フェアリー1）。S85＞60で先手。相手のムーンフォース等はこちらに等倍止まり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルトが×4（みず2×ひこう2）。S85＞81で先手確保。確定1発圏内</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（ドラゴン1×ひこう2＝×2）・りゅうせいぐん（×2）で弱点を突ける。ただしS100＞85で先手は取られる。じしん採用は15.2%と低くこちらの弱点は突かれにくい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はどうだんが×4（あく2×はがね2）。S85＞50で先手。先制のふいうちもこちらには等倍（あく1×はがね1）で一撃にならない。ただしけたぐり（17.6%）採用個体にはかくとう×2を通される</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルトが×2（ほのお1×ひこう2）だがS100＞85で先手を取られる。相手のほのお技はこちらに等倍止まりで一撃では落ちにくい</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

弱点のかくとう・じめんを×2で突ける物理アタッカーと、とくぼう65を上から殴る特殊高速勢を中心に、使用率TOP30から選定しました。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99.2%）が×2、S102でこちらより速い。A130の一致じしんで先手から大ダメージを受ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんを無効化するひこうタイプ（アーマーガア・ギャラドス）を同伴し、ガブリアスの前に引いて受ける。引いた先からでんき・こおり技で弱点を突く</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率71.5%）がかくとう×2。メガ後Sはようきで180とこちらより速く、つるぎのまい（39.3%）で積めばA一致打点で確定圏。しんくうは（26.0%）の先制も負う</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">単体での後出しは困難。じめんを通せるガブリアスやかくとうを無効化するイダイトウ（みず/ゴースト）を後出しし、インファイト後にB・Dが下がった隙を突いて処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（98.0%）が×2。高HP・高Bでこちらの特殊技を耐え、あくび（94.2%）・ふきとばし（44.5%）でステロや積みを流される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・みず・こおり技を持つ高速枠（マスカーニャ等）を同伴し、後出しから弱点（×2）で処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123でこちらより速く、けたぐり（採用率12.5%）採用個体にはかくとう×2を上から通される。素のトリックフラワー（必中・急所）でも継続的に削られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ型で先手を取り10まんボルト圏内に。または、ひこう・どく・むし技を持つ枠で後続から弱点を突く</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおは等倍だがちょうのまい（97.4%）でC・D・命中を積まれると、とくぼう65のこちらは特殊で押し負ける。S100でこちらより速い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">積む前に削るのが前提。いわ技（×4）を持つ高速枠を後出しし、積み始めのターンに弱点で落とす</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0937-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ソウブレイズ（26位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率36.3%）がかくとう×2。つるぎのまい（82.7%）で積まれるとA125の一致打点が重く、かげうち（93.8%）の先制も継続的に削ってくる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお/ゴーストはじめん・あくがともに×2。じしんを持つガブリアスやあく技の高速枠を後出しし、つるぎのまいの前に弱点で処理する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。ブリジュラスが苦手なじめん・かくとう枠に上から打点を入れる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S123の高速枠。くさ技でブリジュラスが重いカバルドン（くさ×2）に打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ゴーストでかくとうを無効化。ブリジュラスの弱点かくとうを受けられる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこうでじめんを無効化。ブリジュラスが苦手なじめん技を受ける枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/フェアリーでかくとうを半減。特殊枠として攻撃役を補完</div>
  </div>
</div>

**パーティ構成の基本方針:**

ブリジュラスは弱点が少なく多くの攻撃を受けられる一方、弱点のかくとう・じめんはともに環境物理アタッカーの主力技で、すばやさも控えめです。残り5体で以下を補います。

1. **じめん対策**: ひこうタイプ（リザードン・ギャラドス）でガブリアス・カバルドンのじしんを無効化する枠
2. **かくとう対策**: ゴースト複合（イダイトウ）やフェアリー（アシレーヌ）でかくとう技を受ける枠
3. **高速地面枠**: ガブリアス等で、ブリジュラスが上から殴られる地面・かくとう枠に先制で打点を入れる
4. **ステルスロック連携**: ステルスロックを撒いたあと、高速アタッカーで交代を強要し削りを最大化

---

## データ分析①：技採用率が示す「アタッカー」と「起点役」の二極化

ブリジュラスの技採用率を並べると、攻撃技と変化技がきれいに2系統に分かれます。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| 10まんボルト | 攻撃 | 66.9% | 特殊メイン |
| りゅうせいぐん | 攻撃 | 64.8% | 一致最大火力 |
| ラスターカノン | 攻撃 | 55.7% | 安定一致技 |
| ステルスロック | 変化 | 49.8% | 起点作り |
| ほえる | 変化 | 23.4% | 強制交代 |
| ドラゴンテール | 変化 | 18.8% | 強制交代＋削り |

攻撃3技がいずれも55%超なのに対し、起点系のステルスロック49.8%・ほえる23.4%・ドラゴンテール18.8%も無視できない採用率を保っています。性格分布でひかえめ40.9%（特殊AT）に対しずぶとい＋おだやかが計41.2%（耐久）とほぼ拮抗していることと符合しており、ブリジュラスは「特殊で殴る型」と「ステロを撒いて流す起点役」が**ほぼ半々で併存**しているのが実態です。

これは対戦相手にとって厄介な不確定要素になります。同じブリジュラスでも、こだわりスカーフ・しろいハーブ（合わせて25.7%）のアタッカー個体か、オボンのみ・たべのこし（合わせて63.3%）の耐久個体かで、出てくるターンの脅威がまったく異なるためです。持ち物採用率を見るとオボン33.0%・たべのこし30.3%と回復実の方が多く、**遭遇時はまず起点役の耐久型を疑い、ステルスロックやほえるでの流しを警戒する**のが確率的に妥当な初手読みになります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">CS特殊アタッカー型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ひかえめ 40.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">りゅうせいぐん・10まんボルト・ラスターカノン・はどうだん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">とくこう125で能動的に上位を削れる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">とくぼう65が低く高速特殊に弱い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">じきゅうりょく耐久型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい＋おだやか 41.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい/おだやか</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ステルスロック・ほえる・10まんボルト・りゅうせいぐん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理を受けてBを上げ起点を作れる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">突破力が低く攻撃役を別途要する</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ブリジュラスははがね/ドラゴンの優秀な耐性（弱点はかくとう・じめんの2タイプのみ）と、とくこう125・ぼうぎょ130を併せ持つ器用なポケモンです。特殊アタッカーと起点役がほぼ半々で併存しており、対面した相手に型を絞らせない不確定さも使用率2位を支える要因です。

弱点はかくとう・じめんの2タイプに限られますが、いずれも環境物理アタッカーの主力技に多く、すばやさ85で上から殴られる展開も多いため、ガブリアス・カバルドンのじしんはパーティ単位でケアする必要があります。じめんを無効化するひこう枠を添え、ブリジュラス自身はでんき・ドラゴン・はがねの広い範囲を押し付けつつステロで削るのが基本戦術です。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [でんき技で弱点を突けるギャラドスのM-2考察](/blog/gyarados-analysis-m2/)
- [ブリジュラスにインファイトが刺さるメガルカリオのM-2考察](/blog/lucario-analysis-m2/)
