// 1v1判定。ダメージ・確定数・実効素早さといったルールは全て対戦エンジン(Rust/wasm)が持ち、
// このファイルは表示のための計算（割合%・記号◎○△▲×の閾値・確率の書式）だけを担う。
//
// 以前はここと damage.ts が simulator/damage.py・battle.py の移植版を持っていたが、
// 「同じ判定が Python と TypeScript に二重実装されていて、片方の修正がもう片方に伝わらない」
// ことがバグの発生源だった（ばけのかわ・マルチスケイル・天候・フィールド・いかく・
// 半減きのみの消費・ロール引数の取り違えが順に表面化した）。ルールを一箇所に集約するため、
// 判定本体は engine/wasm.ts 経由でエンジンを実走させる。
import type { AggregateVerdict, ResolvedBuild, ResolvedMove, Verdict } from "./types";
import { analyze, buildToSpec, koProb, type EngineMove } from "../engine/wasm";

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

/** 確率計算を行う実用上限。これを超える発数は最低乱数側の「確n」表示にする。 */
const PROB_HITS_CAP = 5;
/** エンジンが「倒せない」を表す発数。 */
const OUT_OF_RANGE = 999;

type Evaluated = {
  hp: number; speed: number;
  moves: (EngineMove & { idx: number })[];
};

/** 対面の評価結果。場は対面ごとに1つなので、両方向をまとめて1回で求める。 */
type Pair = { a: Evaluated; b: Evaluated; specA: string; specB: string };

/** 天候の内部名を表示名にする。 */
const WEATHER_JP: Record<string, string> = {
  sunny: "晴れ", rain: "雨", sandstorm: "すなあらし", hail: "あられ",
};

/**
 * この技の数値に実際に効いた条件の表示文字列。
 * エンジンが「その条件を打ち消して計算し直し、値が変わるか」で判定した結果を並べるだけ。
 * 場に出ているものを無条件に並べると、無関係な計算にも注記が付く
 * （ミミッキュのウッドハンマー→カバルドンに「すなあらし」と出た。カバルドンは
 *  じめんで砂のダメージを受けず、砂は草技の威力にも効かない）。
 */
function _conds(m: EngineMove): string | null {
  const c = (m.conds ?? []).map((x) => WEATHER_JP[x] ?? x);
  return c.length ? c.join("・") : null;
}

/**
 * 対面(me, opp)を1回だけエンジンに投げ、両方向の評価を得る。
 *
 * 向きごとに投げ分けると、両者が天候特性を持つ対面（キュウコン vs ペリッパー等）で
 * 「後から出た側の天候が勝つ」規則により場が変わり、与ダメと被ダメで前提が食い違う
 * （実測でPythonと4対面ずれた）。並びは常に (me, opp) に固定する。
 *
 * 技は採用率TOP10プールをそのまま渡す。spec の技欄は4本に切り詰められない
 * （simulator/pokemon.py の override_moves と同じ）ので1回で全技を評価できる。
 */
function _pair(me: ResolvedBuild, opp: ResolvedBuild): Pair {
  const pool = (b: ResolvedBuild) => (b.pool && b.pool.length ? b.pool : b.moves) ?? [];
  const specA = buildToSpec({ ...me, moves: pool(me) });
  const specB = buildToSpec({ ...opp, moves: pool(opp) });
  const r = analyze(specA, specB);
  const side = (x: typeof r.a): Evaluated => ({
    hp: x.hp, speed: x.speed, moves: x.moves.map((m, j) => ({ ...m, idx: j })),
  });
  return { a: side(r.a), b: side(r.b), specA, specB };
}

/**
 * 最大打点技。Python の `_mu_engine._best_cached` と同じ「発数が少ない順、同数なら火力が高い順」。
 * 同数のときの比較には firstLo（1ターン目のHP減少）を使う。表示用の dmgLo は技そのものの
 * ダメージで、ばけのかわ・天候・回復のぶんだけ firstLo と食い違うため、ここで使うと
 * 正本と違う技を選んでしまう（実測で 395対面中23件ずれた）。
 */
