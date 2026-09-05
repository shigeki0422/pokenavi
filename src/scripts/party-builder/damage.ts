// ダメージ計算・1v1判定用の実ダメージ計算。
// 移植元: scripts/simulator/damage.py の calc_damage() / _effective_move_type() / _effective_power() /
//         _apply_attacker_item() / _apply_defender_item() / _apply_attacker_ability() / _apply_defender_ability()
//         scripts/simulator/abilities.py の check_move_immunity() / scrappy_override() / should_ignore_ability()
//
// 移植範囲は scripts/_explain.py の _mu_score() が実際に通るコードパスのみ（フル移植はしない）。
// _mu_score() は BattleField()（天候なし・フィールドなし・じゅうりょくなし）・critical=False・
// フルHP（自分/相手とも常にmax_hpと同値）・能力ランク変化0・状態異常なしの1発だけを評価するため、
// damage.py の以下の分岐は _mu_score の文脈では必ず不発（no-op）になる。実装しない（意図的な省略）:
//   - フィールド（エレキ/グラス/サイコ/ミスト）依存の威力補正 ※BattleField()は常にterrain無し
//   ※天候については当初 BattleField()（weather=None）に合わせて丸ごと省略していたが、実戦の1v1では
//     ひでり/あめふらし/すなおこし/ゆきふらし が場に出た瞬間に必ず発動するため「起こり得ない状態」で
//     評価していた（メガリザードンYの晴れによるほのお技1.5倍が抜け落ちる等）。現在は fieldWeather() で
//     両者の特性から天候を決め、天候補正・雪/砂の防御補正・ソーラービーム半減・すなのちから・
//     サンパワー・ウェザーボールに反映している。天候依存の素早さ上昇（すいすい/ようりょくそ/
//     すながくれ）は effectiveSpeed() が相手情報を持たないため未対応（末尾の未サポート一覧参照）。
//   - 急所関連（critical=Falseで固定）
//   - 能力ランク変化依存の分岐（ランクは常に0＝get_effective_statは素の実数値と同値）
//   - 状態異常依存の分岐（こんじょう/やけど半減/ねつぼうそう/ふしぎなうろこ等。状態異常は常になし）
//   - ひんし数・被弾回数・ターン内フラグ依存（おはかまいり/ふんどのこぶし/じゅうでん/もらいび発動後
//     強化/でんきにかえる/ちいさくなる/半無敵/_acts_second 等）※1回きりの静的評価のため常に初期値
//   - HP満タン前提でのみ判定が変わる「ひんち」補正（もうか/げきりゅう/しんりょく/むしのしらせ）
//     ※_mu_scoreのM/OはHP=max_hp固定のためHP比率は常に1.0＝発動条件を満たさずno-op
// 上記は「builder-dataに特性/持ち物として登場するが、この静的1発評価では効果が出ない」ことを意味する。
// 未サポート一覧は本ファイル末尾のコメントを参照。
import type { ResolvedBuild, ResolvedMove } from "./types";
import { eff } from "./typechart";

// ── 技名の固定集合（damage.py / abilities.py から値を変えずに移植） ──────────────

const SOUND_MOVES = new Set([
  "むしのさざめき", "バークアウト", "ハイパーボイス",
  "なきごえ", "うたう", "ちょうおんぱ", "きんぞくおん",
  "ほえる", "スケイルノイズ", "すてゼリフ",
  "いびき", "いやしのすず", "いやなおと", "うたかたのアリア",
  "おたけび", "さわぐ", "とおぼえ", "ばくおんぱ",
  "ぶきみなじゅもん", "ほろびのうた", "みわくのボイス", "りんしょう",
  "サイコノイズ", "ソウルビート", "ドラゴンエール", "フレアソング",
]);

const BALL_BOMB_MOVES = new Set([
  "きあいだま", "タネばくだん", "エレキボール", "エナジーボール",
  "フォーカスブラスト", "シャドーボール", "ヘドロばくだん", "ロックブラスト",
  "タマゴばくだん", "ウェザーボール", "アシッドボム", "アイスボール",
  "どろばくだん", "マグネットボム", "ポレンパフ", "ジャイロボール",
  "かふんだんご", "がんせきほう", "くちばしキャノン", "でんじほう",
  "はどうだん", "みずあめボム", "タネマシンガン",
]);

const PUNCH_MOVES = new Set(["アームハンマー", "スカイアッパー", "アイスハンマー", "ぶちかまし"]);

const SLICING_MOVES = new Set([
  "アクアカッター", "エアスラッシュ", "エアカッター", "がんせきアックス",
  "クロスポイズン", "サイコカッター", "シェルブレード", "シザークロス",
  "シャドークロー", "せいなるつるぎ", "ソーラーブレード", "つじぎり",
  "つばめがえし", "ドゲザン", "ドラゴンクロー", "ネズミざん",
  "ひけん・ちえなみ", "ブレイククロー", "フェイタルクロー",
  "むねんのつるぎ", "リーフブレード",
]);

// かたいツメ判定用「非接触の物理技」集合（damage.py _NON_CONTACT_PHYSICAL をそのまま移植）
const NON_CONTACT_PHYSICAL = new Set([
  "じしん", "マグニチュード", "いわなだれ", "ストーンエッジ", "ロックブラスト",
  "がんせきふうじ",
  "どくびし", "まきびし", "ステルスロック", "ほのおのせんぷうき",
  "だいばくはつ", "じばく", "ボーンラッシュ",
  "ほねブーメラン", "しっぽをふる", "すなかけ",
  "3ぼんのや", "タネマシンガン",
  "うちおとす", "おはかまいり", "かげぬい",
  "がんせきほう", "くちばしキャノン", "こおりのつぶて", "しおづけ",
  "じさくづき", "じならし", "たいあたり", "つららおとし", "つららばり",
  "ひょうざんおろし", "アクアカッター", "オーラぐるま", "サイコカッター",
  "スケイルショット", "スラッシュ", "タネばくだん", "ダストシュート",
  "デカハンマー", "トリックフラワー", "ドラゴンアロー", "フェイント",
  "ポルターガイスト", "ミサイルばり", "Gのちから",
  "うっぷんばらし", "すなじごく", "だいふんげき", "はなふぶき",
  "ふくろだたき", "ゴッドバード",
  "じわれ", "なげつける", "メタルバースト",
  "どくばりセンボン",
]);

// ちからずく判定用「追加効果を持つ技」集合。
// 移植元: scripts/simulator/damage.py _secondary_effect_moves()（DB move_master.effect_textから機械判定）。
// public/builder-data/moves.json（501技）全件についてPython側で同じ判定を実行し、結果を固定値として埋め込んだもの
// （実行時にDBへアクセスできないため）。moves.json の技構成が変わった場合は再生成が必要。
const SECONDARY_EFFECT_MOVES = new Set([
  "ほのおのパンチ", "かみなりパンチ", "れいとうパンチ", "つるぎのまい", "のしかかり", "かみつく", "かえんほうしゃ",
  "ふぶき", "れいとうビーム", "10まんボルト", "かみなり", "サイコキネシス", "こうそくいどう", "ちいさくなる",
  "かげぶんしん", "だいもんじ", "たきのぼり", "ドわすれ", "とける", "いわなだれ", "いびき", "わたほうし",
  "こわいかお", "ヘドロばくだん", "こごえるかぜ", "あまえる", "こうそくスピン", "アイアンテール", "かみくだく",
  "げんしのちから", "シャドーボール", "ねっぷう", "おきみやげ", "じゅうでん", "フェザーダンス", "ブレイズキック",
  "コメットパンチ", "がんせきふうじ", "コスモパワー", "じんつうりき", "てっぺき", "とびはねる", "マッドショット",
  "ボルテッカー", "りゅうのまい", "みずのはどう", "フレアドライブ", "ロックカット", "どくづき", "あくのはどう",
  "エアスラッシュ", "むしのさざめき", "ドラゴンダイブ", "きあいだま", "エナジーボール", "だいちのちから",
  "わるだくみ", "かみなりのキバ", "こおりのキバ", "ほのおのキバ", "しねんのずつき", "ラスターカノン", "ふんえん",
  "きりばらい", "ほうでん", "ダストシュート", "アイアンヘッド", "ヘドロウェーブ", "ニトロチャージ", "アシッドボム",
  "ねっとう", "じならし", "シェルブレード", "エレキネット", "コットンガード", "ナイトバースト", "ぼうふう",
  "ほのおのまい", "つららおとし", "バークアウト", "じゃれつく", "ムーンフォース", "キングシールド", "マジカルフレイム",
  "かいでんぱ", "つぶらなひとみ", "ちからをすいとる", "どくのいと", "とびかかる", "トロピカルキック", "アクアブレイク",
  "ほおばる", "オーラぐるま", "りんごさん", "Gのちから", "シェルアームズ", "はいよるいちげき", "ねっさのだいち",
  "フェイタルクロー", "バリアーラッシュ", "ひょうざんおろし", "たてこもる", "ひゃっきやこう", "3ぼんのや",
  "ルミナコリジョン", "アクアステップ", "フレアソング", "おかたづけ", "とびつく", "くさわけ", "ひやみず",
  "シャカシャカほう", "エレクトロビーム", "きまぐレーザー", "りゅうのいぶき", "かかとおとし", "クロスポイズン",
  "どくどくのキバ", "はがねのつばさ", "ほのおのムチ", "ブレイククロー", "ローキック", "ワイドブレイカー",
  "あまいかおり", "いとをはく", "いやなおと", "うそなき", "おたけび", "きんぞくおん", "くすぐる", "ゴッドバード",
  "せいちょう", "だくりゅう", "たくわえる", "チャージビーム", "トライアタック", "なみだめ", "どろかけ",
  "むしのていこう", "メテオビーム", "ソウルクラッシュ", "どくばりセンボン",
]);

