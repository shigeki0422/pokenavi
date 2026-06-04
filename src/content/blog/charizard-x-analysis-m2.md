---
title: '【ポケモンチャンピオンズ】メガリザードンX考察 M-2 物理ほのお/ドラゴン型 採用率と立ち回り'
description: 'M-2シーズンで使用率5位のリザードン。そのうち34.9%が選ぶメガリザードンXを徹底分析。かたいツメ×りゅうのまいの崩し力、物理・特殊両対応の構築法、ステロ対策まで実データをもとに解説します。'
pubDate: '2026-05-22'
draft: true
heroImage: '../../assets/hero-charizard-x-m2.png'
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
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" />
  <div>
    <h2 style="margin:0 0 8px">メガリザードンX</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.85rem;color:#555">
      使用率 <strong style="color:#dc2626">5位</strong>（リザードン全体） ／
      メガ石採用率 <strong style="color:#7c3aed">34.9%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

M-2シーズンシングルバトルでリザードン全体は**使用率5位**を記録。そのうち約34.9%がリザードナイトXを持たせてメガリザードンXとして運用されています。シーズントップのメガリザードンYが63.6%という数字を誇る中でも、Xを選ぶプレイヤーが確実に存在している理由は明確です——**かたいツメ×りゅうのまいによる物理崩し力**、そしてほのお/ドラゴンという攻守に優れたタイプ複合にあります。

---

## なぜ今、メガリザードンXが強いのか

### 1. かたいツメ＋りゅうのまいでトップクラスの崩し力

メガリザードンXのとくせい**かたいツメ**は、接触技の威力を×1.3にする効果を持ちます。フレアドライブ（威力120）がかたいツメで実質威力156、ドラゴンクロー（威力80）が実質威力104となります。さらに**りゅうのまい**で+1こうげき・+1すばやさを積めば、積み後の実質ほのお一致フレアドライブはこうげき130×1.5（タイプ一致補正）×1.3（かたいツメ）×1.5（りゅうのまい）という破壊的なダメージを叩き出します。M-2環境で猛威を振るうガブリアスやブリジュラスに対して、りゅうのまい1回から確定2発以内に持ち込めるケースが増えることで、**積みエース型の決定力としてはトップクラス**です。

### 2. ほのお/ドラゴン複合タイプによる広い技範囲

メガリザードンYがひこうタイプを持つのに対し、Xはドラゴンタイプに変化します。このタイプは「こおり弱点がない」という点で特筆されます（ほのおタイプがこおりの弱点を打ち消す）。また、ドラゴン技がタイプ一致で使えるため、**みず/じめん/いわ以外の全タイプに対してほのお or ドラゴンのどちらかで等倍以上**が取れる攻撃範囲を誇ります。特に環境上位のガブリアス・ブリジュラス・カイリューといったドラゴン系には、ドラゴン一致技が突き刺さります。

### 3. こうげき130・とくこう130の両刀ポテンシャル

メガリザードンXはこうげき130・とくこう130という完全な両刀数値を持つ稀有なポケモンです。物理に偏ったAS型（りゅうのまい）だけでなく、ニトロチャージ採用のCS型や、かみなりパンチでギャラドス・アシレーヌといったみず複合をケアする混合型も成立します（みず単体ならほのお技を等倍で受けられるため、かみなりパンチは主にひこう・みず複合への上振れ打点）。相手のHB振りポケモンをとくこう技でケアできる柔軟性は、Xを「読まれにくい」アタッカーとして機能させます。

---

## 基本スペック

### 種族値（メガリザードンX）

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">78</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">111</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>130</strong></span>
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
      <div style="width:50%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>100</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">634</span>
  </div>
</div>

こうげき・とくこう が共に130という完全均等な両刀数値は、レジェンド級ポケモン並みの破壊力を持ちます。ぼうぎょ111は物理耐久面でも水準以上で、積み展開に入りやすい。一方でとくぼう85・HP78というDラインの薄さは、特殊技（特に弱点技）への耐性がなく、水・電気・竜技での確定1発圏に入るリスクがあります。すばやさ種族値100は、環境トップのガブリアス（種族値102）にわずかに届かずブリジュラス（種族値85）より速いという位置取り。**ようき最速のS実数値は152となりガブリアス（最速S実数値169）には及びませんが、りゅうのまい1回でS実数値228相当まで上がり、環境の大半を上から叩けます**。

