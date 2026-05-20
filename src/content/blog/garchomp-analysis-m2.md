---
title: '【ポケモンチャンピオンズ】ガブリアス徹底考察 M-2シーズン使用率1位の全て'
description: 'シーズンM-2シングルバトルで使用率1位のガブリアスを徹底分析。タスキ型・スカーフ型・オボン型の3大構築を解説し、シーズン中の環境変化データや相性の良いパーティ構成まで、実データをもとに紹介します。'
pubDate: '2026-05-20'
heroImage: '../../assets/blog-placeholder-3.jpg'
---

<style>
.poke-icon {
  display: inline-block;
  width: 40px;
  height: 40px;
  vertical-align: middle;
  margin-right: 4px;
}
.poke-icon-lg {
  display: block;
  width: 80px;
  height: 80px;
  margin: 0 auto 8px;
}
.type-badge {
  display: inline-block;
  width: 52px;
  height: 52px;
  vertical-align: middle;
  margin: 2px;
}
.type-badge-sm {
  display: inline-block;
  width: 32px;
  height: 32px;
  vertical-align: middle;
  margin: 1px 2px;
}
.item-icon {
  display: inline-block;
  width: 32px;
  height: 32px;
  vertical-align: middle;
  margin-right: 4px;
  object-fit: cover;
}
.pokemon-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 20px 0;
}
.pokemon-header img {
  width: 96px;
  height: 96px;
}
.type-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 8px 0;
}
.build-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}
.partner-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 12px;
  margin: 16px 0;
}
.partner-card {
  text-align: center;
  padding: 8px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
}
.partner-card img {
  width: 56px;
  height: 56px;
  display: block;
  margin: 0 auto 4px;
}
.partner-card .name {
  font-size: 0.75rem;
  font-weight: bold;
}
.partner-card .rate {
  font-size: 0.7rem;
  color: #666;
}
</style>

<div class="pokemon-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" />
  <div>
    <h2 style="margin:0 0 8px">ガブリアス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px" />
    </div>
  </div>
</div>

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ガブリアスは**使用率1位**を記録しています。前シーズンM-1でも上位523構築のうち**281構築（53.7%）**に採用されるなど、ポケモンチャンピオンズのシングル環境を長期にわたって支配しているポケモンです。

この記事では実際の対戦データをもとに、ガブリアスがなぜ強いのか、どのような型で使われているのか、どんなパーティに入れるべきかを徹底的に掘り下げます。

---

## 基本スペック

### 種族値

| HP | こうげき | ぼうぎょ | とくこう | とくぼう | すばやさ | 合計 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 108 | 130 | 95 | 80 | 85 | 102 | 600 |

攻撃130・素早さ102という数値が際立っています。素早さ102はルカリオ・ゲッコウガといった主要な高速アタッカーを上回り、**最速で使うことでほぼすべての無振りポケモンを先制できる**優秀なライン。さらに攻撃130は環境最高水準で、努力値を振らなくてもダメージが大きい。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ドラゴン" />
  <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="じめん" />
</div>

| 弱点（4倍） | 弱点（2倍） | 無効 |
|:--:|:--:|:--:|
| <img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> こおり | <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> ドラゴン・<img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> フェアリー | <img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> でんき |

弱点はこおり・ドラゴン・フェアリーの3タイプ。一方でポケモンチャンピオンズ環境で多いでんきタイプを**完全無効化**し、じめんタイプの攻撃でブリジュラス・ハラバリーなどの電気ポケモンを一撃で倒せるのが大きな強みです。

---

## なぜ1位なのか——ガブリアスの強さ

### 1. 技範囲が圧倒的に広い

| 技 | 採用率 |
|:--|:--:|
| <img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> じしん | 99.2% |
| <img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> ステルスロック | 51.9% |
| <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> げきりん | 49.0% |
| <img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> がんせきふうじ | 40.3% |
| <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> スケイルショット | 33.0% |
| <img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> いわなだれ | 23.6% |
| <img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> どくづき | 19.6% |
| <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> ほのおのキバ | 14.1% |

じしん1本でブリジュラス・ハラバリーを完封しつつ、ドラゴン技・いわ技・どくづき・ほのおのキバを組み合わせることで**ほぼすべての環境ポケモンに等倍以上が取れます**。これだけの技範囲を持ちながら攻撃130・素早さ102を持つポケモンは他にほとんど存在しません。

下表は上位ポケモンへの各攻撃技の効果をまとめたものです。<span style="color:#e67e22;font-weight:bold">◎</span>=効果抜群（2倍）、<span style="color:#dc2626;font-weight:bold">◎◎</span>=4倍、<span style="color:#94a3b8">○</span>=等倍、<span style="color:#60a5fa">△</span>=いまひとつ、<span style="color:#2563eb;font-weight:bold">△△</span>=¼倍、<span style="color:#64748b">×</span>=無効