const RECKLESS_MOVES = new Set([
  "すてみタックル", "フレアドライブ", "ボルテッカー", "ウェーブタックル",
  "ダブルエッジ", "ブレイブバード", "ウッドハンマー", "とびひざげり", "とびげり",
]);

const FANG_MOVES = new Set([
  "かみつく", "かみくだく", "かみなりのキバ", "ほのおのキバ", "こおりのキバ",
  "どくどくのキバ", "サイコファング",
]);

// ── 連続技（多段ヒット技） ────────────────────────────────────────────────────
// 移植元: scripts/simulator/battle.py の MULTI_HIT_2 / MULTI_HIT_3 / MULTI_HIT_RANDOM_25。
// 集合の中身は値を変えずにそのまま移植する（Python側を変更したらここも同期する）。

/** 常に2発ヒットする技。 */
export const MULTI_HIT_2 = new Set([
  "ダブルキック", "にどげり", "ダブルウイング", "ドラゴンアロー",
  "スパークリングアリア", "ダブルパンツァー", "ツインビーム", "ダブルアタック",
]);

/** 3発ヒットし、1発ごとに威力が20/40/60と上がる技（トリプルアクセル）。 */
export const MULTI_HIT_3 = new Set(["トリプルアクセル"]);

/** 2〜5発ヒット（スキルリンクなら5発固定）の技。 */
export const MULTI_HIT_RANDOM_25 = new Set([
  "スケイルショット", "みずしゅりけん", "ロックブラスト",
  "タネマシンガン", "つららばり", "ミサイルばり",
  "ボーンラッシュ", "あわ", "スイープビンタ",
]);

/**
 * 静的評価で用いるヒット数。移植元: scripts/simulator/features.py の
 * _expected_frac_calc(multi_hit=True) / _move_frac()。
 * battle.pyの_calc_hits()は2〜5発を乱数([2,3,4,5]重み[3,3,1,1])で決めるが、
 * 静的評価（乱数を持たない1v1判定）ではPython側の features.py と同じく
 * 「スキルリンクなら5発、そうでなければ3発」の決定的な期待値を使う。
 * ネズミざん（1〜10発の連続判定）も features.py 同様に1発として扱う
 * （Python側の静的評価と結果を一致させるため。本ファイル末尾の未サポート一覧参照）。
 */
export function multiHitCount(attacker: ResolvedBuild, move: ResolvedMove): number {
  const n = move.n;
  if (MULTI_HIT_2.has(n)) return 2;
  if (MULTI_HIT_3.has(n)) return 3;
  if (MULTI_HIT_RANDOM_25.has(n)) return attacker.ability === "スキルリンク" ? 5 : 3;
  return 1;
}

const PULSE_MOVES = new Set([
  "はどうだん", "みずのはどう", "あくのはどう", "りゅうのはどう", "いやしのはどう", "だいちのはどう",
]);

// ── 特性・持ち物の固定テーブル（scripts/simulator/damage.py / items.py から移植） ──────

const SKIN_ABILITIES: Record<string, string> = {
  "フェアリースキン": "フェアリー",
  "フリーズスキン": "こおり",
  "エレキスキン": "でんき",
  "スカイスキン": "ひこう",
  "ドラゴンスキン": "ドラゴン",
};

const MOLD_BREAKER_ABILITIES = new Set(["かたやぶり", "ターボブレイズ", "テラボルテージ", "きんぞくおん"]);

// check_move_immunity の「特性 → 無効化するタイプ」対応（IMMUNITY_ABILITIES の type エントリのみ抽出）
const IMMUNITY_TYPE: Record<string, string> = {
  "ふゆう": "じめん",
  "うなぎのぼり": "じめん",
  "ちくでん": "でんき",
  "ちょすい": "みず",
  "もらいび": "ほのお",
  "ひらいしん": "でんき",
  "でんきエンジン": "でんき",
  "こんがりボディ": "ほのお",
  "かんそうはだ": "みず",
  "そうしょく": "くさ",
  "どしょく": "じめん",
};

const TYPE_BOOST_ITEMS: Record<string, [string, number]> = {
  "もくたん": ["ほのお", 1.2],
  "とけないこおり": ["こおり", 1.2],
  "しんぴのしずく": ["みず", 1.2],
  "じしゃく": ["でんき", 1.2],
  "くろいメガネ": ["あく", 1.2],
  "ようせいのハネ": ["フェアリー", 1.2],
  "どくバリ": ["どく", 1.2],
  "やわらかいすな": ["じめん", 1.2],
  "するどいくちばし": ["ひこう", 1.2],
  "シルクのスカーフ": ["ノーマル", 1.2],
  "りゅうのキバ": ["ドラゴン", 1.2],
  "くろおび": ["かくとう", 1.2],
  "まがったスプーン": ["エスパー", 1.2],
  "のろいのおふだ": ["ゴースト", 1.2],
  "メタルコート": ["はがね", 1.2],
  "かたいいし": ["いわ", 1.2],
  "ぎんのこな": ["むし", 1.2],
  "きせきのタネ": ["くさ", 1.2],
};

// タイプ半減きのみ: {きのみ名: 半減するタイプ}
const BERRY_RESIST: Record<string, string> = {
  "オッカのみ": "ほのお",
  "イトケのみ": "みず",
  "ソクノのみ": "でんき",
  "リンドのみ": "くさ",
  "ヤチェのみ": "こおり",
  "ヨプのみ": "かくとう",
  "ビアーのみ": "どく",
  "シュカのみ": "じめん",
  "バコウのみ": "ひこう",
  "ウタンのみ": "エスパー",
  "タンガのみ": "むし",
  "ヨロギのみ": "いわ",
  "カシブのみ": "ゴースト",
  "ハバンのみ": "ドラゴン",
  "ナモのみ": "あく",
  "リリバのみ": "はがね",
  "ロゼルのみ": "フェアリー",
};

export type Weather = "sunny" | "rain" | "sandstorm" | "hail" | null;

/**
 * 登場時に天候を発生させる特性。移植元: abilities.py entry_ability() の WEATHER_MAP。
 * 1v1では両者が場に出た時点で必ず発動するため、_mu_score が BattleField()（天候なし）を
 * 渡していたのは「実戦では起こり得ない状態」の評価だった（メガリザードンYのひでりによる
 * ほのお技1.5倍が丸ごと抜け落ちる等。実際に記事レビューで発覚した）。
 */
