# ポケナビ プロジェクトルール

## 概要
ポケモン対戦データ分析サイト「ポケナビ」（https://pokenavi.jp）
VGC・ランクマッチ対戦勢 + DS学習者向け。月10万円不労所得が目標。

## 技術スタック
- **フレームワーク**: Astro v6（MDX、sitemap統合）
- **ホスティング**: Cloudflare Pages（GitHub Actions経由でデプロイ）
- **フォント**: Atkinson（ローカル配置）
- **サイトURL**: https://pokenavi.jp

## ディレクトリ構成
```
src/
├── assets/          # 画像・フォント
├── components/      # Astroコンポーネント
├── content/blog/    # ブログ記事（Markdown/MDX）
├── layouts/         # ページレイアウト
├── pages/           # ルーティング
└── styles/          # グローバルCSS
```

## コンテンツ規約
- ブログ記事は `src/content/blog/` に Markdown で追加
- ファイル名: `{pokemon-name}-analysis.md`（ハイフン区切り、英語）
- フロントマターに `title`, `description`, `pubDate`, `heroImage` を含める
- 記事はポケモン対戦の分析視点で書く（使用率・型・メタへの影響など）
- **公開（`draft: false` に変更）する際は、`pubDate` を必ず公開当日の日付に更新する**（執筆日のまま古い日付で公開しない）

## 記事執筆ガイドライン

### 画像ファイル番号
記事内の画像パスは以下の番号に従う。間違えると画像が表示されない。

**タイプ画像** `/images/types/type-XX-typename.png`
| 番号 | タイプ | 番号 | タイプ |
|------|------|------|------|
| 00 | ノーマル | 09 | ほのお |
| 01 | かくとう | 10 | みず |
| 02 | ひこう | 11 | くさ |
| 03 | どく | 12 | でんき |
| 04 | じめん | 13 | エスパー |
| 05 | いわ | 14 | こおり |
| 06 | むし | 15 | ドラゴン |
| 07 | ゴースト | 16 | あく |
| 08 | はがね | 17 | フェアリー |

**ポケモン画像** `/images/pokemon/pokemon-XXXX-00.webp`
- 番号は全国図鑑番号4桁（例：ゲンガー=#094 → `pokemon-0094-00.webp`）
- メガ進化フォームも `-00`（メガ専用の別ファイルは存在しない）
- 使用する前に `public/images/pokemon/` に実際にファイルが存在するか確認する
- 存在しないファイルを参照する場合は img タグを除去してテキストのみにする

**種族値バー（合計行）**
- 合計値の span には必ず `min-width:40px;white-space:nowrap` を指定する（3桁数値が改行されるのを防ぐ）
- 例: `<span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">580</span>`

**メガシンカ種族値バー（差分表示）**
- 実数値（`width:32px`固定）と差分（`width:40px`固定）を**必ず別 span** にする。同じ span に入れると実数値カラムがずれる
- 差分なし: `<span style="width:32px;text-align:right">78</span><span style="width:40px"></span>`
- 差分あり（増加）: `<span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+46</span>`
- 差分あり（減少）: `<span style="width:32px;text-align:right">92</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#dc2626">-10</span>`
- 合計行も同様に2 span構成: `<span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">700</span><span style="width:40px"></span>`
- generate_pokemon_pages.py の `generate_mega_section()` が自動処理するため、スクリプト経由で生成したページは修正不要。garchomp.md のみ手動管理

