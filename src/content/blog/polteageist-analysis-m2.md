---
title: '【ポケモンチャンピオンズ】ポットデス考察 M-2 使用率62位 からをやぶるバトンの起点役'
description: 'M-2シングルバトルで使用率62位のポットデス（ゴースト単）を徹底分析。からをやぶる採用率99.1%・しろいハーブ93.4%でA/C/Sを積み、バトンタッチ88.4%で後続へ能力上昇を引き継ぐ起点役。のろわれボディ92.7%・ずぶとい70.2%のHB耐久型の立ち回りと後続選びを実データで解説します。'
pubDate: '2026-06-11'
draft: true
heroImage: '../../assets/hero-polteageist-m2.png'
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
  <img src="/images/pokemon/pokemon-0855-00.webp" alt="ポットデス" />
  <div>
    <h2 style="margin:0 0 8px">ポットデス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">62位</strong>　特性: <strong>のろわれボディ 92.7%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/24）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ポットデスは**使用率62位**を記録。特性は**のろわれボディ（採用率92.7%）**が主流で、くだけるよろい（7.3%）は少数派です。

ポットデスの軸は**からをやぶる（採用率99.1%）**で攻撃・特攻・素早さを2段階上げ、**バトンタッチ（88.4%）**で後続へ能力上昇を丸ごと引き継ぐ起点役です。攻撃技はほぼシャドーボール（90.3%）1枚で、本体で殴り勝つよりも「積んで引き継ぐ」ことに役割を寄せています。からをやぶるで下がる防御・特防はしろいハーブ（93.4%）で即座に回復し、性格ずぶとい（70.2%）とHB振りで物理を耐えながら積む立ち回りが主流です。

本記事では、HB耐久に振って積み・バトンを通すのろわれボディ型を基準に、技・持ち物・後続選びを実データで解説します。

---

## なぜポットデスが使われるのか

### 1. からをやぶる＋バトンタッチで後続に能力上昇を渡す

ポットデスの最大の役割は、**からをやぶる**で攻撃・特攻・素早さを2段階上げ、**バトンタッチ**でその上昇を後続へ引き継ぐことです。からをやぶる採用率99.1%・バトンタッチ88.4%とほぼ全個体がこの組み合わせを採用しており、ポットデス自身が殴るより「能力上昇を別のアタッカーに渡す」設計が定着しています。

最多のHBS振り（H24 B24 S18）ではすばやさS実数値108で、からをやぶる2段階上昇（×2）後は**216**まで届きます。この上昇をバトンで受けた後続は、素のすばやさを問わず大半の相手より先に動けます。

### 2. しろいハーブでからをやぶるの隙を消す

からをやぶるは攻撃・特攻・素早さを2段階上げる代わりに、**防御・特防を1段階下げる**デメリットがあります。**しろいハーブ（採用率93.4%）**はこの能力低下を1度だけ回復するため、積んだ直後に防御・特防が下がった状態を即座に元へ戻せます。低下分を打ち消してから殴られるため、積みの隙を最小化できるのが採用理由です。

### 3. ゴースト単で受け出して積み始めやすい

ポットデスはゴースト単タイプで、**ノーマル・かくとう技を無効化**します。ノーマル技のしんそく（カイリュー）やかくとう技のインファイト等を透かせるため、これらの技を主体とする相手の前で受け出してからをやぶるを積み始められます。低い素早さ（最多振りでS実数値108）でも、有効打のない相手に対してなら被弾を抑えて積む隙を作れます。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
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
      <div style="width:67%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">134</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:57%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">114</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">508</span>
  </div>
</div>

とくこう134・とくぼう114が高く、こうげき65・ぼうぎょ65・すばやさ70は控えめです。ずぶとい（B↑）の最多HBS振り（H24 B24 S18）ではぼうぎょ実数値B119まで上がり、HP実数値167と合わせて物理を1発耐えてからをやぶるを積めます。攻撃技を撃つ役割よりも、無補正でもD実数値134の高い特防と補正込みの物理耐久を活かして「積む1ターンを確保する」種族値構成です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ゴースト" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