function _best(e: Evaluated): (EngineMove & { idx: number }) | null {
  let best: (EngineMove & { idx: number }) | null = null;
  for (const m of e.moves) {
    if (m.dmg === null || m.hitsLo === undefined) continue;
    if (!best || m.hitsLo < best.hitsLo! || (m.hitsLo === best.hitsLo && (m.firstLo ?? 0) > (best.firstLo ?? 0))) {
      best = m;
    }
  }
  return best;
}

export function judge1v1(me: ResolvedBuild, opp: ResolvedBuild): Verdict {
  const { a, b } = _pair(me, opp);
  const myBest = _best(a);
  const oppBest = _best(b);

  const myHits = myBest?.hitsLo ?? OUT_OF_RANGE;
  const oppHits = oppBest?.hitsLo ?? OUT_OF_RANGE;
  const fast = a.speed > b.speed;
  const score = _scoreOf(myHits, oppHits, a.speed, b.speed, fast);

  return {
    sym: _scoreSym(score),
    win: myHits < oppHits || (myHits === oppHits && fast),
    fast,
    myS: a.speed,
    oppS: b.speed,
    myHits,
    oppHits,
    myMove: myBest?.n ?? null,
    oppMove: oppBest?.n ?? null,
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
  return _scoreOf(v.myHits ?? OUT_OF_RANGE, v.oppHits ?? OUT_OF_RANGE, v.myS, v.oppS, v.fast);
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
  return {
    sym: _scoreSym(mean),
    dep: _scoreSym(Math.min(...scores)) !== _scoreSym(Math.max(...scores)),
    verdicts,
  };
}

export interface MoveHitDetail {
  n: string;
  /** 最小乱数/最大乱数での与ダメ実数値。変化技・無効技はnull。 */
  dmgLo: number | null;
  dmgHi: number | null;
  /** 相手HPに対する割合(%)。dmgLo/dmgHiと対の関係。 */
  pctLo: number | null;
  pctHi: number | null;
  /** 表示用の確定数。certain=trueなら「確n」、falseなら「乱数n発」のn。 */
  hits: number | null;
  /** 乱数n発時のKO確率(%、0〜100)。certain=true、または無効技の場合はnull。 */
  prob: number | null;
  /** true=最小乱数でもhits発でKO(確定)。false=最大乱数ならhits発だが確率的(prob%)。 */
  certain: boolean;
  /**
   * 素のダメージだけで計算した発数より hits が増えている場合の要因（表示用）。
   * 「51〜61%なのに確定3」のように、%（生ダメージ）と発数（回復・耐え効果込み）で
   * 前提が違うことが読み手に伝わらない問題への対処。増えていなければ null。
   */
  reason: string | null;
  /**
   * このダメージ計算に効いた場の条件（天候・フィールド・入場時の能力変化）。
   * %がどの前提の数字かを示す。無ければ null。
   */
  conds: string | null;
}

/** 発数が生ダメージから素直に計算した値より増えているときの要因名。 */
function _reason(defender: ResolvedBuild, hp: number, dmg: number, hits: number): string | null {
  // 圏外は「倒せない」だけで、耐え効果が理由とは限らない
  // （ふいうちは相手が攻撃しない前提だと不発になる）。要因を挙げると誤った帰属になる。
  if (hits >= OUT_OF_RANGE) return null;
  const raw = dmg > 0 ? Math.ceil(hp / dmg) : OUT_OF_RANGE;
  if (hits <= raw) return null;
  const causes: string[] = [];
  if (["ばけのかわ", "がんじょう", "マルチスケイル", "ファントムガード"].includes(defender.ability)) {
    causes.push(defender.ability);
  }
  if (["きあいのタスキ", "たべのこし", "オボンのみ", "オレンのみ"].includes(defender.item)) {
    causes.push(defender.item);
  }
  return causes.length ? causes.join("・") : null;
}

function _detail(m: EngineMove & { idx: number }, p: Pair, att: number,
                 defender: ResolvedBuild, hp: number): MoveHitDetail {
  const conds = _conds(m);
  const NONE: MoveHitDetail = { n: m.n, dmgLo: null, dmgHi: null, pctLo: null, pctHi: null,
                                hits: null, prob: null, certain: true, reason: null, conds };
  if (m.dmg === null || m.dmgHi === undefined || m.dmgHi <= 0) return NONE;
  const dmgLo = m.dmgLo!, dmgHi = m.dmgHi;
  const lo = m.hitsLo!, hi = m.hitsHi!;
  const base = { n: m.n, dmgLo, dmgHi, pctLo: (dmgLo / hp) * 100, pctHi: (dmgHi / hp) * 100, conds };

  // 最低乱数でも最高乱数でも同じ発数なら乱数の影響を受けない。実用上限を超える場合も、
  // 保証値である最低乱数側の「確n」を出す（判定行と食い違わせないため）。
  // 連続回数が乱数で変わる技（2〜5回・ネズミざん）は、確率計算に回数の分布を
  // 畳み込めていないので「乱数n発(p%)」を出さず保証値の「確n」に寄せる。
  if (lo === hi || hi > PROB_HITS_CAP || lo >= OUT_OF_RANGE || m.varHits) {
    return { ...base, hits: lo, prob: null, certain: true, reason: _reason(defender, hp, dmgLo, lo) };
  }
  const prob = koProb(p.specA, p.specB, att, m.idx, hi) * 100;
  const reason = _reason(defender, hp, dmgHi, hi);
  // 発数 hi は最高乱数側の値なので確率は 100% 未満のはず。丸めで 100 に達した場合は
  // 「乱数n発(100%)」という矛盾表示を避けて確定扱いにする。
  if (prob >= 100) return { ...base, hits: hi, prob: null, certain: true, reason };
  return { ...base, hits: hi, prob, certain: false, reason };
}

/**
 * 仮想敵カード用: 自分の技それぞれがoppに対し確定/乱数何発かの一覧。
 * judge1v1と同じ確定数（耐え効果・ターン終了時の増減はエンジンが処理する）。
 * 変化技・無効(ダメージ0)はhits:null(UI側で「—」表示)。
 */
export function moveBreakdown(me: ResolvedBuild, opp: ResolvedBuild): MoveHitDetail[] {
  const p = _pair(me, opp);
  return p.a.moves.map((m) => _detail(m, p, 0, opp, p.b.hp));
}

/**
 * 対面の与ダメ・被ダメを、同じ場の前提で同時に求める。
 * 向きごとに別々に呼ぶと天候が食い違うため、表示する2行は必ずここから取る。
 */
export function pairHitDetails(me: ResolvedBuild, opp: ResolvedBuild):
    { my: MoveHitDetail | null; opp: MoveHitDetail | null } {
  const p = _pair(me, opp);
  const bm = _best(p.a), bo = _best(p.b);
  return {
    my: bm ? _detail(bm, p, 0, opp, p.b.hp) : null,
    opp: bo ? _detail(bo, p, 1, me, p.a.hp) : null,
  };
}

/** 攻撃側の最大打点技による与ダメ割合と確定数。被ダメ行は pairHitDetails を使うこと。 */
export function bestMoveHitDetail(attacker: ResolvedBuild, defender: ResolvedBuild): MoveHitDetail | null {
  return pairHitDetails(attacker, defender).my;
}

/**
 * 乱数n発の確率(%)を表示用文字列にする。Math.roundだけだと0.2%が「0%」、99.8%が「100%」となり
 * 「乱数なのに0%/100%」という矛盾表示になるため、境界は「<1」「>99」で示す。
 */
export function fmtKoProbPct(prob: number | null | undefined): string {
  const p = prob ?? 0;
  if (p < 1) return '<1';
  if (p > 99 && p < 100) return '>99';
  return String(Math.round(p));
}
