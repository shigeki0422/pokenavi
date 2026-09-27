// 1v1判定。ダメージ・確定数・実効素早さといったルールは全て対戦エンジン(Rust/wasm)が持ち、
// このファイルは表示のための計算（割合%・記号◎○△▲×の閾値・確率の書式）だけを担う。
//
// 以前はここと damage.ts が simulator/damage.py・battle.py の移植版を持っていたが、
// 「同じ判定が Python と TypeScript に二重実装されていて、片方の修正がもう片方に伝わらない」
// ことがバグの発生源だった（ばけのかわ・マルチスケイル・天候・フィールド・いかく・
// 半減きのみの消費・ロール引数の取り違えが順に表面化した）。ルールを一箇所に集約するため、
// 判定本体は engine/wasm.ts 経由でエンジンを実走させる。
import type { AggregateVerdict, ResolvedBuild, ResolvedMove, Verdict } from "./types";
import { analyze, buildToSpec, koProb, scenarioKey, typeDynamic,
         type EngineMove, type EngineSide, type EngineVerdict } from "../engine/wasm";
import { eff } from "./typechart";

/**
 * 旧式: score>=1.5→◎ … の閾値が0.5刻みだったため、素早さの±0.5補正だけで
 * 「確定2 vs 確定1・先手」のような明確な負けが
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
  /** 毎ターン最善手を選び直した場合の手数と技の並び。 */
  seqHits: number;
  seq: string[];
  /** 判定の対戦の毎ターンの与ダメージ(実数値)・回復量・ひるみ・技以外の増減など（エンジンが返すまま）。 */
  turns: EngineSide["turns"];
};

/** 対面の評価結果。場は対面ごとに1つなので、両方向をまとめて1回で求める。 */
type Pair = { a: Evaluated; b: Evaluated; specA: string; specB: string; verdict: EngineVerdict };

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
/** 事前除外から外す技・特性。本体はエンジンが返す表で、ここに直書きしているのは
 * 「エンジン側ではタイプ固定だが、持ち物や形態でタイプが変わりうる」技だけ。
 * 手で並べた表だけにしていたとき だいちのはどう・レイジングブル・うるおいボイスが
 * 抜けていて、サイコフィールドのだいちのはどうが計算前に落ちていた。 */
const EXTRA_TYPE_VARIABLE_MOVES = [
  "めざめるダンス", "さばきのつぶて", "テクノバスター", "マルチアタック", "オーラぐるま",
];

let typeDyn: { moves: Set<string>; abilities: Set<string> } | null = null;
function typeDynSets(): { moves: Set<string>; abilities: Set<string> } {
  if (!typeDyn) {
    const t = typeDynamic();
    typeDyn = {
      moves: new Set([...t.moves, ...EXTRA_TYPE_VARIABLE_MOVES]),
      abilities: new Set(t.abilities),
    };
  }
  return typeDyn;
}

/**
 * タイプ相性で0倍になる攻撃技をエンジンに渡す前に落とす。
 *
 * 倒せない技ほど打ち切りまで実走する（無効技は毎回上限ターンぶん回る）ので、
 * 明らかに0と分かる技を送らないだけで実走回数が目に見えて減る。
 * 落とした技は「—」として表示に戻すため、見た目は変わらない。
 * 特性由来の無効（ふゆう・ちくでん等）は型では判定できないのでそのまま送る。
 */
function _poolEntries(attacker: ResolvedBuild, defender: ResolvedBuild) {
  const src = (attacker.pool && attacker.pool.length ? attacker.pool : attacker.moves) ?? [];
  const dyn = typeDynSets();
  const bend = dyn.abilities.has(attacker.ability);
  return src.map((m) => ({
    m,
    pruned: !bend && !dyn.moves.has(m.n)
      && m.cat !== "status" && typeof m.power === "number" && (m.power as number) > 0
      && eff(m.type, defender.t1, defender.t2) === 0,
  }));
}

/**
 * 対面の評価結果の使い回し。キーはエンジンに渡す spec そのものなので、
 * 「いつ捨てるか」の判断が要らない(spec が違えば別のキーになる)。
 * EV を1振り動かして変わるのは触った1匹の spec だけなので、6匹×31列のうち
 * 再計算されるのはその1匹の31列だけになる。
 */
