---
title: '【ポケモンチャンピオンズ】オーロンゲ考察 M-3 使用率18位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率18位のオーロンゲを徹底分析。いたずらごころ99.5%で変化技を先制発動し、リフレクター88.2%・ひかりのかべ81.3%を先手で展開。ひかりのねんど81.2%で壁8ターン継続。壁貼り役としての立ち回りと型別採用率を実データで解説します。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-grimmsnarl-m3.png'
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
  <img src="/images/pokemon/pokemon-0861-00.webp" alt="オーロンゲ" />
  <div>
    <h2 style="margin:0 0 8px">オーロンゲ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">18位</strong>　特性: <strong>いたずらごころ 99.5%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、オーロンゲは**使用率18位**を記録。特性いたずらごころで変化技の優先度を+1にし、**リフレクター88.2%・ひかりのかべ81.3%を先手で張る壁貼り役**として環境に定着しています。ひかりのねんど81.2%と合わせて壁を8ターン継続させ、後続のエースが動きやすい盤面を整えるのが主な役割です。

---

## なぜ今オーロンゲが18位なのか

### 1. いたずらごころで壁を先手展開できる

特性いたずらごころは変化技の優先度を+1にする。リフレクター・ひかりのかべをすばやさに関係なく先手で張れるため、**相手がどれだけ素早くても1ターン目から壁を展開できる**点が他の壁貼り役にない強みです。すばやさ60と遅い部類ですが、いたずらごころがある限りこの数値は壁展開の速度に影響しません。

### 2. ひかりのねんどで壁を8ターン継続させられる

持ち物採用率1位はひかりのねんど81.2%。ひかりのねんどを持つことでリフレクター・ひかりのかべの効果ターンが通常5ターンから**8ターン**に延長されます。後続エースが8ターンの間、物理・特殊の両方を半減で受けられるため、攻撃技の起点を確実に作れます。

### 3. すてゼリフで能力を下げながら後続へつなぐ

すてゼリフ採用率74.9%は、相手のこうげきとくこうを1段階ずつ下げつつ自分が交代する技です。壁を張った後にすてゼリフを打つことで、**相手の打点を下げながら後続のエースを安全に出せる**流れを作れます。相手の能力低下と壁効果が重なり、後続が大幅に動きやすくなります。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">120</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">510</span>
  </div>
</div>

こうげき120は高い水準ですが、壁貼り役として運用するためほとんど活かされません。ぼうぎょ65・とくぼう75と耐久は低めで、壁なしでは物理・特殊ともに受け出しが難しいステータスです。すばやさ60はいたずらごころで補うため、実質的に変化技限定の行動については速度が問われない構成になっています。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="あく" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="フェアリー" />
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
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

あく×フェアリーの複合タイプは、エスパーとドラゴンを無効化します。かくとうはあく×0.5・フェアリー×2で等倍になり、フェアリーが弱点のあくにとっての天敵であるかくとうを打ち消す形になっています。弱点はどく×2・はがね×2の2タイプのみで、この2タイプを持つ相手には注意が必要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>リフレクター</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">88.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理ダメージを半減。いたずらごころで先手展開</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ソウルクラッシュ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">84.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タイプ一致攻撃技。相手のとくこうを1段階下げる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ひかりのかべ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">81.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊ダメージを半減。いたずらごころで先手展開</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>すてゼリフ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>74.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のこうげきとくこうを1段階下げて強制交代。いたずらごころで先手</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の変化技を3ターン封じる。いたずらごころで先手</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

性格分布はわんぱく63.1%・しんちょう16.1%が上位で、ぼうぎょに振るわんぱく型ととくぼうに振るしんちょう型に二分されます。どちらも役割は壁貼り＋すてゼリフの補助役で、EVの振り先（BかD）で受けやすい攻撃の方向が変わります。

### 型1: わんぱくHB壁貼り型（最多採用）

**性格採用率: わんぱく 63.1%**（B↑ A↓。物理方向の耐久を最大化する構成）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0861-00.webp" alt="オーロンゲ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HBわんぱく壁貼り型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いたずらごころ（99.5%）<br>
<strong>性格:</strong> わんぱく（B↑ A↓）<br>
<strong>EV:</strong> H32 B32（採用率28.7%。最多配分）<br>
<strong>持ち物:</strong> ひかりのねんど（81.2%）
</div>
<div>
<strong>技構成:</strong><br>
・リフレクター<br>
・ひかりのかべ<br>
・すてゼリフ<br>
・ソウルクラッシュ / ちょうはつ
</div>
</div>
</div>