### 事実確認
- タイプ・技・特性は必ず正確に記載する（例：アーマーガアは はがね/ひこう、でんきではない）
- ステータス記号: A=こうげき、B=ぼうぎょ、C=とくこう、D=とくぼう、S=すばやさ、H=HP。**略称は必ず大文字**（AS+H、HBS等。「h」「s」など小文字は不可）
- **努力値ではなく「EV」と表記する**。チャンピオンズでは各ステータスのEVは**最大32スケール**（旧作の252ではない）。「252振り」「努力値252」等の旧表記は使わず、`pokemon_evs` テーブルの実値（ev_h〜ev_s、0〜32）で記載する（例：「A252 S252」→「A32 S32」）
- 技の追加効果も正確に（例：アクアブレイクはBダウン、Dダウンではない）
- 「STAB」は使わず「タイプ一致補正」または「一致技」と書く
- 「上から倒す」「先制できる」の記述は対象ポケモンのSと比較してから書く（例：メガスターミーS120より遅いポケモンを「上から倒せる」と書かない）
- メガ進化タイプ変化による耐性変化を正確に記述する。「無効→等倍」になっても「弱点になる」とは書かない（例：ギャラドスのじめん無効→等倍は「2倍弱点」ではなく「等倍で通る」）
- 「〇〇対策」と書く前にタイプ相性を確認する。逆方向の誤りに注意（例：あくタイプはフェアリーに×2弱点なのでフェアリー対策にならない）
- **複合タイプの相性は2タイプの倍率を必ず掛け合わせて計算する**（例：こおり技はドラゴンに×2だが、ほのお/ドラゴンのメガリザードンXには ×0.5×2=等倍。単タイプの倍率で断定しない）
- **特性を「固有」「専用」と書く前に他の所持ポケモンを確認する**（例：きもったまはガルーラ・ヒスイジュナイパーも持つので固有ではない）
- **「最速」「最高威力」「唯一」など最上級・断定表現は、必ず環境データ・全数値を確認してから使う**。確認できなければ「トップクラス」「高水準」等に留める（例：メガミミロップS135はメガゲッコウガS142がいるため「最速」ではない／インファイト威力120はとびひざげり130より低いので「最高威力」ではない）
- **使用率順位・採用率・実数値は本文・表・見出しで一貫させる**。推定値を書く場合は「推定」と明記し、根拠のない数字を置かない
- **先制技（ねこだまし・マッハパンチ等）の先手はSと無関係**。「Sが高いから先制技で先手」とは書かない（優先度で動く）
- **ねこだましは「場に出た最初のターンのみ使用可能」**。「相手が交代すると効かない」は誤り（交代先にも当たる）。制約を書くなら正しく書く
- **じめん技・割合ダメージ技などHP割合系の効果に「H振りで対策」と書かない**（ステルスロックは最大HP比のダメージなのでH振りで軽減されない）

### 文章スタイル
- 自明な情報は書かない（「1試合に1体しかメガ進化できない」「メガ進化枠を消費するため他のポケモンはメガ石を使えない」等のメガ全般に言えるルール説明、「メガ石採用率がほぼ100%」等の当然の帰結、「Lv50」等の競技で一律の前提条件）
- 過剰・不正確な表現を避ける（「完全支配」→「圧倒的な〜」、「この戦略の恐ろしさは」→「この戦略のポイントは」）
- 採用率がない技・型のデメリットをわざわざ強調しない（例：物理技しか採用されていないのに「特殊技が使えないデメリット」を言及しない）
- 採用率の低い技・戦略を「最大の特徴」「最強ギミック」として取り上げない（例：採用率30%の技を「最大の武器」と書かない）
- 「〇〇タイプとの使い分け」は採用実績のある技・型が複数ある場合のみ書く
- 文脈から突然無関係なポケモンを挿入しない
- 「マッチアップ」は使わず「有利なポケモン」「苦手なポケモン」と書く
- 「純〇〇型」の「純」は不要。「積み型」「耐久型」で十分
- 型ごとの弱みはその型に固有の弱点を書く（他の型にも共通する弱点を特定型の弱みとして書かない）。**技固有の性質（とびひざげりの反動等）も型の弱みに混ぜない**
- 型の強み・弱みは**他の型との対比で具体的に書く**（例：「ようき型はいじっぱり型では抜けないS192のマスカーニャを抜ける」「いじっぱり型はA実数値が約10%高く、ようき型で2発の相手を1発で倒せる」）。「価値が最大化」等の何と比べているか不明な表現は使わない
- 「〜の全て」「〜全て」はタイトルに使わない（仰々しい）。代わりに「採用率と立ち回り」「型別解説」など具体的な表現を使う
- **攻撃側の話と防御側（被弾）の話を混在させない**。「このポケモンの弱点」を語る節に、こちらの攻撃が通る話を入れない
- **苦手なポケモンには使用率圏内（TOP50目安）の実在ポケモンのみ挙げる**。圏外ポケモンを天敵として挙げない
- **「苦手な理由」は対象固有の事情を書く**。「かくとう等倍止まり」「弱点を突かれる」など多くのポケモンに当てはまる汎用的理由を個別の苦手理由にしない（例：かくとうを半減し高耐久でこちらの有効打が乏しい、など踏み込んで書く）
- **日本語の同義反復・違和感を避ける**（「上から動かれると先制を取られる」は重複、「攻撃後に自分が引っ込む」→「攻撃後に交代できる」）
- 冗長で自明な箇条書き例示を並べない（タイプ相性表から自明に導ける内容を1件ずつ列挙しない）