const PAIR_CACHE_MAX = 4000;
const _pairCache = new Map<string, Pair>();

/** キャッシュの当たり外れ。効いているかを画面から確認できるようにしておく
 * (キャッシュは間違っていても速いので、動作確認の手掛かりが要る)。 */
export const pairCacheStats = {
  hit: 0, miss: 0,
  size: () => _pairCache.size,
  keys: (): string[] => [..._pairCache.keys()],
  /** 計測用。空にして計算し直させる。 */
  clear(): void {
    _pairCache.clear();
    pairCacheStats.hit = 0;
    pairCacheStats.miss = 0;
  },
};

function _pair(me: ResolvedBuild, opp: ResolvedBuild): Pair {
  const entA = _poolEntries(me, opp);
  const entB = _poolEntries(opp, me);
  const specA = buildToSpec({ ...me, moves: entA.filter((e) => !e.pruned).map((e) => e.m) });
  const specB = buildToSpec({ ...opp, moves: entB.filter((e) => !e.pruned).map((e) => e.m) });
  // 前提(天候・フィールド・積み)が違えば別の計算なのでキーに混ぜる
  const key = `${scenarioKey()}\u0001${specA}\u0001${specB}`;
  const hit = _pairCache.get(key);
  if (hit) {
    // 参照し直したものを末尾に送る(溢れたときに古いものから落とすため)
    _pairCache.delete(key);
    _pairCache.set(key, hit);
    pairCacheStats.hit++;
    return hit;
  }
  pairCacheStats.miss++;
  const r = analyze(specA, specB);
  // エンジンが返す並びは「落としたあと」の並び。idx は koProb がこの spec を再利用するため
  // 落としたあとの位置でなければならない。表示は元の並びに戻す。
  const side = (x: typeof r.a, ent: ReturnType<typeof _poolEntries>): Evaluated => {
    const moves: (EngineMove & { idx: number })[] = [];
    let k = 0;
    for (const e of ent) {
      if (e.pruned) moves.push({ n: e.m.n, dmg: null, idx: -1 } as EngineMove & { idx: number });
      else { moves.push({ ...x.moves[k], idx: k }); k++; }
    }
    return { hp: x.hp, speed: x.speed, moves, seqHits: x.seqHits, seq: x.seq, turns: x.turns ?? [] };
  };
  const pair: Pair = { a: side(r.a, entA), b: side(r.b, entB), specA, specB, verdict: r.verdict };
  _pairCache.set(key, pair);
  if (_pairCache.size > PAIR_CACHE_MAX) {
    _pairCache.delete(_pairCache.keys().next().value as string);
  }
  return pair;
}

/**
 * 最大打点技。Python の `_mu_engine._best_cached` と同じ「発数が少ない順、同数なら火力が高い順」。
 * 同数のときの比較には firstLo（1ターン目のHP減少）を使う。表示用の dmgLo は技そのものの
 * ダメージで、ばけのかわ・天候・回復のぶんだけ firstLo と食い違うため、ここで使うと
 * 正本と違う技を選んでしまう（実測で 395対面中23件ずれた）。
 */
function _best(e: Evaluated): (EngineMove & { idx: number }) | null {
  // エンジンが選んだ最大打点技（同じ確定数なら反動等の不利益が無い技・命中率の高い技）。判定の対戦で撃つ技と揃える。
  const flagged = e.moves.find((m) => m.best && m.dmg !== null && m.hitsLo !== undefined);
  if (flagged) return flagged;
  let best: (EngineMove & { idx: number }) | null = null;
  for (const m of e.moves) {
    if (m.dmg === null || m.hitsLo === undefined) continue;
    if (!best || m.hitsLo < best.hitsLo! || (m.hitsLo === best.hitsLo && (m.firstLo ?? 0) > (best.firstLo ?? 0))) {
      best = m;
    }
  }
  return best;
}

