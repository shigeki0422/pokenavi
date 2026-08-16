---
title: '【ポケモンチャンピオンズ】カバルドン 考察 M-5 シーズン D方向EV再逆転となまける減少の理由'
description: 'M-5シングルバトルで使用率6位（M-4の4位から下降）のカバルドンを徹底分析。EV最多がH32-B2-D32に再逆転（21.4%）・しんちょう27.2%（+11.2pp）急増・なまける49.5%（-11.9pp）減少の背景を、アシレーヌの使用率上昇と結びつけてDBデータで解説します。'
updatedDate: '2026-08-13'
pubDate: '2026-08-13'
heroImage: '../../assets/hero-hippowdon-m5.png'
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
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" />
  <div>
    <h2 style="margin:0 0 8px">カバルドン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">6位</strong>　特性: <strong>すなおこし 99.8%</strong>
    </div>
  </div>
</div>

> 本記事はM-5シーズンのデータです。M-4記事は[こちら](/blog/hippowdon-analysis-m4/)。

シーズンM-5のシングルバトルで、カバルドンは使用率6位。じめん単タイプで種族値合計525、すなおこしによる砂嵐展開・あくびでの交代誘発・ステルスロック設置を軸とした環境屈指の耐久型ポケモンです。M-4からの変化点（EV配分の再逆転・なまける減少）は後述のデータ分析で解説します。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">108</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:56%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">112</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:59%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">118</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:34%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">68</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">72</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:23.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">47</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">525</span>
  </div>
</div>

HP108・ぼうぎょ118の高耐久が採用の根拠。すばやさは種族値47（実数値67）とM-5使用率上位20位のポケモンの中でも最も低く（次点はアシレーヌ・ギルガルドの種族値60）、先手で動くことは想定せず被弾前提のHP・防御重視型として運用されます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
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

みず・くさ・こおりの3タイプが弱点（×2）。M-5使用率2位のアシレーヌが持つうたかたのアリア（みず、採用率90.8%）は代表的な脅威の一つで、後述の通りD32型でも確定2発を許します。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>すなおこし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.8%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すなのちから</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.2%</td>
</tr>
</tbody>
</table>
</div>

**すなおこし**は場に出ると砂嵐を発生させる特性です。砂嵐中はじめん/いわ/はがねタイプ以外のポケモンが毎ターン最大HPの1/16ずつダメージを受けます。カバルドン自身はじめんタイプのため砂嵐ダメージを受けず、なまけるやたべのこしの回復と組み合わせると長期消耗戦を優位に進められます。採用率99.8%で実質固定です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技のメインウェポン。ブリジュラス（使用率3位、はがね/ドラゴン）に×2で刺さる主力打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">95.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">必中で相手を次ターン強制ねむり。交代を誘発し、ふきとばし・なまけるにつなげやすい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">79.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の場に設置。あくびで交代を誘発した後の継続ダメージ源</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふきとばし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>53.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度-6で相手をランダム交代。積みをリセットできる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なまける</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">49.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの1/2回復。高耐久と組み合わせた長期消耗戦の主軸だがM-5で採用率が下降</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+4で1ターン攻撃を回避。連発で成功率が1/3に低下する点に注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほえる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふきとばしと同じ優先度-6の強制交代技。効果は同じだが採用は少数派</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がんせきふうじ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のすばやさを下げるサブウェポン。ひこう複合のギャラドス等への数少ない有効打だが少数派</td>
</tr>
</tbody>
</table>
</div>

じしん・あくびはほぼ固定で採用されています（98.5%/95.3%）。M-5では継戦手段のステルスロック（79.5%）が単独でふきとばし（53.7%）・なまける（49.5%）を上回る採用率まで伸びており、設置技の重要性が高まっています。

---

## 主な型

### 型1：D32型（特殊耐久重視）

M-5で最多に返り咲いたH32-B2-D32型（EV採用率21.4%）。D124を確保し、アシレーヌ（使用率2位）のうたかたのアリア90.8%・ムーンフォース98.2%を筆頭とする特殊火力に対する耐久を型2（D94）より底上げする方向です。ただしアシレーヌ想定（ひかえめ、C EV32、C実数値195）のうたかたのアリアはD124でも162〜192ダメージ（HP215）を与え、確定2発で突破される点は変わりません。

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">D32型（特殊耐久重視）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなおこし（99.8%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）またはしんちょう（D↑ A↓）<br>
<strong>EV:</strong> H32-B2-D32<br>
<strong>持ち物:</strong> オボンのみ（66.2%）またはたべのこし（31.0%）
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・あくび<br>
・ステルスロック（79.5%）<br>
・なまける（49.5%）またはふきとばし（53.7%）
</div>
</div>
</div>