<div style="overflow-x:auto;margin:16px 0;">
<table style="width:100%;border-collapse:collapse;font-size:0.82rem;">
<thead>
<tr style="background:#f1f5f9;">
  <th style="padding:8px 12px;text-align:left;border:1px solid #cbd5e1;min-width:140px">ポケモン</th>
  <th style="padding:6px 4px;text-align:center;border:1px solid #cbd5e1;min-width:64px"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;display:block;margin:0 auto 2px">じしん</th>
  <th style="padding:6px 4px;text-align:center;border:1px solid #cbd5e1;min-width:64px"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;display:block;margin:0 auto 2px">げきりん</th>
  <th style="padding:6px 4px;text-align:center;border:1px solid #cbd5e1;min-width:72px"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;display:block;margin:0 auto 2px">がんせきふうじ</th>
  <th style="padding:6px 4px;text-align:center;border:1px solid #cbd5e1;min-width:64px"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;display:block;margin:0 auto 2px">どくづき</th>
  <th style="padding:6px 4px;text-align:center;border:1px solid #cbd5e1;min-width:72px"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;display:block;margin:0 auto 2px">ほのおのキバ</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス<br><small style="color:#94a3b8">はがね/ドラゴン</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#64748b">×</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0939-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハラバリー<br><small style="color:#94a3b8">でんき</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ<br><small style="color:#94a3b8">くさ/あく</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ<br><small style="color:#94a3b8">みず/フェアリー</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#64748b">×</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#60a5fa">△</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン<br><small style="color:#94a3b8">ほのお/ひこう</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#64748b">×</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">◎◎<br><small>4倍</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#60a5fa">△</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア<br><small style="color:#94a3b8">はがね/ひこう</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#64748b">×</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#64748b">×</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ<br><small style="color:#94a3b8">かくとう/はがね</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#2563eb;font-weight:bold">△△<br><small>¼倍</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#64748b">×</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス<br><small style="color:#94a3b8">みず/ひこう</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#64748b">×</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#60a5fa">△</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0670-05.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フラエッテ:永遠<br><small style="color:#94a3b8">フェアリー</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#64748b">×</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー<br><small style="color:#94a3b8">ゴースト/どく</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0637-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス<br><small style="color:#94a3b8">ほのお/むし</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">◎◎<br><small>4倍</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#60a5fa">△</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム<br><small style="color:#94a3b8">はがね/むし</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#64748b">×</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">◎◎<br><small>4倍</small></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ<br><small style="color:#94a3b8">ゴースト/フェアリー</small></td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#64748b">×</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;text-align:center;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
</tbody>
</table>
</div>

### 2. ステルスロックを覚える物理アタッカー

```
ステルスロック採用率：51.9%（技2位）
```

使用率上位のアタッカーがまきびき役を兼ねられるのは貴重です。ガブリアスがステルスロックを撒きながらアタッカーとして機能することで、**パーティの枠を節約**できます。

### 3. 特性「さめはだ」が対面を制する

```
さめはだ採用率：99.6%
```

接触技を受けると相手に反動ダメージ（1/8）を与える特性。きあいのタスキを持ったガブリアスに対し、1発で倒せない相手は確定で反動を受けます。これにより**相手の択を狭める**効果があり、特に物理アタッカーとの1対1に強い。

---

## 主要3型の解説

### 型1：きあいのタスキ型（採用率37.5%・最多）

<div class="build-header">
  <img src="/images/items/item-0275-tasuki.png" alt="きあいのタスキ" class="item-icon" style="width:40px;height:40px;" />
  <strong>想定用途：先発ステルスロック撒き＆対面アタッカー</strong>
</div>

```
性格：ようき（52.5%）
努力値：AS（攻撃・素早さ全振り）
持ち物：きあいのタスキ
技構成例：じしん / ステルスロック / げきりん or がんせきふうじ / どくづき
```

最速ようきで素早さを最大まで伸ばし、タスキで先発に出て確実にステルスロックを撒く型。相手が先制技を持っていなければタスキで確定1発の攻撃を耐えてもう1ターン行動できます。

**弱点**：あられやすなあらしによるタスキ消費、先制技（マッハパンチ・かげうちなど）に対して脆い。

**この型を使うパーティの特徴**：ステルスロックを撒いた後、フェアリータイプの一致技を通せるポケモン（アシレーヌ・フラエッテなど）を後続に置く構築が多く見られます。タスキ型ガブリアスと同居率が高いのは下記の通りです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" />
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率 36%</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" />
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率 36%</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" />
    <div class="name">ゲンガー</div>
    <div class="rate">同居率 33%</div>
  </div>
</div>

---

### 型2：こだわりスカーフ型（採用率34.5%・シーズン序盤は拮抗）