/** エンジンの前提文を表示用に言い換える（「最大3ヒット時」「3ヒット時」→連続技の回数の仮定）。工房の技の行と共通。 */
export function condText(c: string | null | undefined, lang: "ja" | "en" | "ko"): string {
  if (!c) return "";
  return String(c).split("・").map((x) => {
    let m = /^最大(\d+)ヒット時$/.exec(x);
    if (m) return lang === "en" ? `all ${m[1]} hits land` : lang === "ko" ? `${m[1]}회 모두 명중 가정` : `${m[1]}発すべて命中を想定`;
    m = /^(\d+)ヒット時$/.exec(x);
    if (m) return lang === "en" ? `${m[1]} hits (expected value for 2-5 hit moves)` : lang === "ko" ? `${m[1]}회 가정(2~5회 기술의 기대값)` : `${m[1]}発を想定（2〜5回技の期待値）`;
    if (lang === "ja") return x;
    m = /^(攻撃|特攻)([+-]\d+)$/.exec(x);
    if (m) return `${COND_TERMS[m[1]][lang]} ${m[2]}`;
    return COND_TERMS[x]?.[lang] ?? x;
  }).join(lang === "en" ? ", " : lang === "ko" ? "·" : "・");
}
/** 前提に出る天候・フィールド・能力の名前の訳。 */
const COND_TERMS: Record<string, { en: string; ko: string }> = {
  晴れ: { en: "Sun", ko: "쾌청" }, 雨: { en: "Rain", ko: "비" }, すなあらし: { en: "Sandstorm", ko: "모래바람" },
  あられ: { en: "Hail", ko: "싸라기눈" }, ゆき: { en: "Snow", ko: "눈" },
  エレキフィールド: { en: "Electric Terrain", ko: "일렉트릭필드" }, グラスフィールド: { en: "Grassy Terrain", ko: "그래스필드" },
  サイコフィールド: { en: "Psychic Terrain", ko: "사이코필드" }, ミストフィールド: { en: "Misty Terrain", ko: "미스트필드" },
  攻撃: { en: "Atk", ko: "공격" }, 特攻: { en: "SpA", ko: "특공" },
};

/** ダメージレースの「技以外のHP減少」の原因。エンジンが対戦中に記録した kind を、見た目のカテゴリと名前にする。
 * cat: self=自分の行動による自傷（反動・いのちのたま・ゴツゴツメット等）/ weather=天候 / status=状態異常 / disguise=ばけのかわ / other */
const CAUSES: Record<string, { cat: string; ja: string; en: string; ko: string; sja: string; sen: string; sko: string }> = {
  recoil: { cat: "self", ja: "技の反動", en: "Recoil", ko: "기술 반동", sja: "反", sen: "R", sko: "반" },
  lifeorb: { cat: "self", ja: "いのちのたまの反動", en: "Life Orb recoil", ko: "생명의구슬 반동", sja: "玉", sen: "LO", sko: "구" },
  helmet: { cat: "self", ja: "ゴツゴツメット", en: "Rocky Helmet", ko: "울퉁불퉁멧", sja: "メ", sen: "RH", sko: "멧" },
  roughskin: { cat: "self", ja: "さめはだ・てつのトゲ", en: "Rough Skin / Iron Barbs", ko: "까칠한피부·철가시", sja: "肌", sen: "RS", sko: "피" },
  liquidooze: { cat: "self", ja: "ヘドロえき", en: "Liquid Ooze", ko: "해감액", sja: "液", sen: "LQ", sko: "액" },
  other: { cat: "self", ja: "自分の行動によるダメージ", en: "Self-inflicted", ko: "자신의 행동에 의한 대미지", sja: "自", sen: "S", sko: "자" },
  recoilEtc: { cat: "self", ja: "反動など", en: "Recoil etc.", ko: "반동 등", sja: "反", sen: "R", sko: "반" },
  sandstorm: { cat: "weather", ja: "すなあらし", en: "Sandstorm", ko: "모래바람", sja: "砂", sen: "SS", sko: "모" },
  weather: { cat: "weather", ja: "天候", en: "Weather", ko: "날씨", sja: "天", sen: "W", sko: "날" },
  poison: { cat: "status", ja: "どく", en: "Poison", ko: "독", sja: "毒", sen: "PSN", sko: "독" },
  badpoison: { cat: "status", ja: "もうどく", en: "Toxic", ko: "맹독", sja: "毒", sen: "TOX", sko: "독" },
  burn: { cat: "status", ja: "やけど", en: "Burn", ko: "화상", sja: "火", sen: "BRN", sko: "화" },
  status: { cat: "status", ja: "状態異常", en: "Status", ko: "상태 이상", sja: "状", sen: "ST", sko: "상" },
  sludge: { cat: "other", ja: "くろいヘドロ", en: "Black Sludge", ko: "검은진흙", sja: "泥", sen: "BS", sko: "진" },
  disguise: { cat: "disguise", ja: "ばけのかわが剥がれた（1/8）", en: "Disguise busted (1/8)", ko: "탈이 벗겨짐(1/8)", sja: "皮", sen: "D", sko: "탈" },
  bind: { cat: "other", ja: "まとわりつく等のしめつけ", en: "Binding (Infestation etc.)", ko: "조이기(엉겨붙기 등)", sja: "縛", sen: "BND", sko: "속" },
  leechseed: { cat: "other", ja: "やどりぎのタネ", en: "Leech Seed", ko: "씨뿌리기", sja: "宿", sen: "LS", sko: "씨" },
  saltcure: { cat: "other", ja: "しおづけ", en: "Salt Cure", ko: "소금절이", sja: "塩", sen: "SC", sko: "소" },
  curse: { cat: "other", ja: "のろい", en: "Curse", ko: "저주", sja: "呪", sen: "CRS", sko: "저" },
  eot: { cat: "other", ja: "ターン終了時のダメージ", en: "End-of-turn damage", ko: "턴 종료 시 대미지", sja: "終", sen: "E", sko: "종" },
};
export function causeCat(kind: string): string { return CAUSES[kind]?.cat ?? "other"; }
export function causeLabel(kind: string, lang: "ja" | "en" | "ko"): string {
  const c = CAUSES[kind]; return c ? (lang === "en" ? c.en : lang === "ko" ? c.ko : c.ja) : kind;
}
export function causeShort(kind: string, lang: "ja" | "en" | "ko"): string {
  const c = CAUSES[kind]; return c ? (lang === "en" ? c.sen : lang === "ko" ? c.sko : c.sja) : "";
}