const WEATHER_ABILITY: Record<string, Exclude<Weather, null>> = {
  "ひでり": "sunny",
  "あめふらし": "rain",
  "すなおこし": "sandstorm",
  "ゆきふらし": "hail",
};

/**
 * この1v1（両者が場に出ている状態）で成立している場の天候。
 * - ノーてんき（チルタリス等）が居れば天候効果は無効（damage.py effective_weather の
 *   field._weather_negated 相当）。
 * - 双方が天候特性を持つ場合は、後から発動する＝素早さの遅い側の天候が残る（本家準拠）。
 *   battle.py は side1→side2 の固定順で上書きするが、その順序を持ち込むと judge1v1 の
 *   自分視点/相手視点で天候が食い違い判定が非対称になるため、対称なルールを採る。
 *   同速時は種族名の辞書順で固定（決定的にするための便宜）。
 */
// ── 入場時効果（対面した瞬間に必ず起きる） ─────────────────────────────
// 移植元: scripts/simulator/abilities.py entry_ability()。
// これを見ていないと「対戦開始時に必ず起きること」を無視した評価になる。
// 実測でも いかく未考慮により物理技のダメージが34%過大に出ていた
// （サイコファング→ギャラドス 71%(確2) → 47%(確3)）。
const INTIMIDATE_IMMUNE = new Set([
  "クリアボディ", "しろいけむり", "かがくへんかガス",
  "マイペース", "どんかん", "きもったま", "せいしんりょく",
]);
const UNCOPYABLE = new Set(["トレース", "かわりもの", "イリュージョン", "ばけのかわ", "かがくへんかガス"]);

/** 入場時にトレースを解決した後の実効特性。 */
export function entryAbility(me: ResolvedBuild, opp: ResolvedBuild): string {
  if (me.ability === "トレース" && !UNCOPYABLE.has(opp.ability)) return opp.ability;
  return me.ability;
}

/**
 * 相手のいかくを受けた後の自分の攻撃ランク。
 * あまのじゃく持ちは「自分への能力変化」が逆転するので +1 になる（abilities.py と同じ）。
 */
export function entryAtkStage(me: ResolvedBuild, opp: ResolvedBuild): number {
  if (entryAbility(opp, me) !== "いかく") return 0;
  const myAb = entryAbility(me, opp);
  if (INTIMIDATE_IMMUNE.has(myAb)) return 0;
  if (myAb === "あまのじゃく") return 1;
  return -1;
}

export type Terrain = "electric" | "grassy" | "psychic" | "misty" | null;

const TERRAIN_ABILITY: Record<string, Exclude<Terrain, null>> = {
  "エレキメイカー": "electric",
  "グラスメイカー": "grassy",
  "サイコメイカー": "psychic",
  "ミストメイカー": "misty",
};

/**
 * この1v1で成立している場のフィールド。天候と同じく、特性の持ち主が場に出た瞬間に張られる。
 * 環境では メガライチュウX の エレキメイカー のみ（でんき技1.3倍・サーフテールの素早さ2倍）。
 */
export function fieldTerrain(a: ResolvedBuild, b: ResolvedBuild): Terrain {
  const ta = TERRAIN_ABILITY[entryAbility(a, b)] ?? null;
  const tb = TERRAIN_ABILITY[entryAbility(b, a)] ?? null;
  // 対戦本体は side1 → side2 の順に入場処理するので、後入場(b)が上書きする
  return tb ?? ta;
}

export function fieldWeather(a: ResolvedBuild, b: ResolvedBuild): Weather {
  const aa = entryAbility(a, b);
  const ab = entryAbility(b, a);
  if (aa === "ノーてんき" || ab === "ノーてんき") return null;
  const wa = WEATHER_ABILITY[aa] ?? null;
  const wb = WEATHER_ABILITY[ab] ?? null;
  // 対戦本体は side1 → side2 の順に入場処理するので、後入場(b)が上書きする
  return wb ?? wa;
}

/**
 * 実効天候（damage.py effective_weather(field, poke) 相当）。
 * メガソーラー特性の所有者だけはノーてんきより優先して常に"sunny"扱い。
 * 引数のpokeは「その天候判定を必要としている側」(damage.pyの呼び出し規約と同じ:
 * 攻撃側のタイプ変化/威力/ダメージ補正はattacker視点、防御側の耐久補正はdefender視点)。
 */
function effectiveWeather(poke: ResolvedBuild, weather: Weather): Weather {
  if (poke.ability === "メガソーラー") return "sunny";
  return weather;
}

function isMegaStoneItem(item: string): boolean {
  return (
    item.endsWith("ナイト") ||
    item.endsWith("ナイトX") ||
    item.endsWith("ナイトY") ||
    item.endsWith("ナイトＸ") ||
    item.endsWith("ナイトＹ")
  );
}

function getTypeBoost(item: string, moveType: string, attackerSpecies: string): number {
  if (item === "でんきだま" && moveType === "でんき" && attackerSpecies.includes("ピカチュウ")) return 2.0;
  const entry = TYPE_BOOST_ITEMS[item];
  if (entry && entry[0] === moveType) return entry[1];
  return 1.0;
}

// ── 技タイプ・威力の実効値（_effective_move_type / _effective_power 相当） ─────────

/**
 * 攻撃時の実効タイプ。移植元: damage.py _effective_move_type()。
 * フィールド依存の分岐（だいちのはどう）は _mu_score 文脈では常にフィールドなし側に固定されるため
 * moves.json の格納値と常に一致する（no-op）。天候依存のウェザーボールだけは例外で、
 * メガソーラー所持者（例: メガメガニウム）の視点では常にsunny扱いとなりタイプがほのおに変わる
 * （effectiveWeather参照）。
 */
const WEATHER_BALL_TYPE: Record<string, string> = {
  sunny: "ほのお",
  rain: "みず",
  sandstorm: "いわ",
  hail: "こおり",
};

function effectiveMoveType(attacker: ResolvedBuild, move: ResolvedMove, weather: Weather): string {
  const t = move.type;
  const ab = attacker.ability;
  if (t === "ノーマル" && SKIN_ABILITIES[ab]) return SKIN_ABILITIES[ab];
  if (ab === "うるおいボイス" && SOUND_MOVES.has(move.n)) return "みず";
  if (move.n === "ウェザーボール") {
    const w = effectiveWeather(attacker, weather);
    return (w && WEATHER_BALL_TYPE[w]) || "ノーマル";
  }
  if (move.n === "レイジングブル") {
    if (attacker.t2) return attacker.t2;
    if (attacker.t1 === "かくとう") return "かくとう";
    return "ノーマル";
  }
  return t;
}

/**
 * 実効威力。移植元: damage.py _effective_power()。
 * best()（scripts/_explain.py）は `mv.power or 0` が偽（DB上power=NULL）の技を候補から除外するため、
 * 可変威力技（くさむすび/けたぐり/ジャイロボール/ヒートスタンプ/ヘビーボンバー/エレキボール/
 * カウンター系/固定ダメ系/OHKO等、power=NULL群）は _mu_score に一切現れない。
 * 残る「DB上power固定値だが_effective_powerで条件分岐する技」は、_mu_score の文脈
 * （ひんし数0・被弾回数0・状態異常なし・HP満タン・天候/フィールドなし・ランク変化0・行動履歴なし）では
 * 全て条件不成立となり DB格納値と常に一致する（おはかまいり/ふんどのこぶし/からげんき/
 * たたりめ/ひゃっきやこう/ベノムショック/どくばりセンボン/ライジングボルト/しっぺがえし/ダメおし/
 * ミストバースト/しおふき/ふんか/アシストパワー/つけあがる/ソーラービーム/ソーラーブレード/
 * じだんだ/やけっぱち/ゆきなだれ/うっぷんばらし/Gのちから）。
 * 実際に静的プロパティ／メガソーラー例外/連続技のヒット位置で条件が変わるのは以下の4技:
 *   - トリプルアクセル: ヒット位置(multiHitIndex)で威力20/40/60
 *   - はたきおとす: 相手の持ち物の有無（メガストーンは対象外）
 *   - アクロバット: 自分の持ち物の有無
 *   - ウェザーボール: 自分がメガソーラー所持なら威力100（そうでなければDB格納値の50のまま）
 * きまぐレーザー（30%で威力2倍）はPython側が真の乱数（random_roll非経由）で非決定的なため、
 * 本移植では基礎威力を採用する決定的近似とする（末尾コメントの既知の非対応を参照）。
 */
