---
title: '【ポケモンチャンピオンズ】ミミッキュ 考察 M-5 シーズン 使用率5位に後退した理由をデータで解説'
description: 'M-5シングルバトルで使用率5位に後退したミミッキュを分析。シャドークロー-10.1pp・いのちのたま-6.2ppの変化と、はがね/ゴースト対策ポケモンの台頭をデータで解説。'
updatedDate: '2026-08-16'
pubDate: '2026-08-16'
heroImage: '../../assets/hero-mimikyu-m5.png'
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
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ（M-5）" />
  <div>
    <h2 style="margin:0 0 8px">ミミッキュ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">5位</strong>（M-4は2位）　特性: <strong>ばけのかわ 100%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-5シーズン時点の集計です

M-5のミミッキュは使用率5位に後退しました。ばけのかわで最初の1発を最大HPの1/8の消費で肩代わりし、つるぎのまいで積んでからいのちのたま補正の一致技で押し切る積みエースという基本コンセプトはM-4から変わっていませんが、技・持ち物の採用率には明確な変化が出ています。詳細は後述のデータ分析で解説します。

---

## 基本スペック

### 種族値

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:27.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">55</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">90</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:25%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:48%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#059669">96</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">476</span>
  </div>
</div>

A90・S96という数値は単体では高くありませんが、ばけのかわで確保したつるぎのまい1積みがA実数値を実質2倍にし、いのちのたまの1.3倍補正と合わせて高い火力に到達します（具体的な確定数は後述の型解説で示します）。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はゴースト・はがねの2タイプのみです。かくとう・ノーマル・ドラゴンの3タイプを無効化します。M-5使用率上位にははがね技採用率の高いメタグロス（9位・バレットパンチ92.6%）、ハッサム（12位・バレットパンチ99.7%）、ゴースト技採用率の高いサーフゴー（21位・シャドーボール98.8%）が存在し、いずれもばけのかわ解除後の主要な脅威になります（詳細は「苦手なポケモン」で解説）。

---

## 特性

<strong>ばけのかわ（100%）</strong> — ばけたすがたの間に技のダメージを受けると、そのダメージの代わりに最大HPの1/8を消費して「ばれたすがた」に変わる特性です。ダメージを完全無効化するのではなく、最大HPの1/8を身代わりのように失う点に注意が必要です。どくどく等、直接ダメージを伴わない変化技による状態異常は防げません。この1発肩代わりを利用してつるぎのまいを安全に積むのがミミッキュの基本戦術ですが、解除された時点で実効HPはすでに最大HPの7/8まで減っています。以下の型解説・苦手対面の耐久計算はすべてこの「最大HP−最大HPの1/8（切り捨て）」の実効HPを基準にしています（H1-A32-B1-S32型はHP131→実効HP115）。ばけのかわ解除後（2発目以降）は種族値通りの耐久（B80・D105）で通常のダメージ計算が適用されます。

---

## 主要な技と採用率（M-5）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center;width:40px">順位</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">M-5採用率</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じゃれつく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">97.3%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">一致技のメイン打点。ドラゴン・あく・かくとうタイプに×2</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かげうち</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">40</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">96.6%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">優先度+1の一致先制技。S負けの相手に先制打点</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>つるぎのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">82.7%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">A2段階アップ。ばけのかわが最大HPの1/8消費で1発肩代わりする間に積む</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>シャドークロー</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">70</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong>57.9%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">じゃれつくが半減されるメタグロス（はがね/エスパー）等に一致×2で通る</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>のろい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">17.3%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">自分の最大HP半分を消費し、以後毎ターン相手に最大HP1/4のダメージを与える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ウッドハンマー</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">16.8%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">非一致だが高威力。じめんタイプの相手に有効</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ドレインパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">12.0%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">与ダメージの半分を回復。長期戦での維持力を確保</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>トリックルーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5.3%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">場の素早さを反転。低速運用のTR軸のみで採用</td>
</tr>
</tbody>
</table>
</div>

じゃれつく・かげうち・つるぎのまいはほぼ固定枠です。4枠目はシャドークロー57.9%が最多で、のろい17.3%・ウッドハンマー16.8%・ドレインパンチ12.0%が選択肢として続きます。

---

## 主な型

### 型1: いのちのたまASいじっぱり型 — 最多採用

**性格採用率: いじっぱり 82.2%**

