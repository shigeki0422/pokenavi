---
title: '【ポケモンチャンピオンズ】ズルズキン考察 M-3 使用率75位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率75位のズルズキンを徹底分析。メガズルズキンはドレインパンチ87.8%・はたきおとす71.0%のメインウェポン2本に、りゅうのまい47.8%の全抜き型とビルドアップ30.8%の耐久積み型が混在。いかく97.7%の特性も詳しく解説。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-scrafty-m3.png'
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
  <img src="/images/pokemon/pokemon-0560-00.webp" alt="ズルズキン" />
  <div>
    <h2 style="margin:0 0 8px">ズルズキン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">75位</strong>　特性: <strong>いかく 97.7%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/22）時点の集計です

シーズンM-3のシングルバトルで、ズルズキンは**使用率75位**を記録。メガズルズキンはズルズキナイトの採用率が96.8%とほぼ全個体がメガ進化前提で運用されており、種族値がHP65/A130/B135/C55/D135/S68（合計588）に向上します。あく/かくとうのタイプ複合はエスパー技を無効化、ゴースト技を半減でき、ドレインパンチによる回復と積み技を組み合わせた耐久積みアタッカーとして機能します。

特性は**いかく97.7%**が支配的で、場に出た瞬間に相手のこうげきを1段階下げることで物理アタッカーへの受け出し性能を高め、ビルドアップやりゅうのまいで積む隙を作ります。

---

## なぜ今ズルズキンが使用率75位なのか

### 1. エスパーを無効化しゴーストを半減するタイプ複合

あく/かくとうの複合により、エスパー技を無効化し、ゴースト技を半減します。環境上位に採用されるサーフゴーのシャドーボール（ゴースト）を軽減し、エスパー技を透かせるため、これらを主力とする特殊アタッカーへの受け出し機会を作れます。

### 2. いかくで積む隙を自ら作り出す

特性いかく（97.7%）は場に出た瞬間に相手のこうげきを1段階下げるため、物理アタッカーへの後出しから積み技に繋ぐ流れが成立します。ビルドアップ（30.8%）ならぼうぎょも同時に上げて耐久を底上げしながら積め、りゅうのまい（47.8%）なら素早さも確保して全抜き態勢に入れます。相手の物理攻撃を受けても、いかく発動済みの状態で積み始めれば実質的な被ダメを抑えながら攻撃力を蓄積できます。

### 3. ドレインパンチで積みながら回復できる自己完結構成

ドレインパンチ（87.8%）は与えたダメージの1/2を回復するため、積んだ後の場持ちを自前で確保できます。あく/かくとうタイプ一致のドレインパンチとはたきおとすの2本柱で広範囲に打点を通しつつ、回復しながら継続的に削り続けます。

---

## 基本スペック

### 種族値

メガ進化後の種族値を主軸に記載します。括弧内はメガ前の値です。

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">65</strong></span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:67.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">135</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:27.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">55</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:67.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">135</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:34%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">68</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">588</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でこうげき130・ぼうぎょ135・とくぼう135と物理耐久と火力が大幅に向上します。一方、すばやさはメガ後でも68と低く、環境の高速帯に先手を取られやすい点が課題です。この低Sを補うためにりゅうのまいでS2段階上昇を狙う型と、積まずにビルドアップで耐久を高めてじっくり削る型に運用が分かれます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="あく" />
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="かくとう" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう（×2）</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう（×2）</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー（×4）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく（×0.25）</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ（×0.5）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はかくとう×2・ひこう×2・フェアリー×4です。フェアリー×4は特に注意が必要で、複数の環境ポケモンから弱点を突かれます。一方、エスパー技を無効化しゴースト技を半減できるため、サーフゴーのシャドーボールや特殊エスパーアタッカーへの後出し機会が生まれます。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center;width:40px">順位</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ドレインパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">87.8%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はたきおとす</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">65</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">71.0%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>りゅうのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">47.8%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>れいとうパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">31.0%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ビルドアップ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">30.8%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくづき</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">18.3%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ちょうはつ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">15.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かみくだく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">13.1%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じごくづき</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10.8%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>アンコール</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8.4%</td>
</tr>
</tbody>
</table>
</div>

