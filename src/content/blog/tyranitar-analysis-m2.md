---
title: '【ポケモンチャンピオンズ】バンギラス考察 M-2 使用率38位 型別採用率と立ち回り'
description: 'M-2シングルバトルで使用率38位のバンギラスを徹底分析。すなおこしによる特防1.5倍と高耐久、はたきおとす採用率75%・ストーンエッジ50.7%の技構成、いじっぱり物理型と特殊耐久型の違い、バンギラスナイト採用率48.7%のメガ運用まで実データで解説します。'
pubDate: '2026-06-04'
draft: true
heroImage: '../../assets/hero-tyranitar-m2.png'
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
  <img src="/images/pokemon/pokemon-0248-00.webp" alt="バンギラス" />
  <div>
    <h2 style="margin:0 0 8px">バンギラス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-05-rock.png" alt="いわ" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">38位</strong>　メガ石採用率: <strong>バンギラスナイト 48.7%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、バンギラスは**使用率38位**。特性**すなおこし**で場に出るだけで砂嵐を展開し、いわタイプ自身の特防が1.5倍になる高い特殊耐久が持ち味です。

注目すべきは持ち物分布です。**バンギラスナイトの採用率は48.7%**で、残り半数以上は たべのこし・オボンのみ・各種半減きのみなどメガ進化しない構成を選んでいます。メガ前提のポケモンではなく、**メガ枠をバンギラスに割くかどうかが構築単位で分かれている**点が、このポケモンを語るうえで重要です。本記事ではメガなしの素のバンギラスを主軸に、メガ運用の差分も併せて解説します。

---

## なぜ今バンギラスが使われるのか

### 1. すなおこしで特殊耐久が自動で1.5倍

バンギラスの最大の強みは特性**すなおこし**（採用率99.4%）です。登場時に砂嵐を展開し、いわタイプである自身の特防が砂嵐中ずっと1.5倍になります。とくぼう種族値100に1.5倍補正が乗るため、HD振り（特防最大振り）型では特殊アタッカーの一致技を1発耐えてから反撃する受け出しが可能になります。

砂嵐は相手のすなおこし非対応ポケモンを毎ターン最大HP1/16ずつ削るため、きあいのタスキを無効化し、後続の確定数を縮める副次効果も持ちます。

### 2. はたきおとすで広範囲に打点と妨害を両立

メイン技の**はたきおとす**（採用率75.0%）は、あくタイプ一致でエスパー・ゴーストに×2が通るうえ、相手の持ち物を叩き落として無力化します。環境上位のオボンのみ・とつげきチョッキ・こだわり系を機能停止させられるため、攻撃しながら相手の耐久・火力プランを崩せるのが強力です。あく技はエスパー（スターミー・マフォクシー）やゴースト（ゲンガー・ギルガルド・ミミッキュ）といった上位の中速〜高速アタッカーに刺さります。

### 3. りゅうのまいで抜き性能を後付けできる

採用率29.4%の**りゅうのまい**を1積みすると、こうげき・すばやさが各1段階上昇します。素のすばやさ種族値61は遅い部類ですが、1積みでS実数値が1.5倍になり、中速帯を抜いて高耐久のまま全抜きを狙う型に化けます。耐久で起点を作ってから積む動きは、はたきおとす主体の対面性能とは別軸の勝ち筋です。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:67%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">134</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">110</span>
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
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">61</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
  </div>
</div>

HP100・防御110・特防100にすなおこしの特防1.5倍が加わり、両受けに寄れる高耐久です。こうげき134も高く、受けたうえで殴り返せます。一方ですばやさ61は低く、素では環境の大半に先手を取られるため、耐久で1発受けてから動くか、りゅうのまいで素早さを補う運用が前提になります。

### メガ進化（バンギラスナイト採用時）

バンギラスナイト採用は48.7%。メガ進化してもタイプ（いわ/あく）・特性（すなおこし）は変わらず、種族値が以下のように伸びます。

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <span style="width:32px;text-align:right">100</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">164</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">150</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <span style="width:32px;text-align:right">95</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">120</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <span style="width:32px;text-align:right">71</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:7px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">700</span><span style="width:40px"></span>
  </div>