### メガ進化前後の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px;border:1px solid #cbd5e1">メガ前</th>
  <th style="padding:8px;border:1px solid #cbd5e1">メガ後（X）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">変化量</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#94a3b8">±0</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px;border:1px solid #cbd5e1">84</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong>130</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">+46</td>
</tr>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1">111</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">+33</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px;border:1px solid #cbd5e1">109</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong>130</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">+21</td>
</tr>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px;border:1px solid #cbd5e1">85</td>
  <td style="padding:8px;border:1px solid #cbd5e1">85</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#94a3b8">±0</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#94a3b8">±0</td>
</tr>
</tbody>
</table>
</div>

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ほのお" />
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ドラゴン" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（4倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効・耐性</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> じめん<br>
    <img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> いわ<br>
    <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> ドラゴン<br>
    <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> フェアリー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <small style="color:#555">こおり弱点なし（ほのおで相殺）／みずも×2(ほのお)×0.5(ドラゴン)＝等倍</small><br>
    ほのお½ / くさ½ / でんき½ / むし½ / みず1
  </td>
</tr>
</tbody>
</table>
</div>

メガリザードンXの重要なポイントは**4倍弱点が存在しない**こと。メガリザードンYが4倍いわ弱点を持つのと対照的に、Xは弱点が4つ（じめん・いわ・ドラゴン・フェアリー）ある代わりに特定タイプでの即死が起きにくい。みず技はほのお×2・ドラゴン×0.5で等倍止まりに抑えられる点も見逃せません。ただし**ステロ（ステルスロック）はいわタイプ扱いのダメージで最大1/4ダメージ**を受けるため、ステロ展開への対策は必須です。

---

## 主要型の解説

### 型1: りゅうのまい型（ようき/いじっぱり・AS）

<div style="background:#fef9ec;border:1px solid #f59e0b;border-radius:8px;padding:14px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:48px;height:48px">
  <div>
    <strong>りゅうのまい型</strong><br>
    <small style="color:#555">AS振り ／ ようき or いじっぱり</small>
  </div>
</div>

<div style="overflow-x:auto">
<table style="width:100%;border-collapse:collapse;font-size:0.88em">
<thead>
<tr style="background:#fef3c7">
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:left">スロット</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:left">技</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:left">用途</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #fcd34d">1</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>りゅうのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-15-dragon.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">A+1・S+1の積み技。1回積めば全抜き射程</td>
</tr>
<tr style="background:#fffbeb">
  <td style="padding:6px 10px;border:1px solid #fcd34d">2</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>フレアドライブ</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">かたいツメで実質156。一致補正込みで234の爆発力</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #fcd34d">3</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>ドラゴンクロー</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-15-dragon.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">かたいツメで実質104。ガブリアス・カイリュー等ドラゴンへの打点</td>
</tr>
<tr style="background:#fffbeb">
  <td style="padding:6px 10px;border:1px solid #fcd34d">4</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>かみなりパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-12-electric.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">ギャラドス・アシレーヌ等みず複合への打点確保。かたいツメで実質97.5</td>
</tr>
</tbody>
</table>
</div>
</div>

**採用率データとの照合**: りゅうのまい26.9%・フレアドライブ33.3%・ドラゴンクロー24.0%・かみなりパンチ18.2%という実データが、この型の採用を裏付けています。

**ようきvs.いじっぱり**: ようきAS振りの場合、S無振り状態でS100グループ（ウルガモスなど）と同速になります。いじっぱりはAをさらに伸ばす代わりにSが落ちるため、S抜き調整が必要。対戦環境にS100ラインのポケモンが多いM-2では**ようき推奨**です。りゅうのまいを1回積んだ後のS実数値は環境上位の大半を上回り、アシレーヌ・マスカーニャ・ミミッキュなどを上から踏めます。

**フレアドライブ運用の注意**: フレアドライブは1/3ダメージの反動があるため連打できません。積んだ後に2体程度で役割を終えるイメージが基本。はねやすめ（採用率22.1%）と組み合わせることで持久力を高める選択肢もあります。

---

### 型2: ニトロチャージCS型（ひかえめ/おくびょう）

