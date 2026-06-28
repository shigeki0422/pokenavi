---
title: '【ポケモンチャンピオンズ】アーマーガア考察 M-3 使用率9位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率9位のアーマーガアを分析。てっぺき+ボディプレス採用率急増、たべのこし68.4%集約の理由、ガブリアス・ライチュウとの同居率から見えるサイクル軸を解説。'
updatedDate: '2026-06-27'
pubDate: '2026-06-27'
heroImage: '../../assets/hero-corviknight-m3.png'
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
  <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア（M-3）" />
  <div>
    <h2 style="margin:0 0 8px">アーマーガア</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">9位</strong>（M-2は6位）　特性: <strong>プレッシャー 60.1%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン時点の集計です

M-3シングルバトルでアーマーガアは**使用率9位**。M-2の6位からやや後退しましたが、ひこう/はがねの複合タイプが持つ優れた耐性を活かした耐久型サイクル役として環境に定着しています。M-3での大きな変化は**てっぺき採用率の急伸（63.5% → 81.6%）とボディプレス採用率の上昇（70.9% → 86.7%）**で、「てっぺきを積んでボディプレスで崩す」セットが対戦の主流となっています。

---

## M-3アーマーガアの技構成

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">M-3採用率</th>
  <th style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">M-2採用率</th>
  <th style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>はねやすめ</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">98.2%</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">98.1%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">+0.1pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>ボディプレス</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">86.7%</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">70.9%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#16a34a"><strong>+15.8pt</strong></td>
</tr>
<tr>
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>てっぺき</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">81.6%</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">63.5%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#16a34a"><strong>+18.1pt</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>とんぼがえり</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">65.7%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">62.1%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">+3.6pt</td>
</tr>
<tr>
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>アイアンヘッド</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">24.9%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">31.1%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#dc2626">-6.2pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>ブレイブバード</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">13.1%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">19.0%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#dc2626">-5.9pt</td>
</tr>
<tr>
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>きりばらい</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">7.4%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">新規</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>ちょうはつ</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">6.8%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">14.9%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#dc2626"><strong>-8.1pt</strong></td>
</tr>
<tr>
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>ビルドアップ</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">5.7%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">14.6%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#dc2626"><strong>-8.9pt</strong></td>
</tr>
</tbody>
</table>
</div>

はねやすめ・ボディプレス・てっぺき・とんぼがえりの4技が実質的な主力構成です。アイアンヘッド・ブレイブバードなどの火力技はいずれも採用率が減少し、ボディプレス+てっぺきのセット採用が主流の型として確立しました。

---

## 基本スペック

### 種族値

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:49%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">98</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">87</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">105</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:26.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">53</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:33.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">67</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">495</span>
  </div>
</div>

ぼうぎょ105とHP98を持ち、物理耐久に優れています。とくぼう85も並以上で、はがね/ひこうの複合による耐性の多さと合わせて場持ちが良好です。すばやさ67は低く、耐久型として使うポジションです。

### タイプ・耐性（ひこう/はがね）

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<table style="width:100%;border-collapse:collapse;font-size:0.9em;margin:12px 0">
  <thead>
    <tr>
      <th style="padding:6px 8px;border:1px solid #e2e8f0;background:#f8fafc;text-align:left">弱点（×2/×4）</th>
      <th style="padding:6px 8px;border:1px solid #e2e8f0;background:#f8fafc;text-align:left">耐性（×½/×¼）</th>
      <th style="padding:6px 8px;border:1px solid #e2e8f0;background:#f8fafc;text-align:left">無効（×0）</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:6px 8px;border:1px solid #e2e8f0">
        <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:36px;height:36px;vertical-align:middle" /> ×2
        <img src="/images/types/type-12-electric.png" alt="でんき" style="width:36px;height:36px;vertical-align:middle" /> ×2
      </td>
      <td style="padding:6px 8px;border:1px solid #e2e8f0">
        <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:36px;height:36px;vertical-align:middle" /> ×½
        <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:36px;height:36px;vertical-align:middle" /> ×½
        <img src="/images/types/type-08-steel.png" alt="はがね" style="width:36px;height:36px;vertical-align:middle" /> ×½
        <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:36px;height:36px;vertical-align:middle" /> ×½
        <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:36px;height:36px;vertical-align:middle" /> ×½
        <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:36px;height:36px;vertical-align:middle" /> ×½
        <img src="/images/types/type-06-bug.png" alt="むし" style="width:36px;height:36px;vertical-align:middle" /> ×¼
        <img src="/images/types/type-11-grass.png" alt="くさ" style="width:36px;height:36px;vertical-align:middle" /> ×¼
      </td>
      <td style="padding:6px 8px;border:1px solid #e2e8f0">
        <img src="/images/types/type-03-poison.png" alt="どく" style="width:36px;height:36px;vertical-align:middle" /> ×0
        <img src="/images/types/type-04-ground.png" alt="じめん" style="width:36px;height:36px;vertical-align:middle" /> ×0
      </td>
    </tr>
  </tbody>