</div>

こうげき164・防御150と物理方面が大きく伸び、防御150＋特防120（すなおこしで実質180相当）の両受けがさらに堅くなります。一方ですばやさは71止まりで遅さは解消されないため、メガ進化してもりゅうのまいや受け出しを前提とする立ち回りは変わりません。メガ進化を選ぶかどうかは、構築のメガ枠を物理性能の底上げに使うか、別のメガに回すかの判断になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-05-rock.png" alt="いわ" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="いわ" />
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="あく" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">4倍弱点</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">2倍弱点</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー
  </td>
</tr>
</tbody>
</table>
</div>

最大の弱点は**かくとう×4**（いわ2×あく2）です。環境にはルカリオ・オオニューラ・ミミロップなど一致かくとう技を持つ上位アタッカーが多く、これらには受け出しが効きません。じめん・みず・くさ・はがね・むし・フェアリーも×2で通ります。一方、エスパー無効はスターミー・マフォクシーへの起点回避に役立ち、ほのお・ひこう・ゴースト・あくを半減できる点も対ゴースト・対あくで噛み合います。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はたきおとす</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65/97</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">75.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致あく技。相手の持ち物を奪うと威力1.5倍。エスパー・ゴーストに×2</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ストーンエッジ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">50.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致いわ技。命中率80。ほのお・ひこう・むし・こおりに刺さる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>45.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・どく・でんき・ほのおへの打点。いわ技を半減するはがねに有効</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">38.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス・カイリュー等のじめん/ドラゴンへの×4打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">交代を読んで設置。高耐久で繰り返し撒き直せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A・S各1段階アップ。抜き型の核となる積み技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ロックブラスト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25×2-5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">連続技。きあいのタスキ・みがわりを貫通。ストーンエッジより命中安定</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がんせきふうじ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中時に相手のSを1段階ダウン。低速を補い高速勢を抜き返す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ばかぢから</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用後A・Bダウン。同族・カビゴン・ドドゲザン等への打点</td>
</tr>
</tbody>
</table>
</div>

はたきおとす・ストーンエッジの一致2技に、対象を補完する じしん／れいとうパンチを加えるのが基本の攻撃構成です。ストーンエッジ（命中80）は外しが怖いため、命中安定を取るならロックブラスト・がんせきふうじが候補になります。ステルスロック・りゅうのまいの採用で、設置役と抜き役のどちらに寄せるかが分かれます。

---

## 主要型の解説

性格分布（いじっぱり51.6%／しんちょう24.1%／ようき14.6%）が型の指標になります。

### 型1: いじっぱり物理アタッカー型（最多採用）

**性格採用率: いじっぱり 51.6%**（物理型の指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0248-00.webp" alt="バンギラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HAいじっぱり物理型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32（余りをD/Bへ）。最多はHA+D<br>
<strong>持ち物:</strong> バンギラスナイト / たべのこし / オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・はたきおとす<br>
・ストーンエッジ / ロックブラスト<br>
・じしん<br>
・れいとうパンチ / ばかぢから
</div>
</div>
</div>

**強み:**

HA振り（HP・こうげき最大振り）でこうげき134を最大化しつつ、すなおこしの特防補正と高い防御で耐久を確保します。いじっぱりHA型の中ではHA+D（採用率9.5%）が最多で、とくぼうにも余りを割き、特殊・物理どちらの攻撃も1発受けてから はたきおとすで持ち物を奪い、反撃する受けつつ殴る運用です。じしん＋れいとうパンチで はがね・じめん/ドラゴンまで打点が広く、相手を選ばず削りを入れられます。

**弱み:**

すばやさ61のまま動くため、かくとう×4を持つルカリオ・オオニューラに上から一致技で落とされると受け出しが成立しません。積み技を持たないこの型は、高耐久のアーマーガア（ひこう/はがね）に対し はたきおとす・いわ技がともに等倍止まりで決定打を欠き、はねやすめで回復されると膠着します。