<div style="background:#f0fdf4;border:1px solid #4ade80;border-radius:8px;padding:14px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:48px;height:48px">
  <div>
    <strong>ニトロチャージCS型</strong><br>
    <small style="color:#555">CS振り ／ ひかえめ or おくびょう</small>
  </div>
</div>

<div style="overflow-x:auto">
<table style="width:100%;border-collapse:collapse;font-size:0.88em">
<thead>
<tr style="background:#dcfce7">
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:left">スロット</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:left">技</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:left">用途</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #86efac">1</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>ニトロチャージ</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">50</td>
  <td style="padding:6px 10px;border:1px solid #86efac">S+1の積み技兼ほのお打点。かたいツメで実質65</td>
</tr>
<tr style="background:#f0fdf4">
  <td style="padding:6px 10px;border:1px solid #86efac">2</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>かえんほうしゃ</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #86efac">C130×タイプ一致補正で安定した主力ほのお技</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #86efac">3</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>エアスラッシュ</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-02-flying.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #86efac">かくとう・むし・くさへの打点確保。命中95%・ひるみ30%</td>
</tr>
<tr style="background:#f0fdf4">
  <td style="padding:6px 10px;border:1px solid #86efac">4</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>オーバーヒート</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #86efac">捨て技気味の超火力フィニッシュ技（C-2・命中90%）</td>
</tr>
</tbody>
</table>
</div>
</div>

**この型の強み**: ニトロチャージでS+1を積みながらほのお打点を同時に確保できる点が優秀です。CS振りひかえめの場合、C130×タイプ一致補正×ひかえめ補正のかえんほうしゃは相手のHB振りポケモンにも大ダメージを与えられます。エアスラッシュは一致補正なしですが、かくとうタイプ（ルカリオ）への確実な打点として機能します。

**CS型の相性**: 相手の物理受け（ぼうぎょ振りポケモン）を特殊技で貫通できるため、**相手の裏をかく読み合い性能**が高い。ただしニトロチャージは威力50と低く、ニトロチャージ段階では即効性がありません。積む余裕を作れるパーティ構成が前提となります。

採用率データでは**ニトロチャージ28.9%・かえんほうしゃ42.4%・エアスラッシュ32.9%・オーバーヒート26.6%**という結果が、CS混合型の実採用を示しています。

---

### 型3: はねやすめ型（ずぶとい・HB）

<div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:8px;padding:14px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:48px;height:48px">
  <div>
    <strong>はねやすめ型</strong><br>
    <small style="color:#555">HB振り ／ ずぶとい</small>
  </div>
</div>

<p style="font-size:0.88em;color:#555;margin:8px 0">
はねやすめ採用率22.1%に示されるように、一定数のプレイヤーが耐久寄りの型を採用。ずぶといHB振りとはねやすめを組み合わせることで、じめん・いわ弱点技への耐性を高めつつ長期戦へ持ち込む戦術です。ただしずぶとい採用率は1.0%と低く、M-2では特殊なサブオプションとなっています。
</p>
</div>

---

## 主要な技と採用率

> 技採用率はリザードンX・Yを区別しない**合算データ**です。フレアドライブ・ドラゴンクロー・りゅうのまいはX型（物理）、ソーラービーム・かえんほうしゃ等の特殊技はX/Y双方に跨がる点に留意してください。以降の各型解説の採用率も同じ合算値を参照しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">用途・補足</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">42.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">安定したほのお打点。CS型の主力技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>フレアドライブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かたいツメで実質156。りゅうのまい型の核</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>エアスラッシュ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう・くさへの打点。ひるみ30%も優秀</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>ニトロチャージ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">50</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S+1の積み+ほのお打点。CS型の加速手段</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A+1・S+1。1積みで全抜き射程に入る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>オーバーヒート</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">C-2の代わりに高威力。フィニッシュ技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>ドラゴンクロー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かたいツメで実質104。ガブリアス・カイリュー等ドラゴンへの打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP50%回復。耐久型・積み後の長期戦向け</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>かみなりパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドス・アシレーヌ等みず複合への打点。かたいツメで実質97.5</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>ソーラービーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">61.0%*</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">※Y型込みの数値。Xではほぼ非採用</td>
</tr>
</tbody>
</table>
</div>