ノーマル・かくとうを無効化できる点が受け出して積み始めるうえで重要で、しんそく（カイリュー）やインファイト・きあいだま等を透かしてからをやぶるを積み始められます。弱点はゴースト・あくの2タイプのみで、被弾面は狭め。ただしゴースト技のシャドーボール、あく技のはたきおとす・ふいうち等は×2で通り、低いHP実数値167では弱点技を1発耐えられない場面があるため、これらを撃つ相手の前では積めません。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>からをやぶる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A・C・Sを2段階上げ、B・Dを1段階下げる積み技。低下はしろいハーブで回復</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">90.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト一致の主攻撃技。20%で相手のとくぼうを1段階下げる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バトンタッチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">88.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">能力上昇・みがわりを引き継いで交代。積んだA・C・Sを後続へ渡す</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちからをすいとる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">80.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のこうげきを1段階下げつつHP回復。物理相手の前で居座りやすくする</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アシストパワー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20〜</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">能力1段階ごとに威力+20。自分で抜く構成向け</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みがわり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バトンで引き継げる身代わり。状態異常・削りを防いで後続を守る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ギガドレイン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・じめん・いわへの打点とHP回復を兼ねる</td>
</tr>
</tbody>
</table>
</div>

からをやぶる99.1%・シャドーボール90.3%・バトンタッチ88.4%・ちからをすいとる80.0%の4枠がほぼ確定枠です。からをやぶるで積み、ちからをすいとるで物理相手の火力を削りつつ居座り、バトンタッチで後続へ繋ぐ「積み・バトン」型が主流で、攻撃技はシャドーボール1枚に絞られています。

---

## 主要型の解説

性格はずぶとい70.2%が支配的で、EVもHB主体（HBS24-24-18など）が中心です。本体で殴り切るより、物理を耐えて積み・バトンを通す耐久寄りの振り方が標準です。

### 型1: からをやぶるバトン型（最多）

**指標: のろわれボディ 92.7%／ずぶとい 70.2%／しろいハーブ 93.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0855-00.webp" alt="ポットデス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HB積みバトン型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> のろわれボディ（92.7%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H24 B24 S18（HBSが最多。HBに寄せる個体も）<br>
<strong>持ち物:</strong> しろいハーブ
</div>
<div>
<strong>技構成:</strong><br>
・からをやぶる<br>
・バトンタッチ<br>
・ちからをすいとる<br>
・シャドーボール
</div>
</div>
</div>

**強み:**

バトンタッチを採用し、からをやぶるで積んだA・C・Sを後続のアタッカーへ丸ごと渡せます。ポットデス自身が抜き役にならないため、シャドーボールが半減・無効の相手でも、積んでバトンするだけで仕事が成立します。ちからをすいとるで物理アタッカーのこうげきを下げつつHPを回復できるので、物理を呼ぶ相手の前では居座りながら積みを通しやすい構成です。

**弱み:**

抜き役を後続に委ねるため、バトン先のアタッカーを通せる盤面が前提になります。次のアシストパワー型と異なり、ポットデス自身は積んでもシャドーボール1枚しか火力源がなく、バトンが読まれて止められると単体での詰め性能が乏しくなります。

---

### 型2: アシストパワー自己完結型（アシストパワー 22.8%）

**指標: アシストパワー 22.8%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0855-00.webp" alt="ポットデス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">アシストパワー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> のろわれボディ（92.7%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）／ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> C32 S32（CSに寄せる抜き構成）<br>
<strong>持ち物:</strong> しろいハーブ
</div>
<div>
<strong>技構成:</strong><br>
・からをやぶる<br>
・アシストパワー<br>
・シャドーボール<br>
・ちからをすいとる / みがわり
</div>
</div>
</div>

**強み:**

アシストパワーは能力1段階につき威力+20で、からをやぶる後はA・C・Sの計6段階上昇で威力140まで伸びます。バトン型と違い、ポットデス自身がC実数値204（ひかえめ）の高特攻でアシストパワーを撃ち、自分で抜きにいける自己完結型です。からをやぶる後はS実数値が244〜268まで上がり、上から連打できます。

**弱み:**

アシストパワー（エスパー）はあくタイプに無効化されるため、サザンドラ（21位）・ドドゲザン（24位）等のあく枠を後続に控えられると、積んでも通せません。バトン型のように後続へ上昇を逃がせず、止められると積み直しが効かない一発勝負になります。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

