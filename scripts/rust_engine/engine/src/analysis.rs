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
use crate::poke::{build_poke, Poke};
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

/// 組み立て済みの両者（メガシンカ前の姿）を返す。同じ対面なら spec のパースをやり直さない。
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
    let a: Poke = build_poke(pack, spec_a, season);
    let b: Poke = build_poke(pack, spec_b, season);
    pack.prepared = Some((spec_a.to_string(), spec_b.to_string(), season.to_string(), a.clone(), b.clone()));
    (a, b)
}

fn setup(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64) -> Battle {
    let mut bt = setup_plain(pack, spec_a, spec_b, season, roll);
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

/// 入場効果と「この状況なら」の指定まで済ませた局面。両者が行動する対戦(sim_pair)は
/// 型変化を対戦本体が技を撃つ時点で処理するので、PRE_FORMS の先回り適用はしない。
fn setup_plain(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64) -> Battle {
    setup_plain_tie(pack, spec_a, spec_b, season, roll, None)
}

/// `tie`: 同速時の先後（Some(true)=side0 が先）。入場効果・メガシンカの順と、以降の行動順に使う。None は対戦本体と同じ side0 が先。
fn plain_key(pack: &Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64, tie: Option<bool>) -> String {
    let sc = pack.scenario;
    format!("{:p}\u{1}{}\u{1}{}\u{1}{}\u{1}{}\u{1}{},{},{},{}\u{1}{:?}", pack as *const Pack, spec_a, spec_b, season,
            roll.to_bits(), sc.weather, sc.terrain, sc.boost, sc.opp_boost, tie)
}

fn setup_plain_tie(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64, tie: Option<bool>) -> Battle {
    // 同じ対面・同じ乱数・同じ前提の開始局面は何度も作る（技ごと・方針ごと）ので、作ったものを複製して使う。
    let key = plain_key(pack, spec_a, spec_b, season, roll, tie);
    if let Some(b) = PLAIN_CACHE.with(|c| c.borrow().iter().find(|(k, _, _)| *k == key).map(|(_, b, _)| b.clone())) {
        return b;
    }
    let (bt, ev) = setup_plain_build(pack, spec_a, spec_b, season, roll, tie);
    PLAIN_CACHE.with(|c| {
        let mut c = c.borrow_mut();
        if c.len() >= 8 { c.remove(0); }
        c.push((key, bt.clone(), std::rc::Rc::new(ev)));
    });
    bt
}

/// 開始局面を作るときの入場効果・メガシンカで発動した特性の記録（再生の表示用。setup_plain_tie と同じ局面）。
fn start_events(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64, tie: Option<bool>) -> Vec<serde_json::Value> {
    let _ = setup_plain_tie(pack, spec_a, spec_b, season, roll, tie);
    let key = plain_key(pack, spec_a, spec_b, season, roll, tie);
    PLAIN_CACHE.with(|c| c.borrow().iter().find(|(k, _, _)| *k == key).map(|(_, _, e)| (**e).clone())).unwrap_or_default()
}

thread_local! {
    static PLAIN_CACHE: RefCell<Vec<(String, Battle, std::rc::Rc<Vec<serde_json::Value>>)>> = RefCell::new(Vec::new());
}

/// 入場効果・メガシンカの前後の見える状態（天候・フィールド・能力ランク・特性）。差分から発動の記録を作る。
type StartSnap = (Option<crate::interner::Sym>, &'static str, [[i32; 5]; 2], [crate::interner::Sym; 2]);

fn start_snap(p0: &Poke, p1: &Poke, f: &Field) -> StartSnap {
    let terr = if f.electric_terrain { "electric" } else if f.grassy_terrain { "grassy" }
        else if f.psychic_terrain { "psychic" } else if f.misty_terrain { "misty" } else { "" };
    let stg = |p: &Poke| [p.stage(0), p.stage(1), p.stage(2), p.stage(3), p.stage(4)];
    (f.weather, terr, [stg(p0), stg(p1)], [p0.ability, p1.ability])
}

/// 1回の入場効果・メガシンカで変わったもの。何も変わらなければ（メガシンカ以外は）記録しない。
fn start_event(packr: &Pack, phase: &str, side: usize, before: &StartSnap, after: &StartSnap) -> Option<serde_json::Value> {
    use serde_json::json;
    let d: Vec<Vec<i32>> = (0..2).map(|z| (0..5).map(|k| after.2[z][k] - before.2[z][k]).collect()).collect();
    // effect: 特性の発動で場や能力ランクが変わった（メガシンカで特性が入れ替わっただけは含めない。入場時のトレース等は含める）
    let fx = before.0 != after.0 || before.1 != after.1 || d.iter().flatten().any(|x| *x != 0);
    let effect = fx || (phase == "entry" && before.3 != after.3);
    if !effect && phase != "mega" { return None; }
    let nm = |s: crate::interner::Sym| packr.intern.resolve(s).to_string();
    Some(json!({
        "phase": phase, "side": side,
        "ability": nm(after.3[side]), "abilities": [nm(after.3[0]), nm(after.3[1])],
        "weather": if before.0 != after.0 { json!(after.0.map(|w| packr.intern.resolve(w).to_string())) } else { json!(null) },
        "terrain": if before.1 != after.1 { json!(after.1) } else { json!(null) },
        "stg": d, "effect": effect,
        "wx0": before.0.map(|w| packr.intern.resolve(w).to_string()),
    }))
}

fn setup_plain_build(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64, tie: Option<bool>)
    -> (Battle, Vec<serde_json::Value>) {
    let mut events: Vec<serde_json::Value> = Vec::new();
    let (a, b) = prepared(pack, spec_a, spec_b, season);
    let mut field = Field {
        roll_override: Some(roll),
        always_hit: true,
        // 「相手も攻撃してくる対面」で互いの最大打点を比べるのが1v1判定なので、
        // ふいうちのように相手の行動に依存する技も通る前提で評価する。
        assume_opp_attacks: true,
        eot_on_last_faint: true,
        no_view: true,
        speed_tie_p1_first: tie,
        ..Default::default()
    };
    let mut s1 = Side { party: vec![a], active_idx: 0, ..Default::default() };
    let mut s2 = Side { party: vec![b], active_idx: 0, ..Default::default() };
    {
        let p: &Pack = pack;
        // 入場時効果はメガシンカ前の姿で、素早さの速い側から（遅い側の天候・フィールドが残る）。
        // 同速は side0 が先（対戦本体と同じ）。分析で先後を指定したとき(tie)はそれに従う。
        let (sa, sb) = (crate::ai::effective_speed(p, &s1.party[0], &field), crate::ai::effective_speed(p, &s2.party[0], &field));
        let b_first = sb > sa || (sb == sa && tie == Some(false));
        if sa == sb { field.start_tie = true; }
        for sx in if b_first { [1usize, 0] } else { [0usize, 1] } {
            let b0 = start_snap(&s1.party[0], &s2.party[0], &field);
            if sx == 1 {
                entry_effects(p, &mut s2, 1, &mut field, &mut s1.party[0]);
            } else {
                entry_effects(p, &mut s1, 0, &mut field, &mut s2.party[0]);
            }
            let a0 = start_snap(&s1.party[0], &s2.party[0], &field);
            events.extend(start_event(p, "entry", sx, &b0, &a0));
        }
    }
    let mut bt = Battle::new(s1, s2, field);
    // 1ターン目の行動前のメガシンカ（対戦本体と同じく素早さの速い側から。メガ後の特性の入場効果＝ひでり等もここ）。
    // 分析は常にメガシンカする前提で、以降の局面はメガシンカ後から始める。
    {
        let p: &Pack = pack;
        let s0 = crate::ai::effective_speed(p, bt.sides[0].active(), &bt.field);
        let s1 = crate::ai::effective_speed(p, bt.sides[1].active(), &bt.field);
        let order = if s1 > s0 || (s1 == s0 && tie == Some(false)) { [1usize, 0] } else { [0usize, 1] };
        if s1 == s0 && bt.sides[0].active().mega.is_some() && bt.sides[1].active().mega.is_some() { bt.field.start_tie = true; }
        for sx in order {
            if bt.sides[sx].active().mega.is_some() {
                let b0 = start_snap(bt.sides[0].active(), bt.sides[1].active(), &bt.field);
                bt.mega_one(p, sx);
                let a0 = start_snap(bt.sides[0].active(), bt.sides[1].active(), &bt.field);
                events.extend(start_event(p, "mega", sx, &b0, &a0));
            }
        }
    }
    apply_scenario(pack, &mut bt);
    (bt, events)
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
    // 積む技が複数あることは稀なので、技欄の先頭にある積み技を使う（自分=side0 と 相手=side1 で同じ扱い）。
    for (side, n) in [(0usize, sc.boost), (1usize, sc.opp_boost)] {
        if n <= 0 { continue; }
        let packr: &Pack = pack;
        let p = &mut bt.sides[side].party[0];
        let boosts = p.moves.iter()
            .find_map(|m| crate::battle::self_boosts(packr, m.name)
                .filter(|v| v.iter().any(|(_, d)| *d > 0)));
        if let Some(v) = boosts {
            for (k, d) in v {
                let next = (p.stage(k) + d * n).clamp(-6, 6);
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

/// 技を1ターン撃ったときの「自分への不利益」。反動・自傷(いのちのたまを除く。どの技でも同じなので比べる意味が無い)・
/// 自分の能力低下・溜め/反動で動けない/暴れ技のロック。対戦本体の処理を1ターン実走して測る。
fn self_drawback(packr: &Pack, before: &Battle, after: &Battle, att: usize, marks: &[crate::battle::RaceMark], dealt: i64) -> bool {
    let (a0, a1) = (before.sides[att].active(), after.sides[att].active());
    let mut lost = 0i64;
    for w in marks.windows(2) {
        if w[1].0 == 1 && w[1].1 == att { lost += w[0].2[att] - w[1].2[att]; }
    }
    if dealt > 0 && a0.item == Some(packr.sy.it.いのちのたま) {
        lost -= (a0.max_hp / 10).max(1);
    }
    let dropped = (0..7u8).any(|k| a1.stage(k) < a0.stage(k));
    let locked = (a1.locked_move.is_some() && a0.locked_move.is_none()) || a1.recharge
        || (a1.charging_move.is_some() && a0.charging_move.is_none());
    lost > 0 || dropped || locked
}

/// 局面を複製して `att` に技 `i` を1ターン撃たせる（相手は動かない）。(撃った後の局面, 削り, 倒せた, 自分への不利益)
fn probe_move(bt: &Battle, packr: &Pack, att: usize, i: usize) -> (Battle, i64, bool, bool) {
    let def = 1 - att;
    let hp_before = bt.sides[def].active().hp;
    let mut probe = bt.clone();
    let step = probe.turn + 1;   // run_loop_lim の上限は累積ターン数
    let (marks, causes) = with_log(|| { drive(&mut probe, packr, att, i, step); });
    let ko = !probe.sides[def].active().is_alive;
    // 削りは技のダメージで測る。防御側がこのターンに食べたきのみ(オボンのみ等)の回復は差し引かない
    // （差し引くと、半分を割ってきのみを発動させる強い技より、割らない弱い技を選んでしまう）。
    // 食べた量は対戦本体が記録した原因から取る（はたきおとす で落とされたきのみを「食べた」扱いにしない）。
    let berry: i64 = causes.iter().filter(|c| c.1 == def && c.2 == "berry").map(|c| -c.3).sum();
    let dealt = hp_before - probe.sides[def].active().hp + berry;
    let bad = self_drawback(packr, bt, &probe, att, &marks, dealt);
    (probe, dealt, ko, bad)
}

/// 技の命中率（必中技は101として最上位）。
fn accuracy_of(mv: &crate::damage::DMove) -> i64 {
    mv.accuracy.unwrap_or(101)
}

/// 今の局面で `att` が撃つ最善の攻撃技 (技, 削り, 優先度, 倒せた)。選び方は greedy_sequence と持久戦の両方で共有する。
///
/// 優先順は「倒すまでの見込みターン数(今の削りで残りHPを割った値。倒せるなら1) → 倒せる手どうしは先制技
/// → 自分への不利益が無い手 → 命中率 → 削り」。同じターン数で倒せるなら反動や能力低下の無い技を選ぶ
/// （メガボーマンダは じしん でも確1なら すてみタックル の反動を受けない）。
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
    // (見込みターン数, -先制(倒せる時だけ), 不利益, -命中, -削り) が小さいほど良い
    let mut best: Option<((i64, i64, bool, i64, i64), (usize, i64, i64, bool))> = None;
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
        let (_, dealt, ko, bad) = probe_move(bt, packr, att, i);
        if dealt <= 0 && !ko { continue; }
        let prio = mv.priority;
        let est = if ko { 1 } else { (hp_before + dealt - 1) / dealt.max(1) };
        let key = (est, if ko { -prio } else { 0 }, bad, -accuracy_of(&mv), -dealt);
        if best.as_ref().map_or(true, |(k, _)| key < *k) {
            best = Some((key, (i, dealt, prio, ko)));
        }
    }
    best.map(|(_, v)| v)
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
    // おやこあい: 単発技は2発目(1発目の25%)が続く（対戦本体の execute_move と同じ式）
    if n.max(1) == 1 && total > 0 && bt.sides[att].party[0].ability == packr.sy.l.おやこあい {
        total += std::cmp::max(1, ((total as f64) * 0.25).floor() as i64);
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
    // 場の条件・能力ランクは、その技のダメージを実際に変えるものだけを出す（ダメージ計算そのものに、条件を外した場合と比べさせる。
    // 表示用の規則表は持たない＝特殊技に攻撃ランク、じめん技にエレキフィールド等の無関係な注記が付かない）。
    if let Some(mv) = bt.sides[att].active().moves.get(move_idx).cloned() {
        let packr: &Pack = pack;
        let def = 1 - att;
        let dmg = |a: &Poke, d: &Poke, f: &Field| -> i64 {
            let (mut a, mut d, mut f) = (a.clone(), d.clone(), f.clone());
            crate::damage::calc_damage(packr, &mut a, &mut d, &mv, &mut f, false, Some(1.0), Some(1.0), &mut |_| 1.0)
        };
        let (a0, d0, f0) = (bt.sides[att].active(), bt.sides[def].active(), &bt.field);
        let base = dmg(a0, d0, f0);
        if base > 0 {
            if let Some(w) = f0.weather {
                let mut f = f0.clone();
                f.weather = None;
                if dmg(a0, d0, &f) != base { out.push(packr.intern.resolve(w).to_string()); }
            }
            let terr = if f0.electric_terrain { Some("エレキフィールド") } else if f0.grassy_terrain { Some("グラスフィールド") }
                else if f0.psychic_terrain { Some("サイコフィールド") } else if f0.misty_terrain { Some("ミストフィールド") } else { None };
            if let Some(tn) = terr {
                let mut f = f0.clone();
                f.electric_terrain = false; f.grassy_terrain = false; f.psychic_terrain = false; f.misty_terrain = false;
                if dmg(a0, d0, &f) != base { out.push(tn.to_string()); }
            }
            let mut v = Vec::new();
            for (k, lbl) in [(0u8, "攻撃"), (2u8, "特攻")] {
                let st = a0.stage(k);
                if st == 0 { continue; }
                let mut a = a0.clone();
                a.set_stage(k, 0);
                if dmg(&a, d0, f0) != base { v.push(format!("{}{}{}", lbl, if st > 0 { "+" } else { "" }, st)); }
            }
            if !v.is_empty() { out.push(v.join("・")); }
            // 防御側の特性による補正（マルチスケイル・ファントムガード・フィルター・あついしぼう等）。特性を外すとダメージが変わるときだけ
            if let Some(none) = packr.intern.get("") {
                if d0.ability != none {
                    let mut d = d0.clone();
                    d.ability = none;
                    if dmg(a0, &d, f0) != base { out.push(format!("防御特性:{}", packr.intern.resolve(d0.ability))); }
                }
            }
        }
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


/// 技のタイプ相性の倍率。対戦本体と同じ関数で出す（スカイスキン等の技タイプ変化・特性や ふうせん による無効を含む）。
pub fn move_effectiveness(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize, move_idx: usize,
) -> Option<f64> {
    let mut bt = setup(pack, spec_a, spec_b, season, 0.0);
    let packr: &Pack = pack;
    let def = 1 - att;
    let Some(mv) = bt.sides[att].active().moves.get(move_idx).cloned() else { return None };
    if mv.category == crate::pack::Cat::Status {
        return None;
    }
    crate::battle::apply_pre_move_forms(packr, &mut bt.sides[att].party[0], &mv);
    let a = bt.sides[att].active();
    let d = bt.sides[def].active();
    let ty = crate::damage::effective_move_type(packr, a, &mv, &bt.field);
    let immune = (!crate::damage::should_ignore_ability(packr, a)
            && crate::damage::check_move_immunity(packr, d, ty, mv.name)
            && !crate::damage::scrappy_override(packr, a, ty, d))
        || (d.item == Some(packr.sy.it.ふうせん) && ty == packr.tc.じめん && !d.grounded);
    Some(if immune { 0.0 } else { crate::damage::type_effectiveness(packr, a, d, &mv, ty) })
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
    // 先に動いたかは、判定の対戦(中央乱数)の1ターン目の実際の行動順で決める（素早さだけでなく技の優先度も効く）。
    let first_act = base["verdict"]["race"].as_array()
        .and_then(|r| r.iter().find(|e| e["turn"] == 1 && e["actor"].is_u64() && e["move"].is_string()))
        .map(|e| (e["actor"].as_u64().unwrap_or(9) as usize, e["move"].as_str().unwrap_or("").to_string()));
    let mut forms: Vec<(usize, String)> = Vec::new();
    if let Some((side, mv)) = first_act {
        let holder = if side == 0 { &pa } else { &pb };
        if is_pr(holder) && !mv.is_empty() { forms.push((side, mv)); }
    }
    if forms.is_empty() {
        return base;
    }
    PRE_FORMS.with(|f| *f.borrow_mut() = forms);
    let mut out = analyze_core(pack, a, b, season);
    PRE_FORMS.with(|f| f.borrow_mut().clear());
    CUR_ATT.with(|c| c.set(usize::MAX));
    // 技ごとのダメージ一覧は、型が変わる前の元のタイプで出す（型の変化は判定・経過・再生だけに反映する）
    for k in ["a", "b"] {
        out[k]["moves"] = base[k]["moves"].clone();
    }
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
        let mut best_key: Option<(i64, i64, bool, i64, i64)> = None;
        let base_bt = setup(pack, a, b, season, 0.0);
        for (i, (name, is_dmg)) in me.moves.iter().enumerate() {
            if !*is_dmg {
                moves.push(json!({"n": name, "dmg": Value::Null}));
                continue;
            }
            // 発数は実走（耐え効果・回復・天候が効く）、与ダメは技そのものの値。
            // 与ダメに実走の1ターン目HP減少を使うと、ばけのかわの身代わり分や砂の削り・
            // たべのこしの回復まで技のダメージとして表示されてしまう。
            let (hits_lo, first_lo) = run_move(pack, a, b, season, att, i, 0.0);
            // 最低乱数で1発なら、乱数が高くても1発（1発目の与ダメは乱数が高いほど大きい）
            let (hits_hi, _) = if hits_lo <= 1 { (hits_lo, 0) } else { run_move(pack, a, b, season, att, i, 1.0) };
            // 判定の対戦(中央乱数)と前提を揃えた確定数。表示の主はこれ（最低〜最高はダメージ幅に残す）。
            let (hits_mid, _) = if hits_lo <= 1 { (hits_lo, 0) } else { run_move(pack, a, b, season, att, i, 0.5) };
            // 連続技の回数は決定的に決める（2〜5回は期待値の3回、スキルリンクは5回、
            // 1発ごとに命中判定がある技は必中前提で最大回数）。幅はダメージ乱数のぶんだけ。
            let dmg_lo = move_damage(pack, a, b, season, att, i, 0.0);
            let dmg_hi = move_damage(pack, a, b, season, att, i, 1.0);
            // 場に出ているものではなく、この技の数値に実際に効いた条件だけを返す
            let conds = relevant_conds(pack, a, b, season, att, i);
            let eff = move_effectiveness(pack, a, b, season, att, i);
            // 最大打点技は「発数が少ない順 → 自分への不利益(反動・自傷・能力低下・溜め等)が無い技 → 命中率 → 初撃のHP減少」。
            // 同じ発数なら反動の無い技を選ぶ（判定の対戦で撃つ技と同じ選び方。best_attack と揃える）。
            let (bad, acc) = {
                let packr: &Pack = pack;
                let acc = base_bt.sides[att].active().moves.get(i).map(accuracy_of).unwrap_or(0);
                (probe_move(&base_bt, packr, att, i).3, acc)
            };
            // 1発で倒せる技どうしは先制技を優先（最後の一撃で先に倒す方が良い）
            let prio = base_bt.sides[att].active().moves.get(i).map(|m| m.priority).unwrap_or(0);
            let key = (hits_mid, if hits_mid <= 1 { -prio } else { 0 }, bad, -acc, -first_lo);
            // 無効（0倍）で倒せない技は最大打点技にしない（反動が無いだけで選ばれ、撃っても何も起きない手になっていた）
            let never = eff == Some(0.0) && hits_mid >= OUT_OF_RANGE;
            if !never && best_key.map_or(true, |k| key < k) {
                best_key = Some(key);
                best = Some((name.clone(), hits_lo, first_lo, move_priority(pack, name), hits_hi, i));
            }
            moves.push(json!({
                "n": name, "dmgLo": dmg_lo, "dmgHi": dmg_hi,
                "hitsLo": hits_lo, "hitsHi": hits_hi, "hitsMid": hits_mid, "conds": conds,
                // タイプ相性の倍率（0=無効）。へんげんじざい/リベロ で変わる前の元のタイプに対して。
                "eff": eff,
                // 最大打点技の選定（発数が同じときのタイブレーク）に使う値。
                "firstLo": first_lo, "selfCost": bad,
            }));
        }
        if let Some(bi) = best.as_ref().map(|x| x.5) {
            for m in moves.iter_mut() {
                if m["n"] == json!(me.moves[bi].0) && m.get("dmgLo").is_some() { m["best"] = json!(true); }
            }
        }
        // 手順考慮: 毎ターン最善手を選び直した場合の手数と並び（初手限定技・ふうせん等で
        // 「同じ技を撃ち続ける」前提と食い違う対面のために出す）。
        let (h1, s1) = greedy_sequence(pack, a, b, season, att, 0.0, false);
        // 暴れ技を持たなければ「暴れ技を避ける」線は同じ手順になる
        let has_rampage = { let packr: &Pack = pack; base_bt.sides[att].active().moves.iter().any(|m| is_rampage(packr, m)) };
        let (h2, s2) = if has_rampage { greedy_sequence(pack, a, b, season, att, 0.0, true) } else { (h1, s1.clone()) };
        let avoid = h2 < h1;
        let (seq_hits, seq_idx) = if avoid { (h2, s2) } else { (h1, s1) };
        let seq_names: Vec<String> = seq_idx.iter()
            .filter_map(|i| me.moves.get(*i).map(|(n, _)| n.clone()))
            .collect();
        out[key] = json!({"hp": me.hp, "speed": me.speed, "moves": moves,
                          "seqHits": seq_hits, "seq": seq_names});
        sides.push(SideVerdictInput {
            best_name: best.as_ref().map(|x| x.0.clone()),
            best_hits: best.as_ref().map(|x| x.1).unwrap_or(OUT_OF_RANGE),
            best_hits_hi: best.as_ref().map(|x| x.4).unwrap_or(OUT_OF_RANGE),
            best_idx: best.as_ref().map(|x| x.5),
            ohko_p: 0.0,
            avoid,
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
    let mut v = verdict_sim(pack, &sides, [&info_a, &info_b], a, b, season, &mut out);
    // 持久戦は方針の1つとして判定の対戦に入った（別計算での記号の上書きは廃止）。旧表示との互換のため空で残す。
    v["stall"] = json!({"side": null, "turns": 0, "seq": Vec::<String>::new()});
    v["plans"] = json!({"me": null, "opp": null});
    out["verdict"] = v;
    out
}


struct SideVerdictInput {
    best_name: Option<String>,
    best_hits: i64,
    /// 最高乱数での発数。1 なら「乱数次第で1発入る」。
    best_hits_hi: i64,
    best_idx: Option<usize>,
    /// 1発で倒せる確率(0〜1)。確定1なら1.0。
    ohko_p: f64,
    /// 毎ターン最善手の並びで、暴れ技を避けた線のほうが短かったか。
    avoid: bool,
}

fn move_priority(pack: &Pack, name: &str) -> i64 {
    pack.move_by_name.get(name).map(|i| pack.moves[*i].priority).unwrap_or(0)
}

/// 判定の本体: 両者が互いの行動の影響を受けながら戦う対戦を、方針の組ごとに回す。
///
/// 一方ずつ相手を棒立ちにして数える発数では、積み技・ねこだまし・かるわざ・自分の能力が
/// 下がる技(からをやぶる・インファイト)が相手の発数や先後に与える影響を表せない。
/// 方針は各側たかだか「最大打点の連打 / 毎ターン最善手 / 準備の1手→攻撃」で、組ごとの対戦結果を
/// スコアにした小さな行列で、各側が相手の最善の応手を前提に自分が最も有利な方針を選ぶ(同点は先の候補)。
fn verdict_sim(pack: &mut Pack, sides: &[SideVerdictInput], infos: [&SideInfo; 2],
               a: &str, b: &str, season: &str, out: &mut serde_json::Value) -> serde_json::Value {
    use serde_json::json;
    let mut plans: [Vec<Plan>; 2] = [Vec::new(), Vec::new()];
    for s in 0..2usize {
        if let Some(bi) = sides[s].best_idx { plans[s].push(Plan::Max(bi)); }
        plans[s].push(Plan::Seq(sides[s].avoid));
        for i in prep_candidates(pack, a, b, season, s) {
            plans[s].push(Plan::Prep(i, sides[s].avoid));
        }
        let status = infos[s].moves.iter().any(|(n, _)| {
            n == pack.intern.resolve(pack.sy.l.どくどく) || n == pack.intern.resolve(pack.sy.l.おにび)
        });
        if status {
            plans[s].push(Plan::Stall(sides[s].avoid));
        }
    }
    // 持久戦の方針がある対面は、毒で削り切るまで見るため打ち切りを STALL_CAP に延ばす（全ての方針の組で同じ打ち切り）。
    let cap = if plans.iter().flatten().any(|p| matches!(p, Plan::Stall(_))) { STALL_CAP } else { CAP };
    let ohko = |s: usize, p: Plan, sim: &SimOut| -> f64 {
        match p { Plan::Prep(..) | Plan::Stall(_) => if sim.t[s] <= 1 { 1.0 } else { 0.0 }, _ => sides[s].ohko_p }
    };
    // (score, ko_first, fast, even)。score は side0 から見た値。
    // 同速を両方の順で回す場合は、順を固定した結果なので「先後ランダム(even)」の扱いはしない（平均で表す）。
    let judge = |sim: &SimOut, p: [Plan; 2]| -> (f64, bool, bool, bool) {
        // 同速はその対戦で回した順（me_first）で先後を決める（(a,b) と (b,a) の結果が符号だけ入れ替わるように）
        let fast = sim.speed[0] > sim.speed[1] || (sim.speed[0] == sim.speed[1] && sim.me_first);
        let ko_first = if sim.t[0] == sim.t[1] && sim.t[0] < OUT_OF_RANGE { sim.first == Some(0) } else { fast };
        let even = !sim.tie_seen && sim.last_tie;
        if sim.mutual { return (0.0, false, fast, even); }
        (score_of(sim.t[0], sim.t[1], ko_first, even, ohko(0, p[0], sim), ohko(1, p[1], sim)), ko_first, fast, even)
    };
    // 方針の組の評価: 自分が先(同速時)の対戦を代表にし、同速のターンがあれば相手が先の対戦も回してスコアを平均する。
    // 戻り値 (平均スコア, 同速で結果が変わったか, 代表の対戦)
    // 戻り値の最後は同点比較用の (自分の残りHP, 相手の残りHP, 自分が倒れたターン, 相手が倒れたターン)。同速なら両順の平均。
    let mut memo = SimMemo::default();
    let mut eval = |pack: &mut Pack, p: [Plan; 2], trace: bool, roll: f64| -> (f64, bool, SimOut, [f64; 4]) {
        let sa = sim_pair_memo(pack, a, b, season, p, trace, true, roll, cap, &mut memo);
        let va = judge(&sa, p).0;
        let met = |s: &SimOut| [s.end_hp[0], s.end_hp[1], s.faint_turn[0] as f64, s.faint_turn[1] as f64];
        if !sa.tie_seen { let ma = met(&sa); return (va, false, sa, ma); }
        let sb = sim_pair_memo(pack, a, b, season, p, false, false, roll, cap, &mut memo);
        let vb = judge(&sb, p).0;
        let (ma, mb) = (met(&sa), met(&sb));
        let avg = [0, 1, 2, 3].map(|k| (ma[k] + mb[k]) / 2.0);
        ((va + vb) / 2.0, va != vb, sa, avg)
    };
    // 各マスの値: (記号のスコア, 相手の残りHPの少なさ, 自分が倒れるまでのターン)。記号が同じ方針どうしは、
    // 相手に多く削りを入れ、長く粘る方を選ぶ（負けが確定でも、ねこだまし等で最善を尽くす経過を見せる）。
    // ダメージ乱数は中央（0.5）の1点。記号・勝敗・経過はすべてこの対戦で決める。
    let roll = ROLL_MID;
    let (score_mid, tie, sim, chosen, ko_first, fast, even) = {
        let (n0, n1) = (plans[0].len(), plans[1].len());
        let mut m: Vec<Vec<(f64, f64, f64, f64, f64)>> = vec![vec![(0.0, 0.0, 0.0, 0.0, 0.0); n1]; n0];
        for i in 0..n0 {
            for j in 0..n1 {
                let (v, _, _sim, mt) = eval(pack, [plans[0][i], plans[1][j]], false, roll);
                m[i][j] = (v.clamp(-SCORE_CLIP, SCORE_CLIP), mt[0], mt[1], mt[2], mt[3]);
            }
        }
        // 方針の比べ方: 勝ち/相打ち・引き分け/負けの区分 → 相手の残りHPの少なさ → 自分が倒れるまでのターン → スコア。
        // 反実仮想の手数差（倒されなかったら何ターンで倒せたか）は最後のタイブレークだけに使う
        // （先に使うと、負けが確定の側が積み・不発のねこだまし等「何もしない方針」を選んでいた）。
        let class = |x: f64| if x > 0.0 { 1.0 } else if x < 0.0 { -1.0 } else { 0.0 };
        // 同じ区分・同じ削り・同じ粘りなら、自分の残りHPが多い方（最後の一撃を反動の無い技で決める等）。
        let cmp = |x: &[f64; 5], y: &[f64; 5]| x.partial_cmp(y).unwrap_or(std::cmp::Ordering::Equal);
        let mine = |c: &(f64, f64, f64, f64, f64)| [class(c.0), -c.2, c.3, c.1, c.0];
        let theirs = |c: &(f64, f64, f64, f64, f64)| [-class(c.0), -c.1, c.4, c.2, -c.0];
        let mut bi = 0usize;
        let mut bv: Option<[f64; 5]> = None;
        for i in 0..n0 {
            let worst = (0..n1).map(|j| mine(&m[i][j])).min_by(|x, y| cmp(x, y)).unwrap();
            if bv.map_or(true, |b| cmp(&worst, &b) == std::cmp::Ordering::Greater) { bv = Some(worst); bi = i; }
        }
        let mut bj = 0usize;
        let mut bw: Option<[f64; 5]> = None;
        for j in 0..n1 {
            let worst = (0..n0).map(|i| theirs(&m[i][j])).min_by(|x, y| cmp(x, y)).unwrap();
            if bw.map_or(true, |b| cmp(&worst, &b) == std::cmp::Ordering::Greater) { bw = Some(worst); bj = j; }
        }
        let chosen = [plans[0][bi], plans[1][bj]];
        let (avg, tie, sim, _) = eval(pack, chosen, true, roll);
        let (score0, ko_first, fast, even) = judge(&sim, chosen);
        let score = if tie { avg } else { score0 };
        (score, tie, sim, chosen, ko_first, fast, even)
    };
    // 圏外(999)の差がそのまま入ると、型ごとの重み付き平均で極端に効くので記号の範囲にクリップする。
    let score = score_mid.clamp(-SCORE_CLIP, SCORE_CLIP);
    let names = |s: usize| -> Vec<String> {
        let upto = if sim.t[s] < OUT_OF_RANGE { sim.t[s] as usize } else { sim.acts[s].len() };
        sim.acts[s].iter().take(upto).flatten()
            .filter_map(|i| infos[s].moves.get(*i).map(|(n, _)| n.clone())).collect()
    };
    let mut seqs: [Vec<String>; 2] = [Vec::new(), Vec::new()];
    let mut preps: [Option<String>; 2] = [None, None];
    for s in 0..2usize {
        let n = names(s);
        let mut uniq: Vec<&String> = n.iter().collect();
        uniq.sort();
        uniq.dedup();
        if matches!(chosen[s], Plan::Prep(..) | Plan::Stall(_)) {
            if let Plan::Prep(i, _) = chosen[s] { preps[s] = infos[s].moves.get(i).map(|(x, _)| x.clone()); }
            let key = if s == 0 { "a" } else { "b" };
            out[key]["seq"] = json!(n);
            out[key]["seqHits"] = json!(sim.t[s]);
            seqs[s] = n;
        } else if uniq.len() >= 2 {
            seqs[s] = n;
        }
    }
    // 毎ターンの与ダメージは実際の対戦の経過どおり（倒れた後の行動は出さない）。
    for s in 0..2usize {
        let key = if s == 0 { "a" } else { "b" };
        out[key]["turns"] = json!(race_turns(&sim, s, infos[s]));
    }
    let (t0, t1) = (sim.t[0], sim.t[1]);
    let draw = t0 >= OUT_OF_RANGE && t1 >= OUT_OF_RANGE;
    json!({
        "sym": score_sym(score),
        "win": if tie { score > 0.0 } else { !draw && !sim.mutual && (t0 < t1 || (t0 == t1 && ko_first)) },
        // 相打ち（同じ行動・同じ区切りで両者が倒れた）。引き分け扱い（スコア0）。同速で順により変わる場合は tie が優先。
        "mutual": sim.mutual && !tie, "mutualTurn": if sim.mutual { json!(t0) } else { json!(null) },
        "draw": draw,
        "score": score,
        "myHits": t0, "oppHits": t1,
        // 同速で先後により結果が変わる場合は、同速だったターンの素早さを出す（決着ターンの素早さとは限らない）
        "myS": if tie { sim.tie_speed.map_or(sim.speed[0], |x| x[0]) } else { sim.speed[0] },
        "oppS": if tie { sim.tie_speed.map_or(sim.speed[1], |x| x[1]) } else { sim.speed[1] },
        "fast": fast, "koFirst": ko_first, "koByPriority": ko_first != fast && sim.prio[0] != sim.prio[1], "even": even,
        // 同速で先後により結果が変わる（両方の順の平均が score。経過 race は自分が先の場合）。
        "tie": tie,
        "myMove": sides[0].best_name, "oppMove": sides[1].best_name,
        "mySeq": seqs[0], "oppSeq": seqs[1],
        "myPrep": preps[0], "oppPrep": preps[1],
        "myPlan": chosen[0].key(), "oppPlan": chosen[1].key(),
        "race": sim.race,
        "raceInit": sim.race_init,
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

/// 判定の対戦を回すダメージ乱数（中央）。
const ROLL_MID: f64 = 0.5;
/// 出力スコアのクリップ幅（記号の範囲 ◎=2 / ×=-2）。
const SCORE_CLIP: f64 = 2.0;

/// 判定用の対戦で各側が取る方針。
#[derive(Clone, Copy, PartialEq, Eq, Hash, Debug)]
pub enum Plan {
    /// 最大打点技(相手を棒立ちにした発数が最少の技)を撃ち続ける。
    Max(usize),
    /// 毎ターン、その時点の局面で最善の攻撃技を選び直す(bool は暴れ技を避けるか)。
    Seq(bool),
    /// 1ターン目に準備の技(積み技1回・ねこだまし)を使い、以降は Seq と同じ。
    Prep(usize, bool),
    /// 持久戦: 相手が状態異常でなければ どくどく/おにび、倒されそうなら回復技、それ以外は Seq と同じ攻撃
    /// (まとわりつく等の拘束技も削りの見込みで選ばれる)。
    Stall(bool),
}

impl Plan {
    fn key(&self) -> &'static str {
        match self { Plan::Max(_) => "max", Plan::Seq(_) => "seq", Plan::Prep(..) => "prep", Plan::Stall(_) => "stall" }
    }
}

/// 両者が同時に行動する判定用の対戦の結果。
pub struct SimOut {
    /// 同速のとき side0 が先に動く順で回した対戦か。
    pub me_first: bool,
    /// 決着したターンの行動順が同速の先後で決まったか。
    pub last_tie: bool,
    /// 各側が相手を倒したターン。倒せなければ OUT_OF_RANGE。先に倒された側の値は、
    /// 倒されずに残っていたら何ターン目に倒せたか（HPを嵩増しして同じ手順を続けた値）。
    pub t: [i64; 2],
    /// 実際の対戦で先に相手を倒した側。
    pub first: Option<usize>,
    /// 決着ターン開始時の実効素早さと、そのターンに撃った技の優先度。
    pub speed: [i64; 2],
    pub prio: [i64; 2],
    /// 各ターンに撃った技(idx)。行動しなかったターンは None。
    pub acts: [Vec<Option<usize>>; 2],
    /// 各ターンの与ダメージ(最低乱数/最高乱数)と防御側の回復量。表示用。
    pub trace: [Vec<(usize, i64, i64, i64)>; 2],
    /// 実際の対戦の経過（倒れるまで）。行動ごと・ターン終了時ごとの両者のHPと、HPが動いた原因。
    pub race: Vec<serde_json::Value>,
    /// 1ターン目の開始時の両者の状態（再生表示の最初の画面）。
    pub race_init: Option<serde_json::Value>,
    /// 同速で、先後が技の優先度でも決まらないターンがあったか（先後を入れ替えて回し直す対象）。
    pub tie_seen: bool,
    /// 同速だったターンの素早さ（表示用）。
    pub tie_speed: Option<[i64; 2]>,
    /// 相打ち（同じ区切りで両者が倒れた）。引き分け扱い。
    pub mutual: bool,
    /// 実際の対戦の終了時の残りHP割合と、倒れたターン（倒れなければ CAP+1）。方針の同点の比較に使う。
    pub end_hp: [f64; 2],
    pub faint_turn: [i64; 2],
}

type BestAttack = Option<(usize, i64, i64, bool)>;

fn plan_action(bt: &Battle, packr: &Pack, side: usize, plan: Plan) -> Option<usize> {
    plan_action_with(bt, packr, side, plan, &mut |s, av| best_attack(bt, packr, s, av))
}

/// `ba(側, 暴れ技を避けるか)` はその局面の best_attack（呼び出し側で使い回せるように外から渡す）。
fn plan_action_with(bt: &Battle, packr: &Pack, side: usize, plan: Plan,
                    ba: &mut dyn FnMut(usize, bool) -> BestAttack) -> Option<usize> {
    match plan {
        // 今の局面で相手に無効（0倍）なら撃たずに、その局面の最善の攻撃技にする（0倍の技で接触を避ける「何もしない手」にしない）。
        // 相手のタイプが試合中に変わり（へんげんじざい・へんしん等）当たるようになれば、その時点から撃つ。
        Plan::Max(i) => if immune_now(bt, packr, side, i) { ba(side, false).map(|x| x.0) } else { Some(i) },
        Plan::Seq(av) => ba(side, av).map(|x| x.0),
        Plan::Prep(i, av) => {
            if bt.turn == 0 { Some(i) } else { ba(side, av).map(|x| x.0) }
        }
        Plan::Stall(av) => stall_action(bt, packr, side, av, ba),
    }
}

/// `att` の技 `i` が今の局面で相手に無効か（タイプ・特性・ふうせん。move_effectiveness と同じ判定を今の局面で行う）。
fn immune_now(bt: &Battle, packr: &Pack, att: usize, i: usize) -> bool {
    let Some(mv) = bt.sides[att].active().moves.get(i).cloned() else { return false };
    if mv.category == crate::pack::Cat::Status || mv.power.unwrap_or(0) <= 0 {
        return false;
    }
    let mut a = bt.sides[att].active().clone();
    crate::battle::apply_pre_move_forms(packr, &mut a, &mv);
    let d = bt.sides[1 - att].active();
    let ty = crate::damage::effective_move_type(packr, &a, &mv, &bt.field);
    (!crate::damage::should_ignore_ability(packr, &a)
        && crate::damage::check_move_immunity(packr, d, ty, mv.name)
        && !crate::damage::scrappy_override(packr, &a, ty, d))
        || (d.item == Some(packr.sy.it.ふうせん) && ty == packr.tc.じめん && !d.grounded)
}

/// 持久戦で状態異常を入れる技（どくどく・おにび）の位置。
fn stall_status_move(packr: &Pack, p: &crate::poke::Poke) -> Option<usize> {
    let l = &packr.sy.l;
    p.moves.iter().position(|m| m.name == l.どくどく || m.name == l.おにび)
}

/// 持久戦の1手（旧・持久戦ルートの選び方と同じ）。相手が状態異常でなく、入るなら状態異常の技。
/// 相手の最善の攻撃で倒されそうで、先に回復でき回復で耐えられるなら回復技。それ以外は最善の攻撃技、無ければ回復技。
fn stall_action(bt: &Battle, packr: &Pack, side: usize, av: bool,
                ba: &mut dyn FnMut(usize, bool) -> BestAttack) -> Option<usize> {
    let def = 1 - side;
    let me = bt.sides[side].active();
    if let Some(lk) = me.choice_locked_move.or(me.locked_move) {
        return me.moves.iter().position(|m| m.name == lk);
    }
    let status_i = stall_status_move(packr, me);
    let heal_i = me.moves.iter().position(|m| is_heal_move(packr, m));
    if bt.sides[def].active().status.is_none() {
        if let Some(si) = status_i {
            let (probe, _, _, _) = probe_move(bt, packr, side, si);
            if probe.sides[def].active().status.is_some() { return Some(si); }
        }
    }
    if let Some(h) = heal_i {
        let foe_best = ba(def, false);
        let (hp, mx) = (me.hp, me.max_hp);
        let will_fall = foe_best.map_or(false, |(_, dealt, _, ko)| ko || dealt >= hp);
        let foe_first = crate::ai::effective_speed(packr, bt.sides[def].active(), &bt.field)
            > crate::ai::effective_speed(packr, me, &bt.field);
        if will_fall && !foe_first && foe_best.map_or(true, |(_, dealt, _, _)| dealt < (hp + mx / 2).min(mx)) {
            return Some(h);
        }
    }
    ba(side, av).map(|x| x.0).or(heal_i)
}

fn act_of(bt: &Battle, side: usize, idx: Option<usize>) -> Action {
    match idx {
        Some(i) => Action {
            kind: ActKind::Move,
            mv: bt.sides[side].active().moves.get(i).cloned(),
            move_idx: i as i64,
            ..Default::default()
        },
        None => Action::default(),
    }
}

/// 行動順を決める優先度（特性・場による補正込み。対戦本体の priority_base）。
fn act_priority(packr: &Pack, bt: &Battle, side: usize, idx: Option<usize>) -> i64 {
    crate::battle::priority_base(packr, &act_of(bt, side, idx), bt.sides[side].active(), &bt.field)
}

/// このターンの行動順が同速の先後（乱数）で決まるか。対戦本体の speed_order を先後を両方に固定して呼び、結果が割れるかで判定する。
fn order_is_tie(packr: &Pack, bt: &Battle, acts: [Option<usize>; 2]) -> bool {
    if acts[0].is_none() || acts[1].is_none() { return false; }
    let (a0, a1) = (act_of(bt, 0, acts[0]), act_of(bt, 1, acts[1]));
    let mut f = bt.field.clone();
    let mut r = |t: bool| {
        f.speed_tie_p1_first = Some(t);
        crate::battle::speed_order(packr, &bt.sides[0], &a0, &bt.sides[1], &a1, &mut f, &mut FixedRng)
    };
    r(true) != r(false)
}

/// 1ターン実走し、そのターンの記録(RACE_LOG)を返す。
fn drive_logged(bt: &mut Battle, packr: &Pack, acts: [Option<usize>; 2]) -> Vec<crate::battle::RaceMark> {
    drive_logged_causes(bt, packr, acts).0
}

/// HPが動いた原因の記録 (区切りの番号, 側, 原因, 量)。
type Causes = Vec<(usize, usize, &'static str, i64)>;

/// 記録(RACE_LOG・RACE_CAUSES)を有効にして f を実行し、区切りと原因を返す。外側の記録は保つ。
fn with_log(f: impl FnOnce()) -> (Vec<crate::battle::RaceMark>, Causes) {
    let saved = crate::battle::RACE_LOG.with(|r| r.borrow_mut().replace(Vec::new()));
    let saved_c = crate::battle::RACE_CAUSES.with(|c| std::mem::take(&mut *c.borrow_mut()));
    f();
    let marks = crate::battle::RACE_LOG.with(|r| std::mem::replace(&mut *r.borrow_mut(), saved)).unwrap_or_default();
    let causes = crate::battle::RACE_CAUSES.with(|c| std::mem::replace(&mut *c.borrow_mut(), saved_c));
    (marks, causes)
}

/// 1ターン実走し、そのターンの区切りと原因を返す。
fn drive_logged_causes(bt: &mut Battle, packr: &Pack, acts: [Option<usize>; 2]) -> (Vec<crate::battle::RaceMark>, Causes) {
    with_log(|| drive_pair(bt, packr, acts))
}

/// 倒れた者が出たターンの勝者。None は相打ち。
/// そのターンの終わり（倒れた後も生き残った側のターン終了時処理まで進める）に両者が倒れていれば相打ち
/// （倒した行動の反動・いのちのたま・ゴツゴツメット、倒した後のターン終了時の毒・天候で自分も倒れた場合）。
/// 6体戦の中の1対面として見ると、同じターンに1体ずつ失う＝交換は五分。片方だけなら生き残った側の勝ち。
fn winner_of(marks: &[crate::battle::RaceMark]) -> Option<usize> {
    let h = marks.last()?.2;
    match (h[0] <= 0, h[1] <= 0) {
        (true, false) => Some(1),
        (false, true) => Some(0),
        _ => None,
    }
}


/// 勝った側 `w` が自分の行動の区切りで、ダメージの原因の記録なしに倒れたか（だいばくはつ・ミストバースト・いやしのねがい等の自分で倒れる技）。
fn self_ko_by_own_move(marks: &[crate::battle::RaceMark], causes: &Causes, w: usize) -> bool {
    for (k, m) in marks.iter().enumerate().skip(1) {
        let p = &marks[k - 1];
        if p.2[w] > 0 && m.2[w] <= 0 {
            if !(m.0 == 1 && m.1 == w) { return false; }
            // その区切りで記録された原因（ゴツゴツメット・さめはだ・反動・いのちのたま等）で倒れたなら自滅技ではない
            let known: i64 = causes.iter().filter(|c| c.0 == k && c.1 == w && c.3 > 0).map(|c| c.3).sum();
            return known < p.2[w];
        }
    }
    false
}


/// 各側が方針 `plans` のとおりに行動する対戦を、指定の乱数（判定は中央乱数 0.5）で決着まで回す。
pub fn sim_pair(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, plans: [Plan; 2],
                want_trace: bool, me_first_on_tie: bool, roll: f64, cap: i64) -> SimOut {
    sim_pair_memo(pack, spec_a, spec_b, season, plans, want_trace, me_first_on_tie, roll, cap, &mut SimMemo::default())
}

type ActHist = Vec<[Option<usize>; 2]>;

/// 1つの対面(同じ乱数)の方針の組を回すあいだの使い回し。局面は「同速時の先後・仮定の続きか・それまでの両者の行動列」で
/// 一意に決まる（固定乱数）ので、同じ行動列の区間は1回だけ実走する（最大打点と毎ターン最善手が同じ技を撃つ等）。
#[derive(Default)]
pub struct SimMemo {
    init: [Option<Battle>; 2],
    act: std::collections::HashMap<(bool, bool, ActHist, usize, Plan), Option<usize>>,
    best: std::collections::HashMap<(bool, bool, ActHist, usize, bool), BestAttack>,
}

impl SimMemo {
    fn action(&mut self, bt: &Battle, packr: &Pack, key: (bool, bool, &ActHist), side: usize, plan: Plan) -> Option<usize> {
        let k = (key.0, key.1, key.2.clone(), side, plan);
        if let Some(v) = self.act.get(&k) { return *v; }
        let best = &mut self.best;
        let v = plan_action_with(bt, packr, side, plan, &mut |s, av| {
            let bk = (key.0, key.1, key.2.clone(), s, av);
            if let Some(x) = best.get(&bk) { return *x; }
            let x = best_attack(bt, packr, s, av);
            best.insert(bk, x);
            x
        });
        self.act.insert(k, v);
        v
    }
}

fn sim_pair_memo(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, plans: [Plan; 2],
                 want_trace: bool, me_first_on_tie: bool, roll: f64, cap: i64, memo: &mut SimMemo) -> SimOut {
    let ti = if me_first_on_tie { 0 } else { 1 };
    let mut bt = match &memo.init[ti] {
        Some(b) => b.clone(),
        None => {
            let b = setup_plain_tie(pack, spec_a, spec_b, season, roll, Some(me_first_on_tie));
            memo.init[ti] = Some(b.clone());
            b
        }
    };
    let start_ev = if want_trace { start_events(pack, spec_a, spec_b, season, roll, Some(me_first_on_tie)) } else { Vec::new() };
    let packr: &Pack = pack;
    let mut hist: ActHist = Vec::new();
    let start_tie = bt.field.start_tie;
    let mut out = SimOut {
        me_first: me_first_on_tie, last_tie: false,
        t: [OUT_OF_RANGE; 2], first: None, speed: [0; 2], prio: [0; 2],
        acts: [Vec::new(), Vec::new()], trace: [Vec::new(), Vec::new()], race: Vec::new(), race_init: None,
        tie_seen: false, tie_speed: None, mutual: false, end_hp: [1.0; 2], faint_turn: [cap + 1; 2],
    };
    let spd = |b: &Battle, s: usize| crate::ai::effective_speed(packr, b.sides[s].active(), &b.field);
    out.speed = [spd(&bt, 0), spd(&bt, 1)];
    // 入場効果・メガシンカの順が同速で決まった対面は、行動順の同速と同じく両順を回す
    if start_tie {
        out.tie_seen = true;
        out.tie_speed = Some(out.speed);
    }
    while bt.turn < cap {
        let acts = [memo.action(&bt, packr, (me_first_on_tie, false, &hist), 0, plans[0]),
                    memo.action(&bt, packr, (me_first_on_tie, false, &hist), 1, plans[1])];
        if order_is_tie(packr, &bt, acts) {
            if !out.tie_seen { out.tie_speed = Some([spd(&bt, 0), spd(&bt, 1)]); }
            out.tie_seen = true;
        }
        // 手前の局面の写しは経過の表示用(want_trace)だけで取る。決着したターンは行動列から再生して作る（毎ターンの複製は重い）
        let snap_t = if want_trace { Some(bt.clone()) } else { None };
        let turn0 = bt.turn;
        if want_trace {
            for s in 0..2usize {
                let Some(mi) = acts[s] else { continue };
                let Some(mv) = bt.sides[s].active().moves.get(mi).cloned() else { continue };
                let dmg = mv.category != crate::pack::Cat::Status && mv.power.unwrap_or(0) > 0;
                let (lo, hi) = if dmg {
                    (move_total_damage(packr, &mut bt.clone(), s, &mv, 0.0),
                     move_total_damage(packr, &mut bt.clone(), s, &mv, 1.0))
                } else { (0, 0) };
                out.trace[s].push((mi, lo, hi, 0));
            }
        }
        let item_before = [bt.sides[0].active().item, bt.sides[1].active().item];
        let hist_before = hist.clone();
        hist.push(acts);
        let (marks, causes) = drive_logged_causes(&mut bt, packr, acts);
        if let Some(snap) = &snap_t {
            if snap.turn == 0 {
                if let Some(m0) = marks.first() {
                    let mut st = race_state(packr, m0);
                    // メガシンカ（分析は組み立て時にメガ後の姿で戦う＝実機の1ターン目の行動前）。再生で「メガシンカした」を出すための情報
                    let mega = |z: usize| {
                        let p = snap.sides[z].active();
                        match (&p.mega, p.mega_evolved) {
                            (Some(md), true) => serde_json::json!({"from": packr.intern.resolve(p.name), "to": md.mega_name,
                                                                  "ability": packr.intern.resolve(p.ability), "stone": md.mega_stone}),
                            _ => serde_json::Value::Null,
                        }
                    };
                    st["mega"] = serde_json::json!([mega(0), mega(1)]);
                    // 入場効果・メガシンカで発動した特性（実際の発動順）。再生の開始画面と1ターン目の先頭に出す
                    st["events"] = serde_json::json!(start_ev);
                    out.race_init = Some(st);
                }
            }
            race_entries(packr, snap, &marks, &causes, acts, &mut out.race);
        }
        for s in 0..2usize { out.acts[s].push(acts[s]); }
        if want_trace {
            for s in 0..2usize {
                if acts[s].is_none() { continue; }
                let d = bt.sides[1 - s].active();
                let l = &packr.sy.l;
                let mut h = 0;
                if d.is_alive {
                    let ib = item_before[1 - s];
                    if ib.is_some() && d.item != ib {
                        if ib == Some(l.オボンのみ) { h += d.max_hp / 4; }
                        else if ib == Some(l.オレンのみ) { h += 10; }
                    }
                    if d.item == Some(l.たべのこし) { h += (d.max_hp / 16).max(1); }
                }
                if let Some(x) = out.trace[s].last_mut() { x.3 = h; }
            }
        }
        let dead = [!bt.sides[0].active().is_alive, !bt.sides[1].active().is_alive];
        for s in 0..2usize {
            let p = bt.sides[s].active();
            out.end_hp[s] = p.hp.max(0) as f64 / p.max_hp.max(1) as f64;
            if dead[s] { out.faint_turn[s] = turn0 + 1; }
        }
        if !dead[0] && !dead[1] {
            continue;
        }
        let snap = match snap_t {
            Some(sn) => sn,
            None => {
                let mut sn = memo.init[ti].clone().expect("init");
                for a in &hist_before { drive_pair(&mut sn, packr, *a); }
                sn
            }
        };
        let turn = snap.turn + 1;
        out.speed = [spd(&snap, 0), spd(&snap, 1)];
        out.prio = [act_priority(packr, &snap, 0, acts[0]), act_priority(packr, &snap, 1, acts[1])];
        out.last_tie = order_is_tie(packr, &snap, acts);
        let Some(winner) = winner_of(&marks) else {
            out.mutual = true;
            out.t = [turn, turn];
            return out;
        };
        let l = 1 - winner;
        out.t[winner] = turn;
        out.first = Some(winner);
        // 負けた側(l)が倒されなかったら何ターン目に「技で」倒せたか。同じターンをやり直し、以降も同じ方針で続ける。
        // 勝った側の自滅(反動等)は l の手柄にしない。
        let w = winner;
        let mut cf = snap.clone();
        // 負けた側に「倒れても行動し続ける」印を付ける。HPは本物のまま（0で止まる）なので、ふんか・オボンのみ・マルチスケイル等の
        // HPで決まる要素は実際どおり。勝った側への反動も実際に減らしたHPが基準のまま（水増しで膨らまない）。
        cf.sides[l].active_mut().undying = true;
        let mut a = acts;
        let mut ch = hist_before;
        loop {
            ch.push(a);
            let (m, mc) = drive_logged_causes(&mut cf, packr, a);
            if cf.turn > turn {
                out.acts[l].push(a[l]);
            }
            if !cf.sides[w].active().is_alive {
                // 仮定の続きで勝った側が倒れたターン。負けた側が生きていたら起きること（技・ゴツゴツメット・さめはだ・反動・毒等）で倒れたら数える。
                // 勝った側が自分の技で倒れた（だいばくはつ・ミストバースト等。原因の記録が無いまま0になる）ときは、負けた側が倒したのではないので数えない。
                if !self_ko_by_own_move(&m, &mc, w) {
                    out.t[l] = cf.turn;
                }
                break;
            }
            if !cf.sides[l].active().is_alive || cf.turn >= cap {
                break;
            }
            // 方針の手の選択は「負けた側がまだ十分なHPで場にいる」前提で行う（0で止まったHPのまま選ぶと、
            // 勝った側の技の見込みダメージが0になって攻撃しなくなる）。実際の進行は本物のHPのまま。
            let (mh0, h0) = { let p = cf.sides[l].active(); (p.max_hp, p.hp) };
            {
                let p = cf.sides[l].active_mut();
                p.max_hp = mh0 * 64;
                p.hp = p.max_hp - (mh0 - h0);
            }
            a = [memo.action(&cf, packr, (me_first_on_tie, true, &ch), 0, plans[0]),
                 memo.action(&cf, packr, (me_first_on_tie, true, &ch), 1, plans[1])];
            {
                let p = cf.sides[l].active_mut();
                p.max_hp = mh0;
                p.hp = h0;
            }
        }
        return out;
    }
    out
}

/// 側 `s` の毎ターンの行: 撃った技の与ダメージ(最低/最高乱数、技そのものの値)、そのターンに相手が回復した量、
/// 相手が技以外で減らしたHP(相手自身の反動・ゴツゴツメット・天候等。`extra`)。ひるんだターンは `flinch`。
/// 自分が倒れて行動できなかったターン以降は出さない。
fn race_turns(sim: &SimOut, s: usize, info: &SideInfo) -> Vec<serde_json::Value> {
    use serde_json::json;
    let y = 1 - s;
    // trace は行動を選んだターンごとに1件。ターン番号に対応付ける。
    let mut lohi: HashMap<i64, (usize, i64, i64)> = HashMap::new();
    let mut k = 0usize;
    for (t, a) in sim.acts[s].iter().enumerate() {
        if a.is_some() {
            if let Some(&(mi, lo, hi, _)) = sim.trace[s].get(k) { lohi.insert(t as i64 + 1, (mi, lo, hi)); }
            k += 1;
        }
    }
    // そのターンに相手(y)が技以外で減らしたHP・回復。s の技によるものは除く。原因の行動が後から動いた側なら late。
    let extras_of = |turn: i64| -> (i64, Vec<serde_json::Value>) {
        let mut heal = 0i64;
        let mut extra: Vec<serde_json::Value> = Vec::new();
        for (fi, f) in sim.race.iter().enumerate().filter(|(_, f)| f["turn"].as_i64() == Some(turn)) {
            let f_late = f["actor"].as_u64().map_or(false, |fa| sim.race[..fi].iter()
                .any(|g| g["turn"].as_i64() == Some(turn) && g["actor"].as_u64().map_or(false, |ga| ga != fa)));
            for ev in f["events"].as_array().into_iter().flatten() {
                if ev["side"].as_u64() != Some(y as u64) { continue; }
                let amt = ev["amount"].as_i64().unwrap_or(0);
                if ev["kind"] == "move" && f["actor"].as_u64() == Some(s as u64) { continue; }
                if amt < 0 { heal -= amt; } else if amt > 0 {
                    extra.push(json!({"kind": ev["kind"], "amount": amt, "turn": turn, "late": f_late}));
                }
            }
        }
        (heal, extra)
    };
    let last_turn = sim.race.iter().filter_map(|e| e["turn"].as_i64()).max().unwrap_or(0);
    let mut rows = Vec::new();
    for turn in 1..=last_turn {
        let mine = sim.race.iter().enumerate()
            .find(|(_, e)| e["turn"].as_i64() == Some(turn) && e["actor"].as_u64() == Some(s as u64));
        let (heal, extra) = extras_of(turn);
        let Some((ei, e)) = mine else {
            // 自分は動けなかった(先に倒された)が、相手はそのターンに反動等でHPを減らした。行動は出さず、HPの変化だけ残す。
            if !extra.is_empty() || heal > 0 {
                rows.push(json!({"n": "", "lo": 0, "hi": 0, "heal": heal, "flinch": false, "idle": true,
                                 "extra": extra, "turn": turn, "late": false}));
            }
            continue;
        };
        // 同じターンに相手が先に動いていれば「後から動いた」（表示は 1' のようにダッシュを付ける）。
        let late = sim.race[..ei].iter().any(|f| f["turn"].as_i64() == Some(turn) && f["actor"].as_u64() == Some(y as u64));
        if e["flinch"] == true {
            rows.push(json!({"n": "", "lo": 0, "hi": 0, "heal": heal, "flinch": true, "extra": extra, "turn": turn, "late": late}));
            continue;
        }
        let (mi, lo, hi) = lohi.get(&turn).copied().unwrap_or((usize::MAX, 0, 0));
        let n = info.moves.get(mi).map(|(x, _)| x.clone()).unwrap_or_default();
        // 判定の対戦で実際に減ったHP（倒したターンは残りHPちょうど）。ダメージレースの棒はこれで描く。
        let dealt: i64 = e["events"].as_array().into_iter().flatten()
            .filter(|ev| ev["side"].as_u64() == Some(y as u64) && ev["kind"] == "move")
            .filter_map(|ev| ev["amount"].as_i64()).filter(|x| *x > 0).sum();
        rows.push(json!({"n": n, "lo": lo, "hi": hi, "dealt": dealt, "heal": heal, "flinch": false, "extra": extra, "turn": turn, "late": late,
                         "blocked": e["blocked"].clone()}));
    }
    rows
}

/// 1ターンぶんの記録(RACE_LOG)を、行動ごと・ターン終了時ごとの「誰のHPが何でいくら動いたか」にする。
/// 量は実際のHPの増減から出し、原因ごとの内訳の合計が必ず増減と一致するようにする
/// （内訳の推定がずれても、残りは「反動など」「ターン終了時」に入る）。amount は正=ダメージ・負=回復。
/// 再生表示用の両者の状態（HP・能力ランク・状態異常・持ち物・ばけのかわ）と天候。
fn race_state(packr: &Pack, m: &crate::battle::RaceMark) -> serde_json::Value {
    use serde_json::json;
    let nm = |s: Option<crate::interner::Sym>| s.map(|x| packr.intern.resolve(x).to_string());
    let side = |z: usize| json!({"hp": m.2[z], "stg": m.5[z], "status": nm(m.6[z]), "item": nm(m.3[z]), "disg": m.4[z]});
    json!({"sides": [side(0), side(1)], "weather": nm(m.7)})
}

fn race_entries(packr: &Pack, snap: &Battle, marks: &[crate::battle::RaceMark], causes: &Causes,
                acts: [Option<usize>; 2], out: &mut Vec<serde_json::Value>) {
    use serde_json::json;
    let turn = snap.turn + 1;
    let Some(first) = marks.first() else { return };
    let mut prev = first;
    for (k, m) in marks.iter().enumerate().skip(1) {
        let (phase, x, hp) = (m.0, m.1, m.2);
        let mut ev: Vec<serde_json::Value> = Vec::new();
        // 対戦本体が記録した原因（反動・いのちのたま・ゴツゴツメット・吸収・きのみ・天候・状態異常・回復等）
        let mut known = [0i64; 2];
        // 技のダメージの頭打ち前の値（HPの増減には入れない。move イベントの raw にだけ付ける）
        let mut raw = [0i64; 2];
        for c in causes.iter().filter(|c| c.0 == k) {
            if c.2 == "rawmove" { raw[c.1] += c.3; continue; }
            ev.push(json!({"side": c.1, "kind": c.2, "amount": c.3}));
            known[c.1] += c.3;
        }
        // 原因の分からない残り（=技のダメージ、行動側の自傷、ターン終了時のその他）
        let rest = |z: usize| prev.2[z] - hp[z] - known[z];
        match phase {
            1 => {
                let y = 1 - x;
                let mv = acts[x].and_then(|i| snap.sides[x].active().moves.get(i));
                // ばけのかわ: この行動で剥がれたなら、技は無効(0)で、減ったHPは剥がれたときの1/8。原因を分けて記録する。
                let busted = !prev.4[y] && m.4[y];
                let ry = rest(y);
                // ばけのかわの1/8は原因(disguise)として記録済み。残り(ry)は連続技の2発目以降など技のダメージ
                let pos = if busted { ev.iter().position(|e| e["kind"] == "disguise").map_or(0, |i| i + 1) } else { 0 };
                if ry > 0 && raw[y] > ry {
                    ev.insert(pos, json!({"side": y, "kind": "move", "amount": ry, "raw": raw[y]}));
                } else if ry > 0 {
                    ev.insert(pos, json!({"side": y, "kind": "move", "amount": ry}));
                } else if ry < 0 {
                    ev.push(json!({"side": y, "kind": "heal", "amount": ry}));
                }
                let rx = rest(x);
                if rx != 0 {
                    // だいばくはつ・じばく・ミストバースト で自分が倒れたぶんは selfko（再生で「◯◯は 倒れた！」の前に原因として出す）
                    let l = &packr.sy.l;
                    let selfko = mv.map_or(false, |m| m.name == l.だいばくはつ || m.name == l.じばく || m.name == l.ミストバースト);
                    let kind = if rx < 0 { "heal" } else if selfko { "selfko" } else { "other" };
                    ev.push(json!({"side": x, "kind": kind, "amount": rx}));
                }
                // 攻撃技を持たず何もしなかった行動は行にしない（表示で空行になるため）
                if mv.is_none() && ev.is_empty() { prev = m; continue; }
                let name = mv.map(|m| packr.intern.resolve(m.name).to_string());
                let blocked = if busted && ry <= 0 { json!("ばけのかわ") } else { json!(null) };
                out.push(json!({"turn": turn, "actor": x, "move": name, "flinch": false, "hp": hp, "events": ev, "blocked": blocked, "st": race_state(packr, m)}));
            }
            2 => {
                out.push(json!({"turn": turn, "actor": x, "move": null, "flinch": true, "hp": hp, "events": ev, "st": race_state(packr, m)}));
            }
            3 => {
                for z in 0..2usize {
                    let r = rest(z);
                    if r != 0 { ev.push(json!({"side": z, "kind": if r > 0 { "eot" } else { "heal" }, "amount": r})); }
                }
                if !ev.is_empty() {
                    out.push(json!({"turn": turn, "actor": null, "move": null, "flinch": false, "hp": hp, "events": ev, "st": race_state(packr, m)}));
                }
            }
            _ => {}
        }
        prev = m;
    }
}

/// 準備の技の候補（積み技1回・ねこだまし）。シナリオで積みを前提にしている側(side0)は積み技を候補にしない。
fn prep_candidates(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize) -> Vec<usize> {
    let bt = setup_plain(pack, spec_a, spec_b, season, 0.5);
    let packr: &Pack = pack;
    let p = bt.sides[att].active();
    let scen_boost = (att == 0 && packr.scenario.boost > 0) || (att == 1 && packr.scenario.opp_boost > 0);
    let mut out = Vec::new();
    for (i, m) in p.moves.iter().enumerate() {
        if m.name == packr.sy.l.ねこだまし {
            // タイプ無効(ゴースト)等で当たらない ねこだまし は「何もしない方針」になるので候補にしない
            let (_, dealt, ko, _) = probe_move(&bt, packr, att, i);
            if dealt > 0 || ko { out.push(i); }
        } else if !scen_boost
            && crate::battle::self_boosts(packr, m.name)
                .map_or(false, |v| v.iter().any(|(k, d)| *d > 0 && *k < 5)) {
            // 自分を強化する技はすべて候補（命中・回避だけを上げる技は、必中前提の判定では効果が無いので除く）
            out.push(i);
        }
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    fn pack() -> Pack {
        Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"))
    }

    const KAME: &str = "カメックス@カメックスナイト:ひかえめ:あくのはどう|からをやぶる|だいちのはどう|はどうだん:0/0/0/32/0/32:メガランチャー";
    const MANDA: &str = "ボーマンダ@ボーマンダナイト:むじゃき:じしん|すてみタックル|だいもんじ|りゅうせいぐん:0/32/0/8/0/24:スカイスキン";
    const NYU: &str = "オオニューラ@ノーマルジュエル:いじっぱり:ねこだまし|アクロバット|インファイト|フェイタルクロー:0/32/0/0/0/32:かるわざ";
    const ACE: &str = "エースバーン@こだわりスカーフ:ようき:かえんボール|とびひざげり|とんぼがえり|ダストシュート:0/32/0/0/0/32:リベロ";
    const GARD: &str = "ギルガルド@たべのこし:れいせい:かげうち|アイアンヘッド|キングシールド|シャドーボール:32/0/0/32/0/0:バトルスイッチ";

    fn idx(bt: &Battle, p: &Pack, side: usize, name: &str) -> usize {
        bt.sides[side].active().moves.iter().position(|m| p.intern.resolve(m.name) == name).unwrap()
    }
    fn spd(p: &Pack, bt: &Battle, s: usize) -> i64 {
        crate::ai::effective_speed(p, bt.sides[s].active(), &bt.field)
    }

    /// からをやぶる→攻撃: 判定の手数・素早さ・相手の手数が、対戦本体を直接回した結果と一致する。
    #[test]
    fn からをやぶる_判定が実際の対戦と一致() {
        let mut p = pack();
        let v = analyze_json(&mut p, KAME, MANDA, "M-3");
        let vd = &v["verdict"];
        assert_eq!(vd["myPrep"], "からをやぶる", "{vd}");
        let seq: Vec<String> = serde_json::from_value(vd["mySeq"].clone()).unwrap();
        assert_eq!(seq[0], "からをやぶる");
        // 対戦本体を直接回す: 1ターン目 からをやぶる / 相手は判定と同じ技
        let mut bt = setup_plain(&mut p, KAME, MANDA, "M-3", 0.0);
        let pr: &Pack = &p;
        let s0 = spd(pr, &bt, 0);
        assert!(s0 < spd(pr, &bt, 1), "カメックスは初期状態では遅い");
        let opp_i = idx(&bt, pr, 1, vd["oppMove"].as_str().unwrap());
        let smash = idx(&bt, pr, 0, "からをやぶる");
        drive_pair(&mut bt, pr, [Some(smash), Some(opp_i)]);
        let k = bt.sides[0].active();
        assert!(k.is_alive);
        // 攻撃はメガ前のボーマンダの いかく で -1 されてから +2
        assert_eq!((k.stage(0), k.stage(1), k.stage(2), k.stage(3), k.stage(4)), (1, -1, 2, -1, 2));
        let s1 = spd(pr, &bt, 0);
        assert_eq!(s1, s0 * 2, "素早さ+2で2倍");
        assert!(s1 > spd(pr, &bt, 1), "積んだ後は先に動ける");
        let mut turn = 1;
        while bt.sides[1].active().is_alive && turn < CAP {
            let a0 = plan_action(&bt, pr, 0, Plan::Seq(false));
            let a1 = Some(opp_i);
            drive_pair(&mut bt, pr, [a0, a1]);
            turn += 1;
        }
        assert!(!bt.sides[1].active().is_alive && bt.sides[0].active().is_alive, "先に倒す");
        assert_eq!(vd["myHits"].as_i64().unwrap(), turn);
        assert_eq!(vd["myS"].as_i64().unwrap(), s1, "決着ターンの素早さは積んだ後の値");
        assert_eq!(vd["koFirst"], true);
        assert_eq!(vd["win"], true);
        // 相手の手数は、からをやぶるで下がった防御に対して数えた値（相手を棒立ちにした確定数以下）。
        let idle = vd["oppHits"].as_i64().unwrap();
        let (base_hits, _) = run_move(&mut p, KAME, MANDA, "M-3", 1, opp_i, 0.0);
        assert!(idle <= base_hits, "守りが下がった分、相手の手数は増えない: {idle} vs {base_hits}");
        // 経過(race): 相手は2ターン目に動く前に倒れる。すてみタックルの反動は相手自身のHPを減らす。
        let race = vd["race"].as_array().unwrap();
        assert!(!race.iter().any(|e| e["turn"] == 2 && e["actor"] == 1), "倒れた後の相手の行動は出さない");
        assert!(race.iter().any(|e| e["events"].as_array().unwrap().iter()
            .any(|x| x["side"] == 1 && x["kind"] == "recoil" && x["amount"].as_i64().unwrap() > 0)));
        let last = race.last().unwrap();
        assert_eq!(last["hp"][1], 0);
        assert_eq!(v["b"]["turns"].as_array().unwrap().len(), 1, "相手の毎ターンは実際に動いた1ターンだけ");
        eprintln!("カメックス vs メガボーマンダ: {vd}");
    }

    /// からをやぶるの後、相手の2発目以降は下がった防御・特防に対して入る。
    #[test]
    fn 準備後の被ダメは下がった能力で数える() {
        let mut p = pack();
        let mut bt = setup_plain(&mut p, KAME, MANDA, "M-3", 0.0);
        let pr: &Pack = &p;
        let smash = idx(&bt, pr, 0, "からをやぶる");
        let atk = idx(&bt, pr, 1, "すてみタックル");
        let mut plain = bt.clone();
        drive_pair(&mut bt, pr, [Some(smash), None]);
        let hp0 = bt.sides[0].active().hp;
        drive_pair(&mut bt, pr, [None, Some(atk)]);
        let lowered = hp0 - bt.sides[0].active().hp;
        let hp1 = plain.sides[0].active().hp;
        drive_pair(&mut plain, pr, [None, Some(atk)]);
        let normal = hp1 - plain.sides[0].active().hp;
        assert!(lowered > normal, "防御-1で被ダメが増える: {lowered} vs {normal}");
    }

    /// ねこだまし＋ノーマルジュエル＋かるわざ: ジュエルが消費されて素早さが2倍になり、相手は1ターン目に動けない。
    #[test]
    fn ねこだまし_ジュエル_かるわざ() {
        let mut p = pack();
        let v = analyze_json(&mut p, NYU, ACE, "M-3");
        let vd = &v["verdict"];
        let mut bt = setup_plain(&mut p, NYU, ACE, "M-3", 0.0);
        let pr: &Pack = &p;
        let s0 = spd(pr, &bt, 0);
        assert!(s0 < spd(pr, &bt, 1), "スカーフのエースバーンが速い");
        let fo = idx(&bt, pr, 0, "ねこだまし");
        let foe = best_attack(&bt, pr, 1, false).map(|x| x.0);
        drive_pair(&mut bt, pr, [Some(fo), foe]);
        let n = bt.sides[0].active();
        assert_eq!(n.item, None, "ノーマルジュエルを消費");
        assert_eq!(n.stage(4), 2, "かるわざ");
        assert_eq!(spd(pr, &bt, 0), s0 * 2);
        assert_eq!(n.hp, n.max_hp, "相手はひるんで動けない");
        assert!(bt.sides[1].active().last_used_move.is_none());

        assert_eq!(vd["myPrep"], "ねこだまし", "{vd}");
        assert_eq!(vd["myS"].as_i64().unwrap(), s0 * 2);
        // 対戦本体をそのまま続けると、判定の手数どおりに先に倒す。相手は1ターン目に動けないので手数は2以上。
        let mut turn = 1;
        while bt.sides[1].active().is_alive && bt.sides[0].active().is_alive && turn < CAP {
            let a0 = best_attack(&bt, pr, 0, false).map(|x| x.0);
            let a1 = best_attack(&bt, pr, 1, false).map(|x| x.0);
            drive_pair(&mut bt, pr, [a0, a1]);
            turn += 1;
        }
        assert!(!bt.sides[1].active().is_alive && bt.sides[0].active().is_alive);
        assert_eq!(vd["myHits"].as_i64().unwrap(), turn);
        assert!(vd["oppHits"].as_i64().unwrap() >= 2, "{vd}");
        assert_eq!(vd["win"], true);
        eprintln!("オオニューラ vs エースバーン: {vd}");
    }

    /// ゴーストにはねこだましが当たらず、ひるみも起きない（相手は1ターン目に動ける）。
    #[test]
    fn ねこだましはゴーストに無効() {
        let mut p = pack();
        let mut bt = setup_plain(&mut p, NYU, GARD, "M-3", 0.0);
        let pr: &Pack = &p;
        let fo = idx(&bt, pr, 0, "ねこだまし");
        let foe = Some(idx(&bt, pr, 1, "シャドーボール"));
        let hp = bt.sides[1].active().hp;
        drive_pair(&mut bt, pr, [Some(fo), foe]);
        assert_eq!(bt.sides[1].active().hp, hp);
        assert!(bt.sides[1].active().last_used_move.is_some());
        assert_eq!(bt.sides[0].active().item, Some(pr.sy.it.ノーマルジュエル), "当たらなければ消費しない");
    }

    /// 相手を技で倒した直後に反動で自分も倒れたら相打ち。技で倒されずに反動で自滅したら相手の勝ち。
    #[test]
    fn 倒した行動の反動で倒れたら相打ち() {
        let hp = |a: i64, b: i64| [a, b];
        // side1 が後攻の技で side0 を倒し、同じ行動の反動で自分も倒れる
        let f = [false, false];
        let z = [[0i32; 5]; 2];
        let m1 = vec![(0u8, 0usize, hp(100, 100), [None, None], f, z, [None, None], None), (1, 0, hp(100, 40), [None, None], f, z, [None, None], None),
                      (1, 1, hp(0, 0), [None, None], f, z, [None, None], None)];
        assert_eq!(winner_of(&m1), None, "倒した行動の反動で自分も倒れたら相打ち");
        // side0 の技で倒せず反動で自滅 → side1 の勝ち
        let m2 = vec![(0u8, 0usize, hp(10, 100), [None, None], f, z, [None, None], None), (1, 0, hp(0, 60), [None, None], f, z, [None, None], None)];
        assert_eq!(winner_of(&m2), Some(1));
        // side0 が技で side1 を倒した後、そのターンのターン終了時に毒で自分も倒れる → 相打ち
        let m3 = vec![(0u8, 0usize, hp(10, 100), [None, None], f, z, [None, None], None), (1, 0, hp(10, 0), [None, None], f, z, [None, None], None),
                      (3, 0, hp(0, 0), [None, None], f, z, [None, None], None)];
        assert_eq!(winner_of(&m3), None, "倒した後のターン終了時に自分も倒れたら相打ち");
    }

    /// 仮定の続きで勝った側が倒れたとき、自分の技で倒れた（原因の記録なし）なら数えない・ゴツゴツメット等の原因があれば数える。
    #[test]
    fn 仮定の続きの自滅技の判定() {
        let f = [false, false];
        let z = [[0i32; 5]; 2];
        let mk = |ph: u8, x: usize, h0: i64, h1: i64| (ph, x, [h0, h1], [None, None], f, z, [None, None], None);
        // side1(勝った側) が自分の行動の区切りで 50→0（原因なし＝だいばくはつ等）
        let m = vec![mk(0, 0, 100, 50), mk(1, 1, 100, 0)];
        assert!(self_ko_by_own_move(&m, &Vec::new(), 1));
        // 同じ区切りでゴツゴツメット50（相手由来）→ 数える
        let c: Causes = vec![(1, 1, "helmet", 50)];
        assert!(!self_ko_by_own_move(&m, &c, 1));
        // 相手の行動の区切りで倒れた → 数える
        let m2 = vec![mk(0, 0, 100, 50), mk(1, 0, 100, 0)];
        assert!(!self_ko_by_own_move(&m2, &Vec::new(), 1));
    }

    /// 同じターン数で倒せるなら反動の無い技を選ぶ（メガボーマンダは じしん でオオニューラを確1）。
    #[test]
    fn 同じ確定数なら反動の無い技() {
        let mut p = pack();
        let manda = "ボーマンダ@ボーマンダナイト:いじっぱり:じしん|すてみタックル|はねやすめ|りゅうのまい:0/32/0/0/0/32:スカイスキン";
        let v = analyze_json(&mut p, NYU, manda, "M-3");
        assert_eq!(v["verdict"]["oppMove"], "じしん", "{}", v["verdict"]);
        let race = v["verdict"]["race"].as_array().unwrap();
        assert!(race.iter().all(|e| e["move"] != "すてみタックル"), "{race:?}");
    }

    /// 「積んだ状態なら」の指定(scenario.boost)がある側は、積み技を準備の手として二重に数えない。
    #[test]
    fn シナリオの積みと準備の手を二重に数えない() {
        let mut p = pack();
        p.scenario.boost = 1;
        let v = analyze_json(&mut p, KAME, MANDA, "M-3");
        p.scenario = crate::pack::Scenario::default();
        assert_ne!(v["verdict"]["myPrep"], "からをやぶる", "{}", v["verdict"]);
    }

    /// 相手側の積み指定(opp_boost): 相手の先頭の積み技の段階を最初から入れ、相手の積み技を準備の手にしない。0 なら従来と完全一致。
    #[test]
    fn 相手側の積み指定() {
        let mut p = pack();
        let manda = "ボーマンダ@ボーマンダナイト:いじっぱり:じしん|すてみタックル|はねやすめ|りゅうのまい:0/32/0/0/0/32:スカイスキン";
        let base = analyze_json(&mut p, KAME, manda, "M-3");
        p.scenario.opp_boost = 0;
        let zero = analyze_json(&mut p, KAME, manda, "M-3");
        assert_eq!(base, zero);
        p.scenario.opp_boost = 1;
        let v = analyze_json(&mut p, KAME, manda, "M-3");
        let bt = setup_plain(&mut p, KAME, manda, "M-3", 0.0);
        let (a1, s1) = (bt.sides[1].active().stage(0), bt.sides[1].active().stage(4));
        p.scenario = crate::pack::Scenario::default();
        assert_eq!((a1, s1), (1, 1), "りゅうのまい+1");
        assert_ne!(v["verdict"]["oppPrep"], "りゅうのまい");
        assert_ne!(v["verdict"]["sym"], base["verdict"]["sym"], "{} vs {}", v["verdict"], base["verdict"]);
    }
}
