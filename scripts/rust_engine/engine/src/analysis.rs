//! 1v1 表示のためのルール層 API。Python の正本は `scripts/_mu_engine.py`。
//!
//! ここが担うのは「対戦本体を実走して確定数とダメージを得ること」だけで、
//! 割合(%)・乱数n発の確率・記号(◎○△▲×)の閾値といった表示計算は呼び出し側に置く。
//! ルールを持つ部分だけを一箇所に集めるのが目的で、表示計算を混ぜると
//! 「同じ判定が二重実装される」という当初の問題がここに再発する。
use crate::battle::{calc_hits, entry_effects, hit_damage, is_accuracy_chained, is_excluded_from_matchup,
                    split2, ActKind, Action, Battle, Side};
use crate::damage::Field;
use crate::pack::Pack;
use crate::poke::{build_poke, mega_evolve_poke, Poke};
use crate::rng::BRng;
use std::cell::{Cell, RefCell};
use std::collections::HashMap;

thread_local! {
    /// へんげんじざい/リベロの持ち主が先に動くとき、相手の攻撃は「持ち主が技を撃った後のタイプ」に当たる。
    /// 各方向を「防御側は動かない」前提で個別に走らせる分析では、防御側の型変化が起きないので、
    /// (型を変える側, その側が撃つ技名) を控えておき、相手の攻撃を計算するときだけ setup で先に適用する。
    static PRE_FORMS: RefCell<Vec<(usize, String)>> = RefCell::new(Vec::new());
    /// いま計算している攻撃側。PRE_FORMS の適用先を「攻撃側ではない方」に限るために使う。
    static CUR_ATT: Cell<usize> = Cell::new(usize::MAX);
}

/// これ以上かかる技は「圏外」。`_mu_engine.CAP` と同値。
/// 5ターンで決着が付かない対面は実戦では交代が挟まるため、そこまでを見る
/// (弱い技ほど打ち切りまで実走するので、上限は計算量にも直結する)。
pub const CAP: i64 = 5;
pub const OUT_OF_RANGE: i64 = 999;
/// ダメージ乱数の段階数（85%〜100% の16段）。
pub const ROLLS: usize = 16;

/// 1.0 ちょうど未満の最大の f64。`_mu_engine` の `math.nextafter(1.0, 0.0)` と同値。
/// 判定は全て `rng() < prob` なので、prob<1 の追加効果は不発、prob=1 の確定効果
/// （必中急所・りゅうせいぐんの特攻ダウン等）だけが発動する。1.0 を入れると
/// `1.0 < 1.0` が偽になり確定効果まで殺す（Python 側で実際に殺していた）。
const ALMOST_ONE: f64 = f64::from_bits(0x3FEF_FFFF_FFFF_FFFF);

/// 連続回数だけ別の値を返す乱数。「回数が抽選で決まる技かどうか」を実測で見分けるために使う。
struct ChoicesRng(i64);
impl BRng for ChoicesRng {
    fn random(&mut self) -> f64 { ALMOST_ONE }
    fn hit_continue(&mut self) -> f64 { 0.0 }
    fn choice(&mut self, _n: usize) -> usize { 0 }
    fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
    fn choices(&mut self) -> i64 { self.0 }
}

struct FixedRng;
impl BRng for FixedRng {
    fn random(&mut self) -> f64 { ALMOST_ONE }
    // 1発ごとの命中判定は必中扱い（always_hit と同じ前提）。外れて止まる技は
    // 常に最大回数まで当たる。ネズミざんが「1発しか当たらない前提」になって
    // 圏外と出るのを避ける。
    fn hit_continue(&mut self) -> f64 { 0.0 }
    fn choice(&mut self, _n: usize) -> usize { 0 }
    fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
    /// 連続技(2〜5発)の回数。重みは 3:3:1:1 で期待値がちょうど 3.0 なので、
    /// その期待値で固定する。最小の2発だと過小、最大の5発だと過大で、
    /// どちらも幅で示すと分布の偏り（4発・5発は各12.5%）を誤解させる。
    /// スキルリンクは calc_hits 側で先に5発と決まるのでここには来ない。
    fn choices(&mut self) -> i64 { 3 }
}

/// 正規化ロール（0.0=最低乱数, 1.0=最高乱数）。`calc_damage` は `0.85 + r*0.15` で使う。
#[inline]
pub fn roll_of(step: usize) -> f64 {
    step as f64 / (ROLLS - 1) as f64
}

/// 表示する条件が「実際にその数値へ効いたか」を確かめるために、場や能力変化を打ち消す指定。
#[derive(Clone, Copy, PartialEq)]
pub enum Suppress {
    None,
    Weather,
    Terrain,
    Stages,
}

fn setup_sup(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64, sup: Suppress,
) -> Battle {
    let mut bt = setup(pack, spec_a, spec_b, season, roll);
    match sup {
        Suppress::None => {}
        Suppress::Weather => {
            bt.field.weather = None;
            bt.field.weather_count = 0;
        }
        Suppress::Terrain => {
            bt.field.electric_terrain = false;
            bt.field.grassy_terrain = false;
            bt.field.psychic_terrain = false;
            bt.field.misty_terrain = false;
            bt.field.electric_terrain_count = 0;
            bt.field.grassy_terrain_count = 0;
            bt.field.psychic_terrain_count = 0;
            bt.field.misty_terrain_count = 0;
        }
        Suppress::Stages => {
            for i in 0..2 {
                let p = &mut bt.sides[i].party[0];
                for k in 0..7u8 {
                    p.set_stage(k, 0);
                }
            }
        }
    }
    bt
}

/// 組み立て済みの両者を返す。同じ対面なら spec のパースとメガ進化をやり直さない。
///
/// setup は技ごと・乱数ごとに呼ばれる（run_move×2・move_damage×2・relevant_conds で
/// 1技あたり5回、1対面で約70回）。中身は乱数値以外まったく同じなので、
/// build_poke のパースが 1v1 判定の実行時間の半分近くを占めていた。
fn prepared(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str) -> (Poke, Poke) {
    if let Some((ka, kb, ks, a, b)) = &pack.prepared {
        if ka == spec_a && kb == spec_b && ks == season {
            return (a.clone(), b.clone());
        }
    }
    let mut a: Poke = build_poke(pack, spec_a, season);
    let mut b: Poke = build_poke(pack, spec_b, season);
    {
        let p: &Pack = pack;
        mega_evolve_poke(p, &mut a);
        mega_evolve_poke(p, &mut b);
    }
    pack.prepared = Some((spec_a.to_string(), spec_b.to_string(), season.to_string(), a.clone(), b.clone()));
    (a, b)
}