### 環境知識（ポケモンチャンピオンズ）
- 現在実装されていないポケモンは言及しない（例：ラグラージは未実装）
- 現環境で実態のない戦略を採用理由にしない（例：フィールド展開ポケモンがほぼいないのに「フィールドメタ」として紹介しない）
- 「〇〇タイプ全般」と書く場合は現環境の実在ポケモンで具体例を挙げる

### データ分析セクション（必須）
本サイトの差別化ポイントは「データサイエンスによる徹底分析」。毎記事に必ず以下のいずれかを1つ以上含めること。

- **シーズン比較**: M-1→M-2などの技採用率・使用率の変化を表で示し、「なぜ変化したか」を考察する
- **カバレッジ計算**: タイプ相性×環境上位ポケモンへの効果倍率を一覧化し、技選択の合理性を定量的に示す
- **採用率の逆説**: 「広く語られる特徴」と「実際の採用率」のギャップを数値で示す（例：みちづれ30%なのに「道連れが最強特徴」と語られる）
- **同居率ネットワーク**: 同居率上位ポケモン同士の関係からチームアーキタイプを識別する

**ルール**:
- 「強い」「弱い」の評価は必ず数値（採用率・使用率・ダメージ倍率等）を根拠にする
- 感覚論で書けることをわざわざ書かない。データからしか言えないことを書く
- 分析セクションの見出しは「## データ分析①：〇〇」形式で番号を振る

### データ根拠
- 確定一発等の計算は使用率上位の実際の性格・努力値振りで行う（計算方法は `florette-analysis-m2.md` に準拠）
- パートナー・同居ポケモンの紹介は `champs.pokedb.tokyo` の同居率データに基づく
- メガ進化パートナーはメガ石採用率データで裏付ける（採用率が低い場合は断定しない）
- 「〇〇と相性が良い」と断定する場合は同居率データを根拠にする

### SEO
- **title**: 「【ポケモンチャンピオンズ】[ポケモン名] 考察 M-X シーズン [特徴的なキーワード]」形式。検索意図に合わせてキーワードを前半に置く
- **description**: 120〜160文字。「使用率〇位」「採用率〇%」等の数値を含め、記事の価値が伝わるよう書く。キーワードを自然に含める
- **見出し（H2/H3）**: 「[ポケモン名]」「M-[X]」「使用率」「考察」等のキーワードを見出しに自然に含める。検索者が知りたいことを見出しで表現する
- **内部リンク**: 記事末尾または本文中に、関連する他の考察記事へのリンクを1〜3件入れる。アンカーテキストはキーワードを含める
- **画像altテキスト**: heroImageのaltには「[ポケモン名]（M-[X]）」等の説明を設定する。記事内の個別ポケモン画像のaltはそのポケモン名にする

## データソース
- ポケモンチャンピオンズ使用率・同居率: https://champs.pokedb.tokyo
- ランキング補助: https://gamewith.jp/pokemon-champions/
- Smogon Usage Stats（参考）

## データ取得ルール
- 使用率・採用率・同居率データはクロール済みDBに保存されているため、ポケモン情報ページ（`src/content/pokemon/`）作成時は**ソースサイトへのアクセス不要**
- チームメイト（同居率TOP10）の順位は**同居率順位**で表示する（使用率順位ではない）
- DBにないデータが必要な場合のみ、ユーザーに確認してからアクセスする