**強み:**

H32 B32振りでぼうぎょを最大化し、物理アタッカーからの先制をできるだけ耐えながら壁を張る構成です。いたずらごころで1ターン目にリフレクターかひかりのかべを先手展開し、2ターン目に残りの壁を張り、3ターン目にすてゼリフで後続へつなぐ3ターンの流れが基本です。ひかりのねんどで壁が8ターン継続するため、後続が複数回の壁恩恵を受けられます。ソウルクラッシュを採用した個体は、相手の変化技枠への打点と相手とくこうダウンを兼ねて攻撃にも参加できます。

**弱み:**

ぼうぎょを伸ばしてもとくぼう75は据え置きのため、特殊アタッカーからの攻撃はひかりのかべを展開する前に大ダメージを受けるリスクがあります。また、どく・はがねタイプの攻撃は壁なしで×2弱点を通されます。こうげき120を持つにもかかわらずA下降性格のため、ソウルクラッシュの打点はわんぱく型より低くなります。

---

### 型2: しんちょうHD壁貼り型

**性格採用率: しんちょう 16.1%**（D↑ A↓。特殊方向の耐久を高める構成）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0861-00.webp" alt="オーロンゲ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HDしんちょう壁貼り型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いたずらごころ（99.5%）<br>
<strong>性格:</strong> しんちょう（D↑ A↓）<br>
<strong>EV:</strong> H31 B32 D3（採用率5.3%。次点配分）<br>
<strong>持ち物:</strong> ひかりのねんど（81.2%）/ たべのこし（14.1%）
</div>
<div>
<strong>技構成:</strong><br>
・リフレクター<br>
・ひかりのかべ<br>
・すてゼリフ<br>
・ちょうはつ / ソウルクラッシュ
</div>
</div>
</div>

**強み:**

わんぱく型がぼうぎょを最大化するのに対し、しんちょう型はとくぼうを底上げして特殊アタッカーへの初動を耐えやすくします。特殊攻撃が多い環境ではひかりのかべを張る前に倒されるリスクが低下します。たべのこしを持つ個体は消耗を抑えながら場に居座り、ちょうはつで相手の補助技を封じる立ち回りが可能です。

**弱み:**

ぼうぎょ65はしんちょう型では補強されないため、物理アタッカーに対してはわんぱく型より脆く、リフレクター展開前に倒される可能性が高まります。たべのこし採用の場合はひかりのねんどを持てないため、壁の継続ターンが5ターンにとどまります。

---

## 環境ポケモンへの相性分析

あく/フェアリーはエスパー・ドラゴンを無効化しますが、壁貼り役として運用するため能動的に有利を取る場面は限定的です。オーロンゲ自身が直接戦うより、壁展開後に後続が有利を作る構図のため、ここでは「壁展開を妨害するポケモン」と「壁展開を活かしやすい相手」の視点で整理します。

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
    <img src="/images/pokemon/pokemon-0282-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サーナイト
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 展開しやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー技を無効化するため相手のエスパー打点を透かして壁を展開できる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 展開しやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン技を無効化するため、カイリューのドラゴン主力技を受けながら壁を張れる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 苦手</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが等倍で通りぼうぎょ65に対して大ダメージ。ドラゴン技はフェアリーで無効化できるが、じしん採用率が高く壁展開を妨害される</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 苦手</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね技が×2弱点。ぼうぎょ65に対して高火力はがね技が刺さる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0454-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドラピオン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 苦手</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どく技が×2弱点。どくタイプのどく技がオーロンゲに刺さる</td>
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
    <div class="rate">エース候補</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">壁下で安全に動けるじめん・ドラゴン物理アタッカー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ">
    <div class="name">ルカリオ</div>
    <div class="rate">エース候補</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">壁下でつるぎのまいを積みやすくなる物理エース</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">エース候補</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">壁下で特殊技を叩き込む高火力特殊エース</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">エース候補</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">壁下でみず・フェアリー特殊技を安全に打てる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">エース候補</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速アタッカー。壁下でさらに先手が通りやすくなる</div>
  </div>
