// ダメージ計算・1v1判定用の実ダメージ計算。
// 移植元: scripts/simulator/damage.py の calc_damage() / _effective_move_type() / _effective_power() /
//         _apply_attacker_item() / _apply_defender_item() / _apply_attacker_ability() / _apply_defender_ability()
//         scripts/simulator/abilities.py の check_move_immunity() / scrappy_override() / should_ignore_ability()
//
// 移植範囲は scripts/_explain.py の _mu_score() が実際に通るコードパスのみ（フル移植はしない）。
// _mu_score() は BattleField()（天候なし・フィールドなし・じゅうりょくなし）・critical=False・
// フルHP（自分/相手とも常にmax_hpと同値）・能力ランク変化0・状態異常なしの1発だけを評価するため、
// damage.py の以下の分岐は _mu_score の文脈では必ず不発（no-op）になる。実装しない（意図的な省略）:
//   - 天候/フィールド依存の威力・ダメージ補正、天候設置特性（ひでり/すなおこし等）、天候依存の速度上昇
//     （すいすい/ようりょくそ/すながくれ）※BattleField()は常にweather=None。
//     ただしメガソーラー特性だけは所有者自身の視点で常にsunny扱いになる例外で、これは実装している
//     （effectiveWeather()。メガメガニウム等のほのお/みず技倍率・ウェザーボールのタイプ/威力に影響）
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

/**
 * 実効天候（damage.py effective_weather 相当）。
 * BattleField()は常にweather=Noneのため、天候関連の分岐は原則すべてno-opだが、
 * メガソーラー特性だけは所有者自身の視点で常に"sunny"を返す例外（他の天候発生特性は
 * entry_ability経由でfieldを書き換える方式のため、_mu_scoreからは呼ばれず無関係）。
 * 引数のpokeは「その天候判定を必要としている側」(damage.pyの呼び出し規約と同じ:
 * 攻撃側のタイプ変化/威力/ダメージ補正はattacker視点、防御側の耐久補正はdefender視点)。
 */