## ポケモン情報ページ作成手順

テンプレートは `src/content/pokemon/garchomp.md`。以下の手順で作成する。

### ステップ1: DBからデータを取得（全て `scripts/pokenavi.db`）

`SEASON`・`POKEMON` を置換して実行。最新クロール日は `MAX(crawled_date)` で自動取得。

```bash
# 使用率・pokemon_id（画像ファイル名の元）
sqlite3 scripts/pokenavi.db "
SELECT rank, pokemon_id, usage_rate
FROM pokemon_usage
WHERE season='M-2' AND rule='single' AND pokemon='POKEMON'
  AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_usage WHERE season='M-2' AND rule='single');"

# 集計日（ページ表示用）
sqlite3 scripts/pokenavi.db "SELECT MAX(crawled_date) FROM pokemon_moves WHERE season='M-2' AND rule='single' AND pokemon='POKEMON';"

# 技TOP10
sqlite3 scripts/pokenavi.db "
SELECT rank, move, usage_rate FROM pokemon_moves
WHERE season='M-2' AND rule='single' AND pokemon='POKEMON'
  AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_moves WHERE season='M-2' AND rule='single' AND pokemon='POKEMON')
ORDER BY rank LIMIT 10;"

# 持ち物TOP10
sqlite3 scripts/pokenavi.db "
SELECT rank, item, usage_rate FROM pokemon_items
WHERE season='M-2' AND rule='single' AND pokemon='POKEMON'
  AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_items WHERE season='M-2' AND rule='single' AND pokemon='POKEMON')
ORDER BY rank LIMIT 10;"

# 特性
sqlite3 scripts/pokenavi.db "
SELECT rank, ability, usage_rate FROM pokemon_abilities
WHERE season='M-2' AND rule='single' AND pokemon='POKEMON'
  AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_abilities WHERE season='M-2' AND rule='single' AND pokemon='POKEMON')
ORDER BY rank LIMIT 5;"

# 性格TOP10
sqlite3 scripts/pokenavi.db "
SELECT rank, nature, usage_rate FROM pokemon_natures
WHERE season='M-2' AND rule='single' AND pokemon='POKEMON'
  AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_natures WHERE season='M-2' AND rule='single' AND pokemon='POKEMON')
ORDER BY rank LIMIT 10;"

# ステータス振りTOP10（H/A/B/C/D/S数値付き）
sqlite3 scripts/pokenavi.db "
SELECT rank, ev_spread, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, usage_rate FROM pokemon_evs
WHERE season='M-2' AND rule='single' AND pokemon='POKEMON'
  AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_evs WHERE season='M-2' AND rule='single' AND pokemon='POKEMON')
ORDER BY rank LIMIT 10;"

# チームメイトTOP10（pokemon_id付き）
sqlite3 scripts/pokenavi.db "
SELECT p.rank, p.partner, u.pokemon_id
FROM pokemon_partners p
LEFT JOIN pokemon_usage u
  ON u.pokemon=p.partner AND u.season=p.season AND u.rule=p.rule
  AND u.crawled_date=(SELECT MAX(crawled_date) FROM pokemon_usage WHERE season='M-2' AND rule='single')
WHERE p.pokemon='POKEMON' AND p.season='M-2' AND p.rule='single'
  AND p.crawled_date=(SELECT MAX(crawled_date) FROM pokemon_partners WHERE season='M-2' AND rule='single' AND pokemon='POKEMON')
ORDER BY p.rank;"
```

### ステップ2: ポケモン画像

`pokemon_usage.pokemon_id` の値（例：`0445-00`）を使い `/images/pokemon/pokemon-0445-00.webp` を参照。
**記憶で図鑑番号を決めつけない**。JOINでpokemon_idがNULLになった場合（名前表記ゆれ）は以下で確認：

```bash
ls public/images/pokemon/ | grep "DEXNUMBER"
# または usage テーブルで名前を検索
sqlite3 scripts/pokenavi.db "SELECT pokemon, pokemon_id FROM pokemon_usage WHERE pokemon LIKE '%NAME%' AND season='M-2' AND rule='single' LIMIT 5;"
```

