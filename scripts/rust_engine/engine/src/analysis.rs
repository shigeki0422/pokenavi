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
use std::collections::HashMap;

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

fn greedy_sequence(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize, roll: f64,
    avoid_rampage: bool,
) -> (i64, Vec<usize>) {
    let def = 1 - att;
    let mut bt = setup(pack, spec_a, spec_b, season, roll);
    let packr: &Pack = pack;
    let n_moves = bt.sides[att].active().moves.len();
    let mut seq: Vec<usize> = Vec::new();
    for _ in 0..CAP {
        if !bt.sides[def].active().is_alive {
            break;
        }
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
        let Some((mi, _, _, _)) = best else { break };
        seq.push(mi);
        let step = bt.turn + 1;
        drive(&mut bt, packr, att, mi, step);
        if !bt.sides[def].active().is_alive {
            return (seq.len() as i64, seq);
        }
    }
    (OUT_OF_RANGE, seq)
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
    // 技を撃つ直前の姿・タイプ変化（へんげんじざい・バトルスイッチ）。対戦本体と共有する
    crate::battle::apply_pre_move_forms(packr, &mut bt.sides[att].party[0], &mv);
    let n = calc_hits(packr, &mv, bt.sides[att].active(), &mut FixedRng);
    // 急所も対戦本体と同じ手順で決める。FixedRng なので crit_chance が 1.0 のものだけ
    // 急所になる＝確定数の前提と一致する（必中急所を落とすと確定数と食い違う）。
    let critical = {
        let a = &bt.sides[att].party[0];
        let d = &bt.sides[1 - att].party[0];
        let c = crate::battle::crit_chance(packr, a, &mv, Some(d));
        FixedRng.random() < c
    };
    let mut total = 0i64;
    for hit_i in 0..n.max(1) {
        let Battle { sides, field, .. } = &mut bt;
        let (sa, sd) = split2(sides, att);
        let att = &mut sa.party[0];
        let def = &mut sd.party[0];
        // 1発ぶんの計算は対戦本体と同じ関数を使う（何発目かの反映を含む）
        let mut r = FixedRng;
        let d = hit_damage(packr, att, def, &mv, field, hit_i, critical, Some(roll), &mut r);
        total += d;
        // マルチスケイル等「満タンのときだけ」の効果を2発目以降に持ち越さないよう、
        // 連続技の各ヒットは HP を減らしながら計算する。倒れても止めない（威力を出すため）。
        def.hp = (def.hp - d).max(1);
    }
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
    use serde_json::{json, Value};
    let mut out = json!({});
    // 場は対面ごとに1つ。並びは (a, b) に固定し、攻撃側だけを切り替える
    // （攻撃側を常に先頭に置くと、両者が天候特性を持つ対面で天候が向きによって変わる）。
    let (info_a, info_b) = side_info(pack, a, b, season);
    let mut sides: Vec<SideVerdictInput> = Vec::new();
    for (key, att, me) in [("a", 0usize, &info_a), ("b", 1usize, &info_b)] {
        let mut moves = Vec::new();
        let mut best: Option<(String, i64, i64, i64)> = None; // (技名, 確定数, 初撃, 優先度)
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
                Some((_, bh, bf, _)) => hits_lo < *bh || (hits_lo == *bh && first_lo > *bf),
            };
            if better {
                best = Some((name.clone(), hits_lo, first_lo, move_priority(pack, name)));
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
        out[key] = json!({"hp": me.hp, "speed": me.speed, "moves": moves,
                          "seqHits": seq_hits, "seq": seq_names});
        sides.push(SideVerdictInput {
            speed: me.speed,
            best_name: best.as_ref().map(|x| x.0.clone()),
            best_hits: best.as_ref().map(|x| x.1).unwrap_or(OUT_OF_RANGE),
            best_prio: best.as_ref().map(|x| x.3).unwrap_or(0),
            seq_hits,
            seq_names,
        });
    }
    let v = verdict_of(pack, &sides[0], &sides[1]);
    out["verdict"] = v;
    out
}

struct SideVerdictInput {
    speed: i64,
    best_name: Option<String>,
    best_hits: i64,
    best_prio: i64,
    seq_hits: i64,
    seq_names: Vec<String>,
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
    let score = score_of(my_hits, opp_hits, ko_first, even);
    json!({
        "sym": score_sym(score),
        "win": my_hits < opp_hits || (my_hits == opp_hits && ko_first),
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
pub fn score_of(my_hits: i64, opp_hits: i64, first: bool, even: bool) -> f64 {
    let diff = (opp_hits - my_hits) as f64;
    // 確定数が同じで先後もランダム（素早さ同値・優先度も同じ）なら真の五分。
    if diff == 0.0 && even {
        return 0.0;
    }
    let base = if diff != 0.0 { diff } else if first { 1.0 } else { -1.0 };
    let win = diff > 0.0 || (diff == 0.0 && first);
    // 確定1で決着する側は、確定数の差が1しかなくても一方的（負ける側は1体を確実に失う）。
    if win && my_hits <= 1 {
        return base.max(2.0);
    }
    if !win && opp_hits <= 1 {
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
