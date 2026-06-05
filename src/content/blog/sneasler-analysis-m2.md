---
title: '【ポケモンチャンピオンズ】オオニューラ考察 M-2 使用率33位 かるわざ型の採用率と立ち回り'
description: 'M-2シングルバトルで使用率33位のオオニューラを徹底分析。かるわざ(採用率78.2%)としろいハーブ(47.4%)が生むS2倍展開、いじっぱりAS型の構築、インファイト・フェイタルクローの採用率と環境上位への相性を実データで解説します。'
pubDate: '2026-06-04'
draft: true
heroImage: '../../assets/hero-sneasler-m2.png'
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
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" />
  <div>
    <h2 style="margin:0 0 8px">オオニューラ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">33位</strong>　特性: <strong>かるわざ 78.2%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、オオニューラは**使用率33位**を記録。種族値S120の高速かくとうアタッカーで、**78.2%がかるわざ**を採用し、しろいハーブ（持ち物採用率47.4%）と組み合わせて素早さを2倍に跳ね上げる展開型が主流です。

オオニューラの軸は、インファイト（採用率98.6%）使用後のBDダウンをしろいハーブで打ち消し、その消費でかるわざを発動させてS実数値を一気に倍化する一連の流れです。元のS120でも高速ですが、かるわざ発動後はメガゲッコウガ級の高速勢すら抜き去る詰め性能を得ます。

---

## なぜオオニューラが詰め筋として機能するのか

### 1. かるわざ＋しろいハーブでS2倍を確定で起動できる

オオニューラの最大の強みは**特性かるわざ**としろいハーブの噛み合いです。かるわざは持ち物を消費すると素早さが2倍になる特性で、インファイト（98.6%）はタイプ一致のメインウェポンでありながら使用後にBとDが1段階下がります。このダウンをしろいハーブが自動で元に戻して消費されるため、**攻撃を撃つだけでかるわざのS2倍がほぼ確定で起動**します。

いじっぱりS最大振り（S32）でS実数値は約172。かるわざ発動でこれが約344相当になり、環境のほぼ全ポケモンを上から叩ける状態になります。インファイトのデメリットを起動キーに転用している点が、この型の設計上の核心です。

### 2. 起動前のS120でも環境上位の中速以下を上から処理できる

しろいハーブ消費前でも、種族値S120はトップクラスです。いじっぱりS最大振りでS実数値約172、最速ようきなら約189に達し、起動を待たずとも以下の中速アタッカーには先手を取れます。

- ガブリアス（S102・使用率1位）
- ブリジュラス（S85・2位）
- サザンドラ（S98・21位）
- マフォクシー（S104・25位）

ただしS120を上回る高速勢には起動前は先手を取られます。最速マスカーニャ（S123・3位）・ゲッコウガ（S122・28位）は、こちらがようきS189でも僅かに上回られるため、かるわざ起動前のターンは無理に正面から撃ち合わないことが前提になります。

### 3. ねこだまし・つるぎのまいで起動ターンを作れる

ねこだまし（採用率36.3%）は優先度+3の先制技で、**相手の素早さに関わらず先制**してひるませます。起動を1ターン安全に進める時間を作る用途で、低耐久のオオニューラが展開の起点を確保するのに使われます。つるぎのまい（30.8%）はA2段階アップで、しろいハーブ起動後の高速インファイトの一撃をさらに伸ばし、半端な耐久ラインを確定圏へ押し込みます。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:20%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right">40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:60%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">120</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">510</span>
  </div>
</div>

こうげき130・すばやさ120の攻撃寄りステータスで、A・Sにリソースが集中しています。一方でぼうぎょ60と耐久は低く、半端なダメージでも上から落とされやすいため、**先手で殴り切るか先制技で詰める**速攻型の立ち回りが前提になります。とくこう40はほぼ死にステータスで、採用される技は物理に統一されています。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="かくとう" />
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="どく" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（¼）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