EVはH1-A32-B1-S32（24.1%）とH2-A32-S32（19.4%）が拮抗しており、A156・S148は共通ですが、HPはH1が131・H2が132、BはH1が101・H2が100と1ずつ異なります。M-4序盤（7/13時点、いじっぱり80.7%）からさらに構成比が高まっています。

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いのちのたまASいじっぱり型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ばけのかわ（100%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H1 A32 B1 S32（採用率24.1%）<br>
<strong>持ち物:</strong> いのちのたま（80.5%）
</div>
<div>
<strong>技構成:</strong><br>
・じゃれつく（97.3%）<br>
・かげうち（96.6%）<br>
・つるぎのまい（82.7%）<br>
・<span style="color:#1d4ed8">シャドークロー57.9% / のろい17.3%</span>
</div>
</div>
</div>

ばけのかわを盾にしてつるぎのまいを1回積みます。積み後のA実数値は312相当となり、いのちのたまの1.3倍補正・タイプ一致1.5倍補正を合わせると、4枠目の技選択が確定数に直結します。積み後のじゃれつく（フェアリー90）はドラゴン・あく・かくとうタイプに×2で通りますが、メタグロス（はがね/エスパー）のようなはがね複合には半減（×0.5）にとどまります。積み後のシャドークロー（ゴースト70）はメタグロスのようなはがね/エスパー複合に×2で通り、じゃれつくが半減される局面を補います（ハッサムのようなむし/はがね複合には等倍にとどまり×2にはなりません）。M-4シーズンでもじゃれつく・かげうち・つるぎのまいを固定枠としシャドークローで補完する同じ型構成が主流でしたが、シャドークローの4枠目採用率は68.0%→57.9%に低下しており（詳細後述）、のろい・ウッドハンマー等への分散が進んでいます。

**強み:**

つるぎのまい1積み後のA実数値312・いのちのたま込みのじゃれつく（フェアリー90）は、フェアリー技が刺さるドラゴンタイプに対して高い火力を発揮します。たとえば最多EV(H2-A32-S32・ようき、B115)のガブリアス（HP185）には、タイプ一致補正・いのちのたま・タイプ相性×2を合わせた最小乱数でもHP185を大きく上回るダメージとなります。ただしガブリアスの持ち物1位はきあいのタスキ（40.2%）で、タスキ所持個体はHP満タンから確定1発を耐えるため、この確定1発が成立するのはタスキ非所持（残り約6割）の場合に限られます。

**弱み:**

S実数値148（いじっぱりS32）を上回るポケモンに対して、ばけのかわ解除後は後手に回ります（型を問わず後手に回る相手については後述のまとめで解説します）。また弱点のはがね技を持つメタグロス・ハッサムに対しては、じゃれつく（フェアリー）が半減（×0.5）にとどまります。メタグロス（はがね/エスパー）にはシャドークロー（ゴースト）が×2で通り火力を補えますが、ハッサム（むし/はがね、ハッサムナイト採用率59.6%・約4割は非メガ）にはシャドークローも等倍止まりで、フェアリー・ゴースト双方が通りにくい相手です（ハッサムはミミッキュ自体の弱点であるはがね技の使い手でもあり、単体で突破が難しい理由は後述の「苦手なポケモン」で解説します）。

---

### 型2: いのちのたまASようき型 — 少数派

**性格採用率: ようき 13.7%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いのちのたまASようき型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ばけのかわ（100%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32-B2-S32（採用率3.5%・S162）<br>
<strong>持ち物:</strong> いのちのたま（80.5%）
</div>
<div>
<strong>技構成:</strong><br>
・じゃれつく（97.3%）<br>
・かげうち（96.6%）<br>
・つるぎのまい（82.7%）<br>
・シャドークロー 57.9%
</div>
</div>
</div>

**強み:**

S実数値162で、いじっぱり型のS148より14速くなります。ただしサザンドラ・サーフゴー・ガブリアス・キラフロル・ブリジュラスはこだわりスカーフ採用率が13.8〜82.9%と無視できない水準で、スカーフ持ちにはS148・S162のどちらでも先手を取れません。一方でメガカイリューやメガ後のリザードン／メガバシャーモ、非メガのウルガモス（S32振り個体に限る）のように、性格やメガの別を問わずS149〜161帯に収まる個体は多く、こうした相手にはようき型のみが先手を取れます（詳細はデータ分析で解説）。

**弱み:**