fn setup(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64) -> Battle {
    let (a, b) = prepared(pack, spec_a, spec_b, season);
    let mut field = Field {
        roll_override: Some(roll),
        always_hit: true,
        // 「相手も攻撃してくる対面」で互いの最大打点を比べるのが1v1判定なので、
        // ふいうちのように相手の行動に依存する技も通る前提で評価する。
        assume_opp_attacks: true,
        ..Default::default()
    };
    let mut s1 = Side { party: vec![a], active_idx: 0, ..Default::default() };
    let mut s2 = Side { party: vec![b], active_idx: 0, ..Default::default() };
    {
        let p: &Pack = pack;
        entry_effects(p, &mut s1, 0, &mut field, &mut s2.party[0]);
        entry_effects(p, &mut s2, 1, &mut field, &mut s1.party[0]);
    }
    let mut bt = Battle::new(s1, s2, field);
    apply_scenario(pack, &mut bt);
    // 防御側の先行する型変化(へんげんじざい・リベロ)。攻撃側自身の型は変えない。
    let cur = CUR_ATT.with(|c| c.get());
    PRE_FORMS.with(|f| {
        for (side, name) in f.borrow().iter() {
            if *side == cur { continue; }
            let packr: &Pack = pack;
            let mv = bt.sides[*side].party[0].moves.iter()
                .find(|m| packr.intern.resolve(m.name) == name.as_str()).cloned();
            if let Some(mv) = mv {
                crate::battle::apply_pre_move_forms(packr, &mut bt.sides[*side].party[0], &mv);
            }
        }
    });
    bt
}

/// 「この状況なら」の指定を場と能力変化に反映する。
///
/// 天候・フィールドは特性由来のもの（すなおこし等）を上書きする。ユーザーが
/// 明示した前提のほうが優先されるべきで、残りターン数は判定の上限(CAP)より
/// 長く取って対面中は切れない扱いにする。
fn apply_scenario(pack: &mut Pack, bt: &mut Battle) {
    let sc = pack.scenario;
    if sc == crate::pack::Scenario::default() {
        return;
    }
    let we = &pack.sy.we;
    let w = match sc.weather {
        1 => Some(we.sunny), 2 => Some(we.rain), 3 => Some(we.sandstorm), 4 => Some(we.hail),
        _ => None,
    };
    if let Some(w) = w {
        bt.field.weather = Some(w);
        bt.field.weather_count = 99;
    }
    if sc.terrain != 0 {
        bt.field.electric_terrain = sc.terrain == 1;
        bt.field.grassy_terrain = sc.terrain == 2;
        bt.field.psychic_terrain = sc.terrain == 3;
        bt.field.misty_terrain = sc.terrain == 4;
        bt.field.electric_terrain_count = if sc.terrain == 1 { 99 } else { 0 };
        bt.field.grassy_terrain_count = if sc.terrain == 2 { 99 } else { 0 };
        bt.field.psychic_terrain_count = if sc.terrain == 3 { 99 } else { 0 };
        bt.field.misty_terrain_count = if sc.terrain == 4 { 99 } else { 0 };
    }
    if sc.boost > 0 {
        // 積む技が複数あることは稀なので、技欄の先頭にある積み技を使う。
        let packr: &Pack = pack;
        let p = &mut bt.sides[0].party[0];
        let boosts = p.moves.iter()
            .find_map(|m| crate::battle::self_boosts(packr, m.name)
                .filter(|v| v.iter().any(|(_, d)| *d > 0)));
        if let Some(v) = boosts {
            for (k, d) in v {
                let next = (p.stage(k) + d * sc.boost).clamp(-6, 6);
                p.set_stage(k, next);
            }
        }
    }
}

/// `att` 側が同じ技を撃ち続け、もう一方は行動しない。`_mu_engine._run_inner` と同じ手順。
///
/// 攻撃側を常に side0 に置くと、両者が天候特性を持つ対面（キュウコン vs ペリッパー等）で
/// 「後から出た側の天候が勝つ」規則により、評価する向きで場が変わってしまう。
/// 場は対面ごとに1つなので、並び (spec_a, spec_b) は固定したまま攻撃側だけを指定する。
fn drive(bt: &mut Battle, pack: &Pack, att: usize, move_idx: usize, max_turns: i64) -> i64 {
    drive_rng(bt, pack, att, move_idx, max_turns, &mut FixedRng)
}

fn drive_rng(bt: &mut Battle, pack: &Pack, att: usize, move_idx: usize, max_turns: i64,
             rng: &mut dyn BRng) -> i64 {
    let mut turns = 0i64;
    bt.run_loop_lim(pack, rng, max_turns, |b2, _r| {
        turns += 1;
        let mv = b2.sides[att].active().moves.get(move_idx).cloned();
        let act = Action { kind: ActKind::Move, mv, move_idx: move_idx as i64, ..Default::default() };
        if att == 0 { [act, Action::default()] } else { [Action::default(), act] }
    }, |_| {});
    turns
}

/// 毎ターン、その時点の局面で一番良い技を選び直して倒すまでの手数と、選んだ技の並び。
///
/// 「同じ技を撃ち続ける」前提だと実戦と食い違う対面がある。
///   - であいがしら等の初手限定技は2ターン目以降失敗するので、単独では圏外になる
///     （実際は であいがしら→ふいうち のように繋ぐ）
///   - ふうせんは1発当てると割れるので、割ってから地面技が通る
/// 選択は「今のターンに倒せる技があればそれ（同点なら優先度の高い方）、無ければ
/// 一番削れる技」。倒しきれるなら先制技で先に倒す方が正しいため、優先度を火力より優先する。
/// 各手の評価は局面を複製して1ターン実際に動かして測る（技の失敗条件・道具の消費・
/// 能力変化まで対戦本体の規則がそのまま効く）。
pub fn run_best_sequence(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize, roll: f64,
) -> (i64, Vec<usize>) {
    // 一番削れる手を選ぶだけだと、げきりん等でロックされて遠回りになることがある
    // （ふうせんを割るのに げきりん を選ぶと2〜3ターン動けず、スケイルショットで割って
    //   じしん を通す線を逃す）。暴れ技を避ける線も走らせて短い方を採る。
    let (h1, s1) = greedy_sequence(pack, spec_a, spec_b, season, att, roll, false);
    let (h2, s2) = greedy_sequence(pack, spec_a, spec_b, season, att, roll, true);
    if h2 < h1 { (h2, s2) } else { (h1, s1) }
}

/// 暴れ技(げきりん等)は数ターン動けなくなるので、避けた線も比べられるようにする。
fn is_rampage(pack: &Pack, mv: &crate::damage::DMove) -> bool {
    let l = &pack.sy.l;
    mv.name == l.げきりん || mv.name == l.あばれる || mv.name == l.はなびらのまい || mv.name == l.だいふんげき
}

/// 今の局面で `att` が撃つ最善の攻撃技 (技, 削り, 優先度, 倒せた)。選び方は greedy_sequence と持久戦の両方で共有する。
fn best_attack(bt: &Battle, packr: &Pack, att: usize, avoid_rampage: bool)
    -> Option<(usize, i64, i64, bool)> {
    let def = 1 - att;
    let n_moves = bt.sides[att].active().moves.len();
    let hp_before = bt.sides[def].active().hp;
    // こだわり系(choice_locked_move)と げきりん等の暴れ技(locked_move)は技を変えられない。
    // 対戦本体は「指定された行動」をそのまま実行するのでロックを見てくれない。
    // ここで候補を絞らないと、スカーフで技を撃ち分ける成立しない手順が出る。
    let locked = {
        let p = bt.sides[att].active();
        p.choice_locked_move.or(p.locked_move)
    };
    let mut best: Option<(usize, i64, i64, bool)> = None; // (技, 削り, 優先度, 倒せた)
    for i in 0..n_moves {
        let Some(mv) = bt.sides[att].active().moves.get(i).cloned() else { continue };
        if let Some(lk) = locked {
            if mv.name != lk { continue; }
        } else if avoid_rampage && is_rampage(packr, &mv) {
            continue;
        }
        if mv.category == crate::pack::Cat::Status || mv.power.unwrap_or(0) <= 0
            || is_excluded_from_matchup(packr, &mv) {
            continue;
        }
        let mut probe = bt.clone();
        let step = probe.turn + 1;   // run_loop_lim の上限は累積ターン数
        drive(&mut probe, packr, att, i, step);
        let dealt = hp_before - probe.sides[def].active().hp;
        let ko = !probe.sides[def].active().is_alive;
        let prio = mv.priority;
        let better = match &best {
            None => dealt > 0 || ko,
            Some((_, bd, bp, bko)) => {
                if ko != *bko { ko }              // 倒せる手を最優先
                else if ko { prio > *bp || (prio == *bp && dealt > *bd) }  // 倒せるなら先制優先
                else { dealt > *bd }              // 倒せないなら一番削れる手
            }
        };
        if better {
            best = Some((i, dealt, prio, ko));
        }
    }
    best
}

