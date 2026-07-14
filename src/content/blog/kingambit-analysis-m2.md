---
title: '【ポケモンチャンピオンズ】ドドゲザン考察 M-2 使用率24位 そうだいしょう型の採用率と立ち回り'
description: 'M-2シングルバトルで使用率24位のドドゲザンを徹底分析。そうだいしょう88.9%・ふいうち99.0%・くろいメガネ66.1%の実データから、つるぎのまいHA型の火力とかくとう×4弱点への対策を解説。環境上位への相性をダメージ計算とともに紹介します。'
updatedDate: '2026-06-11'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-kingambit-m2.png'
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
  <img src="/images/pokemon/pokemon-0983-00.webp" alt="ドドゲザン" />
  <div>
    <h2 style="margin:0 0 8px">ドドゲザン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">24位</strong>　特性: <strong>そうだいしょう 88.9%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事はM-2シーズンのデータです。M-3版は[ドドゲザン考察 M-3](/blog/kingambit-analysis-m3/)をご覧ください。

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ドドゲザンは**使用率24位**。あく/はがねという耐性の多い複合タイプと、特性**そうだいしょう**（採用率88.9%）による火力上乗せを軸にした、つるぎのまい＋先制技ふいうちの物理アタッカーです。

ドドゲザンの強みは、ふいうち（採用率99.0%）の先制で上から削りつつ、こうげき135にそうだいしょう補正とつるぎのまいを重ねた一撃で詰める押し付け性能にあります。一方でかくとうが**×4弱点**という明確な穴があり、環境のかくとう技をどう避けるかが運用の鍵になります。

---

## なぜドドゲザンが使われるのか

### 1. ふいうちの先制で低速を補う

ドドゲザンのすばやさ種族値は**50**と低く、環境上位のアタッカーには軒並み先手を取られます。これを補うのが**ふいうち**（採用率99.0%・優先度+1）です。先制技は優先度で動くため、**相手のすばやさに関わらず先制**でき、低速でも上から削れます。あくタイプ一致＋そうだいしょう補正が乗るため、HP振りの薄い高速アタッカーなら先制1発で落としきれる場面が多くなります。

ただしふいうちは「相手が攻撃技を選んでいるターンのみ成功する」制約があり、変化技・交代を読まれると不発になります。

### 2. そうだいしょうで火力を底上げ

特性**そうだいしょう**（採用率88.9%）は、登場時にその試合で倒れた味方1体につき技の威力が10%上がる特性です（最大5体で+50%）。倒れた数は登場した瞬間に固定されるため、後続を失った終盤に繰り出すほど威力補正が大きくなります。+50%まで乗ればこうげき135の打点が大幅に伸び、ここにつるぎのまいの積みが合わさると半端な耐久では受けきれない火力になります。

### 3. 耐性の多いタイプで居座りやすい

あく/はがねは弱点がかくとう・ほのお・じめんの3タイプのみで、**エスパー・どくを無効化**、さらにノーマル・くさ・こおり・ひこう・いわ・ゴースト・あく・ドラゴン・はがねの9タイプを半減します。エスパー無効はメガスターミー・メガマフォクシーのエスパー技を透かせる点で環境的に重要で、つるぎのまいを積む隙を作りやすいのが居座り適性につながっています。

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
      <div style="width:67.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">135</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">120</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
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
      <div style="width:25%;background:linear-gradient(90deg,#f87171,#ef4444);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">550</span>
  </div>
</div>

こうげき135・ぼうぎょ120・HP100と物理方面の数値が高く、物理耐久を活かして居座りつつ殴る型になります。すばやさ50が低いため自分から先手を取る役回りではなく、ふいうちの先制と物理受け性能で立ち回るのが基本です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="あく" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（4倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
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
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

