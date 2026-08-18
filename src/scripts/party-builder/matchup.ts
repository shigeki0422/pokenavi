// judge1v1() — 1v1判定の差し替え境界。damage.ts(calc_damage移植)を使った本実装。
// 返却形・アルゴリズムは scripts/_explain.py の _mu_score()/_score_sym/_apply_survive/_hits と1対1対応。
import type { AggregateVerdict, ResolvedBuild, ResolvedMove, Verdict } from "./types";
import { effectiveSpeed } from "./stats";
import type { AttackerStages } from "./damage";
import { bestMove, calcHitDamages, calcMoveDetail, fieldWeather, simulateKO, stageAfterUse } from "./damage";

/**
 * 攻撃側の最大打点技(bestMove)による、相手HPに対する与ダメ割合(%、乱数min/max)と
 * 確定数/乱数n発(確率%)を返す。100%を跨ぐダメージ幅(例: 89.1〜105.1%)は
 * 最低乱数では確定しないため、単純に切り上げた「確定N」ではなく
 * 「乱数N発(確率P%)」として示す(_hitDetailForMoveの判定をそのまま利用)。
 * ポップアップの「105〜108%」表示にはこの関数を使う。
 */
export function bestMoveHitDetail(attacker: ResolvedBuild, defender: ResolvedBuild): MoveHitDetail | null {
  const best = bestMove(attacker, defender);
  if (!best) return null;
  return _hitDetailForMove(attacker, best.move, defender);
}

/**
 * 旧式: score>=1.5→◎ … の閾値が0.5刻みだったため、素早さの±0.5補正だけで
 * 「確定2 vs 確定1・先手」のような明確な負け(diff=-1、後述_scoreOf参照)が
 * ちょうど△/▲境界(-0.5)に乗ってしまい、判定文は「負け」なのに記号は△という
 * 矛盾が起きていた(ユーザー報告で発覚)。スコアの刻みを整数(1単位)にし、
 * 「確定数の差で明確に決着が付いている場合は素早さに関わらずその勝敗方向の
 * 記号になる」よう閾値も1刻みに変更。△は真に五分(確定数が同じ、かつ素早さも
 * 同値で先後がランダムになる)場合、または複数の型を平均した結果が
 * 割れている場合にのみ現れる。
 */
function _scoreSym(score: number): Verdict["sym"] {
  if (score >= 2) return "◎";
  if (score >= 1) return "○";
  if (score > -1) return "△";
  if (score > -2) return "▲";
  return "×";
}

/** 反動技（与ダメの一定割合を自分が受ける）。battle.py _apply_recoil() の recoil_moves と同値。 */
const RECOIL_FRAC: Record<string, number> = {
  すてみタックル: 1 / 3,
  フレアドライブ: 1 / 3,
  ボルテッカー: 1 / 3,
  ウェーブタックル: 1 / 3,
  ブレイブバード: 1 / 3,
  ウッドハンマー: 1 / 3,
  もろはのずつき: 1 / 2,
  ワイルドボルト: 1 / 4,
  はめつのひかり: 1 / 2,
};
/** 使うと最大HPの半分を反動として受ける技。battle.py の max_hp_half_recoil と同値。 */
const HALF_HP_RECOIL = new Set(["てっていこうせん"]);
/** HP吸収技と吸収率。battle.py _execute_move() の DRAIN_RATES と同値。 */
const DRAIN_RATES: Record<string, number> = {
  ギガドレイン: 0.5, メガドレイン: 0.5, すいとる: 0.5, ドレインパンチ: 0.5,
  ドレインキッス: 0.75, きゅうけつ: 0.5, パラボラチャージ: 0.5,
  むねんのつるぎ: 0.5, ウッドホーン: 0.5, シャカシャカほう: 0.5,
};

/**
 * 「防御側が1ターンに自分の攻撃で受ける自傷ダメージ／吸収回復」。正=回復、負=ダメージ。
 * 1v1の打ち合いでは防御側も毎ターン最大打点技を撃ち返すため、いのちのたま反動(最大HP1/10)・
 * 反動技(与ダメの1/3等)・HP吸収技(与ダメの1/2回復)は「相手を倒すのに必要な発数」を実際に変える。
 * 例: いのちのたま持ちは3ターンで最大HPの30%を自分で削るため、確定4が確定3になり得る。
 * これらは技を撃った本人のHPに効くため _movesToKO(攻撃側→防御側) の局所情報だけでは出せず、
 * 「防御側が攻撃側に対して選ぶ最大打点技」(bestMove(defender, attacker)) から算出する。
 *
 * battle.py の以下と対応: _execute_move() のいのちのたま反動／DRAIN_RATES、_apply_recoil()。
 * ただしいのちのたま反動は「1回の使用につき1回」とする（battle.py はヒットループ内にあるため
 * 連続技で回数分引かれるが、これは実ゲーム仕様と異なるPython側の既知の差異）。
 * マジックガードは反動・いのちのたま反動とも無効（実ゲーム仕様。battle.py の
 * いのちのたま処理にはマジックガード判定が無く、これもPython側の既知の差異）。
 */