fn greedy_sequence(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize, roll: f64,
    avoid_rampage: bool,
) -> (i64, Vec<usize>) {
    let def = 1 - att;
    let mut bt = setup(pack, spec_a, spec_b, season, roll);
    let packr: &Pack = pack;
    let mut seq: Vec<usize> = Vec::new();
    for _ in 0..CAP {
        if !bt.sides[def].active().is_alive {
            break;
        }
        let Some((mi, _, _, _)) = best_attack(&bt, packr, att, avoid_rampage) else { break };
        seq.push(mi);
        let step = bt.turn + 1;
        drive(&mut bt, packr, att, mi, step);
        if !bt.sides[def].active().is_alive {
            return (seq.len() as i64, seq);
        }
    }
    (OUT_OF_RANGE, seq)
}

/// 持久戦ルートの打ち切りターン数。
pub const STALL_CAP: i64 = 20;

fn is_heal_move(pack: &Pack, mv: &crate::damage::DMove) -> bool {
    let l = &pack.sy.l;
    let n = mv.name;
    n == l.なまける || n == l.じこさいせい || n == l.あさのひざし || n == l.こうごうせい
        || n == l.つきのひかり || n == l.はねやすめ || n == l.タマゴうみ || n == l.ミルクのみ
}

/// 技名の並びに どくどく と回復技の両方があるか。持久戦ルートを走らせるかの枝刈り。
fn stall_capable(pack: &Pack, moves: &[(String, bool)]) -> bool {
    let l = &pack.sy.l;
    let toxic = pack.intern.resolve(l.どくどく);
    let heals = [l.なまける, l.じこさいせい, l.あさのひざし, l.こうごうせい,
                 l.つきのひかり, l.はねやすめ, l.タマゴうみ, l.ミルクのみ]
        .map(|s| pack.intern.resolve(s));
    moves.iter().any(|(n, _)| n == toxic) && moves.iter().any(|(n, _)| heals.contains(&n.as_str()))
}

/// 両者が同時に行動する1ターンを実走する。
fn drive_pair(bt: &mut Battle, pack: &Pack, idx: [Option<usize>; 2]) {
    let mut rng = FixedRng;
    let lim = bt.turn + 1;
    bt.run_loop_lim(pack, &mut rng, lim, |b2, _r| {
        let mk = |side: usize| match idx[side] {
            Some(i) => Action {
                kind: ActKind::Move,
                mv: b2.sides[side].active().moves.get(i).cloned(),
                move_idx: i as i64,
                ..Default::default()
            },
            None => Action::default(),
        };
        [mk(0), mk(1)]
    }, |_| {});
}

/// 持久戦ルートの1ターンぶんの内訳。直接ダメージと毒ダメージ、ターン終了時のHPを分けて持つ
/// (毒は1/16,2/16…と累積するので、合計だけでは「どくどくが効いている」ことが読めない)。
pub struct StallTurn {
    pub n: String,
    /// 技が与える直接ダメージ(威力ベース。変化技は0)。
    pub direct: i64,
    /// このターン終了時の毒ダメージ。
    pub poison: i64,
    /// ターン終了時のバインド(まとわりつく等)のダメージ。
    pub bind: i64,
    /// このターンに防御側が回復した量(オボンのみ等の消費、たべのこし)。
    pub heal: i64,
    /// このターン終了時の防御側HP・攻撃側HP。
    pub def_hp: i64,
    pub att_hp: i64,
}

pub struct StallResult {
    pub turns: i64,
    pub seq: Vec<String>,
    pub trace: Vec<StallTurn>,
    pub def_max: i64,
    pub att_max: i64,
}

/// 持久戦ルート: `att` が どくどく で削りつつ回復技で粘って相手を倒す線。
///
/// 通常の判定は「互いに最大打点を撃ち続ける」ので、どくどく＋回復技の型は
/// 攻撃技が弱いだけで圏外と出て、実際には勝てる対面を取りこぼす。
/// どくどく＋回復技を持たない側は実走せず None を返す（枝刈り）。
/// 相手は毎ターン最善の攻撃技を撃ち続ける。返す手順は連続もそのまま並べる。
#[derive(Clone, Copy, PartialEq)]
pub enum StallOutcome { Win, Lose, Stuck }