function effectivePower(
  attacker: ResolvedBuild,
  defender: ResolvedBuild,
  move: ResolvedMove,
  multiHitIndex: number,
  weather: Weather,
  effType: string
): number {
  let power = move.power ?? 0;
  if (move.n === "トリプルアクセル") {
    // damage.py: power = 20 * (attacker._multi_hit_index + 1) → 1発目20/2発目40/3発目60
    power = 20 * (multiHitIndex + 1);
  } else if (move.n === "はたきおとす") {
    if (defender.item && !isMegaStoneItem(defender.item)) power = Math.floor(power * 1.5);
  } else if (move.n === "アクロバット") {
    if (!attacker.item) power = power * 2;
  } else if (move.n === "ウェザーボール") {
    power = effectiveWeather(attacker, weather) ? 100 : 50;
  }

  const aw = effectiveWeather(attacker, weather);
  // ソーラービーム/ソーラーブレード：晴れ以外の天候(雨/雪/砂)は威力半減
  if ((move.n === "ソーラービーム" || move.n === "ソーラーブレード") &&
      (aw === "rain" || aw === "hail" || aw === "sandstorm")) {
    power = Math.floor(power / 2);
  }
  // すなのちから：砂嵐中はいわ/じめん/はがね技の威力1.3倍（メガガブリアス/メガハガネール等）
  if (aw === "sandstorm" && attacker.ability === "すなのちから" &&
      (effType === "いわ" || effType === "じめん" || effType === "はがね")) {
    power = Math.floor(power * 1.3);
  }
  return power;
}

// ── 無効判定（check_move_immunity / scrappy_override 相当） ─────────────────────

function checkMoveImmunity(defender: ResolvedBuild, moveType: string, moveName: string): boolean {
  const ab = defender.ability;
  if (IMMUNITY_TYPE[ab] === moveType) return true;
  if (ab === "ふしぎなまもり") return eff(moveType, defender.t1, defender.t2) <= 1.0;
  if (ab === "ぼうだん" && BALL_BOMB_MOVES.has(moveName)) return true;
  if (ab === "ぼうおん" && SOUND_MOVES.has(moveName)) return true;
  return false;
}

function scrappyOverride(attacker: ResolvedBuild, moveType: string, defender: ResolvedBuild): boolean {
  if (attacker.ability !== "きもったま") return false;
  if (moveType !== "ノーマル" && moveType !== "かくとう") return false;
  return defender.t1 === "ゴースト" || defender.t2 === "ゴースト";
}

// ── 持ち物補正（_apply_attacker_item / _apply_defender_item 相当） ───────────────

function applyAttackerItem(dmg: number, attacker: ResolvedBuild, move: ResolvedMove, effectiveness: number): number {
  const item = attacker.item;
  if (item === "いのちのたま") return Math.floor(dmg * 1.3);
  if (item === "こだわりハチマキ" && move.cat === "physical") return Math.floor(dmg * 1.5);
  if (item === "こだわりメガネ" && move.cat === "special") return Math.floor(dmg * 1.5);
  if (item === "ちからのハチマキ" && move.cat === "physical") return Math.floor(dmg * 1.1);
  if (item === "ものしりメガネ" && move.cat === "special") return Math.floor(dmg * 1.1);
  if (item === "たつじんのおび" && effectiveness > 1.0) return Math.floor(dmg * 1.2);
  return dmg;
}

interface DefenderItemResult {
  dmg: number;
  consumed: boolean;
}

function applyDefenderItem(dmg: number, item: string, move: ResolvedMove, effectiveness: number): DefenderItemResult {
  if (!item) return { dmg, consumed: false };
  if (item === "ホズのみ" && move.type === "ノーマル" && effectiveness > 0) {
    return { dmg: Math.floor(dmg * 0.5), consumed: true };
  }
  const resistType = BERRY_RESIST[item];
  if (resistType && effectiveness >= 2.0 && move.type === resistType) {
    return { dmg: Math.floor(dmg * 0.5), consumed: true };
  }
  return { dmg, consumed: false };
}

// ── 特性補正（_apply_attacker_ability / _apply_defender_ability 相当） ──────────

function applyAttackerAbility(dmg: number, attacker: ResolvedBuild, move: ResolvedMove, weather: Weather): number {
  const ab = attacker.ability;
  if (ab === "ちからずく" && move.cat !== "status" && SECONDARY_EFFECT_MOVES.has(move.n)) {
    return Math.floor(dmg * 1.3);
  }
  if ((ab === "かたいツメ" || ab === "かたいつめ") && move.cat === "physical" && !NON_CONTACT_PHYSICAL.has(move.n)) {
    return Math.floor(dmg * 1.3);
  }
  if (ab === "てつのこぶし" && (move.n.includes("パンチ") || PUNCH_MOVES.has(move.n))) {
    return Math.floor(dmg * 1.2);
  }
  if (ab === "テクニシャン" && move.power !== null && move.power <= 60) {
    return Math.floor(dmg * 1.5);
  }
  if (ab === "すてみ" && RECKLESS_MOVES.has(move.n)) {
    return Math.floor(dmg * 1.2);
  }
  if (ab === "がんじょうあご" && FANG_MOVES.has(move.n)) {
    return Math.floor(dmg * 1.5);
  }
  if (ab === "メガランチャー" && PULSE_MOVES.has(move.n)) {
    return Math.floor(dmg * 1.5);
  }
  if (ab === "すいほう" && move.type === "みず") {
    return Math.floor(dmg * 2);
  }
  // damage.py の elif 連鎖と同じ位置（すいほうの次はアナライズ→サンパワー）。
  // アナライズ(_acts_second)は静的評価では常に偽のため省略。
  if (ab === "サンパワー" && move.cat === "special" && effectiveWeather(attacker, weather) === "sunny") {
    return Math.floor(dmg * 1.5);
  }
  if (ab === "はがねのせいしん" && move.type === "はがね") {
    return Math.floor(dmg * 1.5);
  }
  return dmg;
}

function applyDefenderAbility(dmg: number, defender: ResolvedBuild, move: ResolvedMove, defenderFullHp: boolean): number {
  const ab = defender.ability;
  if (ab === "マルチスケイル") {
    // damage.py と同じく「HP満タン時のみ」半減。1発目でHPが減れば2発目以降(連続技の2ヒット目以降・
    // 2ターン目以降)は等倍に戻るため、満タン判定は呼び出し側から動的に渡す。
    return defenderFullHp ? Math.floor(dmg * 0.5) : dmg;
  }
  if (ab === "ファーコート" && move.cat === "physical") return Math.floor(dmg * 0.5);
  if (ab === "あついしぼう" && (move.type === "ほのお" || move.type === "こおり")) return Math.floor(dmg * 0.5);
  if (ab === "かんそうはだ" && move.type === "ほのお") return Math.floor(dmg * 1.25);
  if ((ab === "たいねつ" || ab === "すいほう") && move.type === "ほのお") return Math.floor(dmg * 0.5);
  if (ab === "きよめのしお" && move.type === "ゴースト") return Math.floor(dmg * 0.5);
  if (ab === "もふもふ") {
    let d = dmg;
    if (move.cat === "physical") d = Math.floor(d * 0.5);
    if (move.type === "ほのお") d = Math.floor(d * 2);
    return d;
  }
  if (ab === "フィルター" || ab === "ハードロック" || ab === "プリズムアーマー") {
    const e = eff(move.type, defender.t1, defender.t2);
    if (e > 1.0) return Math.floor(dmg * 0.75);
  }
  return dmg;
}

// ── ダメージ計算本体（calc_damage 相当） ────────────────────────────────────────

/**
 * 能力ランク補正倍率。scripts/simulator/pokemon.py の STAT_STAGE_MULT と同一
 * （+n → (2+n)/2倍、-n → 2/(2+n)倍）。
 */