最大の注意点は**かくとうが×4弱点**であること（あく2×はがね2）。環境にはメガルカリオ・メガミミロップなどかくとう技の使い手が多く、これらに上から弱点技を撃たれると物理耐久でも一撃で落ちます。ほのお・じめんの×2弱点も、リザードン・ガブリアス・カバルドンなど上位の主力技と噛み合うため、相手の打点を見て引くか居座るかの判断が重要です。一方でエスパー・どくの無効と9タイプ半減は、メガスターミーやゲンガーのヘドロウェーブなどを透かせる強みになります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70 先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。相手のSに関わらず先制。相手が攻撃技選択時のみ成功</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドゲザン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく一致のメインウェポン。必中</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>86.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね一致技。フェアリー・いわ・こおりに刺さる。20%ひるみ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>72.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A2段階アップ。物理耐久で1ターン耐えてから積む</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>けたぐり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">重さ依存</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく技が等倍以下のはがね（ブリジュラス＝かくとう×2等）や同タイプのドドゲザンへの打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ハサミギロチン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">一撃必殺</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中30。受けループ崩しの一発逆転枠</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>メタルバースト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">反射</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">受けたダメージを1.5倍で反射。高耐久を活かす変則枠</td>
</tr>
</tbody>
</table>
</div>

技構成はふいうち・ドゲザン・アイアンヘッドの一致3技に、つるぎのまいを加えた「積み＋先制」がほぼ確定枠です。けたぐり以下は選択技で、けたぐりはあく技が通りにくいはがね（ブリジュラス等）や同タイプのドドゲザンへの数少ないかくとう打点になります。

---

## 主要型の解説

EVスプレッドはHA基本（HP・こうげき両振り）と、すばやさを伸ばすAS型に大別されます。下記は性格分布（いじっぱり92.0%が大半）とEVの振り分布を指標としています。

### 型1: つるぎのまいHA耐久型（最多採用）

**EV採用率: HA系 合計47.2%**（HA+S 25.8%／HA+B 9.5%／HA+D 9.1%／HA+BD 1.7%／HA 1.1%の合計。いずれもHAを32まで振る）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0983-00.webp" alt="ドドゲザン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまいHAいじっぱり型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> そうだいしょう（88.9%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32（余り2はS/B/Dへ）<br>
<strong>持ち物:</strong> くろいメガネ
</div>
<div>
<strong>技構成:</strong><br>
・つるぎのまい<br>
・ふいうち<br>
・ドゲザン<br>
・アイアンヘッド / けたぐり
</div>
</div>
</div>

**強み:**

H32A32でHP・物理耐久を確保しつつ、こうげき135に最大振りといじっぱり補正を乗せる型です。AS型と比べ、物理アタッカーの攻撃を1ターン耐えてからつるぎのまいを積む動きが安定します。積み後はふいうちの先制1発で高速アタッカーを縛れるようになり、そうだいしょうで終盤さらに火力が伸びます。

くろいメガネ（採用率66.1%）はあく技を1.2倍に強化する持ち物で、ふいうち・ドゲザンの一致あく技の火力を底上げします。

**弱み:**

すばやさをほぼ振らないため、ふいうちが読まれて変化技・交代を合わせられると有効打を入れられません。AS型と比べると素のすばやさで動ける相手が狭く、ふいうちに依存した攻めになります。

---

### 型2: AS型（すばやさ重視）

**EV採用率: AS系 合計17.3%**（AS+H 10.9%・1.4%／AS+B 2.3%／AS+BD 1.5%／AS+D 1.2%の合計。いずれもAを32まで振りSを大きく振る）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0983-00.webp" alt="ドドゲザン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ASいじっぱり型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> そうだいしょう（88.9%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32 S32（余りはHへ）<br>
<strong>持ち物:</strong> くろいメガネ / きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・つるぎのまい<br>
・ふいうち<br>
・ドゲザン<br>
・アイアンヘッド
</div>
</div>
</div>

**強み:**

すばやさを最大まで振るとSは約86になり、HA型（S約70）では抜けないアシレーヌ・ギルガルド（ともに種族値S60）などすばやさに振らない低速ポケモンに、ドゲザン・アイアンヘッドを先に通せます。ふいうち頼みだったHA型に対し、攻撃技の選択肢を読まれても通常技で上から殴れる試合が増えます。ただし抜ける範囲はこの低速帯に限られ、S65以上の相手はS投資で容易にこちらを上回ります。きあいのタスキ（採用率12.8%）を持てば、かくとう×4弱点で本来一撃で落ちる相手にも1回行動を保証できます。

**弱み:**

Hを削るぶんHA型より物理耐久が下がり、つるぎのまいを積むために1ターン耐える動きが安定しません。S投資のわりに種族値50が低く、環境上位の高速アタッカー（メガルカリオS112・メガスターミーS120等）には遠く届かないため、ふいうちの先制が依然として主力である点はHA型と変わりません。