/// 持久戦の実走。`need_heal` なら回復技も持つ側だけ(勝ち筋の判定)、そうでなければ どくどく さえ持てば
/// 走らせる(「勝てない対面でも、どくどくを入れた見込み」の表示用)。倒れた・倒しきれない場合も内訳を返す。
fn simulate_stall(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize, roll: f64, need_heal: bool,
    passive_def: bool, cap: i64,
) -> Option<(StallOutcome, StallResult)> {
    let def = 1 - att;
    let mut bt = setup(pack, spec_a, spec_b, season, roll);
    let packr: &Pack = pack;
    let (toxic_i, heal_i) = {
        let p = bt.sides[att].active();
        (p.moves.iter().position(|m| m.name == packr.sy.l.どくどく),
         p.moves.iter().position(|m| is_heal_move(packr, m)))
    };
    let Some(toxic_i) = toxic_i else { return None };
    if need_heal && heal_i.is_none() { return None; }
    let mut seq: Vec<String> = Vec::new();
    let mut trace: Vec<StallTurn> = Vec::new();
    let (def_max, att_max) = (bt.sides[def].active().max_hp, bt.sides[att].active().max_hp);
    for _ in 0..cap {
        if !bt.sides[att].active().is_alive {
            return None;
        }
        // passive_def: 相手は動かない前提(通常の1v1の各方向5ターンと同じ。相手に倒されるまでで打ち切らない)。
        let foe_best = if passive_def { None } else { best_attack(&bt, packr, def, false) };
        let att_hp = bt.sides[att].active().hp;
        let will_fall = foe_best.map_or(false, |(_, dealt, _, ko)| ko || dealt >= att_hp);
        let foe_clean = bt.sides[def].active().status.is_none();
        let pick = if foe_clean {
            toxic_i
        } else if will_fall && heal_i.is_some() && {
            // 相手が先に動くなら、回復する前に落ちるので無駄。自分が先でも、回復ぶんを足して耐えられないなら無駄。
            let foe_first = crate::ai::effective_speed(packr, bt.sides[def].active(), &bt.field)
                > crate::ai::effective_speed(packr, bt.sides[att].active(), &bt.field);
            !foe_first && foe_best.map_or(true, |(_, dealt, _, _)| dealt < (att_hp + att_max / 2).min(att_max))
        } {
            heal_i.unwrap()
        } else if let Some(x) = best_attack(&bt, packr, att, false) {
            x.0
        } else if let Some(h) = heal_i {
            h
        } else {
            break;
        };
        let locked = {
            let p = bt.sides[att].active();
            p.choice_locked_move.or(p.locked_move)
        };
        if let Some(lk) = locked {
            match bt.sides[att].active().moves.iter().position(|m| m.name == lk) {
                Some(i) if i == pick => {}
                _ => return None,
            }
        }
        let mut idx = [None, None];
        idx[att] = Some(pick);
        idx[def] = foe_best.map(|x| x.0);
        let (def_before, bound_before, item_before) = {
            let d = bt.sides[def].active();
            (d.hp, d.bound_count, d.item)
        };
        // 技の直接ダメージは、実行前の局面で威力ベースに測る(HPの増減から逆算すると、回復と混ざって分けられない)。
        let direct = match bt.sides[att].active().moves.get(pick).cloned() {
            Some(mv) if mv.category != crate::pack::Cat::Status && mv.power.unwrap_or(0) > 0 =>
                move_total_damage(packr, &mut bt.clone(), att, &mv, roll).min(def_before),
            _ => 0,
        };
        drive_pair(&mut bt, packr, idx);
        let name = bt.sides[att].active().moves.get(pick)
            .map(|m| packr.intern.resolve(m.name).to_string())?;
        // 毒ダメージ = 最大HP × 累積カウント/16（ターン終了時に入る。どくどくを撃ったターンにも1/16入る）。
        let (def_after, poison_now) = {
            let d = bt.sides[def].active();
            let poisoned = d.status == Some(packr.sy.st.badpoison);
            (d.hp, if poisoned { (d.max_hp * d.bad_poison_count / 16).max(1) } else { 0 })
        };
        let alive = bt.sides[def].active().is_alive;
        let poison = if alive { poison_now } else { poison_now.min((def_before - direct).max(0)) };
        // バインド: このターン終了時にカウントが減っていれば(撃ったターンに掛かった分も含む)ダメージが入っている。
        let (bound_after, band, item_after) = {
            let d = bt.sides[def].active();
            (d.bound_count, d.bound_by_band, d.item)
        };
        let ticked = (bound_before > 0 && bound_after < bound_before) || (bound_before == 0 && bound_after > 0);
        let bind = if ticked { (def_max / if band { 6 } else { 8 }).max(1) } else { 0 };
        // 回復: オボンのみ・オレンのみはこのターンに消費された分、たべのこしは持っている間。
        let it = &packr.sy.l;
        let mut heal = 0;
        if item_before.is_some() && item_after != item_before {
            if item_before == Some(it.オボンのみ) { heal += def_max / 4; }
            else if item_before == Some(it.オレンのみ) { heal += 10; }
        }
        if item_after == Some(it.たべのこし) { heal += (def_max / 16).max(1); }
        if !alive { heal = 0; }
        trace.push(StallTurn {
            n: name.clone(), direct, poison, bind, heal,
            def_hp: def_after, att_hp: bt.sides[att].active().hp,
        });
        seq.push(name);
        if !bt.sides[att].active().is_alive {
            return Some((StallOutcome::Lose, StallResult { turns: seq.len() as i64, seq, trace, def_max, att_max }));
        }
        if !bt.sides[def].active().is_alive {
            return Some((StallOutcome::Win, StallResult { turns: seq.len() as i64, seq, trace, def_max, att_max }));
        }
        if foe_clean && pick == toxic_i && bt.sides[def].active().status.is_none() {
            return None;
        }
    }
    if seq.is_empty() { return None; }
    Some((StallOutcome::Stuck, StallResult { turns: seq.len() as i64, seq, trace, def_max, att_max }))
}

/// 持久戦で勝てる線（どくどく＋回復技）。勝てなければ None。
pub fn run_stall_route(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize, roll: f64,
) -> Option<StallResult> {
    match simulate_stall(pack, spec_a, spec_b, season, att, roll, true, false, STALL_CAP) {
        Some((StallOutcome::Win, r)) => Some(r),
        _ => None,
    }
}

/// `spec_a` が `move_idx` の技を撃ち続けて `spec_b` を倒すまでの発数と、初撃の与ダメージ。
/// 倒しきれなければ発数は `OUT_OF_RANGE`。
pub fn run_move(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, roll: f64,
) -> (i64, i64) {
    run_move_sup(pack, spec_a, spec_b, season, att, move_idx, roll, Suppress::None)
}

pub fn run_move_sup(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, roll: f64, sup: Suppress,
) -> (i64, i64) {
    let def = 1 - att;
    let mut bt = setup_sup(pack, spec_a, spec_b, season, roll, sup);
    let hp0 = bt.sides[def].active().max_hp;
    // 初撃ダメージは1ターンだけ進めた時点で測る（2発目以降は自己ランク変化等で変わる）
    let packr: &Pack = pack;
    drive(&mut bt, packr, att, move_idx, 1);
    let first = hp0 - bt.sides[def].active().hp;
    let mut turns = 1i64;
    if bt.sides[def].has_alive() {
        turns += drive(&mut bt, packr, att, move_idx, CAP);
    }
    let hits = if bt.sides[def].has_alive() { OUT_OF_RANGE } else { turns };
    (hits, first.max(0))
}

/// 入場効果まで済ませた時点の、両者の実効素早さと最大HP・技名・能力変化。
pub struct SideInfo {
    pub hp: i64,
    pub speed: i64,
    pub moves: Vec<(String, bool)>, // (技名, ダメージ技か)
    /// 入場時に変化した攻撃/特攻ランク（いかく・ダウンロード等）。0なら変化なし。
    pub atk_stage: i32,
    pub spa_stage: i32,
}

/// 対面開始時に成立している場。ダメージ計算に効くので表示側で明示するために返す。
pub struct FieldInfo {
    pub weather: Option<String>,
    pub terrain: Option<String>,
}

pub fn field_info(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str) -> FieldInfo {
    let bt = setup(pack, spec_a, spec_b, season, 0.0);
    let f = &bt.field;
    let w = f.weather.map(|s| pack.intern.resolve(s).to_string());
    let t = if f.electric_terrain { Some("エレキフィールド") }
        else if f.grassy_terrain { Some("グラスフィールド") }
        else if f.psychic_terrain { Some("サイコフィールド") }
        else if f.misty_terrain { Some("ミストフィールド") }
        else { None };
    FieldInfo { weather: w, terrain: t.map(|x| x.to_string()) }
}

pub fn side_info(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str) -> (SideInfo, SideInfo) {
    let bt = setup(pack, spec_a, spec_b, season, 0.0);
    let packr: &Pack = pack;
    let one = |p: &Poke| SideInfo {
        atk_stage: p.stage(0),
        spa_stage: p.stage(2),
        hp: p.max_hp,
        speed: crate::ai::effective_speed(packr, p, &bt.field),
        moves: p
            .moves
            .iter()
            .map(|m| {
                (
                    packr.intern.resolve(m.name).to_string(),
                    m.category != crate::pack::Cat::Status
                        && m.power.unwrap_or(0) > 0
                        && !is_excluded_from_matchup(packr, m),
                )
            })
            .collect(),
    };
    (one(bt.sides[0].active()), one(bt.sides[1].active()))
}