ファイルが存在しない場合は img タグを除去してテキストのみ表示（CLAUDE.md 基本ルール準拠）。

### ステップ3: 技のタイプアイコン

タイプ画像は `/images/types/type-XX-name.png`（番号表は CLAUDE.md 上部を参照）。
技のタイプはゲーム知識から判断し、正確に記載すること。

### ステップ4: 持ち物アイコン

**個別PNGが存在するもの**（`public/images/items/` にある7件）:
| ファイル名 | 持ち物 |
|---|---|
| item-0157-ram.png | ラムのみ |
| item-0158-obon.png | オボンのみ |
| item-0188-yache.png | ヤチェのみ |
| item-0197-haban.png | ハバンのみ |
| item-0275-tasuki.png | きあいのタスキ |
| item-0287-scarf.png | こだわりスカーフ |
| item-0683-garchompite.png | ガブリアスナイト（他メガ石も同様） |

**上記以外は全てスプライトシートを使用**：
```bash
# アイテム番号を item-sprite.css から検索（アイテム番号を知っている場合）
python3 -c "
import re, sys
css = open('public/images/items/item-sprite.css').read()
num = sys.argv[1]  # 例: '0234'
m = re.search(r'--item-' + num + r':([^;]+)', css)
print(m.group(1) if m else 'NOT FOUND')
" 0234
```

スプライトの表示HTML（24px）:
```html
<!-- position の値 = CSS変数の値 × 0.375 -->
<span style="display:inline-block;width:24px;height:24px;background-image:url('/images/items/item-sprite.png');background-size:480px 648px;background-position:Xpx Ypx;flex-shrink:0"></span>
```

主要アイテムのスプライト位置（24px換算済み）:
| 持ち物 | X | Y |
|---|---|---|
| たべのこし | -288 | -192 |
| ひかりのこな | -384 | -168 |
| やわらかいすな | -360 | -192 |
| こだわりメガネ | -216 | -264 |
| こだわりはちまき | -192 | -264 |
| いのちのたま | 0 | -192 |

新しいアイテムのスプライト位置が必要な場合は、アイテム番号をCSSから調べて × 0.375 で換算する。

### ステップ5: 名前表記ゆれへの注意

`pokemon_partners` と `pokemon_usage` で名前が一致しないケースがある（例：フラエッテ(えいえん)↔フラエッテ:永遠）。
JOINでpokemon_idがNULLになった場合は次で確認：

```bash
sqlite3 scripts/pokenavi.db "SELECT DISTINCT pokemon, pokemon_id FROM pokemon_usage WHERE season='M-2' AND rule='single' AND pokemon LIKE '%NAME%';"
```

## 収益モデル
- 月次分析レポート販売（デジタル商品）
- データ分析ツールのサブスク（将来）
- アフィリエイト（`AffiliateProducts.astro` コンポーネント）

## シミュレーター開発ルール（scripts/simulator/）

### 「仕様に反映した」の定義
**以下の3つが揃って初めて「実装完了」とみなす。1つでも欠けていたら未完了。**

1. **REQUIREMENTS.md に記載** — 仕様（動作・フラグ・効果）が文書化されている
2. **実装** — コード・DBに反映されている
3. **テスト** — `scripts/tests/test_all.py` にテストが追加され、全件パスしている

作業完了を報告する前に必ずこの3点を自己チェックすること。