<div class="build-header">
  <img src="/images/items/item-0287-scarf.png" alt="こだわりスカーフ" class="item-icon" style="width:40px;height:40px;" />
  <strong>想定用途：最速スカーフで詰め・対面処理</strong>
</div>

```
性格：ようき（最速）またはいじっぱり（火力優先）
努力値：AS
持ち物：こだわりスカーフ
技構成例：じしん / げきりん / がんせきふうじ / どくづき or ほのおのキバ
```

スカーフ込みで素早さ153（最速時）。環境の高速ポケモンの大半を上回り、こだわり補正で火力も確保。**じしん一発でブリジュラスを倒せる**点が特に強力です。

シーズン序盤（5/13）はタスキとの差が10pt以上ありましたが、5/15〜5/17にかけて両者が35%台で**ほぼ逆転寸前まで拮抗**しました。スカーフ型の採用が増えたタイミングで「タスキ持ちに弱いが先制技対策になるスカーフ」の需要が上昇した動きと考えられます。

| 日付 | タスキ型 | スカーフ型 | 差 |
|:--|:--:|:--:|:--:|
| 5/13 | 39.9% | 29.7% | +10.2pt |
| 5/15 | 36.4% | 33.9% | +2.5pt ← 急接近 |
| 5/17 | 35.8% | 35.0% | **+0.8pt ← 最も拮抗** |
| 5/20 | 37.5% | 34.5% | +3.0pt ← 再びタスキが優位 |

**スカーフ型と同居率が高いポケモン（M-1データ）**：

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" />
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率 45%</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" />
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率 44%</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" />
    <div class="name">アーマーガア</div>
    <div class="rate">同居率 29%</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0115-00.webp" alt="ガルーラ" />
    <div class="name">ガルーラ</div>
    <div class="rate">同居率 25%</div>
  </div>
</div>

火力・制圧力を補う受け枠との組み合わせが多い傾向です。

---

### 型3：オボンのみ型（採用率16.0%）

<div class="build-header">
  <img src="/images/items/item-0158-obon.png" alt="オボンのみ" class="item-icon" style="width:40px;height:40px;" />
  <strong>想定用途：耐久型ステルスロック撒き・居座り</strong>
</div>

```
性格：わんぱく（11.2%）またはずぶとい
努力値：HB（HP・防御）またはHBD（HP・防御・特防）
持ち物：オボンのみ
技構成例：じしん / ステルスロック / ドラゴンテール / がんせきふうじ or どくづき
```

防御面に厚く振り、ドラゴンテールで**相手の交代を強制しながらステルスロックダメージを蓄積**させる型。一見守備的ですが、ドラゴンテール＋ステルスロックの組み合わせは相手パーティへのダメージ源として非常に強力です。

M-1データではイダイトウ（オス）(66%)・フラエッテ（永遠）(64%)との同居率が突出して高く、**イダイトウ・フラエッテという強力な全抜きアタッカーの前座としてドラゴンテール&ステルスロックで盤面を整える**役割が見て取れます。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ（オス）" />
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率 66%</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0670-05.webp" alt="フラエッテ（永遠）" />
    <div class="name">フラエッテ:永遠</div>
    <div class="rate">同居率 64%</div>
  </div>
</div>

---

### 番外：つるぎのまい型（採用率18.3%）

```
性格：ようき or いじっぱり
持ち物：ラムのみ（5.5%）or オボンのみ
技構成例：じしん / スケイルショット or げきりん / ほのおのキバ / つるぎのまい
```

1回積めば攻撃260相当。スケイルショット（複数回ヒット+素早さ上昇）との組み合わせが魅力で、**積んだ後はほぼ全てのポケモンを1発圏内**に入れられます。ラムのみを持たせることでやけど・まひを1度だけ無効化し、安全に積む機会を確保します。

---

### 番外：メガガブリアス型（採用率1.7%）

<div class="build-header">
  <img src="/images/items/item-0683-garchompite.png" alt="ガブリアスナイト" class="item-icon" style="width:40px;height:40px;" />
  <strong>メガシンカ採用率：1.7%</strong>
</div>

ポケモンチャンピオンズではメガシンカが使用可能。メガガブリアスは攻撃170・特攻120に上昇しますが、**素早さが102→92に下がる**のが最大の問題点です。素早さが落ちることで最速無振り相手にも抜かれるケースが増え、スカーフ・タスキ型に比べて採用されにくい状況です。

---

## パーティ構成の考え方

### ガブリアスが苦手なポケモンと対策