ポットデスは「積む隙を作れるか」で相性が決まります。ノーマル・かくとうを無効化でき、弱点はゴースト・あくの2タイプのみと被弾面は狭いものの、低いHP実数値167のため弱点技は1発で落とされます。素のすばやさはS実数値108〜122と遅く、からをやぶる前は大半の相手に先手を取られる点も踏まえ、有利・不利の両面を挙げます。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 有効打はないが居座りは厳しい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（99.2%）・げきりん（47.9%）はいずれもゴーストに等倍で弱点は突かれない。ただし高いこうげきの等倍じしんはHP実数値167に半分以上通り、ちからをすいとるでこうげきを下げないと安全に積めない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0530-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドリュウズ（同居1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 有効打はないが居座りは厳しい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（98.5%）・アイアンヘッド（96.1%）はいずれもゴーストに等倍で弱点は突かれない。物理偏重なのでちからをすいとるでこうげきを下げれば積めるが、下げる前の等倍打点は重い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（同居7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 受け出して積みやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん主体でゴーストに有効打が薄い。S47と遅く、ちからをすいとるで火力を削りながら安全に積める</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（ゴースト×2弱点）で先に落とされる。S実数値はゲンガー側が大きく上回り、積む前に処理される</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（あく×2弱点）でしろいハーブを叩き落としつつ大ダメージ。S123で先手を取られ積めない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0571-01.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゾロアーク（ヒスイ・39位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ノーマル/ゴーストでシャドーボール（49.6%）がゴースト×2弱点。S105で素のすばやさを上回り、積む前に処理される</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

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
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（あく×2弱点）でしろいハーブを叩き落とされ、S123で上から殴られて積めない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先に処理できるフェアリー・どく枠（デカヌチャン等）を合わせるか、ポットデスを後出しせずバトン先で受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（71.1%）がゴースト×2弱点。素早さで上を取られ、積む前に落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく単タイプ（バンギラス・ブラッキー等）を後続に置いてゴースト技を半減し、上から処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（19位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち（93.6%）が先制のゴースト×2弱点。素早さに関係なく先に弱点技を入れられ、HP実数値167では受け切れない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ノーマルタイプ（ゴースト技無効）を後続に置いて受け、上から処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（98.5%）があく×2弱点。S98でこちらの素のすばやさを上回り、積む前に弱点技で落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく技を半減するフェアリー・かくとう枠を後続に合わせ、削り合いを避けて受け回す</td>
</tr>
</tbody>
</table>
</div>

苦手な相手は「ゴースト・あく技で弱点を突いてくる相手」と「素早さで上を取り、積む前に処理する相手」に大別されます。いずれもポットデス単体での切り返しは難しいため、あく技を半減する枠や、ゴースト技を無効化するノーマル枠を後続に置いて受ける構築が前提になります。

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0530-00.webp" alt="ドリュウズ">
    <div class="name">ドリュウズ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">A135の物理エース。バトンでA・Sを受け取り上から抜きにいく</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0354-00.webp" alt="ジュペッタ">
    <div class="name">ジュペッタ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ゴースト枠。バトンでA・Sを受け取りゴースト打点で詰める</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">A125の物理アタッカー。バトンを受けて上昇込みで全抜きを狙う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0571-01.webp" alt="ゾロアーク（ヒスイ）">
    <div class="name">ゾロアーク（ヒスイ）</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ノーマル/ゴースト。S105でバトンのS上昇を受けゴースト打点で抜く</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンであく技を半減。苦手なあく枠への受け回しに</div>
  </div>
</div>

**パーティ構成の基本方針:**

ポットデスは積んでバトンする起点役のため、残り5体で以下の役割を補います。

1. **バトン先のアタッカー**: A・Sを受け取って全抜きを狙える物理エース（ドリュウズ・ギャラドス）を1〜2体置く
2. **あく技の受け**: ブリジュラス（はがね/ドラゴン）等であく技を半減し、はたきおとす・ふいうちの弱点を受ける枠
3. **ゴースト技の受け**: ノーマルタイプ（ゴースト技無効）でゲンガー・ミミッキュのゴースト打点を受ける枠
4. **積む隙の確保**: じめん・かくとう主体の相手（ガブリアス・ドリュウズ等）を呼べる盤面を作り、無効化しながら積み始める

