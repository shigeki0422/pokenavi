---
title: 'メガリザードンX考察 M-2 物理ほのお/ドラゴン型 採用率と立ち回り'
description: 'M-2シーズンで使用率5位のリザードン。そのうち34.9%が選ぶメガリザードンXを徹底分析。かたいツメ×りゅうのまいの崩し力、物理・特殊両対応の構築法、ステロ対策まで実データをもとに解説します。'
updatedDate: '2026-06-05'
pubDate: '2026-06-05'
draft: false
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

メガリザードンXのとくせい**かたいツメ**は、接触技の威力を×1.3にする効果を持ちます。フレアドライブ（威力120）はかたいツメ×1.3・タイプ一致×1.5で実質威力234、ドラゴンクロー（威力80）は同様に実質威力156です。さらに**りゅうのまい**で+1こうげき・+1すばやさを積めば、Aはようき最速A182・いじっぱり最速A200の状態から1.5倍され、フレアドライブの実質威力も351相当に到達します。M-2環境で猛威を振るうガブリアスやブリジュラスに対して、りゅうのまい1回から確定2発以内に持ち込めるケースが増えることで、**積みエース型の決定力としてはトップクラス**です。

### 2. ほのお/ドラゴン複合タイプによる広い技範囲

メガリザードンYがひこうタイプを持つのに対し、Xはドラゴンタイプに変化します。ドラゴン単体ならこおり×2弱点ですが、ほのお複合により×0.5×2＝等倍まで戻り、こおり技で弱点を突かれない点が特筆されます。また、ドラゴン技がタイプ一致で使えるため、**ほのお半減タイプ（みず・いわ・ドラゴンなど）にもドラゴン一致技で等倍以上の打点を持てます**（ドラゴン技を半減/無効にするはがね・フェアリーは除く）。特に環境上位のガブリアス・カイリューといったドラゴン系にはドラゴン一致技が×2で刺さります。

### 3. こうげき130・とくこう130の両刀ポテンシャル

メガリザードンXはこうげき130・とくこう130という均等の両刀数値を持ちますが、リザードン選択時の性格分布（ひかえめ32.7%＋おくびょう30.0%≒Y型／いじっぱり17.6%＋ようき16.8%≒X型）から、**Xを選んだ場合は物理型（いじっぱり・ようき）が事実上前提**となります。Cで殴りたい場合はC159＋ひでりを持つY型が選ばれます。物理型の主軸はりゅうのまい・ニトロチャージで積みつつフレアドライブ・ドラゴンクローで殴る構成で、サブにかみなりパンチを採用する場合はメガギャラドス（みず/あく）・アシレーヌ（みず/フェアリー）・スターミー（みず/エスパー）といったみず系への補完打点になります（みずタイプにはほのお技が半減されますが、でんき技は×2で刺さるため有効。特にギャラドス＝みず/ひこうには×4）。

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

こうげき・とくこう が共に130というこうげき・とくこう均等の両刀数値で、物理・特殊どちらでも高い火力を出せます。ぼうぎょ111は物理耐久面でも水準以上で、積み展開に入りやすい。一方でとくぼう85・HP78というDラインの薄さは、特殊技（特に弱点技）への耐性がなく、水・電気・竜技での確定1発圏に入るリスクがあります。すばやさ種族値100は、環境トップのガブリアス（種族値102）にわずかに届かずブリジュラス（種族値85）より速いという位置取り。**ようき最速のSは167となりガブリアス（最速S169）に2差で抜かれますが、りゅうのまい1回（×1.5）でS250まで上がり、ガブリアス・マスカーニャ（最速S192）を含む環境上位の大半を上から叩けます**。

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
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（¼・½）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> じめん<br>
    <img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> いわ<br>
    <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> ドラゴン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> ほのお ¼<br>
    <img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> くさ ¼<br>
    <img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> むし ½<br>
    <img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> はがね ½<br>
    <img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> でんき ½
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なし</td>
</tr>
</tbody>
</table>
</div>

メガリザードンXの重要なポイントは**4倍弱点が存在しない**こと。メガリザードンYが4倍いわ弱点を持つのと対照的に、Xは弱点3種（じめん・いわ・ドラゴン）がすべて×2止まりで、特定タイプでの即死が起きにくい構造です。フェアリー技はほのお半減×ドラゴン×2＝等倍に収まり、こおり技もほのお半減で等倍止まりです。ほのお・くさは¼で受けられる点も強みですが、**ステルスロックはいわタイプ扱いのダメージで、いわ×2弱点のXは繰り出しごとに最大HPの1/4を固定で削られる**ため、ステルスロック展開への対策は必須です。

---

## 主要型の解説

### 型1: りゅうのまい型（ようき/いじっぱり・AS）

<div style="background:#fef9ec;border:1px solid #f59e0b;border-radius:8px;padding:14px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:48px;height:48px">
  <div>
    <strong>りゅうのまい型</strong>
  </div>
</div>