特殊アタッカーを主体とする相手にぶつける枠。D124以上の特殊耐久でブリジュラス（使用率3位）の連打をなまける（回復107）と組み合わせて受けながら、あくびで交代を誘いつつじしんで削ります。ただしブリジュラスの技はラスターカノン（採用率75.0%、C194想定）ならD124に72〜85ダメージで回復が上回りますが、りゅうせいぐん（採用率72.7%、C194想定）はD124に115〜136ダメージとなまけるの回復量（107）を超えるため受けきれません。アシレーヌのうたかたのアリアも後述の通りなまけるの回復量を上回るため、この型でも受けきることはできません。

**強み:**

わんぱくH215/A132/B154/D124/S67、しんちょうH215/A118/B140/D136/S67。D94では乱数2発だがD124なら確定3発です。ブリジュラスのラスターカノン（C194想定、威力80・はがねSTAB）はD124に72〜85ダメージ（HP215）で、2発合計144〜170ではHP215に届かず3発合計216〜255で確定3発です。D94なら93〜111ダメージで2発合計186〜222とHP215に届く乱数2発まで縮まります。

**弱み:**

特殊方向に寄せているため、メタグロス（使用率9位、メガストーン採用率98.3%）の物理打点には型2（B32型）ほど強くありません。メガメタグロスのサイコファング（A216・いじっぱり想定、かたいツメ込み）はB154に確定3発（87〜105ダメージ）ですが、オボンのみ込みの実効HP268（HP215+回復53）に対し3発合計は261〜315で、ほぼ確実に3発目で落ちます。

---

### 型2：B32型（物理耐久重視）

M-4で最多だったH32-B32-D2型（EV採用率18.6%）。わんぱくのB↑補正と合わせてB187を確保し、メタグロスの物理打点を安定して受けられます。

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">B32型（物理耐久重視）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなおこし（99.8%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32-B32-D2<br>
<strong>持ち物:</strong> オボンのみ（66.2%）またはたべのこし（31.0%）
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・あくび<br>
・ふきとばし（53.7%）<br>
・ステルスロック（79.5%）またはなまける（49.5%）
</div>
</div>
</div>

物理攻撃を主体とする相手にぶつける枠。B187の高い物理耐久でメタグロスの連打を受けながら、あくびで交代を誘いつつじしん（メタグロスに×2）で削ります。

**強み:**

H215/A132/B187/D94/S67。D32型（B154）より33ポイント高い物理耐久を確保でき、メガメタグロスのサイコファング（A216・いじっぱり想定、かたいツメ込み）をオボンのみ込みで安定して3発耐えられます（D32型のB154はほぼ確実に3発目で落ちます）。

**弱み:**

特殊方向のD実数値が94に落ちるため、アシレーヌのうたかたのアリアは高乱数1発（212〜252ダメージ、HP215）です。オボンのみ込みの実効HP268（HP215+回復53）でも2発目は確実に耐えられません（2発合計424〜504）。D32型（確定2発）に比べ、特殊アタッカーに対する耐久面で明確に不利です。

---

## データ分析①：M-4→M-5 採用率変化

### 技採用率（M-4比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">98.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>98.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">≒同</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">94.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>95.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+1.3pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">76.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>79.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.3pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふきとばし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">47.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>53.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+6.0pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なまける</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">61.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">49.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626"><strong>-11.9pp</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">まもる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>15.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+1.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほえる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-0.8pp</td>
</tr>
</tbody>
</table>
</div>

M-5で最も目立つ変化は**なまける-11.9pp（61.4%→49.5%）**です。ステルスロック（+3.3pp）とふきとばし（+6.0pp）が両方とも増えた分、なまけるの採用が押し下げられた形で、回復による長期消耗戦よりも設置技・積みリセットを優先する構成が広がっています。

### 持ち物採用率（M-4比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オボンのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">61.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">66.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+4.3pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たべのこし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>31.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-4.7pp</td>
</tr>
</tbody>
</table>
</div>

オボンのみが66.2%まで伸び、たべのこしとの差が拡大しました。なまけるの採用が下がった分、毎ターンの回復に頼らずHP1/2以下で発動し最大HPの1/4を回復するオボンのみの一撃耐久を重視する構成が優勢です。