---

## データ分析①：技採用率に見る「殴らない」設計

ポットデスの技採用率は、攻撃技より**変化技に偏っている**点に特徴があります。

| 技 | 分類 | 採用率 | 主な役割 |
|---|---|---|---|
| からをやぶる | 変化（積み） | 99.1% | A・C・Sを2段階上昇 |
| バトンタッチ | 変化（交代） | 88.4% | 上昇を後続へ引き継ぐ |
| ちからをすいとる | 変化（妨害＋回復） | 80.0% | 相手のこうげき低下とHP回復 |
| シャドーボール | 攻撃 | 90.3% | 唯一の確定攻撃枠 |

C134の高い特攻を持ちながら、攻撃技はシャドーボール（90.3%）1枚に絞られ、残り3枠はすべて変化技です。アシストパワー（22.8%）・ギガドレイン（4.7%）といった追加の攻撃技は少数派で、大多数の個体が「自分で殴る」より「積んで引き継ぐ」設計に寄っています。

バトンタッチ88.4%・ちからをすいとる80.0%という高採用率は、ポットデスの役割が**抜き役そのものではなく、後続のアタッカーを起動させる露払い**にあることを示しています。高特攻134という攻撃的な種族値を、攻撃ではなくバトンの起点性能に転用しているのが、この技構成から読み取れる構築思想です。

---

## データ分析②：持ち物しろいハーブ93.4%が示す積みの最適化

ポットデスの持ち物はしろいハーブが93.4%とほぼ一択で、2位のきあいのタスキ（4.6%）以下を大きく引き離します。

| 持ち物 | 採用率 | 役割 |
|---|---|---|
| しろいハーブ | 93.4% | からをやぶるの能力低下を1度回復 |
| きあいのタスキ | 4.6% | 弱点1発を耐えて積む保険 |
| メンタルハーブ | 0.6% | ちょうはつ等で積みを止められるのを防ぐ |

からをやぶるは防御・特防を1段階下げるため、積んだ直後は耐久が落ちます。しろいハーブはこの低下を即座に打ち消すため、「積む→耐久低下を回復→殴られても元の耐久で受ける」という流れが成立します。採用率93.4%という偏りは、ポットデスの型がからをやぶる前提で固まっており、積みの隙を最小化する持ち物が最適解として収束していることを示しています。

きあいのタスキ（4.6%）は弱点技を1発耐えて積む保険ですが、しろいハーブの「積み後の耐久維持」と比べて少数派にとどまります。これは、ポットデスがゴースト・あくの2弱点しか持たず、ノーマル・かくとうを無効化できるため、そもそも弱点技を撃たない相手の前で積む立ち回りが基本だからです。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">指標</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">持ち物</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HB積みバトン型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バトンタッチ 88.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しろいハーブ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積んだA・C・Sを後続へ渡す。物理を耐えて積める</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">バトン先を通せる盤面が前提。自身の火力は薄い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">アシストパワー型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アシストパワー 22.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しろいハーブ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C204とS244〜で自分で抜く。バトン読みに依存しない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">あくに無効化される。止められると積み直せない</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ポットデスはからをやぶる（99.1%）で攻撃・特攻・素早さを2段階積み、しろいハーブ（93.4%）で低下を打ち消し、バトンタッチ（88.4%）で後続へ上昇を引き継ぐ起点役です。高い特攻134を持ちながら攻撃技はシャドーボール1枚に絞られ、役割は「自分で抜く」より「後続のアタッカーを起動させる」ことに寄っています。

ゴースト単タイプでノーマル・かくとうを無効化でき、弱点はゴースト・あくの2タイプのみと積む隙を作りやすい一方、HP実数値167と素のすばやさS実数値108〜122は低く、ゴースト・あく技で弱点を突かれると積む前に落とされます。バトン先の物理エース（ドリュウズ・ギャラドス）と、あく技を半減する後続を揃えた構築単位での運用が前提になります。

---

## 関連記事

- [バトン先候補となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [天敵のゴースト枠 ゲンガーのM-2考察](/blog/gengar-analysis-m2/)
- [あく技で弱点を突く高速アタッカー ゲッコウガのM-2考察](/blog/greninja-analysis-m2/)