---

## 環境ポケモンへの相性分析

### 有利・五分なポケモン

使用率上位（TOP30目安）のうち、ドドゲザンと相性がはっきり出る相手を有利・不利の両面から挙げます。あく/はがねはエスパー無効・多耐性で受けに強い一方、すばやさ50と低く、相手の主力技がかくとう・ほのお・じめんならふいうち以外で勝負しづらい点に注意してください。相手の技は採用率を確認したうえで選定しています。

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
    <img src="/images/pokemon/pokemon-0121-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガスターミー（20位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー無効でしねんのずつき（39%）・サイコカッター（25%）を透かせる。主力のアクアブレイク（89%）は等倍（×1）だが、アイススピナー（65%）は×0.5。ドゲザン（みず1×エスパー2＝×2）で大ダメージ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0655-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガマフォクシー（25位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分（炎技に注意）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー無効でサイコショック（50%）・サイコキネシス（38%）を透かす。ドゲザン（ほのお1×エスパー2＝×2）が刺さる。ただしかえんほうしゃ（66%）はこちらに×2弱点。S134で先手を取られるため、ふいうちで縛るか後出し非推奨</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分（格闘技に注意）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（82%・どく）を無効、シャドーボール（71%）も×0.5半減。ドゲザン・ふいうち（ともにゴースト2×どく1＝×2）が刺さる。ただしきあいだま（37%・かくとう）はこちらに×4で、3個体に1体以上が後出し不可。きあいだま非搭載個体には有利だが、採用率が高いため後出しは読みが必要</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0670-05.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フラエッテ:永遠（17位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイアンヘッドがフェアリー単体に×2。主力のムーンフォース（87%・フェアリー2×はがね0.5）はこちらに等倍で通り、めいそう（86%）を積まれると等倍でも負担が大きい。メガ後S102でこちらのS50より速く先手は取られるがふいうちで縛れる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（19位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち（94%・ゴースト）はあくで×0.5半減。じゃれつく（92%・フェアリー）は×1等倍。アイアンヘッド（フェアリー×2）で押せるが、ドレインパンチ（25%・かくとう）採用個体には×4で注意</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

ドドゲザンの×4弱点（かくとう）・×2弱点（ほのお・じめん）を、採用率の高い主力技で突いてくる相手を挙げます。対策はパーティ単位の同伴枠・後出し処理で示します。

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
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（72%・かくとう）が×4。S112で先手を取られ、てきおうりょく補正の一致かくとう技で物理耐久ごと一撃。ふいうちはあく0.5×はがね0.5＝×0.25で削りも通らない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとうを無効化するゴースト（ゲンガー・ミミッキュ）や半減するエスパー・フェアリーを同伴し、ルカリオの前に引いて受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0428-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガミミロップ（13位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（61%）・とびひざげり（34%・かくとう）が×4。S135で先手を取られ、ねこだまし（63%）でひるませてからかくとう技で一撃</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとうを無効化するゴースト（ゲンガー）や半減するエスパー・フェアリーを同伴し、後続から受けてかくとう技を透かす</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（99%・じめん）が×2、S102で先手。つるぎのまいを積む前にじしんで大きく削られ、ふいうち等倍では高HPのガブリアスを削りきれない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんを無効にするひこう（アーマーガア）やふゆう持ち、こおり技持ち（弱点×4）を同伴し、ガブリアスの前に引いて処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技が×2、S100で先手。こちらのあく技はメガY（ほのお/ひこう）・メガX（ほのお/ドラゴン）ともに等倍、アイアンヘッドもどちらに対しても×0.5と打点が乏しい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわ・でんきタイプを同伴し、リザードンに後出しして弱点を突いて処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（98%）が×2、高HB耐久でドゲザン等倍を耐え、あくび（94%）で流される。ステルスロック（84%）展開もこなされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・みず・こおり技持ち（弱点×2以上）を同伴して上から処理する。けたぐりは重さ300kgのカバルドンに最大威力120で当たるが、かくとう等倍＋高HB耐久のため一撃は困難で、突破は同伴枠に任せたい</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0503-01.webp" alt="ダイケンキ(ヒスイ)">
    <div class="name">ダイケンキ(ヒスイ)</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/あくでほのおを半減し、ドドゲザンの弱点リザードンに後出ししやすい</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">メガ後S134の高速特殊枠で、低速のドドゲザンが苦手な相手に上から打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめん枠でステロ展開＋高速アタッカー。ふいうち圏に削るサポート</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ゴーストでほのおを半減、かくとうを無効化し弱点を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率9位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ひこうでじめん無効。高い物理耐久で苦手なガブリアスのじしんを受ける</div>
  </div>