### 性格分布（M-4比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">補正</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わんぱく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">72.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">64.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ とくこう↓</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しんちょう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">27.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう↑ こうげき↓</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のんき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ すばやさ↓</td>
</tr>
</tbody>
</table>
</div>

わんぱくが64.1%と-8.5pp下降した一方、しんちょうは27.2%と**+11.2pp**の大幅増加となりました。M-3→M-4のわんぱく増加傾向から一転し、D方向を意識する構成が広がっています。

### EV配分（M-4比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">EV配分</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">概要</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H32-B2-D32</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">21.4%（新最多）</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・とくぼう全振り</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H32-B32-D2</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.8%（M-4最多）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・ぼうぎょ全振り</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B22-D12</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP全振り・B寄りバランス型</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B6-D28</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP全振り・D寄りバランス型</td>
</tr>
</tbody>
</table>
</div>

M-4最多だったH32-B32-D2（B全振り型）からH32-B2-D32（D全振り型）に再逆転し、M-5の新最多になりました。EV最多が再び入れ替わった背景はデータ分析②で詳述します。

### 代表型の実数値比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">わんぱく H32-B2-D32<br>（M-5最多）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">わんぱく H32-B32-D2<br>（M-4最多）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>215</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>215</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">132</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">132</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ（わんぱく↑）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">154</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">187</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>124</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">94</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">67</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">67</td>
</tr>
</tbody>
</table>
</div>

M-5最多のD32型はD124と、M-4最多のB32型（D94）より30ポイント高い特殊耐久を確保します。その代わりB実数値はB154に下がり、物理方向はB187のB32型に比べて33ポイント低くなります。

---

## データ分析②：EV再逆転の背景——アシレーヌの使用率上昇

M-4→M-5でEV最多がH32-B32-D2からH32-B2-D32へ再逆転した理由を、環境上位の使用率変化から確認します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">主力技（採用率）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:32px;height:32px;vertical-align:middle;margin-right:6px"><strong>アシレーヌ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">2位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（98.2%）・うたかたのアリア（90.8%）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:32px;height:32px;vertical-align:middle;margin-right:6px"><strong>ブリジュラス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>3位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラスターカノン（75.0%）・りゅうせいぐん（72.7%）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">メタグロス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（92.6%）・サイコファング（87.5%）</td>
</tr>
</tbody>
</table>
</div>

アシレーヌが6位から2位へ、ブリジュラスも5位から3位へ順位を上げた一方、物理型のメタグロスは7位から9位に下降しました。アシレーヌのうたかたのアリアはみず技でカバルドンに×2で通り、ブリジュラスのラスターカノン・りゅうせいぐんはいずれも特殊技です。特殊アタッカー2体が使用率を伸ばし物理型のメタグロスが順位を落としたことが、B方向からD方向へのEVシフトと整合します。

---

## 苦手なポケモン