### わざ追加・修正時のチェックリスト
- [ ] DB更新（`move_master`）
- [ ] フラグリスト更新（`_NON_CONTACT_PHYSICAL` / `SLICING_MOVES` / `SOUND_MOVES` 等）
- [ ] 追加効果更新（`battle.py`の`STATUS_EFFECTS`辞書・`DEF_DOWNS`・`SELF_BOOSTS`等）
- [ ] `python3 scripts/simulator/generate_appendix_a.py` 実行（`appendix_a.md` 再生成）
- [ ] REQUIREMENTS.md 付録A を再生成した `appendix_a.md` で置き換え・技数更新
- [ ] REQUIREMENTS.md の付録A以外のセクション（特性・持ち物等）も必要に応じて更新
- [ ] DBの`effect_text`に仕様を記載（これが全技テストの生成元）
- [ ] `python3 scripts/tests/generate_move_tests.py` で全技テスト再生成
- [ ] `python3 scripts/tests/test_move_effects.py` 全件パス確認（自動生成の全技仕様テスト）
- [ ] `python3 scripts/tests/test_all.py` 全件パス確認（コア機能の回帰テスト）
- [ ] **盲点チェック**: 下記スクリプトで「固有仕様ありだがテスト無し」の技が増えていないか確認

### 全技テストの仕組みと現状（重要）
- `scripts/tests/test_move_effects.py` は **DBの`effect_text`から自動生成** される全技仕様テスト（generate_move_tests.pyが生成）
- **盲点ゼロ達成済み（HARD/SOFT両方）**: effect_textの各仕様が、その仕様を狙ったテストで検証されている
  - HARD盲点 = 仕様に対しチェックが一切ない
  - SOFT盲点 = 汎用「副作用発現」のみで狙った検証がない
- 対応済みパターン: 状態異常%/100%、ひるみ%、相手能力ダウン(命中率/回避率含む)、自己能力変化(複数stat・上下・確率・溜めターン)、状態異常付与(変化技)、回復、天候、スクリーン展開/破壊、一撃必殺、ドレイン、バインド、あばれ、じごくづき、外れ自傷、2ターン溜め、効果バツグン上書き、反動、多段ヒット、必中、必中急所、固定ダメージ、ピボット交代、自己ひんし、ハザード設置(変化/ダメージ技)、フィールド、カウンター反射、たくわえ系、個別特例(のろい/あくび/ほおばる/いやしのねがい/キングシールド)
- **検証の強度に注意**: 汎用「副作用発現」チェックは「何かが変わった」だけの弱い検証。深い監査(deep_audit.py)はこれを SOFT盲点 として検出する
- **保証の前提**: effect_textが正確 かつ generate_move_tests.pyにパターンがあること。新しい効果表現の技を追加したら、まずパターン対応を確認し、無ければ`generate_move_tests.py`に追加する
- **注意**: 「優先度だけ当たって本体未検証」「ダメージ>0だけで特殊効果未検証」を見逃さないこと（フリーズドライ/ミラーコートで実際に起きた）