A実数値は142（いじっぱり156より14低い）となり、積み後A284で動くためいじっぱり型積み後A312と比べて火力が下がります。たとえば積み後のシャドークロー（等倍、いのちのたま込み）をメガハッサムの最多EV型（H32-A2-B32・17.5%、B192・HP177）に打つ場合、いじっぱり型の乱数は85〜101、ようき型は75〜91となり、単発ではどちらも確定1発には届きません。ただし2発合計で見ると、いじっぱり型は170〜202でHP177を上回る乱数の組み合わせが8割超に達し2発で削り切れる一方、ようき型は150〜182でHP177を上回る組み合わせが1割に満たず、多くの乱数で2発でも削り切れません。単発の乱数差以上に「2発で処理できるか」の期待値に大きな差が生まれます。なお同じシャドークローをメガメタグロス（H2-A32-S32型・B170・HP157）に打つ場合はいじっぱり型189〜226、ようき型174〜205でどちらも確定1発になり、この相手では型間の火力差は結果を左右しません。

---

## データ分析：ようき型の速度優位が機能する相手の範囲

型2（ようき）のS実数値162は、いじっぱり型のS148より14速くなりますが、この優位が実戦でどこまで機能するかは相手の性格・持ち物分布次第です。数値上ようき型の速度が明確に効くのは、性格・メガ進化の有無を問わず、非スカーフ個体のS実数値がいじっぱり型のS148〜ようき型のS162の間（S149〜161帯）に収まる場合に限られます。この帯に該当する主なポケモンは以下のとおりです（M-5使用率上位・非スカーフを基準にしています）。

- **サザンドラ**（最多性格ひかえめ76.1%・S150で、非スカーフでもいじっぱり型のS148には先手、ようき型のS162には後手）：ただしこだわりスカーフ採用率82.9%と非常に高く、大多数の個体には両型とも先手を取れません。
- **メガカイリュー**（カイリュナイト採用率80.4%、最多性格ひかえめ43.2%でS152。いじっぱり型のS148には先手、ようき型のS162には後手）：2番目に多いおくびょう35.4%はS167でようき型のS162も上回ります。
- **ガブリアス**（最多性格はようき50.9%・S169で、いじっぱり型・ようき型どちらのミミッキュにも先手を取られます。2番目に多いいじっぱり31.6%・S154の個体に対してのみ、いじっぱり型のS148では後手、ようき型のS162なら先手です）：ただし持ち物1位はきあいのタスキ40.2%、2位こだわりスカーフ20.0%で、スカーフ持ちにはどちらの型も先手を取れません。
- **キラフロル**（2番目に多い性格おくびょう42.0%・S151）：最多性格ひかえめ（51.6%・S138）なら両型とも先手を取れます。おくびょう個体のうち非メガ・非スカーフに限ればようき型のみ先手ですが、こだわりスカーフ採用率15.7%に加えキラフロルナイト採用率15.3%もあり、メガ後はS101・おくびょうEV32でS168となってようき型のS162さえ上回るため、この2つを合わせた個体にはようき型でも先手を取れません。
- **サーフゴー**（2番目に多い性格おくびょう28.1%・S149）：最多性格ひかえめ（51.5%・S136）なら両型とも先手を取れますが、おくびょう個体にはようき型のみ先手（ちょうどS148を1超えるボーダーライン）です。こだわりスカーフ採用率31.0%と高めです。
- **ブリジュラス**（3番目に多い性格おくびょう16.8%・S150。2番目はずぶとい17.6%）：最多性格ひかえめ（42.5%・S137）なら両型とも先手を取れますが、おくびょう個体にはようき型のみ先手です。こだわりスカーフ採用率13.8%です。
- **リザードン**（使用率10位・S100、メガ進化後もS100。最多性格ひかえめ34.3%でS152。メガストーン採用率はリザードナイトY57.9%＋X41.1%で計99.0%と大多数がメガ進化し、こだわりスカーフ採用率は0.1%とほぼいない）：メガ後S152はいじっぱり型のS148には先手、ようき型のS162には後手です。2番目に多いおくびょう22.9%はS167で、ようき型のS162も上回ります。
- **ウルガモス**（使用率29位・S100、メガ進化は存在しません）：最多EV配分はH32-B32-S2（12.5%、S実数値122前後）で、多数派はS投資が薄くいじっぱり型のS148にも後手です。S32振り個体はH1-B1-C32-S32（10.1%）＋H2-C32-S32（7.7%）の合計約2割弱に限られ、この個体に限れば性格次第でS152（ひかえめ・ずぶとい等の無補正）〜S167（おくびょう等の+S性格）になります。こだわりスカーフ採用率は1.8%とごく少数です。
- **メガバシャーモ**（使用率23位。バシャーモナイト採用率63.7%、最多性格いじっぱり67.5%でメガ後S152、特性かそく採用率98.9%）：メガ後S152はいじっぱり型のS148には先手、ようき型のS162には後手ですが、これはメガ進化した直後の1ターン目のみです。かそくはターン終了時にS+1段階（×1.5）上昇するため、2ターン目以降はS228となり、ようき型のS162でも先手を取れなくなります。2番目に多いようき18.8%はメガ後S167で、1ターン目からようき型のS162も上回ります。