<div style="display:flex;flex-wrap:wrap;gap:16px;margin-bottom:10px;font-size:0.88em">
  <div style="flex:1;min-width:220px">
    <strong>特性:</strong> もうか（86.1%）※メガ後かたいツメ<br>
    <strong>性格:</strong> ようき（16.8%）or いじっぱり（17.6%）<br>
    <strong>EV:</strong> A32 S32（AS）<br>
    <strong>持ち物:</strong> リザードナイトＸ（34.9%）
  </div>
  <div style="flex:1;min-width:220px">
    <strong>技構成:</strong> りゅうのまい／フレアドライブ／ドラゴンクロー／選択技（はねやすめ or かみなりパンチ）
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
  <td style="padding:6px 10px;border:1px solid #fcd34d">A+1・S+1の積み技。1回でS250まで上がり、環境上位の大半を上から叩ける</td>
</tr>
<tr style="background:#fffbeb">
  <td style="padding:6px 10px;border:1px solid #fcd34d">2</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>フレアドライブ</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">かたいツメで実質156。一致補正込みで実質234相当の火力</td>
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
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>選択技</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">下記の選択技から1つ</td>
</tr>
</tbody>
</table>
</div>

**4枠目の選択技（採用率順）**:
- **はねやすめ（22.1%）**: HP50%回復。フレアドライブの反動（1/3）・ステルスロックの繰り出しダメージ（1/4）を回復しながら長期戦に持ち込む。積み後の場持ち強化に直結する最多採用の選択技。
- **かみなりパンチ（18.2%）**: でんき技。みず複合（メガギャラドス・アシレーヌ・スターミー等）への補完打点。みずタイプにはほのお技が半減されるため、でんき×2で穴を埋める役割。

なお積み技をニトロチャージ（28.9%）に置き換える派生もあります（下記補足参照）。この場合はりゅうのまいと択一になります。

</div>

**採用率データとの照合**: りゅうのまい26.9%・フレアドライブ33.3%・ドラゴンクロー24.0%が型1の必須3技。4枠目は採用率順にはねやすめ22.1%・かみなりパンチ18.2%が選ばれ、プレイスタイルで分かれます。

**ようきvs.いじっぱり**: ようきAS振りはS167で、ウルガモス（S100種族値）最速と同速・カバルドンS47等の中速以下を確実に抜けます。いじっぱりはAが約10%上がり、フレアドライブやドラゴンクローの確定数が伸びる一方、S152となりウルガモス等のS100族最速に抜かれます。**りゅうのまい1回（×1.5）後のSはようき250／いじっぱり228**で、ガブリアス169・マスカーニャ192を含む環境上位の大半を上から叩けます。積みが通る前提なら火力差を活かしたいじっぱりも選択肢。X/Y合算の性格採用率はようき・いじっぱり拮抗です。

**フレアドライブ運用の注意**: フレアドライブは1/3ダメージの反動があるため連打できません。積んだ後に2体程度で役割を終えるイメージが基本。長期戦を狙うなら4枠目をはねやすめ（採用率22.1%）にして持久力を高める選択肢があります。

---

### 補足: ニトロチャージ採用の派生（同じ物理AS型内で）

ニトロチャージは技採用率28.9%。**りゅうのまい（26.9%）の代わりに積み技として採用される選択肢**で、物理AS型（いじっぱり/ようき）内の派生です。S+1とほのお技を1技で両立できる代わりに、A補正が乗らないためフィニッシュ火力はりゅうのまい型に劣ります。

---

## 主要な技と採用率

> 技採用率はリザードンX・Yを区別しない**X/Y合算データ**です。物理技（フレアドライブ・ドラゴンクロー・りゅうのまい・ニトロチャージ・かみなりパンチ）はほぼX選択者に由来し、特殊技（ソーラービーム・オーバーヒート・エアスラッシュ等）はY側の比重が大きいという性質があります。X単独の採用率を直接得ることはできないため、本記事ではX主流の物理技プールについては合算採用率を「Xでの実採用に近い参考値」として扱い、特殊技については「X/Y合算」と明示します。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S+1の積み+ほのお打点。物理AS型でりゅうのまいの代わりに採用する派生</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A+1・S+1。1積みでS250、環境上位の大半を上から動ける</td>
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
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">メガ運用主流（メガ石62.9%）。メガ後みず/あく・最速S146でメガリザードンX（ようき最速S167）より遅いものの、じしん（63.7%）でじめん×2、たきのぼり等のみず技はA155で大きく削られる。こちらが<strong>かみなりパンチ（18.2%）</strong>を採用していない物理積み型では決定打を欠く</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">ブリジュラス・カイリュー（でんき技でみず複合を処理）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">ほのお技を等倍で受け止める高耐久のみず/フェアリー。フェアリー技・みず技はどちらもXに等倍止まりだが、アクアジェット（66.6%）の先制とうたかたのアリアの連打で、無補正のXでは押し切れず削り合いで不利</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">かみなりパンチ採用のX本体（でんき×2）・ブリジュラス</td>
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
</tbody>
</table>
</div>