export const STAT_STAGE_MULT: Record<number, number> = {
  [-6]: 2 / 8, [-5]: 2 / 7, [-4]: 2 / 6, [-3]: 2 / 5, [-2]: 2 / 4, [-1]: 2 / 3,
  0: 1.0,
  1: 3 / 2, 2: 4 / 2, 3: 5 / 2, 4: 6 / 2, 5: 7 / 2, 6: 8 / 2,
};

/** 攻撃側の能力ランク（りゅうせいぐん等の自己ランク変化を複数ターン評価で反映するために使う）。 */
export interface AttackerStages {
  /** 攻撃(A)ランク。 */
  atk?: number;
  /** 特攻(C)ランク。 */
  spa?: number;
}

/** ランク補正適用。pokemon.py get_effective_stat と同じく max(1, floor(base*mult))。 */
export function applyStage(base: number, stage: number): number {
  const s = Math.max(-6, Math.min(6, stage));
  if (s === 0) return base;
  return Math.max(1, Math.floor(base * STAT_STAGE_MULT[s]));
}

export interface DamageOptions {
  /** 0(最低)〜1(最高)のダメージ乱数(0=実際の乱数85%ロール、1=100%ロール)。省略時0(＝最低乱数、確定数計算の前提)。 */
  randomRoll?: number;
  /** 防御側がこの技を受ける時点でHP満タンか(既定true)。マルチスケイル等「HP満タン時のみ」の効果に使う。 */
  defenderFullHp?: boolean;
  /** 攻撃側のA/Cランク(既定0)。りゅうせいぐん等を2回目以降に使う場合の火力低下を再現する。 */
  attackerStages?: AttackerStages;
  /** 防御側の持ち物の上書き(耐性きのみが既に消費済みの状態を表現する)。省略時は defender.item。 */
  defenderItem?: string;
}

interface DamageDetail {
  dmg: number;
  /** 防御側の耐性きのみ(またはホズのみ)がこの1発で消費されたか */
  defenderItemConsumed: boolean;
}

function calcDamageDetail(
  attacker: ResolvedBuild,
  defender: ResolvedBuild,
  move: ResolvedMove,
  defenderItem: string,
  randomRoll: number,
  multiHitIndex = 0,
  defenderFullHp = true,
  attackerStages: AttackerStages = {}
): DamageDetail {
  const NO_DMG: DamageDetail = { dmg: 0, defenderItemConsumed: false };
  if (move.cat === "status") return NO_DMG;

  const ignoreAb = MOLD_BREAKER_ABILITIES.has(attacker.ability);
  const weather = fieldWeather(attacker, defender);
  const terrain = fieldTerrain(attacker, defender);
  const effType = effectiveMoveType(attacker, move, weather);
  const power = effectivePower(attacker, defender, move, multiHitIndex, weather, effType);
  if (!power) return NO_DMG;

  if (!ignoreAb && checkMoveImmunity(defender, effType, move.n)) {
    if (!scrappyOverride(attacker, effType, defender)) return NO_DMG;
  }

  // 攻撃・防御に使う実数値（急所・ランク変化・状態異常は_mu_score文脈では常に中立のため考慮不要）
  let cat: "physical" | "special" = move.cat === "physical" ? "physical" : "special";
  if (move.n === "シェルアームズ") {
    const physRatio = attacker.stats[1] / Math.max(1, defender.stats[2]);
    const specRatio = attacker.stats[3] / Math.max(1, defender.stats[4]);
    cat = physRatio > specRatio ? "physical" : "special";
  }

  // 攻撃側の自己ランク変化(りゅうせいぐん等)を反映。てんねん持ちの相手には攻撃側のランク変化が
  // 無視される(damage.py の def_ignores_atk_stage と同じ)。
  const atkStage = defender.ability === "てんねん" && !ignoreAb
    ? 0
    : (cat === "physical" ? attackerStages.atk ?? 0 : attackerStages.spa ?? 0);
  let atk = applyStage(cat === "physical" ? attacker.stats[1] : attacker.stats[3], atkStage);
  let dfs = cat === "physical" ? defender.stats[2] : defender.stats[4];


  if (move.n === "ボディプレス") atk = attacker.stats[2]; // 自分の防御を攻撃として使う
  if (move.n === "イカサマ") atk = defender.stats[1]; // 相手の攻撃実数値を参照
  if (move.n === "サイコショック" || move.n === "サイコブレイク" || move.n === "シークレットソード") {
    dfs = defender.stats[2]; // 特殊技だが相手の防御で計算
  }
  // せいなるつるぎ/DDラリアット（相手の防御ランク変化を無視）はランクが常に0のため無処理で一致

  // 参照する防御側能力が確定した後に掛ける天候補正（damage.py と同じ順序）。
  // 雪: こおりタイプの防御×1.5 ／ 砂嵐: いわタイプの特防×1.5。
  // 「Bを参照する技」にはサイコショック系・せいなるつるぎ・DDラリアットも含む。
  const usesDefense = cat === "physical" ||
    move.n === "サイコショック" || move.n === "サイコブレイク" || move.n === "シークレットソード" ||
    move.n === "せいなるつるぎ" || move.n === "DDラリアット";
  const defWeather = effectiveWeather(defender, weather);
  if (usesDefense) {
    if (defWeather === "hail" && (defender.t1 === "こおり" || defender.t2 === "こおり")) {
      dfs = Math.floor(dfs * 1.5);
    }
  } else if (defWeather === "sandstorm" && (defender.t1 === "いわ" || defender.t2 === "いわ")) {
    dfs = Math.floor(dfs * 1.5);
  }

  if (cat === "physical" && (attacker.ability === "ちからもち" || attacker.ability === "ヨガパワー")) {
    atk = atk * 2;
  }

  let dmg = Math.floor(Math.floor((Math.floor((2 * 50) / 5 + 2) * power * atk) / dfs) / 50) + 2;

  // 天候補正（damage.py と同じく攻撃側視点。メガソーラー所持者は常にsunny扱い）
  const atkWeather = effectiveWeather(attacker, weather);
  if (atkWeather === "sunny") {
    if (effType === "ほのお") dmg = Math.floor(dmg * 1.5);
    else if (effType === "みず") dmg = Math.floor(dmg * 0.5);
  } else if (atkWeather === "rain") {
    if (effType === "みず") dmg = Math.floor(dmg * 1.5);
    else if (effType === "ほのお") dmg = Math.floor(dmg * 0.5);
  }

  // フィールド補正（damage.py と同じ。地に足が着いている攻撃側にのみ乗る）
  const grounded = !(attacker.t1 === "ひこう" || attacker.t2 === "ひこう" || attacker.ability === "ふゆう");
  if (grounded) {
    if (terrain === "electric" && effType === "でんき") dmg = Math.floor(dmg * 1.3);
    else if (terrain === "psychic" && effType === "エスパー") dmg = Math.floor(dmg * 1.3);
    else if (terrain === "misty" && effType === "ドラゴン") dmg = Math.floor(dmg * 0.5);
    else if (terrain === "grassy" && effType === "くさ") dmg = Math.floor(dmg * 1.3);
  }
  // グラスフィールド: じしん/じならし/マグニチュードは半減（地に足の有無を問わない）
  if (terrain === "grassy" && (move.n === "じしん" || move.n === "じならし" || move.n === "マグニチュード")) {
    dmg = Math.floor(dmg * 0.5);
  }

  const roll = 0.85 + randomRoll * 0.15;
  dmg = Math.floor(dmg * roll);

  // タイプ一致補正（てきおうりょくはSTAB1.5倍→2.0倍）
  if (effType === attacker.t1 || (attacker.t2 !== null && effType === attacker.t2)) {
    dmg = Math.floor(dmg * (attacker.ability === "てきおうりょく" ? 2.0 : 1.5));
  }
  if (move.type === "ノーマル" && SKIN_ABILITIES[attacker.ability]) {
    dmg = Math.floor(dmg * 1.2);
  }
  // フェアリーオーラ: 攻撃側・防御側どちらが持っていてもフェアリー技威力1.33倍（メガフラエッテ等）
  if (effType === "フェアリー" && (attacker.ability === "フェアリーオーラ" || defender.ability === "フェアリーオーラ")) {
    dmg = Math.floor(dmg * 1.33);
  }

  // タイプ相性
  let effectiveness = eff(effType, defender.t1, defender.t2);
  if (effectiveness === 0 && scrappyOverride(attacker, effType, defender)) {
    effectiveness = 1.0;
  }
  if (move.n === "フリーズドライ" && (defender.t1 === "みず" || defender.t2 === "みず")) {
    effectiveness = Math.max(effectiveness, 2.0);
  }
  dmg = Math.floor(dmg * effectiveness);
  if (dmg === 0) return NO_DMG;

  let defenderItemConsumed = false;

  if (attacker.ability !== "ぶきよう") {
    dmg = applyAttackerItem(dmg, attacker, move, effectiveness);
  }
  if (defender.ability !== "ぶきよう") {
    const result = applyDefenderItem(dmg, defenderItem, move, effectiveness);
    dmg = result.dmg;
    defenderItemConsumed = result.consumed;
  }

  dmg = applyAttackerAbility(dmg, attacker, move, weather);
  if (!ignoreAb) {
    dmg = applyDefenderAbility(dmg, defender, move, defenderFullHp);
  }

  // get_pinch_multiplier（もうか/げきりゅう/しんりょく/むしのしらせ）は _mu_score が常にフルHPで
  // 評価するため発動条件（HP<=1/3）を満たさず恒常的にno-op。実装しない。

  if (attacker.ability === "きれあじ" && SLICING_MOVES.has(move.n)) {
    dmg = Math.floor(dmg * 1.5);
  }

  if (attacker.ability !== "ぶきよう") {
    const boost = getTypeBoost(attacker.item, move.type, attacker.sp);
    if (boost > 1.0) dmg = Math.floor(dmg * boost);
  }

  // もらいび発動中のほのお強化／でんきにかえるチャージ中のでんき強化は状態フラグが常に無い(ResolvedBuildに
  // 該当フィールドが存在しない)ため構造的に発生せず無関係。ほのおのたてがみ（メガカエンジシ等）は
  // フラグ非依存の恒常効果のため実装する。
  if (effType === "ほのお" && attacker.ability === "ほのおのたてがみ") {
    dmg = Math.floor(dmg * 1.5);
  }

  return { dmg: Math.max(1, dmg), defenderItemConsumed };
}

