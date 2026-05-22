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

## データソース
- Smogon Usage Stats
- VGC大会リザルト
- Pokémon Showdown

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