---

## 有利を取れる主要ポケモン

苦手な相手だけでなく、リザードンXが有利を取れる相手も押さえておきます。**使用率TOP25のうち、Xの一致技（ほのお・ドラゴン）が×2以上で刺さり、かつ相手の主力技がXの弱点を突かない相手**を選定しました。タイプ相性は2タイプの倍率を掛け合わせて算出しています。

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
    <div class="rate">いわ半減・でんきでみず処理</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">ステロ撒き・物理受け</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ">
    <div class="name">ルカリオ</div>
    <div class="rate">ドラゴン・いわ半減受け</div>
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

**ステロ対策の重要性**: メガリザードンXはステルスロック（ステロ）によって1/4ダメージを受けます。相手側のカバルドン・ガブリアス等のステロ撒きに対しては、**アーマーガアのちょうはつ（採用率14.9%）でステロ展開を妨害する、ハッサムのとんぼがえりでステロ撒き役を削る**といった対策をパーティに組み込むことが前提となります（自軍カバルドンを採用する場合は味方のステロ展開役として運用する別話で、上記は相手のステロ撒きへの対処）。

**アーマーガアとの相性**: アーマーガアはひこうタイプでじしんを無効化でき、ガブリアスのじしん・ギャラドスのじしんといったXの×2弱点技を後出しから受け止められます。受け出し後はちょうはつでステロ展開を妨害し、はねやすめで居座る動きが安定。**Xが苦手なガブリアス・ギャラドスへの後出し役**として相性補完が優秀です。

**先制技ケアの考え方**: Xはアシレーヌのアクアジェット・ドドゲザンのふいうち等の先制技で削れた状態を狩られやすいため、りゅうのまいを積むのは相手の先制技持ちを処理した後が安全。

**無積みで上を取られる速い相手への対応**: マスカーニャ（S123）など無積みのXより速い相手には、ハッサムのバレットパンチ（先制・はがね一致）で処理する、あるいはアーマーガアでひこう半減を活かして受けてから引き先を作る、といった役割分担で対応します。

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
  <td style="padding:8px 14px;border:1px solid #cbd5e1">4倍弱点なし（3種2倍）</td>
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
  <td style="padding:8px 14px;border:1px solid #cbd5e1">相手にHD振り（特殊受け）が多い環境</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">天候展開・火力押し</td>
</tr>
</tbody>
</table>
</div>

---

## データ分析①：X選択者のほぼ全員が「積み技」を採用している

リザードナイトX採用率は34.9%。一方、X選択者主流の積み技2種（りゅうのまい・ニトロチャージ）の技採用率を見ると、興味深い数字が浮かびます。

| データ項目 | 採用率 |
|---|---|
| リザードナイトX | 34.9% |
| いじっぱり＋ようき（X選択者の主性格） | 34.4%（17.6%＋16.8%） |
| りゅうのまい | 26.9% |
| ニトロチャージ | 28.9% |

X採用率34.9%・性格分布34.4%・積み技合計55.8%（りゅうのまい+ニトロチャージ）。同一個体が積み技を2つ採用するのは合理性が薄いため、合計55.8%は「**X選択者のほぼ全員が、りゅうのまいかニトロチャージのいずれかを採用している**」ことを意味します。

これはX型の構築選択がほぼ「**物理AS型＋積み技**」で固定化されていることを示します。C130の両刀ポテンシャルがあるにもかかわらず、Xを選んだ場合の「特殊型」「無積み型」の余地は事実上存在せず、りゅうのまいで積んでから自分で全抜きする物理崩しに完全特化しているのが実態です。

裏を返すと、Cで殴りたいプレイヤーはY型（C159＋ひでり）を選んでおり、X型は「**積み技で隙を作って自分が積み、A130＋かたいツメで物理崩し**」という1つの戦略に絞られた構築になっています。Y型の特殊技プール（ソーラービーム・オーバーヒート等）と完全に役割が分かれているため、対策側は「リザードン＝Y型の特殊エース」と決め打ちすると、X型の物理積みに崩されるリスクを常に抱えることになります。

---

## まとめ

メガリザードンXはM-2シーズンで全リザードン採用の34.9%を占める、**物理崩し特化のメガ進化アタッカー**です。

- **かたいツメ×りゅうのまい**の組み合わせは積み1回でA・Sともに×1.5となり、環境上位の大半を上から叩ける範囲が一気に広がる
- ほのお/ドラゴンのタイプ複合で**4倍弱点が存在しない**ことは安定感に直結
- こうげき130・とくこう130の**両刀ポテンシャル**が相手の対策を難しくする
- ステロ（ステルスロック）は1/4ダメージで大きな痛手→**ステロ対策ポケモンとセット**が前提

メガリザードンY（63.6%）の方が採用率は高いですが、**相手の特殊受け（HD振り）を物理で崩したい・積みエースで対戦を決めたい**という戦略なら、Xを選ぶ明確な理由があります。パーティ全体での弱点補完を意識して構築してみてください。