</div>

**パーティ構成の基本方針:**

ドドゲザンはかくとう×4・ほのお/じめん×2という重い弱点を抱えるため、残り5体で以下の役割を補います。

1. **かくとう対策**: かくとうを無効化するゴースト（ゲンガー・ミミッキュ）や半減するエスパー・フェアリーでメガルカリオ・メガミミロップのかくとう技を受ける枠
2. **じめん対策**: ひこう（アーマーガア）・ふゆうでガブリアス・カバルドンのじしんを無効化する枠
3. **ほのお対策**: みず（ダイケンキ・イダイトウ等）でリザードンのほのお技を受ける枠
4. **削りサポート**: ステルスロック（ガブリアス等）で相手をふいうち圏内に押し込む

---

## データ分析①：くろいメガネ採用率66.1%が示す「あく技偏重」の構成意図

ドドゲザンの持ち物はくろいメガネが66.1%と過半数を占めます。これは「あくタイプ技のみを1.2倍にする」持ち物で、防御を補うタスキ（12.8%）・きのみ系（ヨプ6.9%／ラム4.2%／オボン2.8%）を大きく上回ります。

技採用率と合わせて読むと、ドドゲザンの構成意図が見えます。

| 技 | タイプ | 採用率 | くろいメガネの恩恵 |
|---|---|---|---|
| ふいうち | あく | 99.0% | ○（1.2倍） |
| ドゲザン | あく | 96.4% | ○（1.2倍） |
| アイアンヘッド | はがね | 86.9% | ×（対象外） |
| けたぐり | かくとう | 17.6% | ×（対象外） |

メイン2技がともにあく技で採用率ほぼ100%・96%、くろいメガネが直接効くのはこの2技です。とりわけ**先制技ふいうちの底上げ**が立ち回り上の意味を持ちます。ふいうち本来の威力70がくろいメガネで実質84相当になり、いじっぱりこうげき32振り＋そうだいしょう補正と重なることで、低速のドドゲザンが「上から削られる前にふいうちで縛る」攻めを成立させます。

耐久を補うタスキ・きのみより火力アイテムが優先されている事実は、ドドゲザンが「耐久受け」ではなく「ふいうち＋積みで攻めるアタッカー」として運用されていることを数値で裏付けています。一方でこの偏重は、ふいうちが読まれて変化技・交代を合わせられたときの脆さと表裏一体です。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">採用率（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">つるぎのまいHA耐久型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">HA系 47.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・ふいうち・ドゲザン・アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理を耐えて積める。ふいうち先制で詰め</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ふいうち依存。読まれると有効打なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">AS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">AS系 17.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・ふいうち・ドゲザン・アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">低速帯に上から通常技。タスキで一撃を防げる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理耐久が下がり積みが不安定。高速勢には届かない</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ドドゲザンはあく/はがねの多耐性とエスパー無効を活かして居座り、ふいうち＋つるぎのまいで終盤に火力を伸ばすアタッカーです。すばやさ50は低いものの、採用率99.0%のふいうちと88.9%のそうだいしょうにより、低速を補いながら高速アタッカーを縛れます。

M-2環境ではメガスターミー・メガマフォクシーのエスパー技を透かせる点が明確な強みです。一方でかくとう×4という穴は重く、メガルカリオ・メガミミロップなどかくとう技の使い手にはパーティ単位での受け回しが必須になります。くろいメガネ偏重が示す通り、攻めの起点として扱い、苦手なかくとう・ほのお・じめんは同伴枠で受けるのが基本戦術です。

---

## 関連記事

- [かくとう技でドドゲザンを×4で狩るメガルカリオのM-2考察](/blog/lucario-analysis-m2/)
- [じしんで弱点を突く使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [同じはがねアタッカー ハッサムのM-2考察](/blog/scizor-analysis-m2/)