function _selfDeltaPerTurn(defender: ResolvedBuild, attacker: ResolvedBuild): number {
  if (defender.ability === "マジックガード") return 0;
  const back = bestMove(defender, attacker);
  if (!back) return 0;
  const name = back.move.n;
  let delta = 0;
  if (defender.item === "いのちのたま") delta -= Math.max(1, Math.floor(defender.stats[0] / 10));
  const noRecoil = defender.ability === "いしあたま" || defender.ability === "ロックヘッド";
  if (!noRecoil) {
    if (HALF_HP_RECOIL.has(name)) delta -= Math.max(1, Math.floor(defender.stats[0] / 2));
    else if (RECOIL_FRAC[name]) delta -= Math.max(1, Math.floor(back.dmg * RECOIL_FRAC[name]));
  }
  if (DRAIN_RATES[name] && back.dmg > 0) {
    // 吸収量は「実際に与えたダメージ」に比例するため、相手の残HPを超えては吸収できない
    // （オーバーキル分は回復に乗らない）。これを入れないと、火力の高いきゅうけつ持ち等が
    // 毎ターン与ダメの半分を回復し続ける前提になり「絶対に倒せない(圏外)」が多発する。
    const dealt = Math.min(back.dmg, Math.max(1, attacker.stats[0]));
    let heal = Math.max(1, Math.floor(dealt * DRAIN_RATES[name]));
    if (defender.item === "おおきなねっこ") heal = Math.floor(heal * 1.3);
    delta += heal;
  }
  return delta;
}

/** すなあらしの継続ダメージを受けるか（battle.py _end_of_turn() の砂ダメ判定と同条件）。 */
function _takesSandDamage(p: ResolvedBuild): boolean {
  if (["いわ", "はがね", "じめん"].includes(p.t1)) return false;
  if (p.t2 && ["いわ", "はがね", "じめん"].includes(p.t2)) return false;
  return !["すなかき", "すながくれ", "すなのちから", "ぼうじん", "マジックガード"].includes(p.ability);
}

/**
 * 防御側のターン終了時HP増減を1ターンずつ適用する関数を作る（呼び出しは1ターン目から順に）。
 * 従来 _movesToKO は「毎ターン同じダメージを引くだけ」で、ターンをまたいで蓄積するHP変化を
 * 一切見ていなかったため、たべのこし持ち(builder-dataの約半数)やオボンのみ持ち(同・約半数)の
 * 確定数が実戦より1発少なく出ていた。battle.py _end_of_turn() の処理順に合わせて
 *   自分の攻撃による自傷/吸収 → すなあらし → たべのこし/くろいヘドロ → オボンのみ → オレンのみ
 * の順で適用する。
 * きんちょうかん（攻撃側）がいるときは防御側はきのみを食べられない（battle.py の _berry_blocked）。
 * ねをはる/アクアリング/やどりぎ/状態異常は「変化技を撃たない前提の打ち合い評価」では発生しないため対象外。
 */
function _makeEotStep(attacker: ResolvedBuild, defender: ResolvedBuild) {
  const maxHp = Math.max(1, defender.stats[0]);
  const selfDelta = _selfDeltaPerTurn(defender, attacker);
  const magicGuard = defender.ability === "マジックガード";
  const sand = !magicGuard && fieldWeather(attacker, defender) === "sandstorm" && _takesSandDamage(defender);
  const leftovers = defender.item === "たべのこし";
  const sludge = defender.item === "くろいヘドロ";
  const isPoison = defender.t1 === "どく" || defender.t2 === "どく";
  const berryBlocked = attacker.ability === "きんちょうかん";
  const berry: string = berryBlocked ? "" : defender.item;
  const sixteenth = Math.max(1, Math.floor(maxHp / 16));

  return (turn: number, hpLeft: number, berryLeft: boolean): { hp: number; berry: boolean } => {
    let hp = hpLeft;
    let left = berryLeft;
    hp += selfDelta;
    // 特性由来の天候は5ターンで切れる（battle.py: weather_count=5）
    if (sand && turn <= 5) hp -= sixteenth;
    if (leftovers) hp += sixteenth;
    else if (sludge) hp += isPoison ? sixteenth : -sixteenth;
    if (left && hp > 0 && hp <= Math.floor(maxHp / 2)) {
      if (berry === "オボンのみ") {
        hp += Math.floor(maxHp / 4);
        left = false;
      } else if (berry === "オレンのみ") {
        hp += 10;
        left = false;
      }
    }
    return { hp: Math.min(maxHp, hp), berry: left };
  };
}