export interface MoveDamageDetail {
  /** 1発ごとのダメージ（単発技なら要素1、連続技はヒット数分）。ダメージ0（無効/変化技）なら空配列。 */
  hits: number[];
  /** hits の合計＝この技1回分の総ダメージ。 */
  total: number;
  /** 防御側の耐性きのみ(またはホズのみ)がこの技で消費されたか。 */
  defenderItemConsumed: boolean;
}

/**
 * 技1回分（連続技は全ヒット合計）のダメージ。移植元: scripts/simulator/battle.py の
 * execute_move() のヒットループ（hits = _calc_hits(...) で回して1発ずつ calc_damage）。
 * 1発ごとに乱数・威力補正・タイプ相性を適用して切り捨て、その整数を合算する
 * （Python側と同じ丸め方式。まとめて倍率を掛ける方式ではない）。
 * 防御側の半減きのみは1発目でのみ消費され、2発目以降は持ち物なしとして計算する
 * （battle.pyでも on_item_consumed により2発目以降は item=None になる）。
 */
function moveDamageDetail(
  attacker: ResolvedBuild,
  defender: ResolvedBuild,
  move: ResolvedMove,
  defenderItem: string,
  randomRoll: number,
  defenderFullHp = true,
  attackerStages: AttackerStages = {}
): MoveDamageDetail {
  const count = multiHitCount(attacker, move);
  const hits: number[] = [];
  let item = defenderItem;
  let consumed = false;
  for (let i = 0; i < count; i++) {
    // 連続技の2ヒット目以降はHPが減っているためマルチスケイル等の「HP満タン時」条件を満たさない
    const d = calcDamageDetail(attacker, defender, move, item, randomRoll, i, defenderFullHp && i === 0, attackerStages);
    if (d.dmg <= 0) break; // 無効・威力0なら以降のヒットも同じく0
    if (d.defenderItemConsumed) {
      consumed = true;
      item = "";
    }
    hits.push(d.dmg);
  }
  return { hits, total: hits.reduce((a, b) => a + b, 0), defenderItemConsumed: consumed };
}

/**
 * 技1回分の総ダメージ（連続技は全ヒット合計）。
 * calc_damage(attacker, defender, move, field, critical=False, random_roll) の1発分に加えて
 * battle.py のヒットループ相当を含む。
 */
export function calcDamage(me: ResolvedBuild, opp: ResolvedBuild, move: ResolvedMove, opts: DamageOptions = {}): number {
  return calcMoveDetail(me, opp, move, opts).total;
}

/**
 * 技1回分のダメージ内訳(1発ごと・合計・耐性きのみ消費の有無)。攻撃側の自己ランク変化や
 * 「きのみ消費済み」の状態を跨いだ複数ターン評価(matchup.ts の _movesToKO)から使う。
 */
export function calcMoveDetail(
  me: ResolvedBuild,
  opp: ResolvedBuild,
  move: ResolvedMove,
  opts: DamageOptions = {}
): MoveDamageDetail {
  return moveDamageDetail(
    me, opp, move,
    opts.defenderItem ?? opp.item,
    opts.randomRoll ?? 0,
    opts.defenderFullHp ?? true,
    opts.attackerStages ?? {}
  );
}

/**
 * 技1回分の「1発ごと」のダメージ列。連続技で「1発だけ耐える」効果
 * （ばけのかわ/がんじょう/きあいのタスキ）を正しく扱うために使う。
 */
export function calcHitDamages(
  me: ResolvedBuild,
  opp: ResolvedBuild,
  move: ResolvedMove,
  opts: DamageOptions = {}
): number[] {
  return calcMoveDetail(me, opp, move, opts).hits;
}

/**
 * 使用すると攻撃側自身のA/Cランクが変化する攻撃技（scripts/simulator/battle.py の
 * _apply_secondary() 内 SELF_EFFECTS / SELF_EFFECTS_KO と対応）。
 * ここに載せるのは「発動確率100%」かつ「A または C が変わる＝自分の火力に直接効く」ものだけ。
 *   - 確率発動（コメットパンチ20%/ほのおのまい50%/チャージビーム70%/はがねのつばさ10%/
 *     げんしのちから系10%）は、確定数計算が乱数固定の決定的評価であるため反映しない
 *   - B/D/Sだけが変わる技（インファイト・ぶちかまし・ニトロチャージ・アームハンマー等）は
 *     simulateKO が「攻撃側の火力」しか見ないため対象外（自分の耐久低下は別途未対応の既知の限界）
 *   - とどめばり(A+3)は「相手を倒した時のみ」発動するため、KOまでの手数計算には影響しない
 */
const SELF_STAGE_ON_USE: Record<string, AttackerStages> = {
  りゅうせいぐん: { spa: -2 },
  リーフストーム: { spa: -2 },
  オーバーヒート: { spa: -2 },
  サイコブースト: { spa: -2 },
  ゴールドラッシュ: { spa: -2 },
  ばかぢから: { atk: -1 },
  フレアソング: { spa: 1 },
};

/** 1回使用後の攻撃側ランク。あまのじゃくは変化量が反転する（battle.py と同じ）。 */
export function stageAfterUse(cur: AttackerStages, move: ResolvedMove, ability: string): AttackerStages {
  const d = SELF_STAGE_ON_USE[move.n];
  if (!d) return cur;
  const sign = ability === "あまのじゃく" ? -1 : 1;
  const clamp = (v: number) => Math.max(-6, Math.min(6, v));
  return {
    atk: clamp((cur.atk ?? 0) + sign * (d.atk ?? 0)),
    spa: clamp((cur.spa ?? 0) + sign * (d.spa ?? 0)),
  };
}