/** ダメージレースの棒の1区間。sub=move(技)/disguise/原因名/heal。lbl は起こした行動の番号（後から動いた行動は 1'）。 */
export interface BarItem {
  sub: string; dmg: number; heal: number; lbl: string; turn: number;
  move?: string | null; pctLo?: number | null; pctHi?: number | null;
  /** そのターンの中で先に動いた行動(first)・後から動いた行動(late)・ターン終了時(eot)のどれに伴う区間か */
  order?: "first" | "late" | "eot";
}

const ORDER_TXT = {
  ja: { late: "後", tag: (t: number, o?: string) => `T${t}${o === "late" ? "・後攻" : o === "first" ? "・先攻" : o === "eot" ? "・ターン終了時" : ""}` },
  en: { late: "2nd", tag: (t: number, o?: string) => `T${t}${o === "late" ? " · moved 2nd" : o === "first" ? " · moved 1st" : o === "eot" ? " · end of turn" : ""}` },
  ko: { late: "후", tag: (t: number, o?: string) => `T${t}${o === "late" ? " · 후공" : o === "first" ? " · 선공" : o === "eot" ? " · 턴 종료 시" : ""}` },
};
/** 棒の区間の中に出す「後から動いた」の小さな印。 */
export function lateMark(lang: "ja" | "en" | "ko"): string { return (ORDER_TXT[lang] ?? ORDER_TXT.ja).late; }
/** タップ詳細の見出し（例: T2・後攻）。ターン帯と揃える。 */
export function turnTag(it: BarItem, lang: "ja" | "en" | "ko"): string { return (ORDER_TXT[lang] ?? ORDER_TXT.ja).tag(it.turn, it.order); }

/** 判定の対戦の経過(race)から、HPの持ち主 owner の棒の区間を実際の発生順に並べる。
 * 相手の技のダメージはその行動の時点、自分の行動による自傷(反動・いのちのたま・さめはだ等)はその行動の直後、
 * ターン終了時のもの(天候・どく・たべのこし等)はそのターンの最後。番号は起こした行動の番号。
 * atkTurns は相手(=棒を削る側)の毎ターン行。技の幅(最低〜最高乱数)を引くために使う。 */