りゅうのまい（47.8%）とビルドアップ（30.8%）の採用率が拮抗しており、それぞれ「速度を補ってアタッカーとして全抜きを狙う型」と「耐久を積んで受けながら崩す型」に分かれます。れいとうパンチ（31.0%）は単体ではタイプ一致恩恵がなく、あくまでガブリアス等への補完として採用される選択技です。

---

## 主要型の解説

性格分布はいじっぱり59.8%・ようき19.7%・しんちょう10.0%の順で、いじっぱりが過半を占めます。

### 型1: いじっぱりりゅうのまい全抜き型（最多採用）

**性格採用率: いじっぱり 59.8%**（こうげき最大化の全抜き型。EV分布 H32-A32中心）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0560-00.webp" alt="ズルズキン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HAいじっぱりりゅうのまい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（97.7%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32（HPと火力を主軸に残りを耐久へ）<br>
<strong>持ち物:</strong> ズルズキナイト（96.8%）
</div>
<div>
<strong>技構成:</strong><br>
・ドレインパンチ<br>
・はたきおとす<br>
・りゅうのまい<br>
・れいとうパンチ（選択）
</div>
</div>
</div>

**強み:**

いじっぱりでこうげきを最大化し、りゅうのまいでこうげき・すばやさを同時に積むことで、低Sの欠点を補いながら全抜き態勢に入れます。いかくで場に出た瞬間に相手のこうげきを下げてりゅうのまいの隙を作り、積んだ後はドレインパンチで回復しながら削ります。はたきおとすは持ち物を持つ相手に威力1.5倍で当たり、タイプ一致補正も乗って実質威力約145相当と高く、サブウェポンとして広い範囲をカバーします。

**弱み:**

りゅうのまいを積む前のすばやさ68は環境の大半のポケモンより遅く、積む前に上から弱点技（かくとう×2・ひこう×2・フェアリー×4）を受けると動く隙がありません。かくとう・ひこうの×2弱点は環境上位のポケモン多数から突かれるリスクがあり、対面で積む機会は限られます。

---

### 型2: いじっぱりビルドアップ耐久積み型（2番目に多い積み型）

**性格採用率: いじっぱり 59.8%**（こうげき最大化。りゅうのまい型とEV配分は同等で、積み技がビルドアップに替わる点が型1との差）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0560-00.webp" alt="ズルズキン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HAいじっぱりビルドアップ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（97.7%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32（HPと火力を主軸に残りを耐久へ）<br>
<strong>持ち物:</strong> ズルズキナイト（96.8%）
</div>
<div>
<strong>技構成:</strong><br>
・ドレインパンチ<br>
・はたきおとす<br>
・ビルドアップ<br>
・れいとうパンチ（選択）
</div>
</div>
</div>

**強み:**

ビルドアップはこうげきとぼうぎょを同時に上げるため、いかくと合わせて物理耐久を高めながら積めます。メガ後ぼうぎょ135の高い基礎値にビルドアップを積み重ねることで、物理アタッカーからの打点を実質的に大幅に下げられます。ドレインパンチの回復と合わさることで、物理相手には長期戦で優位を作れます。

**弱み:**

りゅうのまい型と比べてすばやさが上がらないため、素早さを上げないと相手の攻撃を先に受け続ける展開になります。特殊技（ひこう・フェアリー系の特殊技）には物理耐久を積んでも対応できず、特殊アタッカーへの対処は別枠に委ねる必要があります。

---

### 型3: しんちょう特殊耐久型

**性格採用率: しんちょう 10.0%**（D補正で特殊耐久に寄せる型。EV分布 H2-A32-S32 6.2%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0560-00.webp" alt="ズルズキン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">しんちょう特殊耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（97.7%）<br>
<strong>性格:</strong> しんちょう（D↑ S↓）<br>
<strong>EV:</strong> A32 S32（採用率6.2%。こうげきと素早さに振り、しんちょう補正で特殊耐久を確保）<br>
<strong>持ち物:</strong> ズルズキナイト（96.8%）
</div>
<div>
<strong>技構成:</strong><br>
・ドレインパンチ<br>
・はたきおとす<br>
・ビルドアップ / りゅうのまい<br>
・れいとうパンチ（選択）
</div>
</div>
</div>

