//! フル対戦のエントリポイント。`_v3_rollout._greedy_3v3` を Rust だけで再現する。
//!
//! Python 正本（_v3_rollout.py:15-35）:
//!   random.seed(seed) → 6体×2をspecから build_from_spec(randomize=True)
//!   → 指定3体を取り出し最速をリードに並べる（空 BattleField で素早さ評価）
//!   → BattleSide(source6=6体) / Battle(s1,s2,BattleField()).run(ai1,ai2)
//!   ai は GreedyAI + certain_ko_override
use crate::ai::{effective_speed, Ai};
use crate::battle::{Battle, Side};
use crate::cpyrng::CpyRandom;
use crate::damage::Field;
use crate::interner::Sym;
use crate::pack::{Pack, Ty};
use crate::poke::{build_poke_rand, Poke};

pub type PvEntry = (Sym, Ty, Option<Ty>, Ty, Option<Ty>);

pub fn preview_of(party: &[Poke]) -> Vec<PvEntry> {
    party.iter().map(|p| (p.name, p.base_type1, p.base_type2, p.type1, p.type2)).collect()
}

/// `order(P, sub)`: 3体のうち最速をリードに（Python の max は最初の最大要素）
fn order(pack: &Pack, party: &[Poke], sub: &[usize], f: &Field) -> Vec<Poke> {
    let mons: Vec<&Poke> = sub.iter().map(|&i| &party[i]).collect();
    let mut ld = 0usize;
    let mut bv = i64::MIN;
    for (j, m) in mons.iter().enumerate() {
        let v = effective_speed(pack, m, f);
        if j == 0 || v > bv {
            bv = v;
            ld = j;
        }
    }
    let mut out = vec![mons[ld].clone()];
    for (j, m) in mons.iter().enumerate() {
        if j != ld {
            out.push((*m).clone());
        }
    }
    out
}

pub struct BattleOut {
    pub result: i64,
    pub turns: i64,
}

/// 完全ネイティブのフル対戦（AI・RNG込み）。
#[allow(clippy::too_many_arguments)]
pub fn full_battle(
    pack: &mut Pack,
    pa: &[String],
    sa: &[usize],
    pb: &[String],
    sb: &[usize],
    season_a: &str,
    season_b: &str,
    seed: i128,
    ai1: (Ai, bool),
    ai2: (Ai, bool),
    randomize: bool,
    roll_override: Option<f64>,
    mut on_turn: impl FnMut(&Pack, &Battle),
) -> BattleOut {
    let mut rng = CpyRandom::new(seed);
    let f = Field::default();

    let mut a6: Vec<Poke> = Vec::with_capacity(pa.len());
    for s in pa {
        let mut r: Option<&mut dyn crate::rng::BRng> =
            if randomize { Some(&mut rng) } else { None };
        a6.push(build_poke_rand(pack, s, season_a, &mut r));
    }
    let mut b6: Vec<Poke> = Vec::with_capacity(pb.len());
    for s in pb {
        let mut r: Option<&mut dyn crate::rng::BRng> =
            if randomize { Some(&mut rng) } else { None };
        b6.push(build_poke_rand(pack, s, season_b, &mut r));
    }

    let p1 = order(pack, &a6, sa, &f);
    let p2 = order(pack, &b6, sb, &f);
    // HIDDEN_SELECTION 既定ON: 6体ソースの方が多ければそちらを見せ合う
    let pv1 = if b6.len() > p2.len() { preview_of(&b6) } else { preview_of(&p2) };
    let pv2 = if a6.len() > p1.len() { preview_of(&a6) } else { preview_of(&p1) };

    let n6a: Vec<Sym> = a6.iter().map(|p| p.name).collect();
    let n6b: Vec<Sym> = b6.iter().map(|p| p.name).collect();
    let s1 = Side { party: p1, active_idx: 0, source6_names: n6a, ..Default::default() };
    let s2 = Side { party: p2, active_idx: 0, source6_names: n6b, ..Default::default() };
    let field = Field { roll_override, ..Default::default() };
    let mut b = Battle::new(s1, s2, field);
    let packr: &Pack = pack;
    b.start(packr, &pv1, &pv2);
    let result = b.run_with_ai(packr, ai1, ai2, &mut rng, |bt| on_turn(packr, bt));
    BattleOut { result, turns: b.turn }
}

