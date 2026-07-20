// judge1v1() — 1v1判定の差し替え境界。damage.ts(calc_damage移植)を使った本実装。
// 返却形・アルゴリズムは scripts/_explain.py の _mu_score()/_score_sym/_apply_survive/_hits と1対1対応。
import type { AggregateVerdict, ResolvedBuild, ResolvedMove, Verdict } from "./types";
import { effectiveSpeed } from "./stats";
import { bestMove, calcDamage } from "./damage";

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

function _scoreSym(score: number): Verdict["sym"] {
  if (score >= 1.5) return "◎";
  if (score >= 0.5) return "○";
  if (score >= -0.5) return "△";
  if (score >= -1.5) return "▲";
  return "×";
}

/** 移植元: scripts/_explain.py _hits()。ratio<=0（有効打点なし）は999（圏外扱いの大きな手数）。 */
function _hits(ratio: number): number {
  return ratio <= 0 ? 999 : Math.ceil(1 / ratio);
}

/**
 * 移植元: scripts/_explain.py _apply_survive()。
 * ばけのかわ/がんじょう/きあいのタスキの「1発耐え」を確定数に反映する。
 * これらの判定に使うability/itemは耐性きのみの消費(bestMove内の防御側item消費)では変化しない
 * （タスキ/ばけのかわ/がんじょうはBERRY_RESIST/ホズのみの対象外のため、常にResolvedBuildそのものの値でよい）。
 */