**強み:**

しんちょうによるとくぼう補正とメガ後D135の高い特殊耐久を組み合わせることで、いじっぱり型では受けきれない特殊アタッカーへの対面を維持しやすくなります。サーフゴーやエスパー系への後出しから動く運用を意識した型です。いじっぱり型がこうげき補正で火力に寄せるのに対し、こちらは特殊方面の耐久に振ることで、特殊アタッカーへの後出し回数を増やせる点が選択理由になります。

**弱み:**

しんちょうはすばやさを下げる補正のため、S32を振ってもいじっぱり・ようき型ほどの素早さは出ず、りゅうのまいを積まない限り高速帯には後手を踏みます。こうげきも補正なしのA130に依存し、いじっぱり型と比べて積み後の一撃が届かない相手が増えます。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

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
    <img src="/images/pokemon/pokemon-1000-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サーフゴー（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サーフゴーのゴースト技（シャドーボール等）はズルズキンに半減。こちらのはたきおとす（あく）はサーフゴー（はがね/ゴースト）に×2で通り、持ち物を落とす追加効果まで狙える。フェアリー技（マジカルシャイン）はズルズキンに×4だが採用率5.1%とごく一部の個体に限られる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メタグロス（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドレインパンチ（かくとう）ははがね/エスパーに等倍止まりで決定打にならず、はたきおとす（あく）はエスパーに×2で通る。メタグロスはメガ石96.7%でメガ後S110（実数値162）。りゅうのまい未積みのズルズキンS68（実数値120）には先手を取られやすい</td>
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
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手理由</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">対策</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のボディプレス（86.3%）・とんぼがえり（66.5%）で高耐久を活かして受けられ、ドレインパンチ（かくとう）が等倍止まりでズルズキンの攻撃が決定打にならない。ブレイブバード（13.8%）を持つ個体にはひこう×2弱点も突かれる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき技を持つライチュウ・ロトムでアーマーガアのひこうに×2を通して処理する。ズルズキンはアーマーガア対面には出さず、これらの高速でんき枠に役割を委ねる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ライチュウ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さが高くりゅうのまい積み前にでんじほう（96.0%）・きあいだま（95.4%）で削られやすい。フェアリー技（みわくのボイス14.6%・マジカルシャイン7.9%）を持つ個体にはフェアリー×4弱点も突かれる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ライチュウのでんじほう（でんき）はじめんタイプに無効のため、ガブリアスに後出し交代してでんき技を透かす。ただしきあいだま（かくとう）はガブリアスに等倍で通るため過信せず、こおり技持ちで先に処理する選出も用意する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき最速でS実数値169（こだわりスカーフ30.2%）で積み前に先手を取られ、S68の低速からりゅうのまいを積む隙を作りにくい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおり技を持つポケモンでガブリアスを先に処理する。ズルズキンのれいとうパンチは×4で通るが、スカーフ個体（30.2%）には積み後でも後手を踏むため過信しない</td>
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
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。ズルズキンが苦手なひこう・でんき系を別枠でケアしつつ、じしんで広い打点を通す</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ゴーストで広い打点。ズルズキンが苦手なフェアリー系にはがね技で対処できる補完枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ">
    <div class="name">ライチュウ</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速でんき枠。ズルズキンが苦手なアーマーガアにでんじほう（でんき）で弱点を突ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこう/はがね。ズルズキンのかくとう×2弱点をひこうタイプで後出し交代して対処</div>
  </div>
</div>

**パーティ構成の基本方針:**

ズルズキンはいかく＋積み技＋ドレインパンチで物理アタッカーへの受け出しから全抜きを狙える一方、かくとう×2・ひこう×2・フェアリー×4の弱点をパーティ単位でカバーする必要があります。