| 苦手な相手 | 理由 | 解決策 |
|---|---|---|
| <img src="/images/pokemon/pokemon-0730-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:3px">アシレーヌ・<img src="/images/pokemon/pokemon-0670-05.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:3px">フラエッテ | <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">フェアリー技4倍 | <img src="/images/pokemon/pokemon-0212-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:3px">ハッサム・<img src="/images/pokemon/pokemon-0681-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:3px">ギルガルドで受ける |
| <img src="/images/pokemon/pokemon-0149-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:3px">メガカイリュー・<img src="/images/pokemon/pokemon-0635-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:3px">サザンドラ | <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">ドラゴン技2倍 | <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">フェアリータイプで受ける |
| <img src="/images/pokemon/pokemon-0478-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:3px">ユキメノコ・<img src="/images/pokemon/pokemon-0038-01.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:3px">アローラキュウコン | <img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">こおり技4倍 | 先制で倒すか交代で受ける |
| <img src="/images/pokemon/pokemon-0094-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:3px">ゲンガー・<img src="/images/pokemon/pokemon-0778-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:3px">ミミッキュ | 影分身・道連れで崩す | タスキで1ターン確保 |

### 持ち物別・相性の良いポケモン

**<img src="/images/items/item-0275-tasuki.png" alt="きあいのタスキ" class="item-icon" /> タスキ型のパーティ**

ガブリアスがステルスロックを撒いた後、フェアリー耐性を持つ後続につなぐ構築が安定します。

- <img src="/images/pokemon/pokemon-1018-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px" />**ブリジュラス**（電気・はがねで多くに打点、ゴーストタイプ無効）
- <img src="/images/pokemon/pokemon-0730-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px" />**アシレーヌ**（フェアリー技でドラゴンを一掃）
- <img src="/images/pokemon/pokemon-0823-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px" />**アーマーガア**（物理受け、釣り交換先）

**<img src="/images/items/item-0287-scarf.png" alt="こだわりスカーフ" class="item-icon" /> スカーフ型のパーティ**

高速処理で詰める型なので、詰め切れない耐久ポケモンを突破する手段を別枠で用意しておく必要があります。

- <img src="/images/pokemon/pokemon-0094-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px" />**ゲンガー**（催眠・トリックで崩し）
- <img src="/images/pokemon/pokemon-0115-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px" />**ガルーラ**・<img src="/images/pokemon/pokemon-0428-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px" />**ミミロップ**（メガシンカで受けを突破）

**<img src="/images/items/item-0158-obon.png" alt="オボンのみ" class="item-icon" /> オボン型のパーティ（ドラゴンテール構築）**

イダイトウ・フラエッテとの3枚構成が王道。ガブリアスがドラゴンテールで削り、全抜きアタッカーが締める役割分担です。

---

## シーズンM-2での環境的な位置づけ

M-2でガブリアスが1位を保っている背景には、**ブリジュラス・ハラバリーという電気ポケモンの台頭**があります。ガブリアスはでんきタイプを完全無効化した上で、じしん1発でこれらを倒せる数少ないポケモン。使用率2位の<img src="/images/pokemon/pokemon-1018-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px" />ブリジュラスへの最強の回答がガブリアスという構図で、「ブリジュラスに強いポケモン」を採用する際の第一候補になり続けています。

また注目の動向として、**キラフロルナイトの採用率が5/13→5/20の1週間で+19.3pt急増**しています。キラフロルのメガシンカは特殊技主体となるため、ガブリアスにとっての直接的な脅威にはなりにくいですが、特殊アタッカーが増えることでわんぱく型の価値が上がる可能性があります。

---

## まとめ

| 型 | 持ち物 | 採用率 | 強み | 弱み | 主な用途 |
|---|:--:|:--:|---|---|---|
| タスキ型 | <img src="/images/items/item-0275-tasuki.png" alt="きあいのタスキ" class="item-icon" /> | 37.5% | 確実に仕事、先発安定 | 先制技・天候に弱い | SR撒き＋1体処理 |
| スカーフ型 | <img src="/images/items/item-0287-scarf.png" alt="こだわりスカーフ" class="item-icon" /> | 34.5% | 最速、詰め性能高い | タスキ持ちに弱い | 中〜後発の一掃 |
| つるぎのまい型 | <img src="/images/items/item-0157-ram.png" alt="ラムのみ" class="item-icon" /> | 18.3% | 積み後の突破力 | 積む隙が必要 | 詰め・全抜き |
| オボン型 | <img src="/images/items/item-0158-obon.png" alt="オボンのみ" class="item-icon" /> | 16.0% | 耐久力、ドラゴンテール | 火力不足 | SR撒き＋流し |

ガブリアスはタスキ・スカーフ・オボンの3つの型がいずれも20〜37%の採用率を保っており、**どの型かが読みにくい**のも強さの一因です。パーティを見ただけでは「タスキか、スカーフか」の判断が難しく、対面での択を押し付けやすい。

M-2シーズンも折り返し地点を過ぎたころ、ガブリアスはまだ1位の座を守っています。シーズン後半でスカーフとタスキの勢力図がどう変わるかも注目です。