/// `_greedy_3v3(pa, sa, pb, sb, seed) -> 1/2/0`
pub fn greedy_3v3(
    pack: &mut Pack,
    pa: &[String],
    sa: &[usize],
    pb: &[String],
    sb: &[usize],
    season: &str,
    seed: i128,
) -> i64 {
    full_battle(
        pack,
        pa,
        sa,
        pb,
        sb,
        season,
        season,
        seed,
        (Ai::Greedy, true),
        (Ai::Greedy, true),
        true,
        None,
        |_, _| {},
    )
    .result
}


// ══════════════════════════════════════════════════════════════════════════
//  MCTS フル対戦（`_v3_final._mcts_3v3` / `_o1_policy._mcts_vs_dist` の再現）
// ══════════════════════════════════════════════════════════════════════════
use crate::ai::certain_ko_override;
use crate::belief::OpponentBelief;
use crate::net::NetW;
use crate::search::SearchAI;

/// belief のシーズン（`OpponentBelief(L)` の既定引数 season="M-2"）
pub const BELIEF_SEASON: &str = "M-2";

/// `_v3_final._mcts_3v3(pa, sa, pb, sb, seed)`（両者MCTS・certain_ko_override 付き）
#[allow(clippy::too_many_arguments)]
pub fn mcts_3v3(
    pack: &mut Pack,
    net: &NetW,
    pa: &[String],
    sa: &[usize],
    pb: &[String],
    sb: &[usize],
    season_a: &str,
    season_b: &str,
    seed: i128,
    sims: usize,
    mut on_turn: impl FnMut(&Pack, &Battle),
) -> (i64, i64) {
    let mut rng = CpyRandom::new(seed);
    let f = Field::default();
    let mut a6: Vec<Poke> = Vec::with_capacity(pa.len());
    for s in pa {
        let mut r: Option<&mut dyn crate::rng::BRng> = Some(&mut rng);
        a6.push(build_poke_rand(pack, s, season_a, &mut r));
    }
    let mut b6: Vec<Poke> = Vec::with_capacity(pb.len());
    for s in pb {
        let mut r: Option<&mut dyn crate::rng::BRng> = Some(&mut rng);
        b6.push(build_poke_rand(pack, s, season_b, &mut r));
    }
    let p1 = order(pack, &a6, sa, &f);
    let p2 = order(pack, &b6, sb, &f);
    let pv1 = if b6.len() > p2.len() { preview_of(&b6) } else { preview_of(&p2) };
    let pv2 = if a6.len() > p1.len() { preview_of(&a6) } else { preview_of(&p1) };
    let n6a: Vec<Sym> = a6.iter().map(|p| p.name).collect();
    let n6b: Vec<Sym> = b6.iter().map(|p| p.name).collect();
    let s1 = Side { party: p1, active_idx: 0, source6_names: n6a, ..Default::default() };
    let s2 = Side { party: p2, active_idx: 0, source6_names: n6b, ..Default::default() };
    let mut b = Battle::new(s1, s2, Field::default());
    {
        let packr: &Pack = pack;
        b.start(packr, &pv1, &pv2);
    }
    // 実戦の belief（両サイド）は Battle 外に持ち、observe_damage 用に Side へ差し込む
    crate::search::set_belief(&mut b.sides[0], OpponentBelief::new(BELIEF_SEASON));
    crate::search::set_belief(&mut b.sides[1], OpponentBelief::new(BELIEF_SEASON));

    let packr: &Pack = pack;
    let mut ai1 = SearchAI::new(packr, BELIEF_SEASON, seed, sims);
    let mut ai2 = SearchAI::new(packr, BELIEF_SEASON, seed ^ 0x5bd1e995, sims);
    let result = run_two_mcts(packr, net, &mut b, &mut ai1, &mut ai2, &mut rng, on_turn);
    (result, b.turn)
}

/// グローバル乱数を select_party の2引数（BRng と srng クロージャ）へ共有するアダプタ
struct SharedRng<'a>(&'a std::cell::RefCell<CpyRandom>);
impl crate::rng::BRng for SharedRng<'_> {
    fn random(&mut self) -> f64 {
        self.0.borrow_mut().random()
    }
    fn choice(&mut self, n: usize) -> usize {
        self.0.borrow_mut().choice(n)
    }
    fn randint(&mut self, a: i64, b: i64) -> i64 {
        self.0.borrow_mut().randint(a, b)
    }
    fn choices(&mut self) -> i64 {
        self.0.borrow_mut().choices()
    }
}