---

## 弱点となる相手ポケモンと対策

メガリザードンXが苦手とする相手をまとめました。これらに対応できるパートナーの確保が重要です。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#fee2e2">
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">天敵ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">理由</th>
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">対策パートナー案</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">じしん（採用率63.7%）が×2で刺さり、りゅうのまいで上から制圧される（たきのぼりのみず技は等倍）。威嚇でこちらのAも下がる</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">ブリジュラス・カイリュー（でんき技でみず複合を処理）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">ムーンフォース（採用率97.0%）のフェアリー技がドラゴンに×2で刺さる。みず技は等倍だが、アクアジェット（66.6%）の先制で削られる</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">ハッサム（はがねでフェアリー半減・ほのお等倍）・ブリジュラス</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">じしんで2倍弱点。S102でXより速いケースも</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">アーマーガア・ギルガルド</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">無積みのXより速く、トリックフラワーやはたきおとすで先手を取られる（ほのお技は2倍で通る）</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">アーマーガア・ハッサム</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5">ステルスロック展開</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">いわ弱点でステロ1/4ダメージ。大幅に行動制限</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">カバルドン・アーマーガア（ステロ対策）</td>
</tr>
</tbody>
</table>
</div>

---

## 有利を取れる主要ポケモンとの相性

苦手な相手だけでなく、リザードンXが有利を取れる相手も押さえておきます。**使用率TOP25のうち、Xの一致技（ほのお・ドラゴン）が×2以上で刺さり、かつ相手の主力技（pokemon_moves採用率で確認）がXの弱点を突かない相手**を選定しました。タイプ相性は2タイプの倍率を掛け合わせて算出しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#dcfce7">
  <th style="padding:8px 12px;border:1px solid #86efac;text-align:left">相手</th>
  <th style="padding:8px 12px;border:1px solid #86efac;text-align:left">刺さる打点</th>
  <th style="padding:8px 12px;border:1px solid #86efac;text-align:left">有利な理由・留意点</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #86efac"><img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム<br><small>使用率14位</small></td>
  <td style="padding:8px 12px;border:1px solid #86efac">ほのお ×4（むし×2・はがね×2）</td>
  <td style="padding:8px 12px;border:1px solid #86efac">フレアドライブ・かえんほうしゃが一致×4で確1圏。バレットパンチ（はがね½）・インファイト（かくとう等倍）はXの弱点を突かず、被ダメも軽い</td>
</tr>
<tr style="background:#f0fdf4">
  <td style="padding:8px 12px;border:1px solid #86efac"><img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ<br><small>使用率21位</small></td>
  <td style="padding:8px 12px;border:1px solid #86efac">ドラゴン ×2（あく等倍・ドラゴン×2）</td>
  <td style="padding:8px 12px;border:1px solid #86efac">ドラゴンクローが一致×2。あくのはどう・りゅうせいぐんは弱点を突かず、だいちのちから採用は8.9%と低い。りゅうのまい後はS98を上から踏める</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #86efac"><img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー<br><small>使用率16位</small></td>
  <td style="padding:8px 12px;border:1px solid #86efac">ドラゴン ×2（ドラゴン×2・ひこう等倍）</td>
  <td style="padding:8px 12px;border:1px solid #86efac">ドラゴンクローが一致×2でS80を上から叩ける。ただしじしん（15.2%）が×2、しんそく（45.6%）は先制で削られるため過信は禁物</td>
</tr>
<tr style="background:#f0fdf4">
  <td style="padding:8px 12px;border:1px solid #86efac"><img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン<br><small>使用率24位</small></td>
  <td style="padding:8px 12px;border:1px solid #86efac">ほのお ×2（あく等倍・はがね×2）</td>
  <td style="padding:8px 12px;border:1px solid #86efac">一致ほのお技が×2。けたぐり（かくとう等倍・17.6%）以外にXの弱点を突く技がない。ただしふいうち（あく・99.0%）は先制で入るため、削れた状態では注意</td>
</tr>
</tbody>
</table>
</div>

---

## 相性の良いパーティメンバー

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">フェアリー半減・後出し処理</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">ステロ阻止・物理受け</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ">
    <div class="name">ルカリオ</div>
    <div class="rate">フェアリー対策</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">ステロ除去・物理受け</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">ステロ撒き・天敵対策</div>
  </div>