/// `hits` 発以内に防御側を倒せる確率（0.0〜1.0）。各発のダメージ乱数は16段から
/// 独立に選ばれる前提で、局面を分岐させて厳密に数える。
///
/// ターン終了時の増減（たべのこし・オボンのみ・すなあらし・自分の反動）は
/// 対戦本体がそのまま処理するので、ここで再実装しない。以前 TypeScript 側が
/// この部分を独自に持っていたことが、確定数と表示の食い違いの発生源だった。
///
/// 枝は「防御側の残HPと持ち物」で畳む。攻撃側は同じ技を撃ち続けるため、
/// 同じターン数・同じ残HP・同じ持ち物に至った枝はその後の展開も等しい。
pub fn ko_probability(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, hits: usize,
) -> f64 {
    let def = 1 - att;
    let base = setup(pack, spec_a, spec_b, season, 0.0);
    let packr: &Pack = pack;
    let mut states: Vec<(Battle, f64)> = vec![(base, 1.0)];
    let mut ko = 0.0f64;
    for _ in 0..hits {
        let mut next: HashMap<(i64, Option<u16>), (Battle, f64)> = HashMap::new();
        for (bt, w) in states.into_iter() {
            let p = w / ROLLS as f64;
            for step in 0..ROLLS {
                let mut c = bt.clone();
                c.field.roll_override = Some(roll_of(step));
                let lim = c.turn + 1;
                drive(&mut c, packr, att, move_idx, lim);
                if !c.sides[def].has_alive() {
                    ko += p;
                    continue;
                }
                let key = { let d = c.sides[def].active(); (d.hp, d.item) };
                next.entry(key).and_modify(|e| e.1 += p).or_insert((c, p));
            }
        }
        states = next.into_values().collect();
        if states.is_empty() {
            break;
        }
    }
    ko
}


/// 技1回ぶんの与ダメージ（連続技は全ヒットの合計）。表示用。
///
/// 「1ターンで防御側の HP がいくら減ったか」ではなく「その技が与えるダメージ」を返す。
/// 前者を表示に使うと、ばけのかわで直撃が無効化された分・すなあらしの削り・
/// たべのこしの回復まで技のダメージとして出てしまう
/// （カバルドンのじしん→ミミッキュが「18〜18%」と表示された。内訳は身代わり16＋砂8）。
/// 発数の方は run_move（実走）で数えるので、耐え効果や回復はそちらに反映される。
/// 表示するダメージ。
///
/// 防御側が生き残り、かつ切り詰め（きあいのタスキ・がんじょう）も起きていない場合は、
/// 対戦本体に実際に撃たせた値をそのまま使う。連続技の合間に相手の特性が挟まる場合
/// （じきゅうりょくで2発目の防御が上がる等）は、本体の値だけが正しい。
/// 倒れる場合は本体がヒットループを止めてしまうので、そのときだけ自前の計算に落とす
/// （表示は「実際に与えた分」ではなく「その技の威力」なので、頭打ちにしない）。
pub fn move_damage(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, roll: f64,
) -> i64 {
    let (exec, alive, hp) = executed_damage(pack, spec_a, spec_b, season, att, move_idx, roll);
    if exec > 0 && alive && hp > 1 {
        return exec;
    }
    move_damage_sup(pack, spec_a, spec_b, season, att, move_idx, roll, Suppress::None)
}

/// 今の局面で技 `mv` が与えるダメージ（連続技は全ヒットの合計・威力ベース）。`bt` は書き換わるので複製を渡すこと。
fn move_total_damage(packr: &Pack, bt: &mut Battle, att: usize, mv: &crate::damage::DMove, roll: f64) -> i64 {
    // 技を撃つ直前の姿・タイプ変化（へんげんじざい・バトルスイッチ）。対戦本体と共有する
    crate::battle::apply_pre_move_forms(packr, &mut bt.sides[att].party[0], mv);
    let n = calc_hits(packr, mv, bt.sides[att].active(), &mut FixedRng);
    // 急所も対戦本体と同じ手順で決める。FixedRng なので crit_chance が 1.0 のものだけ
    // 急所になる＝確定数の前提と一致する（必中急所を落とすと確定数と食い違う）。
    let critical = {
        let a = &bt.sides[att].party[0];
        let d = &bt.sides[1 - att].party[0];
        let c = crate::battle::crit_chance(packr, a, mv, Some(d));
        FixedRng.random() < c
    };
    let mut total = 0i64;
    for hit_i in 0..n.max(1) {
        let Battle { sides, field, .. } = &mut *bt;
        let (sa, sd) = split2(sides, att);
        let att = &mut sa.party[0];
        let def = &mut sd.party[0];
        // 1発ぶんの計算は対戦本体と同じ関数を使う（何発目かの反映を含む）
        let mut r = FixedRng;
        let d = hit_damage(packr, att, def, mv, field, hit_i, critical, Some(roll), &mut r);
        total += d;
        // マルチスケイル等「満タンのときだけ」の効果を2発目以降に持ち越さないよう、
        // 連続技の各ヒットは HP を減らしながら計算する。倒れても止めない（威力を出すため）。
        def.hp = (def.hp - d).max(1);
    }
    total
}

/// 毎ターンの与ダメージ（最低乱数/最高乱数）。技の並び `seq` を1ターンずつ実走し、各ターンの開始局面で
/// その技が与えるダメージを測る（じきゅうりょくの防御上昇・積み・場の変化が2ターン目以降に効く）。
/// 経路は最低乱数（確定数の前提）で進め、その各局面で最低/最高乱数の値を出す。倒れた時点で止め、
/// 倒しきれなければ CAP ターンまで。回復・砂・たべのこし等のHP増減は含まない（技の威力を出すため）。
pub fn per_turn_damage(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize, seq: &[usize],
) -> Vec<(usize, i64, i64, i64)> {
    let mut bt = setup(pack, spec_a, spec_b, season, 0.0);
    let packr: &Pack = pack;
    let def = 1 - att;
    let mut out = Vec::new();
    for t in 0..CAP as usize {
        if !bt.sides[def].active().is_alive { break; }
        let Some(&mi) = seq.get(t).or(seq.last()) else { break };
        let Some(mv) = bt.sides[att].active().moves.get(mi).cloned() else { break };
        let lo = move_total_damage(packr, &mut bt.clone(), att, &mv, 0.0);
        let hi = move_total_damage(packr, &mut bt.clone(), att, &mv, 1.0);
        if lo <= 0 && hi <= 0 { break; }
        let (item_before, def_max) = { let d = bt.sides[def].active(); (d.item, d.max_hp) };
        let step = bt.turn + 1;
        drive(&mut bt, packr, att, mi, step);
        // このターンに防御側が回復した量(オボンのみ・オレンのみの消費、たべのこし)。倒れていれば0。
        let heal = {
            let d = bt.sides[def].active();
            let l = &packr.sy.l;
            let mut h = 0;
            if d.is_alive {
                if item_before.is_some() && d.item != item_before {
                    if item_before == Some(l.オボンのみ) { h += def_max / 4; }
                    else if item_before == Some(l.オレンのみ) { h += 10; }
                }
                if d.item == Some(l.たべのこし) { h += (def_max / 16).max(1); }
            }
            h
        };
        out.push((mi, lo, hi, heal));
    }
    out
}

