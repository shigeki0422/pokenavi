// 日次Champions OCRワークフロー テンプレート
// 使い方: CRAWL_DATE と TOTAL_RANKS を変更してWorkflowに貼り付け
// 事前に crop_panels.py を実行してからこのWFを使う

export const meta = {
  name: 'champions-ocr-YYYY-MM-DD',
  description: 'Champions使用率詳細OCR',
  phases: [{ title: 'OCR' }],
}

const CRAWL_DATE = 'YYYY-MM-DD'
const CRAWL_DIR = `/tmp/champ_crawl_${CRAWL_DATE}`
const TOTAL_RANKS = 200

const ranks = Array.from({length: TOTAL_RANKS}, (_, i) => i + 1)

const SCHEMA = {
  type: 'object',
  required: ['rank', 'pokemon', 'pokemon_types', 'moves', 'items', 'abilities', 'natures', 'evs', 'partners'],
  properties: {
    rank: { type: 'integer' },
    pokemon: { type: 'string' },
    pokemon_types: { type: 'array', items: { type: 'string' }, description: 'ヘッダーのタイプアイコンから読んだタイプ（例: ["みず","エスパー"]）' },
    moves: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, rate: { type: 'number' } }, required: ['name','rate'] } },
    items: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, rate: { type: 'number' } }, required: ['name','rate'] } },
    abilities: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, rate: { type: 'number' } }, required: ['name','rate'] } },
    natures: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, rate: { type: 'number' } }, required: ['name','rate'] } },
    evs: { type: 'array', items: { type: 'object', properties: { h: {type:'number'}, a: {type:'number'}, b: {type:'number'}, c: {type:'number'}, d: {type:'number'}, s: {type:'number'}, rate: {type:'number'} }, required: ['h','a','b','c','d','s','rate'] } },
    partners: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' } }, required: ['name'] } },
  }
}

phase('OCR')

const results = await pipeline(
  ranks,
  async (rank) => {
    const dir = `${CRAWL_DIR}/detail/${String(rank).padStart(3,'0')}`
    return await agent(
      `ポケモンチャンピオンズ 使用率ランキング ${rank}位の詳細データをOCRしてください。

画像ディレクトリ: ${dir}

以下のクロップ済みファイル（_c_プレフィックス）をReadツールで読み込んでOCRしてください：
- _c_move_00.png, _c_move_01.png（存在する場合）: 技使用率
- _c_item_00.png, _c_item_01.png（存在する場合）: 持ち物使用率
- _c_ability_00.png: 特性使用率
- _c_nature_00.png, _c_nature_01.png（存在する場合）: 性格使用率
- _c_ev_00.png〜_c_ev_07.png（存在する場合）: 努力値配分
- _c_partner_00.png, _c_partner_01.png（存在する場合）: パートナーポケモン（名前のみ）

【ルール】
- **pokemon** と **pokemon_types** は必ず **_c_ability_00.png のヘッダー部分**（画面上部のピンク/白帯）から読む
  - ヘッダーには「スプライット画像 / No.XXX / ポケモン名 / タイプアイコン」が横並びで表示されている
  - pokemon: ヘッダーのテキスト名をそのまま返す（OCR補正・推測禁止）
  - pokemon_types: ヘッダー右端のタイプアイコンをすべて読む（例: ["みず","エスパー"]）
  - スプライット色・タイプ数・タイプの組み合わせはリージョンフォルム判定の根拠になる。必ず正確に読むこと
- 使用率は0〜100のパーセント値（小数あり）
- 画像が真っ黒・空白の場合はそのカテゴリを空配列[]に
- 各リスト内で同じ名前が重複しないこと
- EVは {h,a,b,c,d,s,rate} 形式（各値0〜32の整数、合計0〜66）
- パートナーは名前のみ（使用率不要）

【OCR厳守事項 — 違反禁止】
- 画面に表示されている数値・文字を一字一句そのまま返すこと
- 値が「おかしい」と感じても補正・推測・変換を一切行わない
- 合計が64未満・66超・個別値が32超でも、そのまま返す（ゲートはシステム側で行う）
- 技名・アイテム名・ポケモン名のスペルを「知っている正しい名前」に変えない
- バーの長さから値を推測しない。必ず表示されている数字テキストを読む

rank=${rank} として structured output で返してください。`,
      { label: `rank=${rank}`, phase: 'OCR', schema: SCHEMA, model: 'haiku' }
    )
  }
)

return results.filter(Boolean)