M-5使用率上位20位以内から、タイプ相性またはすばやさで明確にカバルドンを上回る脅威を抽出しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率順位</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手な理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん複合のためじしんは等倍止まり。実数値S169はカバルドンのS67を大きく上回り、つるぎのまい（37.3%）で積まれると止めにくいです。ふきとばし（53.7%）も優先度-6のため先に一撃を受けます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア（90.8%）のみず×2で継続的に削られます。じしんはみず/フェアリー複合に等倍で有効打にはなりますが、うたかたのアリアのダメージがなまけるの回復量を上回る局面が多いです</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（96.9%）のくさ×2に加え、トリプルアクセル（87.3%、こおり×2）も採用率が高く2つの弱点タイプで攻められます。カバルドンのじしんはくさ/あく複合のマスカーニャに半減します</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドスナイト採用率77.8%でメガ進化がほぼ前提。メガ後（みず/あく）ならじしんは等倍で通ります。メガ後A227（いじっぱり想定）のたきのぼり・パワーウィップはどちらもB154に134〜158ダメージ（HP215）と同火力で、りゅうのまい（82.3%）で積まれると止めにくいです</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カイリュナイト採用率80.4%でメガ進化がほぼ前提。ドラゴン/ひこう複合のためじしんは無効（×0）で反撃手段がありません。主脅威はりゅうせいぐん（採用率54.4%、ひかえめC216想定・ドラゴンSTAB）で、D124に127〜151ダメージ・D94に169〜199ダメージ（HP215）とどちらも確定2発です。かえんほうしゃ（66.7%）は威力90で確定4発（D124）にとどまり火力面ではりゅうせいぐんに劣りますが、いずれの技でもじしんが通らない点が根本的な弱点です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">リザードン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">M-4実績でメガ進化計98.8%（リザードナイトY 65.3%・リザードナイトX 33.5%）。メガY（ほのお/ひこう）の場合は特性ひでりで晴れを即展開しソーラービーム（57.5%）を溜めなしで発動、ひかえめC232想定でD124に確定2発・D94に確定1発（HP215）ですが、じしんはほのお/ひこう複合に無効（×0）で反撃手段がありません。一方、採用率33.5%のメガX（ほのお/ドラゴン）にはじしんが×2で通り、確定数を詰めれば有効な反撃手段になります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう/はがね複合のためじしんは無効（×0）で反撃手段がありません。はねやすめ（98.4%）で回復しながらてっぺき（53.2%）・ボディプレス（55.6%）で完全に起点にされます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/ゴースト複合で、なみのり（55.3%）・れいとうビーム（57.2%）と弱点2タイプを過半数採用。実数値S130はカバルドンのS67を上回り先手を取られ、じしんは等倍止まりです</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム（91.1%）のこおり×2が主力。ゲッコウガナイト採用率65.4%でメガ前提が過半数、メガ後S213で確実に先制されます。特性へんげんじざいで氷技にもタイプ一致補正が乗り、C185想定でD124に確定2発（HP215）です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0503-00.webp" alt="ダイケンキ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ダイケンキ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最多採用技のひけん・ちえなみ（99.4%）はあくタイプで等倍止まり。みず技はシェルブレード（31.3%）・アクアカッター（22.8%）採用個体のみ弱点を突けます。最多EV型の実数値S122はS67を上回り先手を取られやすく、じしんもみず単タイプに等倍止まりです</td>
</tr>
</tbody>
</table>
</div>

---

## パートナー（同居率上位）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率1位（M-4：3位）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率3位（M-4：6位）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" loading="lazy">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率6位（M-4：8位）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率7位（M-4：1位）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率8位（M-4：9位）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率9位（M-4：7位）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" loading="lazy">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率10位（M-5新）</div>
  </div>
</div>

**アシレーヌ（1位・M-4：3位）**は同居率トップに浮上しました。ムーンフォース（フェアリー）はカイリュー（使用率8位、カイリュナイト採用率80.4%でドラゴン/ひこう複合）に×2で通り、カバルドンのじしんが無効（×0）となる相手への打点をパーティに補う役割分担です。アシレーヌ自身は場に出ている間カバルドンが展開した砂嵐ダメージを受けます。

**メタグロス（2位）**ははがねタイプのため、カバルドンが苦手とするくさ技全般を半減できます。カバルドンの物理耐久とメタグロスの高いA・Bを組み合わせ、弱点タイプを補い合う役割分担です。

**ブリジュラス（5位）**ははがねタイプのため砂嵐ダメージを受けず、多くのタイプに耐性を持ちます。B130の高い物理耐久でカバルドンと役割が重ならず、ラスターカノン・りゅうせいぐんの特殊打点をパーティに供給する役割分担です。

**ミミッキュ（7位・M-4：1位）**は同居率が大きく下降しましたが引き続き上位に位置します。ばけのかわで一度攻撃を無効化しつつフィニッシャー役を担い、カバルドンがあくびとふきとばしで場を整えた後に積んで全抜きを狙う役割分担です。

---

## まとめ

M-5のカバルドンは使用率6位に下降し、M-4からの主な変化は以下の2点です。

- **EV最多がH32-B2-D32（21.4%）に再逆転**：しんちょう27.2%（+11.2pp）とD124の組み合わせで、使用率を伸ばしたアシレーヌ・ブリジュラスの特殊打点に対応
- **なまける49.5%（-11.9pp）**：ステルスロック・ふきとばしの採用が伸びた分、回復技の優先度が下がる構成へシフト

技4枠の構成は「じしん/あくび/ふきとばし/ステルスロック」か「じしん/あくび/なまける/ステルスロック」かで選出意図が変わります。前者は積みエース対策を自身で担い、後者はステロ設置と長期消耗を優先するかたちです。相手パーティの特殊アタッカーの比重が高いほどD32型、物理アタッカーの比重が高いほどB32型を選ぶのが基本方針です。

---

## 関連記事

- [カバルドン考察 M-4](/blog/hippowdon-analysis-m4/)
- [カバルドン考察 M-3](/blog/hippowdon-analysis-m3/)

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/hippowdon/)**