これらはS実数値が149〜161帯に入る個体に対して、いじっぱり型のS148には後手、ようき型のS162には先手という差が生まれます。一方でリザードンのおくびょう22.9%（S167）・メガバシャーモのようき18.8%（S167、かつ2ターン目以降はかそくでS228）・サザンドラ（スカーフ82.9%）・ガブリアス（きあいのタスキ40.2%・スカーフ20.0%）・キラフロル（スカーフ15.7%・メガ15.3%）のように、性格やスカーフ・メガの採用状況次第でこの帯から外れる個体も多く、該当する個体の割合は相手ごとに確認が必要です。

---

## データ分析：M-4序盤→M-5 採用率変化

技・持ち物・性格の採用率は、M-4シーズン序盤（2026-07-13時点）とM-5シーズン（2026-08-10時点）の集計を比較しています。M-4シーズン自体は2026-07-09〜08-04まで続いており、以下の表はM-4の中でも序盤の時点との比較です。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-4（7/13時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-5（8/10時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">方向</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">シャドークロー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">68.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>57.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-10.1pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">のろい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>17.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+4.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ウッドハンマー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">12.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>16.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+4.3pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">いのちのたま</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">86.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>80.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-6.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">のろいのおふだ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>5.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+3.2pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>82.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+1.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">14.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-0.9pp</td>
</tr>
</tbody>
</table>
</div>

もっとも大きな変化はシャドークロー-10.1ppです。代わりに増えたのろい（+4.1pp）・ウッドハンマー（+4.3pp）はいずれも非一致・変則的な技で、4枠目の選択が「シャドークロー一強」から分散する動きが見えます。いのちのたまも-6.2ppとなり、ゴースト技のみを1.2倍にするのろいのおふだが2.2%→5.4%に増加しています（のろいのおふだはじゃれつくには効果がないため、かげうち・シャドークロー中心の運用でのみ選択肢になります）。

このシャドークロー-10.1pp（68.0%→57.9%）は、メガメタグロス対面の打点に直結します。積み後のじゃれつく（フェアリー90・A312・いのちのたま込み）はメガメタグロス（はがね/エスパー、B170・HP157）に半減（×0.5）で通り59〜71ダメージにとどまりますが、シャドークロー（ゴースト70・×2）なら189〜226で確定1発です。つまりシャドークローを持たない構成（4枠目にのろい・ウッドハンマーを採用した個体）は、メガメタグロス相手にじゃれつく＋かげうちを重ねても2発以上必要になり、対策側に後続を用意する猶予を与えやすくなります。シャドークローの採用率低下がそのままメガメタグロス対面の突破力低下に結びついている一例です。

使用率自体もM-4の2位からM-5は5位に後退しました。ここでは使用率順位の推移をM-4最終盤（8/4時点）とM-5（8/10時点）で比較します。同時期に、ミミッキュの弱点であるはがね・ゴースト技を高採用率で持つポケモンの使用率が上昇しています。ハッサム（バレットパンチ99.7%）は23位→12位、サーフゴー（シャドーボール98.8%）は29位→21位まで順位を上げており、こうした対策ポケモンの台頭がミミッキュの使用率後退の一因になっている可能性があります。

---

## 苦手なポケモン

