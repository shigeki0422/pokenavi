//! 1v1 表示のためのルール層 API。Python の正本は `scripts/_mu_engine.py`。
//!
//! ここが担うのは「対戦本体を実走して確定数とダメージを得ること」だけで、
//! 割合(%)・乱数n発の確率・記号(◎○△▲×)の閾値といった表示計算は呼び出し側に置く。
//! ルールを持つ部分だけを一箇所に集めるのが目的で、表示計算を混ぜると
//! 「同じ判定が二重実装される」という当初の問題がここに再発する。
use crate::battle::{entry_effects, ActKind, Action, Battle, Side};
use crate::damage::Field;
use crate::pack::Pack;
use crate::poke::{build_poke, mega_evolve_poke, Poke};
use crate::rng::BRng;
use std::collections::HashMap;

/// これ以上かかる技は「圏外」。`_mu_engine.CAP` と同値。
pub const CAP: i64 = 12;
pub const OUT_OF_RANGE: i64 = 999;
/// ダメージ乱数の段階数（85%〜100% の16段）。
pub const ROLLS: usize = 16;

/// 1.0 ちょうど未満の最大の f64。`_mu_engine` の `math.nextafter(1.0, 0.0)` と同値。
/// 判定は全て `rng() < prob` なので、prob<1 の追加効果は不発、prob=1 の確定効果
/// （必中急所・りゅうせいぐんの特攻ダウン等）だけが発動する。1.0 を入れると
/// `1.0 < 1.0` が偽になり確定効果まで殺す（Python 側で実際に殺していた）。
const ALMOST_ONE: f64 = f64::from_bits(0x3FEF_FFFF_FFFF_FFFF);

struct FixedRng;
impl BRng for FixedRng {
    fn random(&mut self) -> f64 { ALMOST_ONE }
    fn choice(&mut self, _n: usize) -> usize { 0 }
    fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
    /// 連続技(2〜5発)の回数。確定数は保証値なので最小の2発。
    /// Python の `random.choices([2,3,4,5], ...)` を先頭固定した値と同じ。
    fn choices(&mut self) -> i64 { 2 }
}

/// 正規化ロール（0.0=最低乱数, 1.0=最高乱数）。`calc_damage` は `0.85 + r*0.15` で使う。
#[inline]
pub fn roll_of(step: usize) -> f64 {
    step as f64 / (ROLLS - 1) as f64
}

fn setup(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64) -> Battle {
    let mut a: Poke = build_poke(pack, spec_a, season);
    let mut b: Poke = build_poke(pack, spec_b, season);
    {
        let p: &Pack = pack;
        mega_evolve_poke(p, &mut a);
        mega_evolve_poke(p, &mut b);
    }
    let mut field = Field { roll_override: Some(roll), always_hit: true, ..Default::default() };
    let mut s1 = Side { party: vec![a], active_idx: 0, ..Default::default() };
    let mut s2 = Side { party: vec![b], active_idx: 0, ..Default::default() };
    {
        let p: &Pack = pack;
        entry_effects(p, &mut s1, 0, &mut field, &mut s2.party[0]);
        entry_effects(p, &mut s2, 1, &mut field, &mut s1.party[0]);
    }
    Battle::new(s1, s2, field)
}

/// 攻撃側が同じ技を撃ち続け、防御側は行動しない。`_mu_engine._run_inner` と同じ手順。
fn drive(bt: &mut Battle, pack: &Pack, move_idx: usize, max_turns: i64) -> i64 {
    let mut rng = FixedRng;
    let mut turns = 0i64;
    bt.run_loop_lim(pack, &mut rng, max_turns, |b2, _r| {
        turns += 1;
        let mv = b2.sides[0].active().moves.get(move_idx).cloned();
        [
            Action { kind: ActKind::Move, mv, move_idx: move_idx as i64, ..Default::default() },
            Action::default(),
        ]
    }, |_| {});
    turns
}

/// `spec_a` が `move_idx` の技を撃ち続けて `spec_b` を倒すまでの発数と、初撃の与ダメージ。
/// 倒しきれなければ発数は `OUT_OF_RANGE`。
pub fn run_move(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, move_idx: usize, roll: f64,
) -> (i64, i64) {
    let mut bt = setup(pack, spec_a, spec_b, season, roll);
    let hp0 = bt.sides[1].active().max_hp;
    // 初撃ダメージは1ターンだけ進めた時点で測る（2発目以降は自己ランク変化等で変わる）
    let packr: &Pack = pack;
    drive(&mut bt, packr, move_idx, 1);
    let first = hp0 - bt.sides[1].active().hp;
    let mut turns = 1i64;
    if bt.sides[1].has_alive() {
        turns += drive(&mut bt, packr, move_idx, CAP);
    }
    let hits = if bt.sides[1].has_alive() { OUT_OF_RANGE } else { turns };
    (hits, first.max(0))
}

/// 使用 k 回目（1-origin）の与ダメージを、16段の乱数それぞれについて返す。
/// k-1 回目までは最低乱数で進めた状態を基準にする（乱数n発の確率計算の入力）。
pub fn damage_dist(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, move_idx: usize, k: usize,
) -> [i64; ROLLS] {
    let mut base = setup(pack, spec_a, spec_b, season, 0.0);
    let packr: &Pack = pack;
    if k > 1 {
        drive(&mut base, packr, move_idx, (k - 1) as i64);
    }
    let mut out = [0i64; ROLLS];
    for (step, slot) in out.iter_mut().enumerate() {
        let mut bt = base.clone();
        bt.field.roll_override = Some(roll_of(step));
        let before = bt.sides[1].active().hp;
        let lim = bt.turn + 1;
        drive(&mut bt, packr, move_idx, lim);
        *slot = (before - bt.sides[1].active().hp).max(0);
    }
    out
}

/// 入場効果まで済ませた時点の、両者の実効素早さと最大HP・技名。
pub struct SideInfo {
    pub hp: i64,
    pub speed: i64,
    pub moves: Vec<(String, bool)>, // (技名, ダメージ技か)
}

pub fn side_info(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str) -> (SideInfo, SideInfo) {
    let bt = setup(pack, spec_a, spec_b, season, 0.0);
    let packr: &Pack = pack;
    let one = |p: &Poke| SideInfo {
        hp: p.max_hp,
        speed: crate::ai::effective_speed(packr, p, &bt.field),
        moves: p
            .moves
            .iter()
            .map(|m| {
                (
                    packr.intern.resolve(m.name).to_string(),
                    m.category != crate::pack::Cat::Status && m.power.unwrap_or(0) > 0,
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
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, move_idx: usize, hits: usize,
) -> f64 {
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
                drive(&mut c, packr, move_idx, lim);
                if !c.sides[1].has_alive() {
                    ko += p;
                    continue;
                }
                let key = { let d = c.sides[1].active(); (d.hp, d.item) };
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