/**
 * simulateKO に渡す用の「1本道シミュレーション」版 eot。きのみ消費状態を内部に閉じ込める。
 * 分岐（乱数ごとに枝分かれする確率計算）では状態を外から引き回す必要があるため、
 * 本体は状態を引数で受け取る _makeEotStep 側に置く。
 */
function _makeEotFn(attacker: ResolvedBuild, defender: ResolvedBuild) {
  const step = _makeEotStep(attacker, defender);
  let berry = true;
  return (turn: number, hpLeft: number): number => {
    const r = step(turn, hpLeft, berry);
    berry = r.berry;
    return r.hp;
  };
}

/**
 * 技を何回使えば相手を倒せるか（＝確定数。有効打点なしは999で圏外扱い）。
 * 本体は damage.ts の simulateKO（自己ランク変化・耐性きのみ消費・マルチスケイル・
 * 1発耐え効果を含むターン単位シミュレーション）。ここではそれに加えて、
 * 防御側のターン終了時HP増減（たべのこし/オボンのみ/砂/自分の反動・吸収）を eot として渡す。
 * eot の算出には逆向きの bestMove が必要なため、この合成は bestMove を持たない damage.ts 側では
 * できない（循環依存になる）。技の「選定」は eot 無しの simulateKO、最終的な確定数は本関数。
 */
function _movesToKO(
  attacker: ResolvedBuild,
  move: ResolvedMove,
  defender: ResolvedBuild,
  hp: number,
  roll: number,
  ignoreSurvive = false
): number {
  return simulateKO(attacker, move, defender, hp, roll, {
    ignoreSurvive,
    eot: _makeEotFn(attacker, defender),
  });
}

/**
 * 1v1判定本体。移植元: scripts/_explain.py _mu_score()。
 * 互いの最大打点1発の確定数（乱数0.85固定）・素早さ先後から勝敗スコアを算出する。
 */
export function judge1v1(me: ResolvedBuild, opp: ResolvedBuild): Verdict {
  const myBest = bestMove(me, opp);
  const oppBest = bestMove(opp, me);

  const myS = effectiveSpeed(me.stats[5], me.item);
  const oppS = effectiveSpeed(opp.stats[5], opp.item);
  const fast = myS > oppS;

  const myHits = myBest ? _movesToKO(me, myBest.move, opp, Math.max(1, opp.stats[0]), 0) : 999;
  const oppHits = oppBest ? _movesToKO(opp, oppBest.move, me, Math.max(1, me.stats[0]), 0) : 999;

  const score = _scoreOf(myHits, oppHits, myS, oppS, fast);
  const win = myHits < oppHits || (myHits === oppHits && fast);

  return {
    sym: _scoreSym(score),
    win,
    fast,
    myS,
    oppS,
    myHits,
    oppHits,
    myMove: myBest?.move.n ?? null,
    oppMove: oppBest?.move.n ?? null,
    stub: false,
  };
}

/**
 * 判定スコア = 確定数の差(相手の確定数-自分の確定数)。差がある時点で勝敗は
 * 確定数だけで決着しているため素早さは無関係(以前は±0.5の素早さ補正を
 * 常に足していたため、diff=-1のような明確な負けが△/▲境界に乗る不具合が
 * あった)。確定数が同数の場合のみ素早さが先後を決めるため、素早さが同値
 * なら真の五分(0)、そうでなければ先手側の勝ち(±1)とする。
 */
function _scoreOf(myHits: number, oppHits: number, myS: number, oppS: number, fast: boolean): number {
  const diff = oppHits - myHits;
  if (diff !== 0) return diff;
  if (myS === oppS) return 0;
  return fast ? 1 : -1;
}
/** Verdict(judge1v1の返却値)からスコアを再算出する(judgeVsBuildsの集約専用)。 */
function _scoreOfVerdict(v: Verdict): number {
  return _scoreOf(v.myHits ?? 999, v.oppHits ?? 999, v.myS, v.oppS, v.fast);
}