---

### 型2: しんちょう特殊耐久型（2番目に多い構成）

**性格採用率: しんちょう 24.1%**（特殊受け型の指標。いじっぱりに次ぐ2番手）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0248-00.webp" alt="バンギラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HDしんちょう特殊受け型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> しんちょう（D↑ C↓）<br>
<strong>EV:</strong> H32 D32（余りをA/Bへ）。最多はHD+A<br>
<strong>持ち物:</strong> たべのこし / オボンのみ / ヨプのみ
</div>
<div>
<strong>技構成:</strong><br>
・はたきおとす<br>
・ストーンエッジ / じしん<br>
・ステルスロック<br>
・れいとうパンチ / ばかぢから
</div>
</div>
</div>

**強み:**

しんちょうHD（とくぼう最大振り）＋すなおこし1.5倍で特殊耐久がいじっぱり型より一段高く、特殊アタッカーの一致技をより安定して受けられます。ステルスロックを絡めれば、受け出しのたびに撒き直して相手の交代を咎められます。かくとう×4のヨプのみを持てば、本来受からないかくとう技を1回だけ耐えて反撃する択も作れます。

**弱み:**

こうげきに振らないためいじっぱり型より火力が落ち、決定力よりサポート寄りになります。物理アタッカーに対してはいじっぱり型ほどの反撃ダメージが出ず、相手を倒しきれずターンを渡しやすいのが、同じバンギラスでも物理型と異なる弱みです。

---

### 型3: ようきりゅうのまい抜き型

**性格採用率: ようき 14.6%**（S振り抜き型の指標。いじっぱり・しんちょうに次ぐ3番手）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0248-00.webp" alt="バンギラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ASようき抜き型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32 S32（余りをHへ）。最多採用のEV配分<br>
<strong>持ち物:</strong> バンギラスナイト / ラムのみ
</div>
<div>
<strong>技構成:</strong><br>
・りゅうのまい<br>
・はたきおとす<br>
・ストーンエッジ<br>
・じしん / れいとうパンチ
</div>
</div>
</div>

**強み:**

S振りでりゅうのまいを1積みするとS実数値が124→186まで伸び、最速ガブリアス（S実数値169）を含む中速〜高速帯を抜き返して全抜きを狙えます。耐久重視のHA・HD型では積んでも素早さが足りず抜き性能が出ないため、S投資で抜き役に振り切れる点がこの型固有の強みです。受けではなく、対面で1回積んでから制圧する攻めの勝ち筋を持ちます。

**弱み:**