/// 表示するダメージは「実際に与えた分」ではなく「その技の威力」。
/// execute_move は相手が倒れた時点でループを止めるため、そちらの合計は使えない
/// （トリプルアクセルが 199% → 101% と頭打ちになった）。ここでは対戦本体と同じ前処理を
/// 通したうえで、全ヒットぶんを計算する。
pub fn move_damage_sup(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, roll: f64, sup: Suppress,
) -> i64 {
    let mut bt = setup_sup(pack, spec_a, spec_b, season, roll, sup);
    let packr: &Pack = pack;
    let Some(mv) = bt.sides[att].active().moves.get(move_idx).cloned() else { return 0 };
    let total = move_total_damage(packr, &mut bt, att, &mv, roll);
    if total == 0 && mv.power.is_none() {
        // がむしゃらのように威力がDBに無く、対戦本体の中でHPから決まる技。
        // calc_damage は 0 を返すので、実際に撃たせた値を使う。
        // タイプ無効で0の技は威力を持つので、ここには来ない。
        let (d, _, _) = executed_damage(pack, spec_a, spec_b, season, att, move_idx, roll);
        return d;
    }
    total

}


/// この技の計算時に場に出ていた条件を返す。
///
/// 以前は「その条件を打ち消して計算し直し、与ダメか確定数が変わったときだけ効いたとみなす」
/// という実測方式だったが、技ごとに条件のぶんだけ再実走するため、1v1判定全体の
/// 約半分をこの注記の生成が占めていた（6匹×31体の描画で650ms中320ms）。
/// 場に出ているものをそのまま返す方式に変える。無関係な条件にも注記が付くが
/// （砂が草技の威力に効かない場合など）、表示のために計算を倍にする価値は無い。
pub fn relevant_conds(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize, move_idx: usize,
) -> Vec<String> {
    let bt = setup(pack, spec_a, spec_b, season, 0.0);
    let mut out = Vec::new();
    if let Some(w) = bt.field.weather {
        out.push(pack.intern.resolve(w).to_string());
    }
    let f = &bt.field;
    if f.electric_terrain { out.push("エレキフィールド".to_string()); }
    else if f.grassy_terrain { out.push("グラスフィールド".to_string()); }
    else if f.psychic_terrain { out.push("サイコフィールド".to_string()); }
    else if f.misty_terrain { out.push("ミストフィールド".to_string()); }
    {
        let p = &bt.sides[att].party[0];
        let a = p.stage(0);
        let c = p.stage(2);
        let mut v = Vec::new();
        if a != 0 { v.push(format!("攻撃{}{}", if a > 0 { "+" } else { "" }, a)); }
        if c != 0 { v.push(format!("特攻{}{}", if c > 0 { "+" } else { "" }, c)); }
        if !v.is_empty() { out.push(v.join("・")); }
    }
    // 連続技は回数を仮定しているので、その前提だけは明示する。
    if let Some(mv) = bt.sides[att].active().moves.get(move_idx) {
        let p = bt.sides[att].active();
        let hits = calc_hits(pack, mv, p, &mut FixedRng);
        let hits_alt = calc_hits(pack, mv, p, &mut ChoicesRng(5));
        if is_accuracy_chained(pack, mv) {
            out.push(format!("最大{}ヒット時", hits));
        } else if hits != hits_alt {
            out.push(format!("{}ヒット時", hits));
        }
    }
    out
}


/// 対戦本体に1回だけ技を撃たせ、(実際に与えたダメージ, 防御側の生存, 残HP) を返す。
/// 表示には使わない（相手が倒れるとそこで止まるため）。move_damage が
/// 対戦本体の前処理を取りこぼしていないかを機械的に確かめる監査用。
pub fn executed_damage(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, roll: f64,
) -> (i64, bool, i64) {
    let mut bt = setup(pack, spec_a, spec_b, season, roll);
    let packr: &Pack = pack;
    let Some(mv) = bt.sides[att].active().moves.get(move_idx).cloned() else { return (0, true, 0) };
    let act = Action { kind: ActKind::Move, mv: Some(mv), move_idx: move_idx as i64, ..Default::default() };
    let opp_mv = bt.sides[1 - att].active().moves.first().cloned();
    let opp_act = Action { kind: ActKind::Move, mv: opp_mv, move_idx: 0, ..Default::default() };
    let mut rng = FixedRng;
    let mut d = 0i64;
    {
        let Battle { sides, field, .. } = &mut bt;
        crate::battle::execute_move(packr, sides, field, att, &act, Some(&opp_act), &mut rng, &mut d);
    }
    let def = bt.sides[1 - att].active();
    (d, def.is_alive, def.hp)
}

/// 1v1の全結果（各技の与ダメ・確定数・手順・記号判定）を JSON で返す。
///
/// 表示側は工房(wasm)・提案API(PyO3)・ポケモン情報ページ(ビルド時wasm)の3経路あるが、
/// ルールも記号もここだけで決める。提案API側だけ判定式が古いまま取り残され、
/// 同じ対面で工房と結論が食い違っていた（score の刻みが 0.5 と 1 で違う、
/// 先制技での決着・手順・確定1の扱いが無い）。
pub fn analyze_json(pack: &mut Pack, a: &str, b: &str, season: &str) -> serde_json::Value {
    let base = analyze_core(pack, a, b, season);
    // へんげんじざい/リベロの持ち主が先に動く対面は、相手の攻撃を「技を撃った後のタイプ」に対して計算し直す。
    let (pa, pb) = prepared(pack, a, b, season);
    let is_pr = |p: &Poke| p.ability == pack.sy.l.へんげんじざい || p.ability == pack.sy.ai.リベロ;
    let spd = |k: &str| base[k]["speed"].as_i64().unwrap_or(0);
    let first_move = |seq_key: &str, best_key: &str| -> Option<String> {
        base["verdict"][seq_key].as_array().and_then(|a| a.first()).and_then(|x| x.as_str())
            .or_else(|| base["verdict"][best_key].as_str()).map(|x| x.to_string())
    };
    let mut forms: Vec<(usize, String)> = Vec::new();
    if is_pr(&pa) && spd("a") > spd("b") {
        if let Some(n) = first_move("mySeq", "myMove") { forms.push((0, n)); }
    }
    if is_pr(&pb) && spd("b") > spd("a") {
        if let Some(n) = first_move("oppSeq", "oppMove") { forms.push((1, n)); }
    }
    if forms.is_empty() {
        return base;
    }
    PRE_FORMS.with(|f| *f.borrow_mut() = forms);
    let out = analyze_core(pack, a, b, season);
    PRE_FORMS.with(|f| f.borrow_mut().clear());
    CUR_ATT.with(|c| c.set(usize::MAX));
    out
}