/**
 * 「同じ技をn回目に使った時の1発ごとのダメージ列」を返す関数を作る。呼び出しは use=1,2,3… の
 * 昇順である前提（内部で状態を持つ）。ターンを跨いで変化する要素をここで一元的に扱う:
 *   - 攻撃側の自己ランク変化: りゅうせいぐん等は2回目以降 C-2 の状態で撃つことになる
 *   - 防御側の耐性きのみ消費: 1回目で消費されたら2回目以降は持ち物なしで計算する
 *   - 防御側のHP満タン限定効果（マルチスケイル）: full 引数で切り替える
 */
function makeSeqFn(attacker: ResolvedBuild, move: ResolvedMove, defender: ResolvedBuild, roll: number) {
  let item = defender.item;
  // 入場時のいかくを初期ランクに反映する（対面した瞬間に必ず起きるため）
  let stages: AttackerStages = { atk: entryAtkStage(attacker, defender), spa: 0 };
  return (_use: number, full: boolean): number[] => {
    const d = calcMoveDetail(attacker, defender, move, {
      randomRoll: roll,
      defenderFullHp: full,
      attackerStages: stages,
      defenderItem: item,
    });
    if (d.defenderItemConsumed) item = "";
    stages = stageAfterUse(stages, move, attacker.ability);
    return d.hits;
  };
}

export interface SimulateKOOptions {
  /** ばけのかわ/がんじょう/きあいのタスキの「1発耐え」を無視した素の発数を返す。 */
  ignoreSurvive?: boolean;
  /** 防御側のターン終了時HP増減（たべのこし/オボン/砂/自傷）。省略時はターン終了時変化なし。 */
  eot?: (turn: number, hpLeft: number) => number;
  /** 打ち切り上限（超えたら999＝圏外扱い）。技選定など多数回呼ぶ場面の実用上限。 */
  maxUses?: number;
}

/**
 * 技を何回使えば相手を倒せるか（＝確定数。有効打点なしは999で圏外扱い）。
 *
 * 移植元: scripts/_explain.py _hits() + _apply_survive() だが、連続技を正しく扱うため
 * 「HPを削るシミュレーション」に置き換えている。ばけのかわ/がんじょう/きあいのタスキの
 * 「1発耐え」は連続技でも1発分にしか働かない（battle.py execute_move のヒットループと同じ）:
 *   - ばけのかわ: 最初の1ヒットを完全に無効化し、残りのヒットは通常通り通る
 *   - がんじょう/きあいのタスキ: 「HP満タン時に致死ダメージを受けた時」のみHP1で耐える。
 *     連続技は1ヒット目でHPが減るため、2ヒット目以降は発動条件(hp==max_hp)を満たさない
 * 耐え判定に使うability/itemは耐性きのみの消費では変化しない（タスキ/ばけのかわ/がんじょうは
 * BERRY_RESIST/ホズのみの対象外のため、常にResolvedBuildそのものの値でよい）。
 *
 * ダメージはターンごとに makeSeqFn で計算し直す（1発目の値の使い回しはしない）。これにより
 * マルチスケイル（HPが減った2ターン目以降は半減しない）と、りゅうせいぐん等の自己ランク低下
 * （2回目以降は C-2 ＝ 実ダメージ約2/3）の双方が正しく反映される。
 *
 * ターンを跨ぐ防御側のHP増減は eot（matchup.ts が bestMove を使って組み立てる）に委ねる。
 * damage.ts 側は eot 無しでも成立するため、bestMove から循環なしで呼び出せる。
 */
export function simulateKO(
  attacker: ResolvedBuild,
  move: ResolvedMove,
  defender: ResolvedBuild,
  hp: number,
  roll: number,
  opts: SimulateKOOptions = {}
): number {
  const { ignoreSurvive = false, eot, maxUses = 999 } = opts;
  const seqFn = makeSeqFn(attacker, move, defender, roll);
  let hpLeft = hp;
  let disguise = !ignoreSurvive && defender.ability === "ばけのかわ";
  let endure = !ignoreSurvive && (defender.ability === "がんじょう" || defender.item === "きあいのタスキ");
  let prevHp = Infinity;
  let stall = 0;
  for (let use = 1; use <= maxUses; use++) {
    const seq = seqFn(use, hpLeft === hp);
    if (!seq.length || seq.reduce((a, b) => a + b, 0) <= 0) return 999;
    for (const raw of seq) {
      if (disguise) {
        // ばけのかわ: ダメージは無効化するが最大HPの1/8を消費する（battle.py:992 と同仕様）。
        // 削りを数えないと1手多く見積もる（例: 1発44%なら確3のはずが確4になる）。
        disguise = false;
        hpLeft -= Math.max(1, Math.floor(defender.stats[0] / 8));
        if (hpLeft <= 0) return use;
        continue;
      }
      let d = raw;
      if (endure && hpLeft === hp && d >= hpLeft) {
        d = hpLeft - 1;
        endure = false;
      }
      hpLeft -= d;
      if (hpLeft <= 0) return use;
    }
    if (eot) {
      hpLeft = eot(use, hpLeft);
      if (hpLeft <= 0) return use;
    }
    // 回復量が与ダメを上回りHPが減らなくなったら永久に倒せない＝圏外。
    // オボンのみ等の1回限りの回復でHPが一時的に増えるターンがあるため、2ターン連続で
    // 前進しなかった場合にだけ打ち切る。
    stall = hpLeft >= prevHp ? stall + 1 : 0;
    if (stall >= 2) return 999;
    prevHp = hpLeft;
  }
  return 999;
}

/**
 * 攻撃側の技のうち相手への与ダメが最大の技を返す。移植元: scripts/_explain.py の best()（_mu_score内）。
 * 状態異常技・DB上威力NULLの技（可変威力技）は候補から除外する（best()と同じフィルタ）。
 * 相手の耐性きのみ消費は、同一ループ内で後続の技評価に反映する（Pythonのオブジェクト共有と同じ挙動）。
 *
 * 確定数計算は最低乱数(実際の85%ロール)を前提にする必要があるが、移植元のPython版
 * (scripts/simulator/damage.py)がrandom_roll引数を「0(最低)〜1(最高)の正規化値」として
 * 定義しているにもかかわらず、この値に実際の乱数値0.85をそのまま渡していたため、
 * 内部で roll=0.85+0.85*0.15=97.75% とほぼ最大乱数で計算されてしまっていた
 * (最低乱数85%では確定数に届かないのに「確定」と表示される実例で発覚)。
 * 正しい最低乱数(0=実際の85%ロール)を渡すよう修正。
 *
 * 【選定基準】かつては「1発目のダメージが最大の技」を選んでいたが、りゅうせいぐん等
 * 「使用後に自分のランクが下がる技」では2発目以降の火力が落ちるため、1発目が最大でも
 * KOまでの発数は多くなり得る。1v1判定が見ているのは1発の火力ではなく「同じ技を撃ち続けて
 * 何発で倒せるか」なので、候補技ごとに simulateKO で実際の発数を出し、
 *   ①最小乱数での発数(＝確定数)が少ない → ②最大乱数での発数が少ない → ③1発目のダメージが高い
 * の優先順で選ぶ。
 * 例: メガカイリューC216 vs ブラッキーH202 では、りゅうせいぐん(1発目111・確定5)より
 * エアスラッシュ(1発目64・確定4)の方が実際には早く倒せる。
 * simulateKO には eot(たべのこし等のターン終了時HP増減)を渡さない。eot の算出には
 * 逆向きの bestMove が必要で循環するため、選定時は打点のみで比較し、最終的な確定数表示は
 * matchup.ts の _movesToKO(eot 込み)で行う。
 * 発数は SELECT_HITS_CAP 発で打ち切る(超過はすべて同値扱い＝③の火力比較に落ちる)。
 */
/** bestMove の技選定で確定数シミュレーションを打ち切る発数（これを超える差は判定に影響しない）。 */
const SELECT_HITS_CAP = 8;