ミミッキュの弱点はゴースト・はがねの2タイプ（いずれも×2）で、ばけのかわ解除後はこの2タイプの技に対して脆くなります。ばけのかわは技のダメージを最大HPの1/8消費に置き換えて解除される特性のため、解除された時点でミミッキュのHPはすでに最大HPの7/8まで減っています。以下はM-5使用率上位から該当ポケモンを挙げたもので、ミミッキュ側はH1-A32-B1-S32いじっぱり型（HP131・実効HP115）を基準に、物理技はB101、特殊技はD125を防御側の基準値として使用しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">主力技（採用率）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ダメージ目安</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ブリジュラス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ラスターカノン（75.0%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ひかえめC194基準で140〜168ダメージ・確定1発（実効HP115基準）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガメタグロス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">バレットパンチ（92.6%・優先度+1）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">確定1発（実効HP115基準・16乱数全て実効HPを上回る）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0212-00.webp" alt="メガハッサム" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガハッサム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">バレットパンチ（99.7%・優先度+1、ハッサムナイト採用率59.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">確定1発（実効HP115基準・メガ時、A189基準）。Aへの振り量に関わらず確定。非メガ（A130）の場合は最多EV型（H32-A2-B32・17.5%、A167、A無振りに近い）だと114〜134の乱数で16分の14が実効HP115を上回る高乱数1発にとどまり確定ではなく、A特化型（H32-A32-B2・10.4%等、A200）では134〜162で確定1発になります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アイアンヘッド（35.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">最多EV配分H32-B32-D2（採用率42.9%、A無振り。性格は別途わんぱくが最多63.8%）が相手の場合、アイアンヘッドのダメージは実効HP115基準でも16乱数中1発しか上回らず非確定です。ミミッキュ側もアーマーガアの高い耐久を崩しにくく、互いに決定打を欠く相手です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ（オス）" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">イダイトウ（オス）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">シャドーボール（72.4%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">確定1発（実効HP115基準）。特性てきおうりょく採用率94.8%で一致ゴースト技が通常の1.5倍ではなく2倍補正になります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ゲンガー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">シャドーボール（88.3%、ゲンガナイト採用率80.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">確定1発（実効HP115基準）。最多性格おくびょう（76.3%）でC182・S178、メガ時（ゲンガナイト80.6%）はC222・S200とミミッキュより速くなります（S148/S162）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギルガルド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポルターガイスト（62.9%）・シャドーボール（32.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">確定1発（実効HP115基準）。攻撃時は特性バトルスイッチでブレードフォルム（A140・B50。通常のシールドフォルムA50・B140から入れ替わる）になり、A211（いじっぱりA32EV基準）で計算します。ミミッキュのじゃれつくは半減されますが、かげうちは×2で通ります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">サーフゴー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">シャドーボール（98.8%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">確定1発（実効HP115基準）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0983-00.webp" alt="ドドゲザン" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ドドゲザン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アイアンヘッド（86.9%）／ふいうち（98.9%・優先度+1）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アイアンヘッドは確定1発（実効HP115基準）。ふいうちは相手が攻撃技を選択したターンのみ成功する技で、そのターンは優先度+1でミミッキュのS実数値を無視して先制されます（つるぎのまいを選んだ積みターンには失敗します）</td>
</tr>
</tbody>
</table>
</div>

メガメタグロス・メガハッサムのバレットパンチは威力40ですが、優先度+1のためミミッキュのS実数値に関係なく先制で当たり、それぞれ特性（かたいツメ・テクニシャン）で威力が底上げされます。メガメタグロス（特性かたいツメで接触技1.3倍、A216いじっぱり基準）・メガハッサム（特性テクニシャンで威力60以下の技が1.5倍、ハッサムナイト採用率59.6%、A189基準）はいずれも、ばけのかわ解除後のミミッキュ標準型（B101・実効HP115）に対し確定1発です（非メガハッサムのA無振り個体は確定ではなく高乱数1発にとどまります。詳細は下表参照）。積み終える前にばけのかわを剥がされるとどちらの相手にも崩されやすくなります。

**対策：**はがね技・ゴースト技の両方を半減できるのは、同居率8位のゲッコウガ（みず/あく）と同居率6位のギャラドス（メガ進化後のみみず/あく、メガ前・素早さ負けで後出しした直後の1ターンはゴースト技が等倍）です。この2体を軸に後出しし、被弾自体を避けるのが基本方針です。リザードンははがね技のみ半減でゴースト技は等倍、ガブリアスはいずれも等倍のため後出し要員にはなりません。

---

## 有利なポケモン