/**
 * 相手の複数型(≤3)を踏まえた集約判定。移植元: scripts/_explain.py matchup_grid()。
 * 各型についてjudge1v1でスコアを求め、
 *   sym = _scoreSym(平均スコア)
 *   dep = _scoreSym(最悪スコア) !== _scoreSym(最良スコア)  （型により有利不利のシンボルが割れる）
 * を移植元と同一のロジックで算出する。opps は resolveTarget 済みの相手の各型(≤3)。
 */
export function judgeVsBuilds(me: ResolvedBuild, opps: ResolvedBuild[]): AggregateVerdict {
  return judgeVsBuildsMulti([me], opps);
}

/**
 * 自分側の複数型(≤3) × 相手側の複数型(≤3) の総当たり集約判定。
 * 従来は「自分は採用率最多の1型固定・相手だけ3型」という非対称だったため、
 * 自分の型が変われば結論が変わる相手でもその揺れが見えなかった。自分側も
 * 持ち物/性格/EV違いの型を並べ、全ペアのスコア平均をシンボル化する。
 * dep(型依存) は全ペアの最良・最悪シンボルが割れるかで判定するので、
 * 「自分の型次第で有利不利が変わる」場合もここで拾われる。
 */
export function judgeVsBuildsMulti(mes: ResolvedBuild[], opps: ResolvedBuild[]): AggregateVerdict {
  const verdicts: Verdict[] = [];
  for (const me of mes) for (const opp of opps) verdicts.push(judge1v1(me, opp));
  if (!verdicts.length) throw new Error("judgeVsBuildsMulti: 型が空です");
  const scores = verdicts.map(_scoreOfVerdict);
  const mean = scores.reduce((a, b) => a + b, 0) / scores.length;
  const sym = _scoreSym(mean);
  const dep = _scoreSym(Math.min(...scores)) !== _scoreSym(Math.max(...scores));
  return { sym, dep, verdicts };
}

/**
 * 技1本の16段階ダメージ乱数分布(85〜100%の1%刻み、calcDamageのrandomRoll=i/15と対応)。
 * scripts/simulator/damage.py の `random.choice([85..100])/100` と同じ16通りを、
 * calcDamage を16回呼んで再現する。
 * 連続技はcalcDamageが1回分(全ヒット合計)を返すため、ここでの1要素＝技1回分の合計ダメージ
 * （全ヒットに同じ乱数を適用する近似。ヒットごとに独立乱数を引く厳密分布ではないが、
 *  Python側にも厳密分布の実装は無く、表示用の目安として合計の上下限は一致する）。
 * stages に「そのターン開始時点での攻撃側ランク」を渡すことで、りゅうせいぐん等を
 * 2回目以降に撃つ場合の低下後の分布も作れる。
 */
function _hitDamageDistribution(
  attacker: ResolvedBuild,
  move: ResolvedMove,
  defender: ResolvedBuild,
  defenderFullHp = true,
  stages: AttackerStages = {}
): number[] {
  const out: number[] = [];
  for (let i = 0; i <= 15; i++) {
    out.push(
      calcMoveDetail(attacker, defender, move, { randomRoll: i / 15, defenderFullHp, attackerStages: stages }).total
    );
  }
  return out;
}

/**
 * hits発以内に防御側を倒せる確率(0〜1)を、残HPの状態DPで厳密に計算する。
 * 各発は16段階乱数からiidで選ばれる前提。distsByUse[k] は「k+1回目に使う時」の分布
 * （2回目以降はマルチスケイルが外れ、りゅうせいぐん等の自己ランク低下が乗る）。
 *
 * 旧実装は「合計ダメージが閾値以上か」の畳み込みで、ターン跨ぎのHP増減(たべのこし/オボンのみ/
 * 砂/反動)を"実効HP"に線形近似で足し込んでいた。オボンのみのように発動が残HPに依存する回復は
 * この近似では取りこぼされ（残HPを線形に仮定すると発動閾値を跨がない）、確率が100%と算出されて
 * 「乱数2発なのに確定2」と表示される不整合を起こしていた（実際は最低乱数だと確定3）。
 * ここでは残HPそのものを状態に持ち、各ターンのダメージ後に実際の eot を適用することで、
 * きのみの発動有無を含めて _movesToKO の逐次シミュレーションと同じ経路を全乱数分岐で辿る。
 */