function effectiveWeather(poke: ResolvedBuild): "sunny" | null {
  return poke.ability === "メガソーラー" ? "sunny" : null;
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
function effectiveMoveType(attacker: ResolvedBuild, move: ResolvedMove): string {
  const t = move.type;
  const ab = attacker.ability;
  if (t === "ノーマル" && SKIN_ABILITIES[ab]) return SKIN_ABILITIES[ab];
  if (ab === "うるおいボイス" && SOUND_MOVES.has(move.n)) return "みず";
  if (move.n === "ウェザーボール") {
    return effectiveWeather(attacker) === "sunny" ? "ほのお" : "ノーマル";
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
 * 全て条件不成立となり DB格納値と常に一致する（おはかまいり/ふんどのこぶし/からげんき/トリプルアクセル/
 * たたりめ/ひゃっきやこう/ベノムショック/どくばりセンボン/ライジングボルト/しっぺがえし/ダメおし/
 * ミストバースト/しおふき/ふんか/アシストパワー/つけあがる/ソーラービーム/ソーラーブレード/
 * じだんだ/やけっぱち/ゆきなだれ/うっぷんばらし/Gのちから）。
 * 実際に静的プロパティ／メガソーラー例外で条件が変わるのは以下の3技:
 *   - はたきおとす: 相手の持ち物の有無（メガストーンは対象外）
 *   - アクロバット: 自分の持ち物の有無
 *   - ウェザーボール: 自分がメガソーラー所持なら威力100（そうでなければDB格納値の50のまま）
 * きまぐレーザー（30%で威力2倍）はPython側が真の乱数（random_roll非経由）で非決定的なため、
 * 本移植では基礎威力を採用する決定的近似とする（末尾コメントの既知の非対応を参照）。
 */
function effectivePower(attacker: ResolvedBuild, defender: ResolvedBuild, move: ResolvedMove): number {
  let power = move.power ?? 0;
  if (move.n === "はたきおとす") {
    if (defender.item && !isMegaStoneItem(defender.item)) power = Math.floor(power * 1.5);
  } else if (move.n === "アクロバット") {
    if (!attacker.item) power = power * 2;
  } else if (move.n === "ウェザーボール") {
    // メガソーラー所持時のみ「天候あり」扱い(常にsunny)で威力100。それ以外は天候なしで50(DB格納値と一致)。
    power = effectiveWeather(attacker) ? 100 : 50;
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

function applyAttackerAbility(dmg: number, attacker: ResolvedBuild, move: ResolvedMove): number {
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
  return dmg;
}

function applyDefenderAbility(dmg: number, defender: ResolvedBuild, move: ResolvedMove): number {
  const ab = defender.ability;
  if (ab === "マルチスケイル") {
    // damage.pyは defender.hp == defender.max_hp を条件とするが、_mu_scoreの評価対象は常にフルHP
    return Math.floor(dmg * 0.5);
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

export interface DamageOptions {
  /** 0(最低)〜1(最高)のダメージ乱数。省略時 0.85（_mu_score.best() が使う固定値と同じ）。 */
  randomRoll?: number;
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
  randomRoll: number
): DamageDetail {
  const NO_DMG: DamageDetail = { dmg: 0, defenderItemConsumed: false };
  if (move.cat === "status") return NO_DMG;

  const ignoreAb = MOLD_BREAKER_ABILITIES.has(attacker.ability);
  const effType = effectiveMoveType(attacker, move);
  const power = effectivePower(attacker, defender, move);
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

  let atk = cat === "physical" ? attacker.stats[1] : attacker.stats[3];
  let dfs = cat === "physical" ? defender.stats[2] : defender.stats[4];

  if (move.n === "ボディプレス") atk = attacker.stats[2]; // 自分の防御を攻撃として使う
  if (move.n === "イカサマ") atk = defender.stats[1]; // 相手の攻撃実数値を参照
  if (move.n === "サイコショック" || move.n === "サイコブレイク" || move.n === "シークレットソード") {
    dfs = defender.stats[2]; // 特殊技だが相手の防御で計算
  }
  // せいなるつるぎ/DDラリアット（相手の防御ランク変化を無視）はランクが常に0のため無処理で一致

  if (cat === "physical" && (attacker.ability === "ちからもち" || attacker.ability === "ヨガパワー")) {
    atk = atk * 2;
  }

  let dmg = Math.floor(Math.floor((Math.floor((2 * 50) / 5 + 2) * power * atk) / dfs) / 50) + 2;

  // 天候補正: メガソーラー所持者視点でのみ常にsunny扱い(それ以外は天候なしのためno-op)
  if (effectiveWeather(attacker) === "sunny") {
    if (effType === "ほのお") dmg = Math.floor(dmg * 1.5);
    else if (effType === "みず") dmg = Math.floor(dmg * 0.5);
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

  dmg = applyAttackerAbility(dmg, attacker, move);
  if (!ignoreAb) {
    dmg = applyDefenderAbility(dmg, defender, move);
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

/** calc_damage(attacker, defender, move, field, critical=False, random_roll) 相当の単発ダメージ計算。 */
export function calcDamage(me: ResolvedBuild, opp: ResolvedBuild, move: ResolvedMove, opts: DamageOptions = {}): number {
  return calcDamageDetail(me, opp, move, opp.item, opts.randomRoll ?? 0.85).dmg;
}

/**
 * 攻撃側の技のうち相手への与ダメが最大の技を返す。移植元: scripts/_explain.py の best()（_mu_score内）。
 * 状態異常技・DB上威力NULLの技（可変威力技）は候補から除外する（best()と同じフィルタ）。
 * 相手の耐性きのみ消費は、同一ループ内で後続の技評価に反映する（Pythonのオブジェクト共有と同じ挙動）。
 */
export function bestMove(me: ResolvedBuild, opp: ResolvedBuild): { move: ResolvedMove; dmg: number } | null {
  let bestDmg = 0;
  let best: ResolvedMove | null = null;
  let oppItem = opp.item;
  for (const mv of me.moves) {
    if (mv.cat === "status" || !mv.power) continue;
    const detail = calcDamageDetail(me, opp, mv, oppItem, 0.85);
    if (detail.defenderItemConsumed) oppItem = "";
    if (detail.dmg > bestDmg) {
      bestDmg = detail.dmg;
      best = mv;
    }
  }
  return best ? { move: best, dmg: bestDmg } : null;
}

/*
 * ── 未サポート一覧（builder-dataに登場するが本ファイルでは実装しない） ──────────────
 *
 * 1) 静的1発評価という_mu_scoreの前提により恒常的にno-opとなるため実装しない特性・持ち物
 *    （「未対応」ではなく「この文脈では効果が無いことが仕様」）:
 *    天候設置・天候依存: ひでり/すなおこし/あめふらし/ゆきふらし/すいすい/ようりょくそ/すながくれ/
 *      サンパワー(ダメ枠)/あめうけざら/アイスボディ/かんそうはだ(EOT)/だっぴ/うるおいボディ/てんきや/ぎたい
 *    HP満タン前提で不発: もうか/げきりゅう/しんりょく/むしのしらせ（get_pinch_multiplier）
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
 *    - きまぐレーザー: Python側は真の乱数(30%)で威力2倍。本移植は基礎威力を採用する決定的近似
 *      （ゴールデンテストで当該技が最大打点技に選ばれるビルドはPython実行時の乱数次第で不一致になり得る）
 *
 * 3) 特性・持ち物として存在するがダブルバトル/一般戦闘ロジック側の効果でありcalc_damage自体には
 *    現れないもの（damage.py/abilities.pyのcalc_damage呼び出し経路の外）は本ファイルの対象外。
 */