</table>

弱点はほのおとでんきの2タイプのみで、M-3環境上位のじめん技（ガブリアスのじしん等）を完全に無効化できます。むしとくさへの×¼の耐性も持ち、物理技を中心に受け出せる範囲が広い点が特徴です。

---

## M-3採用型：てっぺき+ボディプレス耐久型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:48px;height:48px" />
  <strong>てっぺき+ボディプレス型（M-3主流）</strong>
</div>
<div style="display:flex;gap:16px;flex-wrap:wrap;margin:8px 0">
  <div style="flex:1;min-width:200px">
    <strong>特性:</strong> プレッシャー（60.1%）/ ミラーアーマー（38.0%）<br>
    <strong>性格:</strong> わんぱく（64.7%）<br>
    <strong>EV:</strong> H32 B32 D2（53.4%）<br>
    <strong>持ち物:</strong> たべのこし（68.4%）/ オボンのみ（27.3%）
  </div>
  <div style="flex:1;min-width:200px">
    <strong>技構成:</strong><br>
    ・はねやすめ（98.2%）<br>
    ・ボディプレス（86.7%）<br>
    ・てっぺき（81.6%）<br>
    ・とんぼがえり（65.7%）
  </div>
</div>
</div>

**H32 B32 D2 わんぱく（B↑/D↓）の実数値: H189 A107 B155 C73 D95 S87**

H189でたべのこしの毎ターン回復量は11。B155からてっぺき1積みでB310（2.0倍）となり、ボディプレスの実質威力も2.0倍に伸びます。わんぱくでBを上昇させてボディプレスの打点を底上げしつつ、はねやすめで持久力を確保する構成です。D2の余り振りはD実数値が95となり、わんぱくによるとくぼうの低下（0振り時107→95）を若干補います。

**のんきの場合（採用率23.5%）はS実数値が78まで下がる**ため、相手のS調整次第で有意差が出ることがあります。とんぼがえりでサイクルを回すため、基本的な動き自体は性格で変わりません。

### てっぺき+ボディプレスの狙い

ボディプレス（かくとう、威力80）はこうげき種族値ではなくぼうぎょ種族値を攻撃力として参照します。アーマーガアのぼうぎょ105（わんぱくB32でB155）に加え、てっぺき1積みで防御段階+2（実質B155×2.0=310相当）になると、ボディプレスの実質威力は**非積み時の2.0倍**に上昇します。てっぺき2積みなら2.5倍相当。火力と耐久を同時に上げる動きとして、M-3で急速に普及しました。

ボディプレスがかくとうタイプ技であるため、ブリジュラス（はがね/ドラゴン）に×2で通ります。M-3使用率4位のブリジュラスに対して有効打を持てる点が、M-2からの採用率上昇（70.9% → 86.7%）の背景の一つと考えられます。

### 苦手なポケモン

**ライチュウ（使用率5位）** がアーマーガアにとって最大の障害です。ライチュウは96.4%がメガライチュウYに進化し、おくびょうH2-C32-S32での実数値はC196・S182に達します。でんじほう（でんき、採用率96.0%）はアーマーガア（ひこう/はがね）に×2で通り、S87のアーマーガアは先手を取れません。きあいだま（かくとう、採用率95.4%）もアーマーガアに等倍で通るため、でんじほうを受けきることはできません。ライチュウへの交代は基本的に許容できません。

**リザードン（使用率8位）** も同様に危険です。リザードナイトY採用率77.5%でほのお/ひこうのメガリザードンYになり、かえんほうしゃ（採用率47.5%）やフレアドライブ（20.8%）がアーマーガア（ひこう/はがね）に×2で通ります。

**バシャーモ（使用率11位）** はバシャーモナイト採用率76.1%でメガバシャーモ（ほのお/かくとう）になります。ほのお技が×2で通るため有効打がありません。

---

## データ分析①：M-2→M-3の技採用率変化が示す戦術シフト

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">M-2</th>
  <th style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">増減</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>てっぺき</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">63.5%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">81.6%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#16a34a"><strong>+18.1pt</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>ボディプレス</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">70.9%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">86.7%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#16a34a"><strong>+15.8pt</strong></td>