ミミッキュの一致技じゃれつく（フェアリー90）はドラゴン・あく・かくとうタイプに刺さります。ここではM-5使用率20位以内のうち、じゃれつくが×2で通る相手を漏れなく挙げます（同居率上位のパートナーと重複するポケモンも、型の相性としては別に成立するため掲載しています）。ダメージはいのちのたまASいじっぱり型（積み後A312）を基準に、相手はEV最多分布・B無振りを基準としています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">相手の主力技（採用率）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じゃれつくのダメージ目安</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じしん（99.5%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ドラゴン/じめん複合に×2で確定1発（358〜423）。特性さめはだでミミッキュも反動を受け、きあいのタスキ（40.2%）持ちには耐えられます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">マスカーニャ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">トリックフラワー（96.9%）・はたきおとす（65.1%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">くさ/あく複合に×2で確定1発（460〜540）。最多性格ようき（S実数値192）で速く、スカーフの有無に関わらず先手を取られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じしん（76.8%）・りゅうのまい（82.3%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メガ後（みず/あく、採用率77.8%）にじゃれつくが×2で通り、実質+1段階（A234相当、いかく99.2%込み）で239〜282ダメージ・確定1発（HP171基準）です。ただしメガギャラドスの特性はかたやぶりで、ばけのかわ（ばけたすがた）を無視して1発目から実ダメージが直接ミミッキュに通ります。じしん（じめん・等倍）でも85〜100ダメージが最大HP131（ばけのかわ非適用時）に直接入るため、通常なら1/8消費で済むはずの1発目がそのまま大きく削られる点には注意が必要です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カイリュー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">かえんほうしゃ（66.7%）・りゅうせいぐん（54.4%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ドラゴン/ひこう複合に×2で通りますが、メガ後（80.4%）は特性マルチスケイルで乱数1発（152〜179、確定ではない）にとどまります。りゅうせいぐんはミミッキュに無効</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">サザンドラ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">あくのはどう（99.2%）・りゅうせいぐん（93.0%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">あく/ドラゴン複合に×4で確定1発（748〜889）。ただしこだわりスカーフ採用率82.9%でS225となり、ミミッキュより速く先手を取られることが多い相手です。主力りゅうせいぐんはミミッキュに無効なので、先制されても致命傷にはなりません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ゲッコウガ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">れいとうビーム（91.1%）・あくのはどう（86.4%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">みず/あく複合に×2で425〜500ダメージ・確定1発（メガ後HP149基準）。メガ進化率65.4%で、メガ後はS実数値213に達し先手を取られます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位のパートナー

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じしんではがね複合に打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね技を半減し耐性補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお技ではがね複合を処理</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">アンコールで積みターンを作る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ステルスロックで削りを補助</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">りゅうのまいで積み、じしんで打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス">
    <div class="name">メタグロス</div>
    <div class="rate">同居率7位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">バレットパンチで先制打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ">
    <div class="name">ゲッコウガ</div>
    <div class="rate">同居率8位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">広範囲に刺さる特殊打点を供給</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率9位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">物理耐性の高い相手を特殊打点で処理</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率10位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">とんぼがえりで安全に繰り出す</div>
  </div>
</div>

---

## まとめ

M-5のミミッキュは使用率5位に後退しましたが、いのちのたまASいじっぱり型を中心とした積みエースという基本構造はM-4から継続しています。変化点はシャドークロー-10.1ppに象徴される4枠目の分散と、いのちのたま-6.2pp・のろいのおふだ+3.2ppという持ち物選択の多様化です。同時にハッサム・サーフゴーといったはがね・ゴースト技を持つポケモンの台頭がみられ、ばけのかわ解除後の一撃を警戒した立ち回りが以前より重要になっています。

なお、S実数値148（型1・いじっぱり）とS実数値162（型2・ようき）はいずれも、使用率上位のガブリアス（最多性格ようき50.9%・S169）やマスカーニャ（最多性格ようき・スカーフなしでもS192）を上回れません。これは型による差ではなく、ミミッキュ自体のS種族値96に起因する共通の弱点です。この2体に対してはどちらの型でも先手を取れないため、積みターンの確保はばけのかわの1発肩代わりと先制技かげうちに依存する点は型を問わず共通です。

---

## 関連記事

- [ミミッキュ M-4 考察](/blog/mimikyu-analysis-m4/)
- [ミミッキュ M-3 考察](/blog/mimikyu-analysis-m3/)
- [使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/mimikyu/)**