エスパーが**×4の致命的な弱点**となる点が最大の注意点です。じめん・ひこうも×2で通り、いずれもオオニューラのぼうぎょ60では一撃で落とされかねません。一方でかくとう・むしを¼、くさ・どく・いわ・あくを半減で受けられるため、マスカーニャのはたきおとす（あく0.5）・トリックフラワー（くさ0.5）やゲッコウガのあくのはどう（あく0.5）といった環境上位の高速勢の主力を軽減でき、被弾しても一撃で崩されにくくなります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致メインウェポン。使用後BとD1段階ダウン→しろいハーブ消費でかるわざ起動</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>フェイタルクロー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">95.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致どく技。30%でどく・まひ・ねむりのいずれかを付与。フェアリー・エスパーへの打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じごくづき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>52.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく打点。命中後2ターン相手の音技を封じる。ゴースト・エスパーへの打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねこだまし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>36.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+3。場に出た最初のターンのみ。ひるませて起動ターンを稼ぐ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>30.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A2段階アップ。起動後の全抜き圏を拡大</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代できる。不利対面から後続へ繋ぐ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクロバット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55／110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物がない時に威力2倍。しろいハーブ消費後は威力110で撃てる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>いわなだれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう・ほのお・むしへの打点。30%でひるみ</td>
</tr>
</tbody>
</table>
</div>

インファイト・フェイタルクローの2つの一致技でほぼ枠が確定し、残りはじごくづき（あく）でゴースト・エスパー耐性持ちを崩すか、ねこだまし・つるぎのまいで起動・全抜きを補助するかの選択になります。

---

## 主要型の解説

性格分布はいじっぱり65.4%・ようき29.4%で、AS物理型に二分されます。

### 型1: かるわざAS型（最多採用）

**性格採用率: いじっぱり 65.4%**（AS物理型の指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">かるわざ・しろいハーブ いじっぱりAS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かるわざ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32 S32（余り2はHに振る＝最多型）<br>
<strong>持ち物:</strong> しろいハーブ
</div>
<div>
<strong>技構成:</strong><br>
・インファイト<br>
・フェイタルクロー<br>
・じごくづき / つるぎのまい<br>
・ねこだまし / じごくづき
</div>
</div>
</div>

**強み:**

いじっぱりでこうげき実数値を最大化し、しろいハーブ起動後の高速インファイトで一気に削り切る型です。EVはA32 S32が基本で、余り2をHに振る配分（採用率46.4%）が最多。S実数値約172で起動前からガブリアス（S102）・ブリジュラス（S85）の上を取れ、しろいハーブ消費後はS約344相当となり最速マスカーニャ（S123）・ゲッコウガ（S122）すら抜き返します。

ようき型（採用率29.4%）と比べてこうげき実数値が約10%高く、つるぎのまいを積まずとも半端な耐久ラインを一撃圏に入れられるのが利点です。

**弱み:**

しろいハーブを起動に使うため、起動キーであるインファイトを撃つ初動でB・Dが下がる隙が生まれます。エスパー（×4）・じめん・ひこう（×2）を持つ相手の前では、起動ターンに弱点技を合わせられると低耐久ゆえ即座に崩されます。ようき型と異なり起動前のS172圏では同速帯のS120ポケモンや、ようきなら五分に持ち込める一部の高速勢にも先手を許す点が、いじっぱり型固有のリスクです。

---

### 型2: かるわざAS型（ようき）

**性格採用率: ようき 29.4%**（AS物理型の指標。いじっぱりに次ぐ2番手）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">かるわざ・しろいハーブ ようきAS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かるわざ<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32 S32<br>
<strong>持ち物:</strong> しろいハーブ / きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・インファイト<br>
・フェイタルクロー<br>
・ねこだまし<br>
・じごくづき / つるぎのまい
</div>
</div>
</div>

**強み:**

ようきでS実数値約189まで上げ、起動前の素の状態でもS120ミラーで先手を取り、いじっぱり（S172）では同速・後攻になるS120前後の相手を確実に抜ける点がいじっぱり型との差です。最速マスカーニャ（S192）・ゲッコウガ（S191）には僅差で及ばないものの、起動を待たず多くの相手に先制で一致技を通せます。きあいのタスキを持つ場合は一発耐えてからの確定行動を保証でき、ねこだまし＋一致技で2回行動して詰める動きが安定します。

**弱み:**

いじっぱり型に比べこうげき実数値が約10%低く、つるぎのまい未経由ではガブリアス級の高耐久を一撃圏に入れにくくなります。きあいのタスキ採用時はかるわざが起動しないため、S2倍による追い抜きを捨てて素のS189で戦う構成になります。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出るポケモン