**盲点の定量チェック（技追加後に必ず実行）:**
```bash
python3 scripts/tests/generate_move_tests.py   # 全技テスト再生成
python3 scripts/tests/test_move_effects.py      # 全件パス確認
python3 scripts/tests/deep_audit.py             # 未分類/SOFT/弱いテスト が全て0であること
python3 scripts/tests/test_all.py               # コア回帰
```
`deep_audit.py` は effect_textから各仕様を抽出し、対応する狙ったテストがあるかを照合する。3つの観点を出力:
- **未分類**: 検出器もIGNOREも無い句（=完全な見落とし）
- **SOFT**: 「副作用発現」汎用テストのみで狙った検証が無い句
- **弱いテスト**: 多段技に「複数回ヒット検証」が無い／可変威力ダメージ技に条件比較テストが無い（`dmg>0`だけ）＝**ネズミざん型の漏れ**を構造的に検出。さらに**DB威力が固定値なのに`_effective_power`内で条件付き倍率（×2/×1.5/÷2）がかかる技**（やけっぱち型）に具体値テストが無い場合も検出（gate L。やけど依存と誤実装していたやけっぱちを取り逃した穴を塞ぐもの）。**generate_move_tests.pyの重複elif分岐**（同じ技名が2つ以上の`elif name==`/`in(...)`条件に現れ後続がデッドコード化＝テスト無言消失）も検出（gate M）。**条件付き(トリガー型)効果**（「効果A、ただし条件を満たすとB」）でBのpositiveのみ書きAのnegative（条件不成立）を書き忘れる漏れ（とどめばり型）も検出（gate N。所持条件「持っていない場合」等も対象）。**「A状態・B状態…のいずれかにする」型**で1状態しか発生検証していない漏れ（フェイタルクロー型）も検出（gate O）。なお gate L は乗算倍率だけでなく加算/式（おはかまいり=50+50×ひんし数 等）の固定威力技も対象。**「失敗/無効」negativeテストが意図した条件でなくタイプ無効(0倍)で偽成立していないか**（ダメージ技で相手HP不変=失敗と主張するテストが、実は相性0倍で常にダメ0なだけ＝ポルターガイスト型）も検出（gate P）。**2ターン技で「天候で即攻撃」例外があり使ったターンに能力上昇する技**で、溜め時だけ副次効果を検証し即攻撃時の検証が漏れる片側漏れ（エレクトロビーム型）も検出（gate Q）。**複合効果の専用テスト要求**（gate R＝フォルムチェンジ「フォルム」検証／引き継ぎ「引き継」検証／天候別回復の全分岐2/3・1/4検証）。gate N は「しか使えない／場合にしか使える」等の使用条件negativeも対象。**【一般化】gate S**＝effect_textに条件表現（`場合`/`ていれば`/`しか`/`限り`/`でないと`等）を含む句があれば、分岐検証の痕跡（負例マーカー or 本体チェック2個以上）を要求する。マーカー列挙(gate N)で拾えない条件表現も対象にする汎用ゲート。ダブル前提句（`味方`/`2匹`/`それぞれ`/`全体`）と文書化stub（まねっこ）は除外。「とき/時」は「その時に」等の参照表現を誤検出するため対象外。**ハザード設置テストの厳密性**（gate T＝まきびし/どくびし/ねばねばネット等の設置技テストが自分のハザード属性のみを判定し、`stealth_rock_set`等の他ハザードフラグをOR混入して別ハザードで偽成立していないか。ステルスロックはrun時確定許容のため対象外）。**入替(スワップ)技の双方向検証**（gate U＝パワースワップ/ガードスワップ/スキルスワップ/スピードスワップ等が自分・相手の両方の入替を検証しているか。片側のみ＝「コピー」でも偽成立する漏れを検出。道具入替・場所入替は別系統で除外）。**列挙マッピングの全件検証**（gate V＝「天候A：タイプX、天候B：タイプY…」のようにN個の対応を列挙する句で全対応を検証しているか。gate Oの一般化でウェザーボール型の部分被覆を検出）
3つとも0でなければ generate_move_tests.py にパターン追加または実装修正が必要。
**注意**: ラベルには技名が含まれるため、検出器の期待語に技名だけを使うと誤検証になる（`verify_labels()`が技名・ボイラープレートを除外して判定する）。新規検出器の期待語は技名でなく「効果を表す語」にすること。

### テスト方針
テストファイル: `scripts/tests/test_all.py`（`python3 scripts/tests/test_all.py` で実行）

**以下のいずれかに該当する変更は、指摘なしでテストを追加する:**

- わざをDBに追加・修正した場合
  - DB属性（type, category, power, pp, accuracy）の正しさを確認するテスト
  - 可変威力技（power=NULL）は威力計算が正常に動作するテスト
  - 物理技は接触・非接触の分類が正しいかテスト
- 特性・持ち物の効果を追加・修正した場合
  - 効果が発動する/しないケースを各1件以上
- バトルロジックを変更した場合
  - 変更した動作の正常ケース・境界ケース

### テスト実装の原則
- `dmg()` は命中判定をスキップするためダメージ計算テストに使う（`execute()` は命中率が絡む）
- 速度・重さなど数値依存の威力計算は `pokemon.speed` 等を直接書き換えて比率を確定させる
- 新規技のダメージテストは STAB・タイプ相性で倍率がかかる組み合わせを選ぶ

### REQUIREMENTS.md の確認ルール
- 「appendixでは正しい」と言う場合は、生成スクリプトの stdout ではなく **ファイルの内容** を確認してから言う

## 開発コマンド
```bash
npm run dev      # 開発サーバー起動
npm run build    # ビルド
npm run preview  # ビルド確認
```