</div>

**ステロ対策の重要性**: メガリザードンXはステルスロック（ステロ）によって1/4ダメージを受けます。**カバルドン・アーマーガアのような高耐久ポケモンでステロを撒かせない**、あるいはステロを除去できるポケモンをパーティに入れることが前提となります。

**アーマーガアとの相性**: アーマーガアはひこうタイプでじしんを無効化でき、ガブリアスのじしん・ギャラドスのじしんといったXの×2弱点技を後出しから受け止められます。受け出し後はちょうはつでステロ展開を妨害し、はねやすめで居座る動きが安定。**Xが苦手なガブリアス・ギャラドスへの後出し役**として相性補完が優秀です。

**先制技ケアの考え方**: Xはアシレーヌのアクアジェット・ドドゲザンのふいうち等の先制技で削れた状態を狩られやすいため、りゅうのまいを積むのは相手の先制技持ちを処理した後が安全。マスカーニャ（S123）など無積みで上を取る相手には、対面で積まず一度引いてから再展開する判断も有効です。

---

## XとYの使い分けまとめ

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:10px 14px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:10px 14px;border:1px solid #cbd5e1">メガリザードンX</th>
  <th style="padding:10px 14px;border:1px solid #cbd5e1">メガリザードンY</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">採用率</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">34.9%</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong>63.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">主力の向き</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">物理崩し・積みエース</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">特殊崩し・天候展開</td>
</tr>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">最大弱点</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">4倍弱点なし（4種2倍）</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fee2e2">いわ4倍</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ステロダメージ</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">1/4（いわ2倍）</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fee2e2"><strong>1/2（いわ4倍）</strong></td>
</tr>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">積み技</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">りゅうのまい（A+S）/ ニトロチャージ（S）</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">なし（火力で押す）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">選ぶ状況</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">相手にHB振りが多い環境</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">天候展開・火力押し</td>
</tr>
</tbody>
</table>
</div>

---

## データ分析①：「積みエース」の実態 — りゅうのまいは採用率5位

メガリザードンXは「かたいツメ×りゅうのまいの積みエース」として語られることが多いですが、実際の技採用率を順に並べると意外な実態が見えてきます。

| 順位 | 技 | 採用率 | 分類 |
|---|---|---|---|
| 1 | かえんほうしゃ | **42.4%** | 特殊ほのお |
| 2 | フレアドライブ | 33.3% | 物理ほのお |
| 3 | エアスラッシュ | 32.9% | 特殊ひこう |
| 4 | ニトロチャージ | 28.9% | S積み |
| **5** | **りゅうのまい** | **26.9%** | **物理A・S積み** |

「積みエースの象徴」であるりゅうのまいは採用率5位（26.9%）で、最多技かえんほうしゃ（42.4%）より**15.5ポイント低い**数値です。さらにS積み技のニトロチャージ（28.9%）にも及ばない結果となっています。

この数字が示すのは、メガリザードンXの実運用が「物理りゅうのまい型」と「特殊ニトロチャージCS型」に二分されているという現実です。「X=物理積みエース」というイメージが先行しがちですが、実際は約40%が特殊技主体のCS型構成を採用しています。

相手が「X=物理型」と読んで物理受けを投入してくる場面では、特殊CS型が有効に刺さります。YではなくXを選ぶ理由のひとつに、この「型の読み合い性能」があります。

---

## まとめ

メガリザードンXはM-2シーズンで全リザードン採用の34.9%を占める、**物理崩し特化のメガ進化アタッカー**です。

- **かたいツメ×りゅうのまい**の組み合わせは積み1回から全抜き射程が広がる破壊力
- ほのお/ドラゴンのタイプ複合で**4倍弱点が存在しない**ことは安定感に直結
- こうげき130・とくこう130の**両刀ポテンシャル**が相手の対策を難しくする
- ステロ（ステルスロック）は1/4ダメージで大きな痛手→**ステロ対策ポケモンとセット**が前提

メガリザードンY（63.6%）の方が採用率は高いですが、**相手のHB振りポケモンを崩したい・積みエースで対戦を決めたい**という戦略なら、Xを選ぶ明確な理由があります。パーティ全体での弱点補完を意識して構築してみてください。