export function raceBarItems(race: NonNullable<Verdict["race"]>, owner: 0 | 1, hpOwner: number,
                             atkTurns: SeqStep[]): BarItem[] {
  const out: BarItem[] = [];
  const pct = (x: number) => (x / Math.max(1, hpOwner)) * 100;
  race.forEach((e, i) => {
    const late = e.actor != null && race.slice(0, i).some((f) => f.turn === e.turn && f.actor != null && f.actor !== e.actor);
    const lbl = `${e.turn}${late ? "'" : ""}`;
    const order = e.actor == null ? "eot" : late ? "late" : "first";
    for (const ev of e.events) {
      if (ev.side !== owner || ev.amount === 0) continue;
      if (ev.amount < 0) { out.push({ sub: "heal", dmg: 0, heal: pct(-ev.amount), lbl, turn: e.turn, order }); continue; }
      if (ev.kind === "move" || ev.kind === "disguise") {
        const row = atkTurns.find((r) => r.turn === e.turn && !r.flinch && !r.idle);
        out.push({ sub: ev.kind, dmg: pct(ev.amount), heal: 0, lbl, turn: e.turn, move: e.move,
                   pctLo: row?.pctLo ?? null, pctHi: row?.pctHi ?? null, order });
      } else {
        out.push({ sub: ev.kind, dmg: pct(ev.amount), heal: 0, lbl, turn: e.turn, order });
      }
    }
  });
  return out;
}

/** 毎ターン表示の番号。後から動いたターンは 1' のようにダッシュを付け、ひるんで動けなかったターンは番号を出さない。 */
export function stepLabel(s: SeqStep, i: number): string {
  if (s.flinch || s.idle) return "";
  return `${s.turn ?? i + 1}${s.late ? "'" : ""}`;
}

/** 反動など(技以外のHP減少)の番号。それを起こした行動と同じ番号にする。 */
export function extraLabel(x: { turn?: number; late?: boolean }, fallback: string): string {
  return x.turn != null ? `${x.turn}${x.late ? "'" : ""}` : fallback;
}

/** 判定の対戦で `att` 側が技で相手を倒したか（反動等の自滅は倒した扱いにしない）。 */
export function koByMove(race: Verdict["race"] | undefined, att: 0 | 1): boolean {
  const def = 1 - att;
  return !!race && race.some((e) => e.actor === att && e.hp[def] <= 0
    && e.events.some((x) => x.side === def && x.kind === "move" && x.amount > 0));
}

export function judge1v1(me: ResolvedBuild, opp: ResolvedBuild): Verdict {
  // 記号・勝敗・確定数・先後の決め方はすべてエンジン(analysis::analyze_json)にある。
  // ここで組み直すと、同じルールを提案API(Python)と工房(TS)で二重に持つことになり、
  // 実際に提案側だけ判定式が古いまま取り残されて結論が食い違った。
  const v = _pair(me, opp).verdict as EngineVerdict & Pick<Verdict, "draw" | "stall">;
  return { ...v, stub: false };
}

/** Verdict(judge1v1の返却値)からスコアを再算出する(judgeVsBuildsの集約専用)。 */
function _scoreOfVerdict(v: Verdict): number {
  return v.score;
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
  const weights: number[] = [];
  // 型の重み＝種全体に占める型の割合。割合の無い型（型プールに無い種・工房で編集した型）は等しく扱う。
  // 等しく平均すると、多数派の型で勝てても少数派の2型で負ければ不利になっていた（ボーマンダ）
  const w = (b: ResolvedBuild, all: ResolvedBuild[]) => (all.every((x) => x.weight && x.weight > 0) ? b.weight! : 1);
  for (const me of mes) for (const opp of opps) {
    verdicts.push(judge1v1(me, opp));
    weights.push(w(me, mes) * w(opp, opps));
  }
  if (!verdicts.length) throw new Error("judgeVsBuildsMulti: 型が空です");
  const scores = verdicts.map(_scoreOfVerdict);
  const wsum = weights.reduce((a, b) => a + b, 0);
  const mean = scores.reduce((a, sc, i) => a + sc * weights[i], 0) / wsum;
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
  /** タイプ相性の倍率（0=無効）。変化技などは null。 */
  eff?: number | null;
}