fn analyze_core(pack: &mut Pack, a: &str, b: &str, season: &str) -> serde_json::Value {
    use serde_json::{json, Value};
    CUR_ATT.with(|c| c.set(usize::MAX));
    let mut out = json!({});
    // 場は対面ごとに1つ。並びは (a, b) に固定し、攻撃側だけを切り替える
    // （攻撃側を常に先頭に置くと、両者が天候特性を持つ対面で天候が向きによって変わる）。
    let (info_a, info_b) = side_info(pack, a, b, season);
    let mut sides: Vec<SideVerdictInput> = Vec::new();
    for (key, att, me) in [("a", 0usize, &info_a), ("b", 1usize, &info_b)] {
        CUR_ATT.with(|c| c.set(att));
        let mut moves = Vec::new();
        let mut best: Option<(String, i64, i64, i64, i64, usize)> = None; // (技名, 確定数, 初撃, 優先度, 最高乱数での発数, 技idx)
        for (i, (name, is_dmg)) in me.moves.iter().enumerate() {
            if !*is_dmg {
                moves.push(json!({"n": name, "dmg": Value::Null}));
                continue;
            }
            // 発数は実走（耐え効果・回復・天候が効く）、与ダメは技そのものの値。
            // 与ダメに実走の1ターン目HP減少を使うと、ばけのかわの身代わり分や砂の削り・
            // たべのこしの回復まで技のダメージとして表示されてしまう。
            let (hits_lo, first_lo) = run_move(pack, a, b, season, att, i, 0.0);
            let (hits_hi, _) = run_move(pack, a, b, season, att, i, 1.0);
            // 連続技の回数は決定的に決める（2〜5回は期待値の3回、スキルリンクは5回、
            // 1発ごとに命中判定がある技は必中前提で最大回数）。幅はダメージ乱数のぶんだけ。
            let dmg_lo = move_damage(pack, a, b, season, att, i, 0.0);
            let dmg_hi = move_damage(pack, a, b, season, att, i, 1.0);
            // 場に出ているものではなく、この技の数値に実際に効いた条件だけを返す
            let conds = relevant_conds(pack, a, b, season, att, i);
            // 最大打点技は「発数が少ない順、同数なら初撃のHP減少が大きい順」。
            let better = match &best {
                None => true,
                Some((_, bh, bf, _, _, _)) => hits_lo < *bh || (hits_lo == *bh && first_lo > *bf),
            };
            if better {
                best = Some((name.clone(), hits_lo, first_lo, move_priority(pack, name), hits_hi, i));
            }
            moves.push(json!({
                "n": name, "dmgLo": dmg_lo, "dmgHi": dmg_hi,
                "hitsLo": hits_lo, "hitsHi": hits_hi, "conds": conds,
                // 最大打点技の選定（発数が同じときのタイブレーク）に使う値。
                "firstLo": first_lo,
            }));
        }
        // 手順考慮: 毎ターン最善手を選び直した場合の手数と並び（初手限定技・ふうせん等で
        // 「同じ技を撃ち続ける」前提と食い違う対面のために出す）。
        let (seq_hits, seq_idx) = run_best_sequence(pack, a, b, season, att, 0.0);
        let seq_names: Vec<String> = seq_idx.iter()
            .filter_map(|i| me.moves.get(*i).map(|(n, _)| n.clone()))
            .collect();
        // 表示する技の並び: 手順が単発の最大打点より遠回りでなく2種以上なら手順、無ければ最大打点の連打。
        let best_hits_v = best.as_ref().map(|x| x.1).unwrap_or(OUT_OF_RANGE);
        let mut uniq: Vec<&String> = seq_names.iter().collect();
        uniq.sort();
        uniq.dedup();
        let turn_seq: Vec<usize> = if uniq.len() >= 2 && seq_hits <= best_hits_v {
            seq_idx.clone()
        } else {
            best.as_ref().map(|x| vec![x.5]).unwrap_or_default()
        };
        let turns: Vec<Value> = if turn_seq.is_empty() { Vec::new() } else {
            per_turn_damage(pack, a, b, season, att, &turn_seq).into_iter()
                .filter_map(|(mi, lo, hi, heal)| me.moves.get(mi).map(|(n, _)| json!({"n": n, "lo": lo, "hi": hi, "heal": heal})))
                .collect()
        };
        out[key] = json!({"hp": me.hp, "speed": me.speed, "moves": moves,
                          "seqHits": seq_hits, "seq": seq_names, "turns": turns});
        sides.push(SideVerdictInput {
            speed: me.speed,
            best_name: best.as_ref().map(|x| x.0.clone()),
            best_hits: best.as_ref().map(|x| x.1).unwrap_or(OUT_OF_RANGE),
            best_prio: best.as_ref().map(|x| x.3).unwrap_or(0),
            best_hits_hi: best.as_ref().map(|x| x.4).unwrap_or(OUT_OF_RANGE),
            best_idx: best.as_ref().map(|x| x.5),
            ohko_p: 0.0,
            seq_hits,
            seq_names,
        });
    }
    // 「乱数次第で1発入る」側の確率。記号を極端にしてよいかの判断に使う。
    // 確定1なら1.0、最高乱数でも1発にならないなら0.0。それ以外だけ実際に確率を出す
    // （1対面あたり最大2回で、条件に当たること自体が少ない）。
    for (att, side) in [(0usize, 0usize), (1usize, 1usize)] {
        CUR_ATT.with(|c| c.set(att));
        let (hits, hits_hi, idx) = (sides[side].best_hits, sides[side].best_hits_hi, sides[side].best_idx);
        sides[side].ohko_p = if hits <= 1 {
            1.0
        } else if hits_hi == 1 {
            match idx { Some(i) => ko_probability(pack, a, b, season, att, i, 1), None => 0.0 }
        } else {
            0.0
        };
    }
    CUR_ATT.with(|c| c.set(usize::MAX));
    let mut v = verdict_of(pack, &sides[0], &sides[1]);
    apply_stall(pack, &mut v, [&info_a, &info_b], a, b, season);
    out["verdict"] = v;
    out
}