function _koProbabilityWithEot(
  distsByUse: number[][],
  hits: number,
  maxHp: number,
  eotStep: ReturnType<typeof _makeEotStep>
): number {
  // key = `${残HP}|${きのみ未消費?1:0}`、値 = その状態に到達する確率
  let states = new Map<string, number>([[`${maxHp}|1`, 1]]);
  let ko = 0;
  for (let use = 1; use <= hits; use++) {
    const dist = distsByUse[Math.min(use - 1, distsByUse.length - 1)];
    if (!dist.length) break;
    const next = new Map<string, number>();
    for (const [key, w] of states) {
      const sep = key.indexOf("|");
      const hp = Number(key.slice(0, sep));
      const berry = key.slice(sep + 1) === "1";
      const p = w / dist.length;
      for (const d of dist) {
        const afterHit = hp - d;
        if (afterHit <= 0) {
          ko += p;
          continue;
        }
        const r = eotStep(use, afterHit, berry);
        if (r.hp <= 0) {
          ko += p;
          continue;
        }
        const k2 = `${r.hp}|${r.berry ? 1 : 0}`;
        next.set(k2, (next.get(k2) ?? 0) + p);
      }
    }
    states = next;
    if (!states.size) break;
  }
  return ko;
}

/** 確率計算(畳み込みDP)を行う実用上限。超える場合は保守側(最小乱数の確定数)の「確m」表示にフォールバックする。 */
const PROB_HITS_CAP = 5;

export interface MoveHitDetail {
  n: string;
  /** 最小乱数(0.85)/最大乱数(1.0)での与ダメ実数値。無効技(ダメージ0)・変化技はnull。 */
  dmgLo: number | null;
  dmgHi: number | null;
  /** 相手HPに対する割合(%)。dmgLo/dmgHiと対の関係。 */
  pctLo: number | null;
  pctHi: number | null;
  /** 表示用の確定数(耐え補正込み)。certain=trueなら「確n」、falseなら「乱数n発」のn。 */
  hits: number | null;
  /** 乱数n発時のKO確率(%、0〜100)。certain=true、または無効技の場合はnull。 */
  prob: number | null;
  /** true=最小乱数でもhits発でKO(確定)。false=最大乱数ならhits発だが確率的(prob%)。 */
  certain: boolean;
}

/**
 * 技1本の与ダメ内訳。確定数/乱数n発(確率%)の判定は以下のロジック:
 *   - baseHitsLo = 最小乱数(0.85)でのダメージから計算した確定数(必ずこの発数以内でKOできる保証値)
 *   - baseHitsHi = 最大乱数(1.0)でのダメージから計算した確定数(最良ケースの発数)
 *   - baseHitsLo === baseHitsHi なら乱数の影響を受けず確定 → 「確n」
 *   - 異なる場合は baseHitsHi 発でKOできる確率を、残HPを状態に持つDP(ターン終了時のHP増減込み)で
 *     算出 → 「乱数n発(p%)」
 *   - baseHitsHi が実用上限(PROB_HITS_CAP)を超える場合、または耐え効果(ばけのかわ/がんじょう/
 *     きあいのタスキ)が絡む場合はDPを省略し、保守的な baseHitsLo 側の「確n」表示にフォールバックする
 * 「確n」として表示する値は常に baseHitsLo（＝judge1v1の確定数と同じ最低乱数基準）であり、
 * 判定行と食い違わないことが不変条件（scripts/tests/ts_bestmove_check.ts で全ビルド総当たり検証）。
 * 例: 素のHPに対し乱数1発(25%)の技を持つ相手がきあいのタスキを持つ場合、最低乱数でも最大乱数でも
 * 2発なので「確定2」になる。
 */