使用率TOP30から、オオニューラと相性がはっきり分かれる相手を有利・不利の両面で挙げます。一致のインファイト（かくとう）とフェイタルクロー（どく）、サブのじごくづき（あく）が刺さるかどうかと、相手の主力技がオオニューラの弱点（エスパー×4／じめん・ひこう×2）を突くかで評価します。倍率は2タイプの掛け合わせで計算しています。

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
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 超有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトが×4（あく2×はがね2）。S50で確実に先手。先制技ふいうち（採用率99%）もこちらにあく0.5で半減</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトが×2（はがね2×ドラゴン1）。S85で先手確保。つるぎのまい1積みで確定圏。特殊型主体でこちらの弱点を突く技が乏しい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトが×2（あく2×ドラゴン1）。S98で先手。かえんほうしゃ（67%）はこちらに等倍止まりで弱点を突かれない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利（起動後）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトが×2（くさ1×あく2）。主力トリックフラワー（くさ0.5）・はたきおとす（あく0.5）はこちらに半減で撃ち合いに強い。素の最速個体（S192）には僅差で先攻されるため、しろいハーブ起動後に先手を確定させたい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じごくづき（あく×2、採用率52.3%）採用個体ならS110＜120で先手で削れる。主力のヘドロウェーブ（どく81.7%）・きあいだま（かくとう37.4%）はいずれもこちらに×0.5で弱点を突かれない。みちづれ（30.5%）で相討ちを狙われる点に注意</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">▲ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S102＜120で先手は取れるが、インファイト等倍（かくとう vs ドラゴン1×じめん1）で108HPを一撃にできず、返しのじしん（99.2%）が×2でこちらを落とす</td>
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
    <img src="/images/pokemon/pokemon-0655-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マフォクシー（25位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコショック（50.4%）・サイコキネシス（38.3%）がエスパー×4で、低耐久のオオニューラは一撃。S104＜120で先手は取れるが、こちらのインファイトはほのお1×エスパー0.5＝×0.5半減で一撃に届かない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェイタルクロー（どく×2）なら先手で大ダメージ。確実に倒すにはあく・はがねタイプ（ドドゲザン等）を同伴し後出しで処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0121-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">スターミー（20位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のアクアブレイク（89.2%）・アイススピナー（64.9%）はこちらに等倍だが、しねんのずつき（39.4%）・サイコカッター（24.7%）のエスパー技を持つ個体はこちらに×4で一撃。S115＜120で先手は取れるがインファイト（みず/エスパーに等倍）では一撃にできず、エスパー技採用個体には撃ち負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェイタルクロー（どく等倍）で削れるが確定数は遅い。エスパー技を半減するはがね・あくタイプを同伴して後出しで処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">高HP・高Bでインファイト等倍（かくとう vs じめん1）では一撃にできず、じしんがこちらに×2。S47で遅いが殴り合いで決定力負け</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">単体では崩しにくい。くさ・みず・こおりタイプ（弱点×2）を同伴して上から処理する。とんぼがえりで有利な後続に繋ぐ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主流のメガY（ほのお/ひこう）にはアクロバット（ひこう）が等倍、いわなだれ（×4）は採用率9.2%と低い。エアスラッシュ等ひこう技はこちらに×2、メガXのフレアドライブも痛い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわなだれ採用個体なら先手で弱点を突ける。非採用ならみず・いわ・でんきタイプを同伴し後出しで処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エアスラッシュ（55.6%）がひこう×2でこちらを脅かす。インファイト等倍では高HPを一撃にできず、しんそく（45.6%・優先度+1）で削られると先制返しも受ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおり・フェアリー・いわタイプ（弱点×2〜4）を同伴して上から落とす。マルチスケイル下では単体での突破は困難</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 同居率の高いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0939-00.webp" alt="ハラバリー">
    <div class="name">ハラバリー</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき枠。オオニューラが苦手なひこう・みず勢に上から打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0115-00.webp" alt="ガルーラ">
    <div class="name">ガルーラ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高耐久の物理アタッカー。受けにくい相手の起点を作る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめん枠。オオニューラが等倍止まりのはがね・どくにじしんで打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでひこう・エスパーを半減し弱点を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率9位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ゴーストでエスパーを半減。みず技でじめん勢に打点</div>
  </div>
