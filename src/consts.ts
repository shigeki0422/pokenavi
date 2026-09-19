// Place any global data in this file.
// You can import this data from anywhere in your site by using the `import` keyword.

export const SITE_TITLE = 'ポケナビ';
// 1v1事前計算（builder-data）が対象とするシーズン。scripts/gen_builder_data.py の BUILDER_SEASON と揃える
export const MATCHUP_SEASON = 'M-6';
// シーズン名は入れない（固定値だと更新のたびに検索結果の説明文が古いまま残る）。
// トップページはsrc/pages/index.astroでranking.jsonの最新シーズンを差し込む。
export const SITE_DESCRIPTION = 'ポケモンチャンピオンズの使用率・勝率・パーティ構成をデータで分析。対戦シミュレーターとパーティ提案で最新環境を攻略。';
