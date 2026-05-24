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
- 技の追加効果も正確に（例：アクアブレイクはBダウン、Dダウンではない）
- 「STAB」は使わず「タイプ一致補正」または「一致技」と書く
- 「上から倒す」「先制できる」の記述は対象ポケモンのSと比較してから書く（例：メガスターミーS120より遅いポケモンを「上から倒せる」と書かない）
- メガ進化タイプ変化による耐性変化を正確に記述する。「無効→等倍」になっても「弱点になる」とは書かない（例：ギャラドスのじめん無効→等倍は「2倍弱点」ではなく「等倍で通る」）
- 「〇〇対策」と書く前にタイプ相性を確認する。逆方向の誤りに注意（例：あくタイプはフェアリーに×2弱点なのでフェアリー対策にならない）

### 文章スタイル
- 自明な情報は書かない（「1試合に1体しかメガ進化できない」「メガ進化枠を消費するため他のポケモンはメガ石を使えない」等のメガ全般に言えるルール説明、「メガ石採用率がほぼ100%」等の当然の帰結、「Lv50」等の競技で一律の前提条件）
- 過剰・不正確な表現を避ける（「完全支配」→「圧倒的な〜」、「この戦略の恐ろしさは」→「この戦略のポイントは」）
- 採用率がない技・型のデメリットをわざわざ強調しない（例：物理技しか採用されていないのに「特殊技が使えないデメリット」を言及しない）
- 採用率の低い技・戦略を「最大の特徴」「最強ギミック」として取り上げない（例：採用率30%の技を「最大の武器」と書かない）
- 「〇〇タイプとの使い分け」は採用実績のある技・型が複数ある場合のみ書く
- 文脈から突然無関係なポケモンを挿入しない
- 「マッチアップ」は使わず「有利なポケモン」「苦手なポケモン」と書く
- 「純〇〇型」の「純」は不要。「積み型」「耐久型」で十分
- 型ごとの弱みはその型に固有の弱点を書く（他の型にも共通する弱点を特定型の弱みとして書かない）
- 「〜の全て」「〜全て」はタイトルに使わない（仰々しい）。代わりに「採用率と立ち回り」「型別解説」など具体的な表現を使う

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

## 開発コマンド
```bash
npm run dev      # 開発サーバー起動
npm run build    # ビルド
npm run preview  # ビルド確認
```