</div>

**パーティ構成の基本方針:**

オオニューラはエスパー×4を筆頭に弱点が刺さりやすく耐久も低いため、残り5体で以下を補います。

1. **エスパー対策**: あく・はがねタイプ（ブリジュラス等）でエスパー技を受ける枠
2. **じめん対策**: ひこう・くさタイプを置き、ガブリアス・カバルドンのじしんを受ける枠
3. **起点作り**: ねこだまし・とんぼがえりで対面を整え、有利な相手に起動を通す
4. **高速の上から処理**: オオニューラが起動前に抜けないマスカーニャ・ゲッコウガをでんき・氷技で先に削る枠

---

## データ分析①：かるわざ起動を支える持ち物選択の偏り

オオニューラの持ち物は、しろいハーブ47.4%・きあいのタスキ21.5%・オボンのみ16.8%・こだわりスカーフ6.4%と分かれます。特性かるわざ採用が78.2%である一方、起動キーとして最適なしろいハーブは47.4%にとどまる点に、この型の設計上のジレンマが表れています。

| 持ち物 | 採用率 | かるわざ起動 | 役割 |
|---|---|---|---|
| しろいハーブ | 47.4% | ○（インファイトのダウンを消費） | S2倍展開・能力低下の打ち消し |
| きあいのタスキ | 21.5% | △（被弾で消費＝受動的） | 一発保証・ねこだまし併用の起点 |
| オボンのみ | 16.8% | △（HP50%で消費＝受動的） | 低耐久を一度だけ補強 |
| こだわりスカーフ | 6.4% | ×（消費しない） | 素のS120のまま先手固定 |

しろいハーブは**インファイトを撃つ自分のターンに能動的に消費でき、起動タイミングを自分で決められる**点で他と一線を画します。きあいのタスキ・オボンのみも消費でかるわざは起動しますが、いずれも被弾を前提とした受動的な消費のため、起動した頃にはHPが削れており低耐久のオオニューラでは詰めに繋げにくい。スカーフ型に至ってはかるわざと噛み合わず、素のS120を固定する別系統の運用です。かるわざ採用78.2%に対ししろいハーブが半数弱という数値は、「能動起動の安定性（しろいハーブ）」と「一発保証の安心感（タスキ）」のどちらを取るかで使用者の選好が割れていることを示しています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">かるわざAS型（いじっぱり）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 65.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">インファイト・フェイタルクロー・じごくづき・ねこだまし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A実数値が高く一撃の火力で勝る。起動後の全抜き性能</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">起動前S172で最速マスカーニャ・ゲッコウガに先攻される</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">かるわざAS型（ようき）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき 29.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">インファイト・フェイタルクロー・ねこだまし・じごくづき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">起動前S189でS120ミラーや中速上限を抜ける。タスキ併用で起点化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A実数値が約10%低く高耐久を一撃にしにくい</td>
</tr>
</tbody>
</table>
</div>

**総評:**

オオニューラはかるわざ（採用率78.2%）としろいハーブ（47.4%）の組み合わせで、インファイトの能力ダウンを起動キーに転用してS2倍を狙う詰め型アタッカーです。起動後はマスカーニャ・ゲッコウガといった環境最速級すら抜き返し、こうげき130の一致インファイト・フェイタルクローで上から削り切ります。

一方でぼうぎょ60の低耐久とエスパー×4・じめん/ひこう×2の弱点は重く、ガブリアス・カバルドンのじしんやマフォクシー・スターミーのエスパー技の前では先手を取っても突破しきれない場面が多い。使用率33位という立ち位置は、この「起動が決まれば最速級・決まる前は紙耐久」という両極端さを反映しています。ねこだまし・とんぼがえりで対面を選び、有利な相手に起動を通せるかが勝敗を分けます。

---

## 関連記事

- [同じ高速かくとうアタッカー メガルカリオのM-2考察](/blog/lucario-analysis-m2/)
- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [後出しで処理したいリザードン(Y)のM-2考察](/blog/charizard-y-analysis-m2/)
</content>
</invoke>