</tr>
<tr>
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>とんぼがえり</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">62.1%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">65.7%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">+3.6pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>アイアンヘッド</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">31.1%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">24.9%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#dc2626">-6.2pt</td>
</tr>
<tr>
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>ちょうはつ</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">14.9%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">6.8%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#dc2626"><strong>-8.1pt</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>ビルドアップ</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">14.6%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">5.7%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#dc2626"><strong>-8.9pt</strong></td>
</tr>
<tr>
  <td style="padding:6px 12px;border:1px solid #e2e8f0"><strong>ブレイブバード</strong></td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">19.0%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center">13.1%</td>
  <td style="padding:6px 12px;border:1px solid #e2e8f0;text-align:center;color:#dc2626">-5.9pt</td>
</tr>
</tbody>
</table>
</div>

てっぺきとボディプレスがともに大きく増加し、単純な物理火力技（アイアンヘッド・ブレイブバード）と変化技（ちょうはつ・ビルドアップ）は減少しています。

M-2では採用率上位だったちょうはつ（14.9%）が6.8%に落ちた点が目立ちます。M-3環境では使用率4位のブリジュラスが特殊技（とくこう125）を主力とするため、ちょうはつで特殊積みを防ぐよりも、てっぺき+ボディプレスで物理・物理参照特殊の両面から崩しにいく構成が選ばれた結果とみられます。

ビルドアップ（こうげきとぼうぎょを同時に+1）からてっぺき（ぼうぎょのみ+2）への移行も同じ文脈で、「ボディプレス参照のBを2段階効率よく上げる」目的でてっぺきが選ばれていると読めます。

---

## データ分析②：同居率ネットワークとサイクル構築の実態

M-3でアーマーガアと同居率が高いポケモン（上位5体）：

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" />
    <div class="name">ガブリアス</div>
    <div class="rate">使用率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" />
    <div class="name">ライチュウ</div>
    <div class="rate">使用率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0691-00.webp" alt="ドラミドロ" />
    <div class="name">ドラミドロ</div>
    <div class="rate">使用率29位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" />
    <div class="name">マスカーニャ</div>
    <div class="rate">使用率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" />
    <div class="name">ミミッキュ</div>
    <div class="rate">使用率2位</div>
  </div>
</div>

同居率1位のガブリアスとの組み合わせは、役割分担が明確です。ガブリアスのじめん技弱点（×2）をアーマーガアが完全無効化し、アーマーガアのほのお・でんき弱点をガブリアスの高速アタッカーとしての性能でカバーします。アーマーガアがとんぼがえりでガブリアスを後出しするサイクル回しが機能します。

ライチュウが同居2位に入っている点は注目に値します。アーマーガアがライチュウのでんき技に×2弱点を持つため、同一パーティに入る際は選出を分ける前提の採用です。ライチュウが苦手とするじめん複合（ラグラージ等）にアーマーガアが無効化で対応し、アーマーガアが苦手とするでんき・ほのお系にライチュウが打点を持つ、役割の補完関係で成立しています。

---

## 立ち回りの基本

アーマーガアはとんぼがえりによる対面操作と、てっぺき+ボディプレスによる崩しの2軸で動きます。

**とんぼがえりサイクル**では、アーマーガアを初手または受け出しで展開し、有利な相手への圧力をかけながらとんぼがえりで後続に繋ぎます。とんぼがえりはむしタイプ（威力70）ですが、ブリジュラス（はがね/ドラゴン）には×0.5の半減で通るため、ブリジュラスへの打点はボディプレスが主軸です。ガブリアスへの後出しからとんぼがえりでサイクルを回す使い方が基本です。

**てっぺき積み**では、交代や相手の変化技などで隙が生まれたターンに使用します。てっぺき1積みでB310相当になり、その後のボディプレスでブリジュラスへの×2効果もあって相手を削れます。はねやすめを絡めてたべのこし（毎ターンH11回復）と合わせた長期戦を狙います。

**ほのお・でんきへの対処**は後続に任せるのが基本です。ライチュウやリザードンが見えたターンに引くことで、アーマーガアの体力を温存します。

---

## まとめ

M-3のアーマーガアは、てっぺき+ボディプレスセットの普及によりM-2よりも崩し能力が上がっています。使用率9位と安定した採用を受けており、ガブリアス（1位）やミミッキュ（2位）との同居率が高いことから、上位構築のサイクル軸として機能しています。

ほのおとでんきの2タイプへの弱点は変わらず、メガライチュウY（使用率5位）とメガリザードンY（使用率8位）が上位に多いM-3環境では、これらへの選出調整がアーマーガア採用時の課題です。

---

## 関連記事

- [【ポケモンチャンピオンズ】ガブリアス考察 M-3 使用率1位](/blog/garchomp-analysis-m3/)
- [【ポケモンチャンピオンズ】ミミッキュ考察 M-3 使用率2位 型別採用率と立ち回り](/blog/mimikyu-analysis-m3/)