</div>

**パーティ構成の基本方針:**

オーロンゲは自身がエースとして詰める役割ではなく、壁展開＋すてゼリフで後続のエースを通す補助役です。残り5体の構成では以下を意識します。

1. **物理エース**: リフレクターで物理ダメージが半減するため、ツルギのまい等で積んだ物理アタッカーが壁下でさらに受けにくくなる
2. **特殊エース**: ひかりのかべで特殊ダメージが半減するため、めいそう等を積んだ特殊アタッカーが壁下で安全に行動できる
3. **どく・はがね対策**: オーロンゲが苦手などく・はがねタイプに対してサイクルを回せるポケモンを同伴する
4. **8ターンの活用**: ひかりのねんど8ターンの壁を最大限活用できるよう、エースが積んで全抜きを狙う構成が壁展開と噛み合う

---

## データ分析①：リフレクター・ひかりのかべ・すてゼリフの採用率から読む役割の固定度

オーロンゲの技採用率上位4技を並べると、役割の均質性が際立ちます。

| 技 | 採用率 | 役割 |
|---|---|---|
| リフレクター | 88.2% | 物理壁展開 |
| ソウルクラッシュ | 84.0% | 攻撃＋とくこうダウン |
| ひかりのかべ | 81.3% | 特殊壁展開 |
| すてゼリフ | 74.9% | 能力ダウン＋後続へ交代 |

リフレクター・ひかりのかべ・すてゼリフはいずれも70%以上の採用率で、**実質的に固定技の扱い**です。技4枠のうち3枠は上記3技でほぼ確定し、残り1枠にソウルクラッシュ（84.0%）かちょうはつ（33.0%）が入る構成になっています。

ソウルクラッシュの採用率84.0%は壁貼り役の技構成としては高い数値で、**攻撃技をほぼ全個体が採用している**点が特徴的です。壁貼りだけでなく、ソウルクラッシュによる相手とくこうダウンを絡めてすてゼリフのAC両下げと組み合わせる動きが定石化していると読めます。壁を張り切った後にソウルクラッシュ→すてゼリフで相手のAとCを両方下げて後続に繋げば、壁効果と能力低下が重なって後続への圧力を最大化できます。

持ち物はひかりのねんど81.2%が支配的で、たべのこし14.1%と二択に近い分布です。ひかりのねんどが4/5の個体に採用されていることから、**壁の8ターン継続を前提とした後続エースの設計**が環境で主流と判断できます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HBわんぱく壁貼り型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">わんぱく 63.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">リフレクター・ひかりのかべ・すてゼリフ・ソウルクラッシュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ぼうぎょを最大化し物理を耐えながら壁を展開できる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">とくぼうは据え置きで特殊アタッカーへの初動が不安定</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HDしんちょう壁貼り型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう 16.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">リフレクター・ひかりのかべ・すてゼリフ・ちょうはつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">とくぼうを底上げし特殊アタッカーへの初動を安定させる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ぼうぎょは据え置きで物理アタッカーへは脆い</td>
</tr>
</tbody>
</table>
</div>

**総評:**

オーロンゲはいたずらごころによるすばやさ非依存の壁展開と、ひかりのねんどによる8ターン継続が強みの補助役です。リフレクター88.2%・ひかりのかべ81.3%・すてゼリフ74.9%の3技が実質固定で、対面した相手はまずこの3技の流れを警戒する必要があります。

弱点はどく・はがねの2タイプで、これらの攻撃で壁展開前に突破されると役割を果たせません。ちょうはつ33.0%の採用は相手の壁貼り・積み技・回復技を封じる逆妨害として機能し、壁合戦になる対面ではちょうはつを先手で打つことで相手の補助行動を止められます。

---

## 関連記事

- [使用率1位 ガブリアスのM-3考察](/blog/garchomp-analysis-m3/)
- [壁展開の天敵となるドドゲザンのM-3考察](/blog/dodonzo-analysis-m3/)
- [オーロンゲの後続エースとして定番のルカリオのM-3考察](/blog/lucario-analysis-m3/)