/// `_o1_policy._mcts_vs_dist(pa, sa, pb, seed)`
/// subject(pa) は sa 固定・相手(pb) は見せ合いから temperature=0.3 で選出（グローバル乱数）。
#[allow(clippy::too_many_arguments)]
pub fn mcts_vs_dist(
    pack: &mut Pack,
    net: &NetW,
    pa: &[String],
    sa: &[usize],
    pb: &[String],
    season_a: &str,
    season_b: &str,
    seed: i128,
    sims: usize,
) -> i64 {
    let cell = std::cell::RefCell::new(CpyRandom::new(seed));
    let f = Field::default();
    let mut a6: Vec<Poke> = Vec::with_capacity(pa.len());
    for s in pa {
        let mut sr = SharedRng(&cell);
        let mut r: Option<&mut dyn crate::rng::BRng> = Some(&mut sr);
        a6.push(build_poke_rand(pack, s, season_a, &mut r));
    }
    let mut b6: Vec<Poke> = Vec::with_capacity(pb.len());
    for s in pb {
        let mut sr = SharedRng(&cell);
        let mut r: Option<&mut dyn crate::rng::BRng> = Some(&mut sr);
        b6.push(build_poke_rand(pack, s, season_b, &mut r));
    }
    let p1 = order(pack, &a6, sa, &f);
    let idx2 = {
        let packr: &Pack = pack;
        let mut sr = SharedRng(&cell);
        let mut srng = || cell.borrow_mut().random();
        crate::ai::select_party(packr, &mut b6, &mut a6, 3, 0.3, 50.0, &mut sr, &mut srng)
    };
    let p2: Vec<Poke> = idx2.iter().map(|&i| b6[i].clone()).collect();

    let pv1 = if b6.len() > p2.len() { preview_of(&b6) } else { preview_of(&p2) };
    let pv2 = if a6.len() > p1.len() { preview_of(&a6) } else { preview_of(&p1) };
    let n6a: Vec<Sym> = a6.iter().map(|p| p.name).collect();
    let n6b: Vec<Sym> = b6.iter().map(|p| p.name).collect();
    let s1 = Side { party: p1, active_idx: 0, source6_names: n6a, ..Default::default() };
    let s2 = Side { party: p2, active_idx: 0, source6_names: n6b, ..Default::default() };
    let mut b = Battle::new(s1, s2, Field::default());
    {
        let packr: &Pack = pack;
        b.start(packr, &pv1, &pv2);
    }
    crate::search::set_belief(&mut b.sides[0], OpponentBelief::new(BELIEF_SEASON));
    crate::search::set_belief(&mut b.sides[1], OpponentBelief::new(BELIEF_SEASON));
    let packr: &Pack = pack;
    let mut ai1 = SearchAI::new(packr, BELIEF_SEASON, seed, sims);
    let mut ai2 = SearchAI::new(packr, BELIEF_SEASON, seed ^ 0x5bd1e995, sims);
    let mut rng = cell.into_inner();
    run_two_mcts(packr, net, &mut b, &mut ai1, &mut ai2, &mut rng, |_, _| {})
}

/// 両者 SearchAI + certain_ko_override でターンループを回す共通部
fn run_two_mcts(
    packr: &Pack,
    net: &NetW,
    b: &mut Battle,
    ai1: &mut SearchAI,
    ai2: &mut SearchAI,
    rng: &mut CpyRandom,
    mut on_turn: impl FnMut(&Pack, &Battle),
) -> i64 {
    b.run_loop(
        packr,
        rng,
        |bt, rng| {
            let mut out: [crate::battle::Action; 2] = [Default::default(), Default::default()];
            for sx in 0..2usize {
                let mut bl = bt.sides[sx].belief.0.take().unwrap();
                let ai: &mut SearchAI = if sx == 0 { ai1 } else { ai2 };
                let a = ai.choose(packr, net, &mut bt.sides, sx, &mut bt.field, &mut bl, rng);
                bt.sides[sx].belief.0 = Some(bl);
                let (me, op) = crate::battle::split2(&mut bt.sides, sx);
                out[sx] = certain_ko_override(packr, a, me, op, &mut bt.field, rng);
            }
            out
        },
        |bt| on_turn(packr, bt),
    )
}