HD型のような特殊耐久補強がなく、積む前に上から殴られると起点を作れません。ラムのみ以外の弱点ケアきのみを持てないため、積みターンを与えてくれる遅い相手や交代際でしか起動できず、HA・HD型より対面の安定性で劣ります。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、バンギラスと相性がはっきり出るポケモンを有利・不利の両面から挙げます。エスパー無効とほのお・ひこう・ゴースト・あく半減に噛み合う相手には強い一方、かくとう×4およびじめん・みず・はがねの×2を突いてくる相手には脆い点に注意してください。

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
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとすがゴースト×2。主力のヘドロウェーブ（どく・採用率81.7%）は半減。ただしきあいだま（37.4%）採用個体にはかくとう×4を返されるため、無採用個体に強い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0121-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">スターミー（20位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ エスパー技には強い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しねんのずつき（39.4%）等のエスパー技を無効化。ただし主力のアクアブレイク（89.2%）が×2弱点で、メガスターミーのS120から先制され、先制アクアジェット（86.9%）まで持つため対面では押し負ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド（11位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんがはがね/ゴースト複合に×2。主力のかげうち（96.2%）・ポルターガイスト（67.6%）のゴースト技を半減し受けつつ殴れる。せいなるつるぎ（31.7%）採用個体のかくとう×4には注意</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ れいとうパンチ採用時有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチがドラゴン/ひこうに×4。ただし採用率38.6%のため、無採用個体ではドラゴン技を半減するに留まり決め手を欠く</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ ストーンエッジ採用時有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ストーンエッジがほのお/ひこうのメガYに×4、ほのお技も半減で受けやすい。ただしメガX（ほのお/ドラゴン）にはいわ×2止まりで、こうげき種族値130の物理技を等倍で受けるため一方的には倒せない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">▲ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率72.4%）がかくとう×4。じしん・はたきおとす・いわ技はいずれも等倍止まりで決定打を欠き、先制のバレットパンチ（99.7%）込みで先に削られやすい</td>
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
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率71.5%）がかくとう×4。メガ進化でS112、こうげき種族値145の一致技で耐久を貫かれる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう技を半減するピクシー（フェアリー）に後出しし、インファイト・はどうだん・しんくうは（先制）をいずれも×0.5で受ける。アーマーガア（ひこう/はがね）はインファイトこそ等倍だが、はがね技（コメットパンチ・バレットパンチ）を半減し高い防御で耐えてはねやすめで居座れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">オオニューラ（33位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（98.6%）・フェイタルクロー（95.4%）でかくとう×4。先制のねこだまし＋高速かくとう技で上から崩される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のフェイタルクロー（あく）・インファイト・じごくづき（あく・52.3%）をいずれも半減するピクシー（フェアリー）に後出しする。フェイタルクローはあく半減でピクシーがほぼ受け切れる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0428-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミロップ（13位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（61.1%）・とびひざげり（33.5%）がかくとう×4。S135で先手、ねこだまし＋一致かくとうで上から落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト・マッハパンチ（かくとう）・とびひざげりを半減するピクシー（フェアリー）に後出しする。トリプルアクセル（こおり）はフェアリーに等倍のため受け切りには耐久ラインの確認が要る。先発対面なら出てくる前提でいわ技を入れ、メガ進化前のS105を削っておく</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99.2%）が×2。S102で先制され、こちらのいわ技を半減（じめん0.5）される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチ（×4）採用個体で先制されても1発で落とす。じしんを無効化するひこう（アーマーガア等）を同伴して受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア・なみのり等のみず技が×2。先制のアクアジェット（採用率66.6%）まで持ち、削れた状態を上から詰められる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず半減のくさ・ドラゴン（フシギバナ・ブリジュラス等）を同伴。はたきおとすでオボンのみを奪い、後続のくさ枠で起点にする</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ技等倍（ひこう×2×はがね0.5）・はたきおとす等倍と決定打を欠く。はねやすめで回復され、高い防御で削り合いに持ち込まれると突破できない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんはひこうで無効化されるため通らない。でんき・ほのお技を持つ後続で突破する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0154-00.webp" alt="メガニウム">
    <div class="name">メガニウム</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">くさ枠でバンギラスの弱点みず・じめんを半減。受け回しの軸を共有</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0571-01.webp" alt="ゾロアーク(ヒスイ)">
    <div class="name">ゾロアーク(ヒスイ)</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ノーマル/ゴーストで高速特殊打点。物理偏重の構成に特殊軸を補う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速じめん枠。バンギラスが苦手なはがねにじしんで打点、砂下で全抜きを狙える</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめんを無効・かくとうを等倍で受け、高い防御でルカリオ・ガブリアスを受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ゴースト複合でかくとうを無効化し受け先を担う。フェアリーへの打点も補完</div>
  </div>
</div>

**パーティ構成の基本方針:**

バンギラスはかくとう×4が最大の穴で、みず・じめん・はがねも×2と弱点が多いため、残り5体で以下の役割を補います。