/** 手順の各手。%は技そのものの値(単発行と同じ基準)で、確定数は手順全体で1つなので持たない。 */
export interface SeqStep {
  n: string;
  pctLo: number | null;
  pctHi: number | null;
  conds: string | null;
  /** そのターンに相手が回復した量(最大HP比%)。オボンのみ・たべのこし等。 */
  healPct?: number | null;
  /** ひるんで動けなかったターン。 */
  flinch?: boolean;
  /** 先に倒されて動けなかったが、そのターンに相手が反動等でHPを減らした行（行動は無い）。 */
  idle?: boolean;
  /** 技が特性で無効になった（ばけのかわ）。値は無効にした特性名。 */
  blocked?: string | null;
  /** 判定の対戦(中央乱数)で実際に減らしたHP(最大HP比%)。ダメージレースの棒の長さに使う。 */
  pctDealt?: number | null;
  /** 判定の対戦のターン番号と、そのターンに後から動いたか（表示は 1' のようにダッシュを付ける）。 */
  turn?: number;
  late?: boolean;
  /** そのターンに相手が技以外で減らしたHP(最大HP比%)。相手自身の反動・ゴツゴツメット・天候等。 */
  extra?: { kind: string; pct: number; turn?: number; late?: boolean }[];
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
  const eff = m.eff ?? null;
  const NONE: MoveHitDetail = { n: m.n, dmgLo: null, dmgHi: null, pctLo: null, pctHi: null,
                                hits: null, prob: null, certain: true, reason: null, conds, eff };
  if (m.dmg === null || m.dmgHi === undefined || m.dmgHi <= 0) return NONE;
  const dmgLo = m.dmgLo!, dmgHi = m.dmgHi;
  const lo = m.hitsLo!, hi = m.hitsHi!;
  const base = { n: m.n, dmgLo, dmgHi, pctLo: (dmgLo / hp) * 100, pctHi: (dmgHi / hp) * 100, conds, eff };