1. **かくとう×2対策**: ひこうタイプ（アーマーガア等）やゴーストタイプでかくとう技を受ける枠を用意する
2. **ひこう・フェアリー対策**: でんき技・はがね技を持つ枠でひこう・フェアリー弱点に打点を入れる
3. **速度補完**: S68という低速を補うため、高速アタッカーで相手を消耗させてからズルズキンを通す
4. **いかく連携**: いかくを活かして物理アタッカーに後出しし、積む隙を確保してから全抜きに繋ぐ

---

## データ分析①：りゅうのまい47.8% vs ビルドアップ30.8%が示す「積みの方向性の分裂」

ズルズキンの積み技採用率を見ると、りゅうのまい（47.8%）とビルドアップ（30.8%）が拮抗しており、合計78.6%の個体がいずれかの積み技を採用しています。

| 積み技 | 採用率 | 上昇ステータス | 狙い |
|---|---|---|---|
| りゅうのまい | 47.8% | こうげき・すばやさ各+1 | 低SをS+1で補い全抜きを狙う |
| ビルドアップ | 30.8% | こうげき・ぼうぎょ各+1 | いかくと合わせて物理耐久を高め長期戦 |

この分裂は、メガズルズキンの低S（68）という数値が引き起こす設計上の二択を示しています。S68はりゅうのまい1積み後でもS実数値が大幅に伸びるとはいえ、積む前に上から潰されるリスクが常にあります。りゅうのまい型はそのリスクを承知で「1積みで速くなる賭け」を取り、ビルドアップ型はSの問題には目をつぶって「物理耐久を高めてドレインパンチで粘る方針」に徹します。

れいとうパンチ（31.0%）の採用率がビルドアップとほぼ同率で存在することも注目点で、ガブリアス（使用率1位）のドラゴン/じめん複合に対してれいとうパンチは×4の有効打になります。ガブリアスが最大の仮想敵であるため、ドラゴン・ひこう対策として選択される構図が読み取れます。

持ち物はズルズキナイト96.8%と、メガ進化が前提の設計です。持ち物固定のため、はたきおとすで相手の持ち物を落とす追加効果の恩恵を自分が受けることはできません。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HAいじっぱりりゅうのまい型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 59.8% / りゅうのまい 47.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ドレインパンチ・はたきおとす・りゅうのまい・れいとうパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">1積みで速度・火力を同時に確保して全抜きを狙える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積む前に上から弱点を突かれると動けない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HAいじっぱりビルドアップ型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり 59.8% / ビルドアップ 30.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ドレインパンチ・はたきおとす・ビルドアップ・れいとうパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">いかく+ビルドアップで物理耐久を高めながらドレインパンチで粘れる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">Sが上がらないため特殊技や高速ポケモンには対処できない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HSしんちょう耐久型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう 10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ドレインパンチ・はたきおとす・ビルドアップ/りゅうのまい・れいとうパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">D135+しんちょう補正で特殊技への後出しを維持しやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">こうげきの補正がなく積み後の火力がいじっぱり型に劣る</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガズルズキンはいかく97.7%＋ズルズキナイト96.8%でほぼ全個体がメガ前の威圧とメガ後の高耐久・高火力を組み合わせた運用に特化しています。ドレインパンチ（87.8%）とはたきおとす（71.0%）のタイプ一致2本は広いタイプへの打点を確保し、積み技はりゅうのまい（47.8%）とビルドアップ（30.8%）に分かれて「全抜き志向」か「耐久志向」かが個体ごとに異なります。

フェアリー×4弱点は対戦中に最も警戒すべき点で、フェアリー技持ちへの対面は大きな負担になります。かくとう×2・ひこう×2も複数の環境ポケモンから突かれるため、パーティではこれらをカバーするひこう・ゴースト枠を用意し、安全に積める対面を選んで通すのが現実的な運用方針です。

---

## 関連記事

- [サーフゴーのM-3考察](/blog/gholdengo-analysis-m3/)
- [メタグロスのM-3考察](/blog/metagross-analysis-m3/)
- [コノヨザルのM-3考察](/blog/annihilape-analysis-m3/)