/// 持久戦ルート(どくどく＋回復)の結果を判定に反映する。
/// すでに明確な勝ちの側は走らせない。片方だけが持久戦で勝てるなら記号を○/▲に寄せ、
/// 両方勝てるなら通常の判定のままにする。
fn apply_stall(pack: &mut Pack, v: &mut serde_json::Value, infos: [&SideInfo; 2],
               a: &str, b: &str, season: &str) {
    use serde_json::json;
    let score = v["score"].as_f64().unwrap_or(0.0);
    let mut route: [Option<StallResult>; 2] = [None, None];
    for att in 0..2usize {
        CUR_ATT.with(|c| c.set(att));
        let own = if att == 0 { score } else { -score };
        if own >= 1.0 || !stall_capable(pack, &infos[att].moves) {
            continue;
        }
        // 相手の最大乱数(自分も最大乱数になる)で勝てても、最低乱数では倒しきれないことがある。
        // 乱数に左右されず勝てる線だけを採る。
        route[att] = run_stall_route(pack, a, b, season, att, 1.0)
            .and_then(|_| run_stall_route(pack, a, b, season, att, 0.0));
    }
    // 勝ち筋が無い側でも、どくどくを持つなら「入れた場合の見込み」を返す(表示用。判定は変えない)。
    let mut plans: [Option<serde_json::Value>; 2] = [None, None];
    for att in 0..2usize {
        CUR_ATT.with(|c| c.set(att));
        if route[att].is_some() || !infos[att].moves.iter().any(|(n, _)| n == pack.intern.resolve(pack.sy.l.どくどく)) {
            continue;
        }
        if let Some((oc, r)) = simulate_stall(pack, a, b, season, att, 0.0, false, true, CAP) {
            let trace: Vec<serde_json::Value> = r.trace.iter().map(|t| json!({
                "n": t.n, "direct": t.direct, "poison": t.poison, "bind": t.bind, "heal": t.heal,
                "defHp": t.def_hp, "attHp": t.att_hp,
            })).collect();
            let oc_s = match oc { StallOutcome::Win => "win", StallOutcome::Lose => "lose", StallOutcome::Stuck => "stuck" };
            plans[att] = Some(json!({"outcome": oc_s, "turns": r.turns, "seq": r.seq, "trace": trace,
                                     "defMax": r.def_max, "attMax": r.att_max}));
        }
    }
    CUR_ATT.with(|c| c.set(usize::MAX));
    v["plans"] = json!({"me": plans[0].take(), "opp": plans[1].take()});
    let [mine, theirs] = route;
    let (side, picked) = match (mine, theirs) {
        (Some(r), None) => (Some("me"), Some(r)),
        (None, Some(r)) => (Some("opp"), Some(r)),
        _ => (None, None),
    };
    match (side, picked) {
        (Some(side), Some(r)) => {
            let new_score = if side == "me" { score.max(1.0) } else { score.min(-1.0) };
            v["score"] = json!(new_score);
            v["sym"] = json!(score_sym(new_score));
            v["win"] = json!(side == "me");
            let trace: Vec<serde_json::Value> = r.trace.iter().map(|t| json!({
                "n": t.n, "direct": t.direct, "poison": t.poison, "bind": t.bind, "heal": t.heal,
                "defHp": t.def_hp, "attHp": t.att_hp,
            })).collect();
            v["stall"] = json!({"side": side, "turns": r.turns, "seq": r.seq, "trace": trace,
                                "defMax": r.def_max, "attMax": r.att_max});
        }
        _ => {
            v["stall"] = json!({"side": null, "turns": 0, "seq": Vec::<String>::new()});
        }
    }
}

struct SideVerdictInput {
    speed: i64,
    best_name: Option<String>,
    best_hits: i64,
    best_prio: i64,
    /// 最高乱数での発数。1 なら「乱数次第で1発入る」。
    best_hits_hi: i64,
    best_idx: Option<usize>,
    /// 1発で倒せる確率(0〜1)。確定1なら1.0。
    ohko_p: f64,
    seq_names: Vec<String>,
    seq_hits: i64,
}

fn move_priority(pack: &Pack, name: &str) -> i64 {
    pack.move_by_name.get(name).map(|i| pack.moves[*i].priority).unwrap_or(0)
}

/// 途中で技を切り替える手順。同じ技が並ぶだけ、または単発の最大打点より遠回りな
/// 手順は情報にならない（判定の確定数とも食い違う）ので出さない。
fn seq_for(side: &SideVerdictInput) -> Vec<String> {
    let mut uniq: Vec<&String> = side.seq_names.iter().collect();
    uniq.sort();
    uniq.dedup();
    if uniq.len() < 2 || side.seq_hits > side.best_hits {
        return Vec::new();
    }
    side.seq_names.clone()
}

fn verdict_of(pack: &Pack, me: &SideVerdictInput, opp: &SideVerdictInput) -> serde_json::Value {
    use serde_json::json;
    let my_seq = seq_for(me);
    let opp_seq = seq_for(opp);
    let my_hits = me.best_hits.min(me.seq_hits);
    let opp_hits = opp.best_hits.min(opp.seq_hits);
    // 決着ターンに実際に撃つ技の優先度。手順が採用された場合はその最後の技。
    let my_p = my_seq.last().map(|n| move_priority(pack, n)).unwrap_or(me.best_prio);
    let opp_p = opp_seq.last().map(|n| move_priority(pack, n)).unwrap_or(opp.best_prio);
    let fast = me.speed > opp.speed;
    // 先後が効くのは確定数が同じときだけ。差が付いている対面で「先制技で先手」と
    // 出すと、決着に関係ない情報が勝敗理由のように見える。
    let ko_first = if my_hits == opp_hits && my_p != opp_p { my_p > opp_p } else { fast };
    // 先後がランダムになるのは、素早さも決着ターンの優先度も同値のときだけ。
    let even = me.speed == opp.speed && my_p == opp_p;
    let score = score_of(my_hits, opp_hits, ko_first, even, me.ohko_p, opp.ohko_p);
    let draw = my_hits >= OUT_OF_RANGE && opp_hits >= OUT_OF_RANGE;
    json!({
        "sym": score_sym(score),
        "win": !draw && (my_hits < opp_hits || (my_hits == opp_hits && ko_first)),
        "draw": draw,
        "score": score,
        "myHits": my_hits, "oppHits": opp_hits,
        "myS": me.speed, "oppS": opp.speed,
        "fast": fast, "koFirst": ko_first, "koByPriority": ko_first != fast, "even": even,
        "myMove": me.best_name, "oppMove": opp.best_name,
        "mySeq": my_seq, "oppSeq": opp_seq,
    })
}

/// 判定スコア = 確定数の差（相手の確定数 - 自分の確定数）。差がある時点で勝敗は
/// 確定数だけで決着しているため素早さは無関係。確定数が同数の場合のみ先後が効く。
pub fn score_of(my_hits: i64, opp_hits: i64, first: bool, even: bool,
                my_ohko_p: f64, opp_ohko_p: f64) -> f64 {
    // 互いに倒せない対面は素早さに関わらず引き分け。
    if my_hits >= OUT_OF_RANGE && opp_hits >= OUT_OF_RANGE {
        return 0.0;
    }
    let diff = (opp_hits - my_hits) as f64;
    // 確定数が同じで先後もランダム（素早さ同値・優先度も同じ）なら真の五分。
    if diff == 0.0 && even {
        return 0.0;
    }
    let base = if diff != 0.0 { diff } else if first { 1.0 } else { -1.0 };
    let win = diff > 0.0 || (diff == 0.0 && first);
    // 確定1で決着する対面は一方的に見えるが、「先に動ける側が乱数次第で1発入る」なら
    // その乱数で勝負が決まるので極端な記号にしない。
    // 例: マスカーニャ(S262・先手)の乱数1発56% vs メガカメックスの確定1。
    //     56%で無償突破できる対面を × と出していた。
    if win && my_hits <= 1 {
        // 相手が先手で、乱数次第で先に1発入れてくる
        if !first && opp_ohko_p >= 0.5 { return 0.0; }
        if !first && opp_ohko_p > 0.0 { return base; }
        return base.max(2.0);
    }
    if !win && opp_hits <= 1 {
        // 自分が先手で、乱数次第で先に1発入れられる
        if first && my_ohko_p >= 0.5 { return 0.0; }
        if first && my_ohko_p > 0.0 { return base; }
        return base.min(-2.0);
    }
    base
}

/// スコアから記号へ。刻みは整数1単位（0.5刻みだった頃は「確定2 vs 確定1・後手」の
/// 明確な負けが△/▲の境界に乗り、判定文と記号が食い違っていた）。
pub fn score_sym(score: f64) -> &'static str {
    if score >= 2.0 { "◎" } else if score >= 1.0 { "○" }
    else if score > -1.0 { "△" } else if score > -2.0 { "▲" } else { "×" }
}