  // 最低乱数でも最高乱数でも同じ発数なら乱数の影響を受けない。実用上限を超える場合も、
  // 保証値である最低乱数側の「確n」を出す（判定行と食い違わせないため）。
  if (lo === hi || hi > PROB_HITS_CAP || lo >= OUT_OF_RANGE) {
    return { ...base, hits: lo, prob: null, certain: true, reason: _reason(defender, hp, dmgLo, lo) };
  }
  // 主表示は判定の対戦と同じ中央乱数で数えた発数。中央でも最低乱数と同じなら「確定」、
  // そうでなければ「乱数n発(その発数以内に倒せる確率)」。
  const mid = m.hitsMid ?? hi;
  if (mid === lo) {
    return { ...base, hits: lo, prob: null, certain: true, reason: _reason(defender, hp, dmgLo, lo) };
  }
  const prob = koProb(p.specA, p.specB, att, m.idx, mid) * 100;
  const reason = _reason(defender, hp, (dmgLo + dmgHi) / 2, mid);
  // 丸めで 100 に達した場合は「乱数n発(100%)」という矛盾表示を避けて確定扱いにする。
  if (prob >= 100) return { ...base, hits: mid, prob: null, certain: true, reason };
  return { ...base, hits: mid, prob, certain: false, reason };
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

/** 技ごとのダメージ幅(確定数は持たない)。仮想敵カードの技チップ用。 */
export interface MoveDamage {
  n: string;
  dmgLo: number; dmgHi: number;
  pctLo: number; pctHi: number;
  /** 計算の前提(天候・場・連続技の回数の仮定など)。無ければ null。 */
  conds: string | null;
  /** タイプ相性の倍率（0=無効）。 */
  eff?: number | null;
}

/**
 * 仮想敵カード用: 自分の各技→相手、相手の各技→自分のダメージ幅。同じ場の前提・同じ対面計算から取る。
 * ターンごとの変化や技の使い分けは確定数では表せないので、ここはダメージ幅だけを返し、
 * 勝敗に関わる数え方は1v1内訳の表(pairHitDetails)に任せる。変化技・無効(ダメージ0)は含めない。
 */
export function moveDamages(me: ResolvedBuild, opp: ResolvedBuild):
    { my: MoveDamage[]; opp: MoveDamage[]; myHasMoves: boolean; oppHasMoves: boolean } {
  const p = _pair(me, opp);
  const conv = (moves: Evaluated["moves"], hpDef: number): MoveDamage[] => moves
    .filter((m) => m.dmg !== null && m.dmgHi != null && m.dmgHi > 0)
    .map((m) => ({
      n: m.n, dmgLo: m.dmgLo!, dmgHi: m.dmgHi!,
      pctLo: (m.dmgLo! / hpDef) * 100, pctHi: (m.dmgHi! / hpDef) * 100,
      conds: _conds(m),
      eff: m.eff ?? null,
    }));
  return {
    my: conv(p.a.moves, p.b.hp), opp: conv(p.b.moves, p.a.hp),
    myHasMoves: p.a.moves.length > 0, oppHasMoves: p.b.moves.length > 0,
  };
}

/** 手順の各手を表示用にする。%は同名の技の単発計算をそのまま使う
 * (単発行と基準を揃える。実走のHP減少を使うと ばけのかわ・砂・回復まで技のダメージに見える)。 */
function _steps(e: Evaluated, cmpHits: number | null, hpDef: number): SeqStep[] {
  const seq = e.seq ?? [];
  const hits = e.seqHits ?? OUT_OF_RANGE;
  // 単発表示のほうが手数が少ないときは出さない。最大打点が乱数1発のとき手順に置き換えると
  // 「乱数1発(63%)」という判断材料が消えてしまう。
  if (new Set(seq).size < 2 || hits >= OUT_OF_RANGE || hits > (cmpHits ?? OUT_OF_RANGE)) return [];
  const names = seq;
  const byName = new Map(e.moves.map((m) => [m.n, m]));
  return names.map((n) => {
    const m = byName.get(n);
    const lo = m?.dmgLo, hi = m?.dmgHi;
    return {
      n,
      pctLo: lo == null ? null : (lo / hpDef) * 100,
      pctHi: hi == null ? null : (hi / hpDef) * 100,
      conds: m ? _conds(m) : null,
    };
  });
}

/** 毎ターンの与ダメージ（判定の対戦の経過どおり。倒れた後の行動は無い）。表の毎ターン表示は2件以上のときだけ使う。
 * %は防御側の最大HPに対する割合。防御上昇・積みなど、ターンごとに変わる値がそのまま出る。 */
function _turns(e: Evaluated, hpDef: number): SeqStep[] {
  if (!e.turns) return [];
  return e.turns.map((t) => ({
    n: t.n, pctLo: (t.lo / hpDef) * 100, pctHi: (t.hi / hpDef) * 100, conds: null,
    healPct: t.heal ? (t.heal / hpDef) * 100 : null,
    flinch: !!t.flinch, idle: !!t.idle,
    pctDealt: t.dealt != null ? (t.dealt / hpDef) * 100 : null,
    blocked: t.blocked ?? null,
    turn: t.turn, late: !!t.late,
    extra: (t.extra ?? []).map((x) => ({ kind: x.kind, pct: (x.amount / hpDef) * 100, turn: x.turn, late: x.late })),
  }));
}

/**
 * 対面の与ダメ・被ダメを、同じ場の前提で同時に求める。
 * 向きごとに別々に呼ぶと天候が食い違うため、表示する2行は必ずここから取る。
 */
export function pairHitDetails(me: ResolvedBuild, opp: ResolvedBuild):
    { my: MoveHitDetail | null; opp: MoveHitDetail | null;
      mySteps: SeqStep[]; oppSteps: SeqStep[]; myTurns: SeqStep[]; oppTurns: SeqStep[] } {
  const p = _pair(me, opp);
  // 判定の説明で「撃つ技」として出すのは判定の対戦で選んだ技（myMove/oppMove）。一覧の best は元のタイプで計算した最大打点で、
  // へんげんじざい等で判定側の技と違うことがある。
  const pick = (e: Evaluated, n: string | null | undefined) =>
    (n ? e.moves.find((m) => m.n === n && m.dmg !== null && m.hitsLo !== undefined) : undefined) ?? _best(e);
  const bm = pick(p.a, p.verdict?.myMove), bo = pick(p.b, p.verdict?.oppMove);
  const my = bm ? _detail(bm, p, 0, opp, p.b.hp) : null;
  const oppD = bo ? _detail(bo, p, 1, me, p.a.hp) : null;
  return {
    my,
    opp: oppD,
    mySteps: _steps(p.a, my?.hits ?? null, p.b.hp),
    oppSteps: _steps(p.b, oppD?.hits ?? null, p.a.hp),
    myTurns: _turns(p.a, p.b.hp),
    oppTurns: _turns(p.b, p.a.hp),
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