function _hitDetailForMove(attacker: ResolvedBuild, move: ResolvedMove, defender: ResolvedBuild): MoveHitDetail {
  const NONE: MoveHitDetail = { n: move.n, dmgLo: null, dmgHi: null, pctLo: null, pctHi: null, hits: null, prob: null, certain: true };
  if (move.cat === "status") return NONE;

  // 連続技(トリプルアクセル等)は1回分＝全ヒット合計で評価する(dmg/確定数とも)
  const hitsLoArr = calcHitDamages(attacker, defender, move, { randomRoll: 0 });
  const hitsHiArr = calcHitDamages(attacker, defender, move, { randomRoll: 1 });
  const dmgLo = hitsLoArr.reduce((a, b) => a + b, 0);
  const dmgHi = hitsHiArr.reduce((a, b) => a + b, 0);
  if (dmgHi <= 0) return NONE;

  const hp = Math.max(1, defender.stats[0]);
  const pctLo = (dmgLo / hp) * 100;
  const pctHi = (dmgHi / hp) * 100;
  const baseHitsLo = _movesToKO(attacker, move, defender, hp, 0);
  const baseHitsHi = _movesToKO(attacker, move, defender, hp, 1);

  if (baseHitsLo === baseHitsHi || baseHitsHi > PROB_HITS_CAP) {
    return { n: move.n, dmgLo, dmgHi, pctLo, pctHi, hits: baseHitsLo, prob: null, certain: true };
  }

  // 耐え効果(ばけのかわ/がんじょう/タスキ)で発数が底上げされている場合は、保守側
  // (最低乱数の確定数=判定行と同じ値)の「確n」表示にする。
  // 乱数側の確率DPは耐え効果(1発無効化・HP1で耐える)を分布に織り込めないため、
  // ここで最大乱数側の発数を「確定」と称すると判定行(最低乱数)と食い違う
  // （例: ばけのかわのミミッキュに対し内訳「確定2」・判定「確定3」）。
  // なお「素で乱数1発の技＋きあいのタスキ」のように耐えによって最低/最大乱数の発数が
  // 揃うケースは、上の baseHitsLo === baseHitsHi の分岐で既に「確定2」になる。
  const hasSurvive =
    defender.ability === "ばけのかわ" || defender.ability === "がんじょう" || defender.item === "きあいのタスキ";
  if (hasSurvive) {
    return { n: move.n, dmgLo, dmgHi, pctLo, pctHi, hits: baseHitsLo, prob: null, certain: true };
  }

  // 1回目は「相手HP満タン・自分ランク0」、2回目以降は「HP非満タン・自己ランク変化後」の分布を使う
  const distsByUse: number[][] = [];
  let stages: AttackerStages = { atk: 0, spa: 0 };
  for (let use = 1; use <= baseHitsHi; use++) {
    distsByUse.push(_hitDamageDistribution(attacker, move, defender, use === 1, stages));
    stages = stageAfterUse(stages, move, attacker.ability);
  }
  // ターン跨ぎのHP増減（たべのこし回復・オボンのみ・砂・防御側自身の反動）は残HPに依存して
  // 発動するため、実効HPへの線形近似ではなく残HPを状態に持つDPで厳密に反映する。
  const prob = _koProbabilityWithEot(distsByUse, baseHitsHi, hp, _makeEotStep(attacker, defender)) * 100;
  // baseHitsLo > baseHitsHi である以上、最低乱数の経路はbaseHitsHi発では倒せない＝確率は100%未満。
  // 万一丸め等で100%に達した場合は「乱数n発(100%)」という矛盾表示を避けて確定扱いにする。
  if (prob >= 100) return { n: move.n, dmgLo, dmgHi, pctLo, pctHi, hits: baseHitsHi, prob: null, certain: true };
  return { n: move.n, dmgLo, dmgHi, pctLo, pctHi, hits: baseHitsHi, prob, certain: false };
}

/**
 * 仮想敵カード用: 自分の技それぞれ(最大4)がoppに対し確定/乱数何発かの一覧(与ダメ実数値・HP比込み)。
 * judge1v1と同じ耐え補正(ばけのかわ/がんじょう/きあいのタスキ)込みの確定数/乱数発数。
 * 変化技・無効(ダメージ0)はhits:null(UI側で「—」表示)。
 */
export function moveBreakdown(me: ResolvedBuild, opp: ResolvedBuild): MoveHitDetail[] {
  return me.moves.map((mv) => _hitDetailForMove(me, mv, opp));
}

/**
 * 乱数n発の確率(%)を表示用文字列にする。Math.roundだけだと0.2%が「0%」、99.8%が「100%」となり
 * 「乱数なのに0%/100%」という矛盾表示になるため、境界は「<1」「>99」で示す。
 * prob=0ちょうど（有効HP近似で最大乱数合計にわずかに届かない場合に起こり得る）も、
 * 発数自体は厳密シミュレーション(_movesToKO)で到達可能と判定されている以上、真の確率は0ではないので「<1」とする。
 */
export function fmtKoProbPct(prob: number | null | undefined): string {
  const p = prob ?? 0;
  if (p < 1) return '<1';
  if (p > 99 && p < 100) return '>99';
  return String(Math.round(p));
}