1. **かくとう対策**: かくとう無効のゴースト（ギルガルド）・かくとう半減のフェアリー（ピクシー）でルカリオ・オオニューラの一致かくとうを受ける。アーマーガアはかくとう等倍だが高耐久とはがね半減で受け先になる
2. **みず・じめん対策**: くさ（メガニウム等）でアシレーヌ・ガブリアスの攻撃を半減して受ける
3. **はがね突破**: じしん持ちのガブリアス等でブリジュラスを×2で処理する（アーマーガアはひこうでじしん無効のため、でんき・ほのお技で対処する）
4. **砂嵐の活用**: すなあらしを活かせるいわ・じめんタイプを並べ、相手の削りと特防補正を共有する

---

## データ分析①：メガ石採用率48.7%が示す「メガ前提でない」バンギラス

メガ石採用率がほぼ100%に達するルカリオ（97.4%）やミミロップなど他のメガ枠ポケモンと異なり、バンギラスナイトの採用率は**48.7%**にとどまります。持ち物分布を見ると、構築側がメガ進化と非メガをほぼ二分していることが分かります。

| 持ち物 | 採用率 | 役割 |
|---|---|---|
| バンギラスナイト | 48.7% | メガで物理性能と両受けを底上げ |
| たべのこし | 10.1% | 居座り・受け回しを延命 |
| オボンのみ | 9.5% | 中盤の被弾を1回耐える保険 |
| ヨプのみ | 8.5% | かくとう×4を1回だけ耐える |
| ラムのみ | 5.8% | あくび・状態異常を解除 |
| シュカのみ | 5.6% | じめん×2を1回軽減 |

メガ以外の上位を占めるのは たべのこし・オボンのみ・ヨプ／シュカといった**居座りと弱点ケアの持ち物**です。これは「すなおこしの特防補正＋高耐久で受けながら はたきおとすで起点を作る」という、メガ枠を消費しない受け運用が確立していることを示します。とくにヨプのみ8.5%・シュカのみ5.6%は、それぞれかくとう×4・じめん×2という**最も致命的な弱点を1回だけ凌ぐ**ためのピンポイント採用で、弱点の多さを持ち物で補う発想が読み取れます。

逆に言えば、メガを切ってよい構築であればバンギラスナイトで防御150・特防実質180相当の鉄壁に化けるため、相手の物理アタッカーが多い対面ではメガが有力です。メガ前提ではなく、構築のメガ枠と相手の脅威に応じて持ち物を選べる柔軟さが、このポケモンが幅広い構築で採用される理由になっています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">いじっぱり物理型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 51.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">はたきおとす・ストーンエッジ・じしん・れいとうパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">受けつつ高火力で反撃。広い打点</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">低速で先制を取られる。はがね突破に難</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">しんちょう特殊受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう 24.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">はたきおとす・ステルスロック・りゅうのまい・じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊耐久が一段上。設置と居座りが安定</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">火力が下がり倒しきれずターンを渡す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ようき抜き型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき 14.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">りゅうのまい・はたきおとす・ストーンエッジ・じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積んで高速帯を抜き全抜きを狙える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">耐久補強がなく積む前に崩れやすい</td>
</tr>
</tbody>
</table>
</div>

**総評:**

バンギラスはすなおこしの特防補正と高耐久を土台に、はたきおとす（採用率75%）で持ち物を奪いながら起点を作る受けアタッカーです。エスパー無効・ほのお半減を活かした対ゲンガー・対ギルガルド等のゴースト/はがね対面に強く、れいとうパンチでじめん/ドラゴンまで打点を伸ばせます。

一方でかくとう×4が明確な穴で、ルカリオ・オオニューラ・ミミロップといった上位かくとうアタッカーには受け出しが効きません。低速ゆえ先手を取られやすく、これらはパーティのひこう・フェアリー枠でケアするのが前提になります。メガ石採用率48.7%が示すように、メガ進化で物理の鉄壁に化ける運用と、メガ枠を温存して居座る運用のどちらにも対応できる点が、使用率38位を支える汎用性です。

---

## 関連記事

- [天敵となる使用率9位 ルカリオのM-2考察](/blog/lucario-analysis-m2/)
- [同居する高速地面枠 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [受け先候補 アーマーガアのM-2考察](/blog/corviknight-analysis-m2/)