/**
 * リチャージ技（使用後1ターン行動不能）。battle.py の RECHARGE_MOVES と一致させる。
 * bestMove()は「毎ターン使える」前提でダメージ効率を比較するため、これらの技を
 * 選ぶと実際の消費ターン数(使用回数の2倍)を過小評価してしまう。ターン消費を
 * 正しく織り込むまでは候補から除外し、常用可能な技だけで比較する。
 */
export const RECHARGE_MOVES = new Set([
  "ギガインパクト", "ブラストバーン", "はかいこうせん",
  "ハイドロカノン", "ハードプラント", "がんせきほう",
]);

export function bestMove(
  me: ResolvedBuild,
  opp: ResolvedBuild
): { move: ResolvedMove; dmg: number; hits: number[]; hitsAfter: number[] } | null {
  let bestDmg = 0;
  let bestHits: number[] = [];
  let bestItemAtUse = opp.item;
  let best: ResolvedMove | null = null;
  let oppItem = opp.item;
  // 技プール(採用率TOP10)があればそちらから最大打点を選ぶ。1v1判定を「4技固定の型」ではなく
  // 「その種が実際に採用する技の中で相手に最も刺さる技を打ち合った場合」で行うため
  // (gen_builder_data.py の mpool と対。ユーザーが4技を決めた自分の枠には pool は無い)。
  const candidates = me.pool && me.pool.length ? me.pool : me.moves;
  const defHp = Math.max(1, opp.stats[0]);
  let bestLo = Infinity;
  let bestHi = Infinity;
  for (const mv of candidates) {
    if (mv.cat === "status" || !mv.power) continue;
    if (RECHARGE_MOVES.has(mv.n)) continue;
    const itemAtUse = oppItem;
    const detail = moveDamageDetail(me, opp, mv, oppItem, 0);
    if (detail.defenderItemConsumed) oppItem = "";
    if (detail.total <= 0) continue;
    const lo = simulateKO(me, mv, opp, defHp, 0, { maxUses: SELECT_HITS_CAP });
    const hi = simulateKO(me, mv, opp, defHp, 1, { maxUses: SELECT_HITS_CAP });
    const better =
      lo !== bestLo ? lo < bestLo :
      hi !== bestHi ? hi < bestHi :
      detail.total > bestDmg;
    if (!better) continue;
    bestLo = lo;
    bestHi = hi;
    bestDmg = detail.total;
    bestHits = detail.hits;
    bestItemAtUse = itemAtUse;
    best = mv;
  }
  if (!best) return null;
  // 2回目以降(＝防御側のHPが満タンでない状態)で同じ技を使った時のダメージ列。マルチスケイルのように
  // 「HP満タン時のみ」の耐久特性は1発目にしか乗らないため、確定数シミュレーション(simulateKO)では
  // こちらを使う。耐性きのみが1発目で消費される場合はその消費後の状態で計算する。
  const afterItem = moveDamageDetail(me, opp, best, bestItemAtUse, 0).defenderItemConsumed ? "" : bestItemAtUse;
  const hitsAfter = moveDamageDetail(me, opp, best, afterItem, 0, false).hits;
  return { move: best, dmg: bestDmg, hits: bestHits, hitsAfter };
}

/*
 * ── 未サポート一覧（builder-dataに登場するが本ファイルでは実装しない） ──────────────
 *
 * 1) 静的1発評価という_mu_scoreの前提により恒常的にno-opとなるため実装しない特性・持ち物
 *    （「未対応」ではなく「この文脈では効果が無いことが仕様」）:
 *    天候EOT系: あめうけざら/アイスボディ/かんそうはだ(EOT)/だっぴ/うるおいボディ
 *      ※ひでり/すなおこし/あめふらし/ゆきふらし と、それに依存するダメージ補正（サンパワー/
 *        すなのちから/ウェザーボール/ソーラービーム/雪の氷B・砂の岩D）は実装済み（fieldWeather）。
 *      ※てんきや/ぎたい（天候・フィールドでタイプが変わる）はbuilder-dataに保有種が無いため未実装。
 *      ※すいすい/ようりょくそ/すながくれ（天候依存の素早さ）は effectiveSpeed(stats.ts) が
 *        速度と持ち物しか受け取らない設計のため未対応。フシギバナ/ウツボット/リーフィアの
 *        ようりょくそが晴れパ相手で効かない（＝先後判定が実戦とズレ得る）。既知の未対応。
 *      ※砂嵐/雪の継続ダメージ(EOT 1/16)は本評価が「互いの最大打点の確定数」だけを見るため対象外。
 *    HP満タン前提で不発: もうか/げきりゅう/しんりょく/むしのしらせ（get_pinch_multiplier）
 *      ※_movesToKO は複数ターン削るが、攻撃側のHPは常に満タンとして扱うため実戦の
 *        「瀕死になって1.5倍」は再現しない。マルチスケイル(防御側・実装済み)と非対称な既知の限界。
 *    ランク変化前提(常に0)で無意味: てんねん、いかりのつぼ、うなぎのぼり、ぎゃくじょう、かちき、まけんき、
 *      あまのじゃく、ムラっけ 等の能力ランク変化系
 *    状態異常前提(常になし)で不発: こんじょう/ふしぎなうろこ/ねつぼうそう/やけど半減/どくのトゲ/
 *      ほのおのからだ/ほうし/せいでんき/はやおき/ふみん/めんえき/やるき/だっぴ 等
 *    行動履歴・被弾履歴前提で不発: じしんかじょう/うなぎのぼり(on_ko)/そうだいしょう/アナライズ/
 *      じきゅうりょく/くだけるよろい/ねばりかわ/ながいしっぽ/はりこみ/でんきにかえる(被弾後)/
 *      もらいび(被弾後の強化)/ほのおのたてがみ/じゅうでん/シンクロ/どくしゅ/あくしゅう/おうじゃのしるし
 *    場に出た時のみ発動（1v1静的評価では対象外）: いかく/ダウンロード/トレース/かんろなミツ/かわりもの/
 *      マイティチェンジ/さいせいりょく/しぜんかいふく
 *    ダブル専用・性別依存で単体戦では無効(NO_SINGLE_BATTLE_EFFECT準拠): いやしのこころ/おもてなし/
 *      きみょうなくすり/きょうせい/テレパシー/フラワーベール/フレンドガード/プラス/マイナス/レシーバー/
 *      すじがねいり/とうそうしん/メロメロボディ
 *    情報表示のみ: おみとおし/きけんよち
 *    ダメージ計算と無関係な特性（命中率・状態異常付与確率・交代時等、calc_damageの対象外）:
 *      プレッシャー/ノーガード/せいしんりょく/どんかん/マイペース/クリアボディ/ミラーアーマー/
 *      ちどりあし/ふくつのこころ/はやあし/はっこう/するどいめ/ゆきがくれ/ふくがん/ものひろい/
 *      イリュージョン/スキルリンク/マジシャン/マジックガード/マジックミラー/わるいてぐせ/
 *      キノコのほうし等の追加効果系、しゅうかく/はんすう/くいしんぼう等のきのみ関連(EOT)
 *
 * 2) 実在するが本移植では未実装（発生頻度・実装コストの兼ね合いで省略。将来対応の余地あり）:
 *    - フェアリーオーラ（フェアリー技1.33倍。builder-dataに保有ポケモン無し）
 *    - フライングプレス/だいちのはどう(フィールド展開時)/サイコブレイク/シークレットソード
 *      （builder-dataの実使用0件、コードパスとしては用意しやすいが未確認のため保留）
 *    - ネズミざん: battle.pyでは1〜10発の連続判定（スキルリンクで10発固定）だが、Python側の
 *      静的評価(features.py _expected_frac_calc)が1発扱いのため本移植も1発とする（Python一致優先）
 *    - きまぐレーザー: Python側は真の乱数(30%)で威力2倍。本移植は基礎威力を採用する決定的近似
 *      （ゴールデンテストで当該技が最大打点技に選ばれるビルドはPython実行時の乱数次第で不一致になり得る）
 *
 * 3) 特性・持ち物として存在するがダブルバトル/一般戦闘ロジック側の効果でありcalc_damage自体には
 *    現れないもの（damage.py/abilities.pyのcalc_damage呼び出し経路の外）は本ファイルの対象外。
 */