function _applySurvive(n: number, defender: ResolvedBuild): number {
  if (defender.ability === "ばけのかわ") return n + 1;
  if (defender.ability === "がんじょう") return n === 1 ? 2 : n;
  if (defender.item === "きあいのタスキ") return n === 1 ? 2 : n;
  return n;
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

  const myr = (myBest?.dmg ?? 0) / Math.max(1, opp.stats[0]);
  const thr = (oppBest?.dmg ?? 0) / Math.max(1, me.stats[0]);
  const myHits = _applySurvive(_hits(myr), opp);
  const oppHits = _applySurvive(_hits(thr), me);

  const score = (oppHits - myHits) + (fast ? 0.5 : -0.5);
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
 * judge1v1の内部score((oppHits-myHits)+(fast?0.5:-0.5))を返却済みのVerdictから再算出する。
 * judge1v1自体はscoreを返さない(Verdict形は不変)ため、集約(judgeVsBuilds)専用にここで復元する。
 * 移植元: scripts/_explain.py _mu_score() の `score` と同じ式。
 */
function _scoreOf(v: Verdict): number {
  const myHits = v.myHits ?? 999;
  const oppHits = v.oppHits ?? 999;
  return (oppHits - myHits) + (v.fast ? 0.5 : -0.5);
}

/**
 * 相手の複数型(≤3)を踏まえた集約判定。移植元: scripts/_explain.py matchup_grid()。
 * 各型についてjudge1v1でスコアを求め、
 *   sym = _scoreSym(平均スコア)
 *   dep = _scoreSym(最悪スコア) !== _scoreSym(最良スコア)  （型により有利不利のシンボルが割れる）
 * を移植元と同一のロジックで算出する。opps は resolveTarget 済みの相手の各型(≤3)。
 */
export function judgeVsBuilds(me: ResolvedBuild, opps: ResolvedBuild[]): AggregateVerdict {
  const verdicts = opps.map((opp) => judge1v1(me, opp));
  const scores = verdicts.map(_scoreOf);
  const mean = scores.reduce((a, b) => a + b, 0) / scores.length;
  const sym = _scoreSym(mean);
  const dep = _scoreSym(Math.min(...scores)) !== _scoreSym(Math.max(...scores));
  return { sym, dep, verdicts };
}

/**
 * 技1本の16段階ダメージ乱数分布(85〜100%の1%刻み、calcDamageのrandomRoll=i/15と対応)。
 * scripts/simulator/damage.py の `random.choice([85..100])/100` と同じ16通りを、
 * calcDamage(既存関数・挙動変更なし)を16回呼んで再現する。
 */
function _hitDamageDistribution(attacker: ResolvedBuild, move: ResolvedMove, defender: ResolvedBuild): number[] {
  const out: number[] = [];
  for (let i = 0; i <= 15; i++) out.push(calcDamage(attacker, defender, move, { randomRoll: i / 15 }));
  return out;
}

/**
 * n発(各発が独立に16段階乱数からiidで選ばれる前提)の合計ダメージがthreshold以上になる確率(0〜1)を、
 * ダメージ値分布の畳み込みDPで正確に計算する(16^nの近似ではなく厳密値。nが小さい前提での状態数管理)。
 */
function _nHitKoProbability(dist16: number[], hits: number, threshold: number): number {
  let dp = new Map<number, number>();
  for (const d of dist16) dp.set(d, (dp.get(d) ?? 0) + 1);
  for (let h = 1; h < hits; h++) {
    const next = new Map<number, number>();
    for (const [sum, cnt] of dp) {
      for (const d of dist16) {
        const s2 = sum + d;
        next.set(s2, (next.get(s2) ?? 0) + cnt);
      }
    }
    dp = next;
  }
  let total = 0;
  let ok = 0;
  for (const [sum, cnt] of dp) {
    total += cnt;
    if (sum >= threshold) ok += cnt;
  }
  return total > 0 ? ok / total : 0;
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
 *   - 異なる場合は baseHitsHi 発で相手の有効HPを超える確率を16段階乱数の畳み込みDPで算出 → 「乱数n発(p%)」
 *   - baseHitsHi が実用上限(PROB_HITS_CAP)を超える場合は畳み込みを省略し、保守的な baseHitsLo 側の
 *     「確n」表示にフォールドバックする(発数が多い場面では確率の精密表示より安全側の目安を優先)
 * 耐え(ばけのかわ/がんじょう/きあいのタスキ)は _applySurvive と同じ規約で「素の確定数に+1」を
 * 表示用の発数にのみ適用する(確率は素のHP閾値に対する値のまま据え置き)。
 * 例: 素のHPに対し乱数1発(50%)の技を持つ相手がきあいのタスキを持つ場合 → 表示は「乱数2発(50%)」。
 * これは1発目を必ず耐える(HP1で確定生存)ため実質2発必要になるが、2発目は残りHP1に対して
 * ほぼ確実に当たる(乱数最低でもダメージ>0なら止め刺せる)ため、真の合成確率は本来やや高くなる。
 * 本実装は _mu_score/_apply_survive が採用する「耐え=固定+1発、確率は素のまま」という単純化と
 * 矛盾しないよう、あえて確率を再計算せずhitsのみ+1する設計にしている(既存の判定ロジックとの整合を優先)。
 */
function _hitDetailForMove(attacker: ResolvedBuild, move: ResolvedMove, defender: ResolvedBuild): MoveHitDetail {
  const NONE: MoveHitDetail = { n: move.n, dmgLo: null, dmgHi: null, pctLo: null, pctHi: null, hits: null, prob: null, certain: true };
  if (move.cat === "status") return NONE;

  const dmgLo = calcDamage(attacker, defender, move, { randomRoll: 0 });
  const dmgHi = calcDamage(attacker, defender, move, { randomRoll: 1 });
  if (dmgHi <= 0) return NONE;

  const hp = Math.max(1, defender.stats[0]);
  const pctLo = (dmgLo / hp) * 100;
  const pctHi = (dmgHi / hp) * 100;
  const baseHitsLo = _hits(dmgLo / hp);
  const baseHitsHi = _hits(dmgHi / hp);

  if (baseHitsLo === baseHitsHi || baseHitsHi > PROB_HITS_CAP) {
    const hits = _applySurvive(baseHitsLo, defender);
    return { n: move.n, dmgLo, dmgHi, pctLo, pctHi, hits, prob: null, certain: true };
  }

  const dist = _hitDamageDistribution(attacker, move, defender);
  const prob = _nHitKoProbability(dist, baseHitsHi, hp) * 100;
  const hits = _applySurvive(baseHitsHi, defender);
  return { n: move.n, dmgLo, dmgHi, pctLo, pctHi, hits, prob, certain: false };
}

/**
 * 仮想敵カード用: 自分の技それぞれ(最大4)がoppに対し確定/乱数何発かの一覧(与ダメ実数値・HP比込み)。
 * judge1v1と同じ耐え補正(ばけのかわ/がんじょう/きあいのタスキ)込みの確定数/乱数発数。
 * 変化技・無効(ダメージ0)はhits:null(UI側で「—」表示)。
 */
export function moveBreakdown(me: ResolvedBuild, opp: ResolvedBuild): MoveHitDetail[] {
  return me.moves.map((mv) => _hitDetailForMove(me, mv, opp));
}
