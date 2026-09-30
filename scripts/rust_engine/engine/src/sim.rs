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
    // 計測用: SEL_KEEP_ORDER=1 なら渡された並び（先頭＝sub[0]）のまま使う（選出の先頭を比べる用。既定は最速を先頭）
    if std::env::var("SEL_KEEP_ORDER").map(|v| v == "1").unwrap_or(false) {
        return mons.into_iter().cloned().collect();
    }
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
    // 検証用: BELIEF_PROBE=1 で両サイドに信念を付けて走らせ、終局後の P1 の信念を控える
    // （Python の同じ対戦と、信念の更新が 1:1 か突き合わせるため）
    let probe = std::env::var("BELIEF_PROBE").map(|v| v == "1").unwrap_or(false);
    if probe {
        crate::search::set_belief(&mut b.sides[0], OpponentBelief::new(belief_season()));
        crate::search::set_belief(&mut b.sides[1], OpponentBelief::new(belief_season()));
    }
    // 検証用: PREDICT_PROBE=1 で各ターン終了時の両AIの「相手の型の読み」を控える（predict.py と突き合わせ）
    let pprobe = std::env::var("PREDICT_PROBE").map(|v| v == "1").unwrap_or(false);
    let joint = std::env::var("JOINT_BUILD").map(|v| v != "0").unwrap_or(true);
    let mut app: [Vec<String>; 2] = [Vec::new(), Vec::new()];
    let mut snaps: Vec<(i64, String, String)> = Vec::new();
    let result = b.run_with_ai(packr, ai1, ai2, &mut rng, |bt| {
        if pprobe {
            for s in 0..2 {
                let n = packr.intern.resolve(bt.sides[1 - s].active().name).to_string();
                if !app[s].contains(&n) {
                    app[s].push(n);
                }
            }
            let a = crate::predict::snapshot(packr, &bt.sides[0], &app[0], joint).to_string();
            let c = crate::predict::snapshot(packr, &bt.sides[1], &app[1], joint).to_string();
            snaps.push((bt.turn, a, c));
        }
        on_turn(packr, bt)
    });
    if pprobe {
        PPROBE.with(|c| *c.borrow_mut() = std::mem::take(&mut snaps));
    }
    if probe {
        if let Some(bl) = b.sides[0].belief.0.take() {
            let season = belief_season().to_string();
            let mut out = Vec::new();
            for (name, pb) in bl.species.iter() {
                let mut pb = pb.clone();
                let pw: Vec<f64> = match (packr.build_pool.get(name),
                                          crate::poke::get_pokemon_template(packr, name, &season)) {
                    (Some(arr), Some(t)) => pb.pool_weights(packr, &t, arr).to_vec(),
                    _ => Vec::new(),
                };
                out.push((name.clone(), pb.post.clone(), pw, pb.known_moves.clone(),
                          pb.known_item.clone(), pb.item_lost, pb.absent_items.clone()));
            }
            PROBE.with(|c| *c.borrow_mut() = out);
        }
    }
    BattleOut { result, turns: b.turn }
}

type ProbeRow = (String, Vec<f64>, Vec<f64>, Vec<String>, Option<String>, bool, Vec<String>);
thread_local! {
    static PROBE: std::cell::RefCell<Vec<ProbeRow>> = const { std::cell::RefCell::new(Vec::new()) };
}

thread_local! {
    static PPROBE: std::cell::RefCell<Vec<(i64, String, String)>> = const { std::cell::RefCell::new(Vec::new()) };
}

/// PREDICT_PROBE=1 で走らせた直前の対戦の、各ターンの (ターン, side1の読みJSON, side2の読みJSON)
pub fn predict_probe_take() -> Vec<(i64, String, String)> {
    PPROBE.with(|c| std::mem::take(&mut *c.borrow_mut()))
}

pub fn belief_probe_take() -> Vec<ProbeRow> {
    PROBE.with(|c| std::mem::take(&mut *c.borrow_mut()))
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

/// belief のシーズン。Python の `belief._default_belief_season()` と同じ解決順
/// （BELIEF_SEASON > POOL_SEASON > M-6）。以前は "M-2" 固定で、M-6 の対戦でも
/// M-2 の使用率分布から相手の型を決定化していた。
pub fn belief_season() -> &'static str {
    static S: std::sync::OnceLock<String> = std::sync::OnceLock::new();
    S.get_or_init(|| {
        std::env::var("BELIEF_SEASON")
            .or_else(|_| std::env::var("POOL_SEASON"))
            .unwrap_or_else(|_| "M-6".to_string())
    })
}

/// `_v3_final._mcts_3v3(pa, sa, pb, sb, seed)`（両者MCTS・certain_ko_override 付き）
#[allow(clippy::too_many_arguments)]
/// 側ごとに探索量を変えられる版。sims=A側 / sims_b=B側。
/// A/B ハーネスが SIMS_B を渡しても黙って無視されていたため追加（探索量の比較が
/// 実際には同一 sims の健全性チェックになっていた）。
#[allow(clippy::too_many_arguments)]
pub fn mcts_3v3_sims(
    pack: &mut Pack,
    net: &NetW,
    net_b: Option<&NetW>,
    pa: &[String],
    sa: &[usize],
    pb: &[String],
    sb: &[usize],
    season_a: &str,
    season_b: &str,
    seed: i128,
    sims: usize,
    sims_b: usize,
    on_turn: impl FnMut(&Pack, &Battle),
) -> (i64, i64) {
    mcts_3v3_inner(pack, net, net_b, pa, sa, pb, sb, season_a, season_b, seed, sims, sims_b, on_turn)
}

pub fn mcts_3v3(
    pack: &mut Pack,
    net: &NetW,
    net_b: Option<&NetW>,
    pa: &[String],
    sa: &[usize],
    pb: &[String],
    sb: &[usize],
    season_a: &str,
    season_b: &str,
    seed: i128,
    sims: usize,
    on_turn: impl FnMut(&Pack, &Battle),
) -> (i64, i64) {
    mcts_3v3_inner(pack, net, net_b, pa, sa, pb, sb, season_a, season_b, seed, sims, sims, on_turn)
}

#[allow(clippy::too_many_arguments)]
fn mcts_3v3_inner(
    pack: &mut Pack,
    net: &NetW,
    net_b: Option<&NetW>,
    pa: &[String],
    sa: &[usize],
    pb: &[String],
    sb: &[usize],
    season_a: &str,
    season_b: &str,
    seed: i128,
    sims: usize,
    sims_b: usize,
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
    crate::search::set_belief(&mut b.sides[0], OpponentBelief::new(belief_season()));
    crate::search::set_belief(&mut b.sides[1], OpponentBelief::new(belief_season()));

    let packr: &Pack = pack;
    let mut ai1 = SearchAI::new(packr, belief_season(), seed, sims);
    let mut ai2 = SearchAI::new(packr, belief_season(), seed ^ 0x5bd1e995, sims_b);
    // 側2だけ探索パラメータを変える（*_2 の env）。A/B で片側だけ設定を振るため。
    // SearchAI::new が読む MCTS_FPU 等は両側に同じく効くので、そのままでは片側比較にならない。
    let f2 = |k: &str| std::env::var(format!("{k}_2")).ok().and_then(|v| v.parse::<f64>().ok());
    if let Some(v) = f2("MCTS_FPU") { ai2.mcts_fpu = v; }
    if let Some(v) = f2("RM_PRIOR_MIX") { ai2.rm_prior_mix = v; }
    if let Some(v) = f2("MCTS_P_FLOOR") { ai2.mcts_p_floor = v; }
    if let Some(v) = f2("QSELECT_FRAC") { ai2.qselect_frac = v; }
    if let Some(v) = f2("SOLVE_PLAY") { ai2.solve_play = v > 0.5; }
    if let Some(v) = f2("MCTS_MAX_DEPTH") { ai2.mcts_max_depth = v as usize; }
    // ORACLE_2=0 で側2だけ通常の決定化に戻す（片側だけ完全情報＝型予測の伸び代の測定）。
    // ORACLE=1 は両側に効くので「隠れ情報の無い別ゲーム」になってしまう。
    if let Some(v) = f2("ORACLE") { ai2.oracle = v > 0.5; }
    if let Some(v) = f2("JOINT_BUILD") { ai2.joint_build = v > 0.5; }
    if let Some(v) = f2("ITEM_GONE") { ai2.item_gone = v > 0.5; }
    if let Some(v) = f2("AI_KO_PRECISE") { ai2.ko_precise = v > 0.5; }
    if let Some(v) = f2("AI_PRUNE_IMMUNE") { ai2.prune_immune = v > 0.5; }
    if let Some(v) = f2("ORACLE_MIX") { ai2.oracle_mix = v; }
    if let Some(v) = f2("ORACLE_REVEAL") { ai2.oracle_reveal = v as u32; }
    let result = run_two_mcts(packr, [net, net_b.unwrap_or(net)], &mut b, &mut ai1, &mut ai2, &mut rng, on_turn);
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
    crate::search::set_belief(&mut b.sides[0], OpponentBelief::new(belief_season()));
    crate::search::set_belief(&mut b.sides[1], OpponentBelief::new(belief_season()));
    let packr: &Pack = pack;
    let mut ai1 = SearchAI::new(packr, belief_season(), seed, sims);
    let mut ai2 = SearchAI::new(packr, belief_season(), seed ^ 0x5bd1e995, sims);
    let mut rng = cell.into_inner();
    run_two_mcts(packr, [net, net], &mut b, &mut ai1, &mut ai2, &mut rng, |_, _| {})
}

/// mcts_vs_dist のパリティ調査用。結果に加えて「選出した3匹の添字」と
/// 「各ターン終了時の状態ハッシュ」を返す。Python 側と同じ encode_battle/sv_hash なので
/// 何ターン目から食い違うかを直接突き合わせられる。
pub fn mcts_vs_dist_trace(
    pack: &mut Pack,
    net: &NetW,
    pa: &[String],
    sa: &[usize],
    pb: &[String],
    season_a: &str,
    season_b: &str,
    seed: i128,
    sims: usize,
) -> (i64, Vec<usize>, Vec<u64>, Vec<String>, Vec<String>, Vec<String>, Vec<String>, Vec<String>, Vec<String>, Vec<String>, Vec<f64>) {
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
    crate::search::set_belief(&mut b.sides[0], OpponentBelief::new(belief_season()));
    crate::search::set_belief(&mut b.sides[1], OpponentBelief::new(belief_season()));
    let packr: &Pack = pack;
    let mut ai1 = SearchAI::new(packr, belief_season(), seed, sims);
    let mut ai2 = SearchAI::new(packr, belief_season(), seed ^ 0x5bd1e995, sims);
    let mut rng = cell.into_inner();
    let hs = std::cell::RefCell::new(Vec::<u64>::new());
    // ターン0（start直後・AIが動く前）の局面も記録する
    {
        let e0 = crate::statec::encode_battle(packr, &b, false);
        hs.borrow_mut().push(crate::statec::sv_hash(&e0.vals));
    }
    let f_names = std::cell::RefCell::new(Vec::<String>::new());
    let f_vals = std::cell::RefCell::new(Vec::<String>::new());
    ACT_LOG.with(|l| *l.borrow_mut() = Some(Vec::new()));
    ROOT_LOG.with(|l| *l.borrow_mut() = Some(Vec::new()));
    CFG_LOG.with(|l| *l.borrow_mut() = Some(Vec::new()));
    EVAL_LOG.with(|l| *l.borrow_mut() = Some(Vec::new()));
    DET_LOG.with(|l| *l.borrow_mut() = Some(Vec::new()));
    EVAL_X.with(|l| *l.borrow_mut() = Some(Vec::new()));
    let res = run_two_mcts(packr, [net, net], &mut b, &mut ai1, &mut ai2, &mut rng, |pk, bt| {
        let named = f_vals.borrow().is_empty();
        let e = crate::statec::encode_battle(pk, bt, named);
        if named {
            *f_vals.borrow_mut() = e.vals.iter().map(sv_str).collect();
            if let Some(ns) = &e.names {
                *f_names.borrow_mut() = ns.clone();
            }
        }
        hs.borrow_mut().push(crate::statec::sv_hash(&e.vals));
    });
    let acts = ACT_LOG.with(|l| l.borrow_mut().take()).unwrap_or_default();
    let roots = ROOT_LOG.with(|l| l.borrow_mut().take()).unwrap_or_default();
    let cfgs = CFG_LOG.with(|l| l.borrow_mut().take()).unwrap_or_default();
    let evals = EVAL_LOG.with(|l| l.borrow_mut().take()).unwrap_or_default();
    let dets = DET_LOG.with(|l| l.borrow_mut().take()).unwrap_or_default();
    let ex = EVAL_X.with(|l| l.borrow_mut().take()).unwrap_or_default();
    (res, idx2, hs.into_inner(), f_names.into_inner(), f_vals.into_inner(), acts, roots, cfgs, evals, dets, ex)
}

/// パリティ調査用: 6匹の構築＋select_party まで進めて、
/// 「選んだ添字」と「その直後に共有RNGから引く次の乱数」を返す。
/// mcts_vs_dist は ai.choose に共有RNGを渡すので、ここで消費数がズレると
/// 以降の探索・ダメージロールが全部ズレる（選出結果が一致していても起きる）。
pub fn select_party_rng_probe(
    pack: &mut Pack,
    pa: &[String],
    pb: &[String],
    season: &str,
    seed: i128,
) -> (Vec<usize>, f64) {
    let cell = std::cell::RefCell::new(CpyRandom::new(seed));
    let mut a6: Vec<Poke> = Vec::new();
    for s in pa {
        let mut sr = SharedRng(&cell);
        let mut r: Option<&mut dyn crate::rng::BRng> = Some(&mut sr);
        a6.push(build_poke_rand(pack, s, season, &mut r));
    }
    let mut b6: Vec<Poke> = Vec::new();
    for s in pb {
        let mut sr = SharedRng(&cell);
        let mut r: Option<&mut dyn crate::rng::BRng> = Some(&mut sr);
        b6.push(build_poke_rand(pack, s, season, &mut r));
    }
    let idx2 = {
        let packr: &Pack = pack;
        let mut sr = SharedRng(&cell);
        let mut srng = || cell.borrow_mut().random();
        crate::ai::select_party(packr, &mut b6, &mut a6, 3, 0.3, 50.0, &mut sr, &mut srng)
    };
    let nxt = cell.borrow_mut().random();
    (idx2, nxt)
}

fn sv_str(v: &crate::statec::SV) -> String {
    use crate::statec::SV;
    match v {
        SV::N => "None".to_string(),
        SV::I(x) => x.to_string(),
        SV::F(x) => format!("{x}"),
        SV::S(x) => x.clone(),
        SV::B(x) => x.to_string(),
    }
}

/// 学習用の教師記録: (手番側, 盤面1037次元, [(行動index, 訪問数)], 探索の根の価値)。
/// ターン番号は Python 側が対局内の記録順から復元する。
/// 根の価値＝訪問数で重み付けした Q。最終勝敗（0/1）より分散が小さい価値ターゲットになる。
pub type PiRec = (usize, Vec<f64>, Vec<(usize, i64)>, f64);

thread_local! {
    static PI_TRACE: std::cell::RefCell<Option<Vec<PiRec>>> = std::cell::RefCell::new(None);
}

/// VALUE_Q=max で価値ターゲットを「根の最善手の値」にする（既定は訪問数重み付き平均）。
/// 訪問が極端に少ない手のノイズを拾わないよう、総訪問の1/50未満は除外する。
/// 探索木の内部ノードを教師にする割合（env NODE_TRACE、0=無効）。
/// 軌道上の局面だけだと「選ばれなかった手の先」＝MCTSが実際に評価する分布が学習データに入らず、
/// 兄弟局面どうしの差も一度も見ないまま終わる。展開時の特徴ベクトルは葉の評価で計算済みなので、
/// 記録するだけなら追加コストはほぼゼロ。
/// 木ノードを教師として採用する最小訪問数（env NODE_MIN_VISITS、既定30）。
pub fn node_min_visits() -> i64 {
    static S: std::sync::OnceLock<i64> = std::sync::OnceLock::new();
    *S.get_or_init(|| {
        std::env::var("NODE_MIN_VISITS").ok().and_then(|v| v.parse().ok()).unwrap_or(30)
    })
}

pub fn node_trace_rate() -> f64 {
    static S: std::sync::OnceLock<f64> = std::sync::OnceLock::new();
    *S.get_or_init(|| std::env::var("NODE_TRACE").ok().and_then(|v| v.parse().ok()).unwrap_or(0.0))
}

/// 終盤の厳密ソルバで AI の手を採点する（env SOLVE_DEPTH>0 で有効）。
/// 記録: (手番側, 均衡値, [(手index, 相手の均衡戦略に対する期待勝率)], AIが選んだ手index, 残り体数,
///        ノード数, 評価したマス数, 全幅なら評価したはずのマス数)
pub type SolveRec = (usize, f64, Vec<(usize, f64)>, usize, usize, u64, u64, u64);

thread_local! {
    static SOLVE_TRACE: std::cell::RefCell<Vec<SolveRec>> = const { std::cell::RefCell::new(Vec::new()) };
}

pub fn solve_depth() -> u32 {
    static S: std::sync::OnceLock<u32> = std::sync::OnceLock::new();
    *S.get_or_init(|| std::env::var("SOLVE_DEPTH").ok().and_then(|v| v.parse().ok()).unwrap_or(0))
}

/// 対象にする終盤の上限（両側の生存数の合計）。
pub fn solve_max_alive() -> usize {
    static S: std::sync::OnceLock<usize> = std::sync::OnceLock::new();
    *S.get_or_init(|| std::env::var("SOLVE_MAX_ALIVE").ok().and_then(|v| v.parse().ok()).unwrap_or(3))
}

/// 採点の記録を取るか（env SOLVE_RECORD、既定1）。対戦で使うだけなら0にしてコストを省く。
pub fn solve_record() -> bool {
    static S: std::sync::OnceLock<bool> = std::sync::OnceLock::new();
    *S.get_or_init(|| std::env::var("SOLVE_RECORD").map(|v| v != "0").unwrap_or(true))
}

pub fn solve_trace_push(r: SolveRec) {
    SOLVE_TRACE.with(|l| l.borrow_mut().push(r));
}

pub fn solve_trace_take() -> Vec<SolveRec> {
    SOLVE_TRACE.with(|l| std::mem::take(&mut *l.borrow_mut()))
}

pub fn value_q_max() -> bool {
    static S: std::sync::OnceLock<bool> = std::sync::OnceLock::new();
    *S.get_or_init(|| std::env::var("VALUE_Q").map(|v| v == "max").unwrap_or(false))
}

pub fn pi_trace_enabled() -> bool {
    PI_TRACE.with(|l| l.borrow().is_some())
}

/// 探索木の内部ノードの教師: (盤面1037次元, 逆伝播済みの値, [(行動index, 訪問数)])。
/// MCTS はこのノードの下も探索しているので**訪問分布も取れる**。
/// 逆に、π を出せるだけ探索されていないノードは値も信用できないので、閾値は両者で共通にする。
pub type NodeRec = (Vec<f64>, f64, Vec<(usize, i64)>);

thread_local! {
    static NODE_TRACE: std::cell::RefCell<Vec<NodeRec>> = const { std::cell::RefCell::new(Vec::new()) };
}

pub fn node_trace_push(rec: NodeRec) {
    NODE_TRACE.with(|l| l.borrow_mut().push(rec));
}

pub fn node_trace_take() -> Vec<NodeRec> {
    NODE_TRACE.with(|l| std::mem::take(&mut *l.borrow_mut()))
}

/// 序盤 burn ターンを両側ランダムで進める（教師生成の開始局面を広げる）。
/// ランダム手の局面は ai.choose を通らないので PI_TRACE にも入らない。
thread_local! {
    static BURN_TURNS: std::cell::Cell<i64> = const { std::cell::Cell::new(0) };
}

pub fn set_burn_turns(n: i64) {
    BURN_TURNS.with(|c| c.set(n));
}

fn burn_turns() -> i64 {
    BURN_TURNS.with(|c| c.get())
}

pub fn pi_trace_push(rec: PiRec) {
    PI_TRACE.with(|l| {
        if let Some(v) = l.borrow_mut().as_mut() {
            v.push(rec);
        }
    });
}

/// mcts_3v3 を回しつつ、各手番の (盤面, 根の訪問分布) を集める＝価値・方策ヘッドの教師生成。
#[allow(clippy::too_many_arguments)]
pub fn mcts_3v3_trace(
    pack: &mut Pack,
    // net: 教師側（側1）のネット。反復学習で「1周前のネットに教師を作らせる」ために差し替える
    net: &NetW,
    // net_b: 相手側のネット。None で両側同じ。教師を1種類の相手だけで作ると
    // 価値関数がその相手に過適合するため、棋風・強さの違う相手を混ぜられるようにする。
    net_b: Option<&NetW>,
    pa: &[String],
    sa: &[usize],
    pb: &[String],
    sb: &[usize],
    season_a: &str,
    season_b: &str,
    seed: i128,
    sims: usize,
    burn: i64,
) -> (i64, Vec<PiRec>, Vec<NodeRec>) {
    PI_TRACE.with(|l| *l.borrow_mut() = Some(Vec::new()));
    let _ = node_trace_take();
    set_burn_turns(burn);
    let (r, _) =
        mcts_3v3(pack, net, net_b, pa, sa, pb, sb, season_a, season_b, seed, sims, |_, _| {});
    set_burn_turns(0);
    let t = PI_TRACE.with(|l| l.borrow_mut().take()).unwrap_or_default();
    (r, t, node_trace_take())
}

/// パリティ調査用の行動記録（`mcts_vs_dist_trace` からのみ使う）
thread_local! {
    static ACT_LOG: std::cell::RefCell<Option<Vec<String>>> = std::cell::RefCell::new(None);
    static ROOT_LOG: std::cell::RefCell<Option<Vec<String>>> = std::cell::RefCell::new(None);
    static CFG_LOG: std::cell::RefCell<Option<Vec<String>>> = std::cell::RefCell::new(None);
    static EVAL_LOG: std::cell::RefCell<Option<Vec<String>>> = std::cell::RefCell::new(None);
    static DET_LOG: std::cell::RefCell<Option<Vec<String>>> = std::cell::RefCell::new(None);
    static EVAL_TAG: std::cell::RefCell<bool> = const { std::cell::RefCell::new(false) };
    static EVAL_X: std::cell::RefCell<Option<Vec<f64>>> = std::cell::RefCell::new(None);
}

/// determinize 後の相手の実数値を記録する。既定では何もしない。
#[allow(clippy::too_many_arguments)]
pub fn det_log_push(
    name: &str, max_hp: i64, hp: i64, a: i64, b: i64, c: i64, d: i64, sp: i64,
) {
    DET_LOG.with(|l| {
        let mut bb = l.borrow_mut();
        let Some(v) = bb.as_mut() else { return };
        if v.len() < 24 {
            v.push(format!("{name} HP{max_hp}({hp}) A{a} B{b} C{c} D{d} S{sp}"));
        }
    });
}

/// 葉のネット評価を記録する（入力xのハッシュと価値）。既定では何もしない。
pub fn eval_log_push(xh: u64, v: f64) {
    // 葉展開(expand_with_value)からの評価だけを拾う。downside_guard 等の呼び出しを
    // 混ぜると両エンジンでログの系列が揃わず、比較そのものが無意味になる（実際に一度そうなった）。
    if !EVAL_TAG.with(|t| *t.borrow()) {
        return;
    }
    EVAL_LOG.with(|l| {
        let mut b = l.borrow_mut();
        let Some(vv) = b.as_mut() else { return };
        if vv.len() < 60 {
            vv.push(format!("{xh:016x} {v:.17}"));
        }
    });
}

pub fn eval_tag_set(on: bool) {
    EVAL_TAG.with(|t| *t.borrow_mut() = on);
}

/// 葉展開の特徴ベクトル(905次元)を先頭から最大12本、連結して保存する。
pub fn eval_x_push(x: &[f64]) {
    if !EVAL_TAG.with(|t| *t.borrow()) {
        return;
    }
    EVAL_X.with(|l| {
        let mut b = l.borrow_mut();
        let Some(v) = b.as_mut() else { return };
        if v.len() < 12 * 905 {
            v.extend_from_slice(x);
        }
    });
}

/// belief から引いた相手の型を記録する（search.rs から呼ばれる。既定では何もしない）。
#[allow(clippy::too_many_arguments)]
/// 決定化の的中率（計測用）。開示済みの技の本数（0..=4）ごとに分ける。
/// 全ターンを平均すると「情報ゼロの1ターン目」と「技が3本見えた終盤」が混ざり、
/// 型プールの狙い（1本見えたら残りが絞れる）が見えない。
/// 各段 [試行数, 持ち物一致, 特性一致, 技の一致本数, 技4本完全一致, 全一致(持ち物・特性・技), 性格一致, 努力値一致,
///        全項目一致(持ち物・特性・技・性格・努力値)]
thread_local! {
    static DET_HIT: std::cell::RefCell<[[u64; 9]; 5]> =
        const { std::cell::RefCell::new([[0; 9]; 5]) };
}

#[allow(clippy::too_many_arguments)]
pub fn det_hit_add(known: usize, item: bool, abil: bool, moves_hit: u64,
                   all_moves: bool, full: bool, nature: bool, ev: bool) {
    DET_HIT.with(|c| {
        let v = &mut c.borrow_mut()[known.min(4)];
        v[0] += 1;
        v[1] += item as u64;
        v[2] += abil as u64;
        v[3] += moves_hit;
        v[4] += all_moves as u64;
        v[5] += full as u64;
        v[6] += nature as u64;
        v[7] += ev as u64;
        v[8] += (full && nature && ev) as u64;
    });
}

/// 決定化の整合チェック（計測用）。[確認数, 引いた型: 技/持ち物/特性/不発の持ち物 と矛盾,
/// 真の型: 技/持ち物/特性/不発の持ち物 と矛盾]。真の型側の矛盾は開示処理のバグ
thread_local! {
    static DET_CONSIST: std::cell::RefCell<[u64; 9]> = const { std::cell::RefCell::new([0; 9]) };
}

pub fn det_consist_add(bad: &[bool; 8]) {
    DET_CONSIST.with(|c| {
        let mut v = c.borrow_mut();
        v[0] += 1;
        for (i, b) in bad.iter().enumerate() {
            v[i + 1] += *b as u64;
        }
    });
}

/// 枠ごとの当たり率（計測用）。[判明本数 0..=4][真の技の採用率順位 0..=3] = [未判明の枠の数, 当たった数]
thread_local! {
    static DET_SLOT: std::cell::RefCell<[[[u64; 2]; 4]; 5]> = const { std::cell::RefCell::new([[[0; 2]; 4]; 5]) };
}

pub fn det_slot_add(known: usize, rank: usize, hit: bool) {
    DET_SLOT.with(|c| {
        let mut v = c.borrow_mut();
        v[known.min(4)][rank.min(3)][0] += 1;
        v[known.min(4)][rank.min(3)][1] += hit as u64;
    });
}

pub fn det_slot_take() -> Vec<u64> {
    DET_SLOT.with(|c| {
        let v = *c.borrow();
        *c.borrow_mut() = [[[0; 2]; 4]; 5];
        v.iter().flat_map(|a| a.iter().flat_map(|b| b.iter().copied())).collect()
    })
}

pub fn det_consist_take() -> Vec<u64> {
    DET_CONSIST.with(|c| {
        let v = *c.borrow();
        *c.borrow_mut() = [0; 9];
        v.to_vec()
    })
}

pub fn det_hit_take() -> Vec<u64> {
    DET_HIT.with(|c| {
        let v = *c.borrow();
        *c.borrow_mut() = [[0; 9]; 5];
        v.iter().flat_map(|r| r.iter().copied()).collect()
    })
}

pub fn cfg_log_push(
    pack: &Pack,
    name: &str,
    ev: &crate::pack::EvEntry,
    nature: &str,
    item: Option<&str>,
    ability: &str,
    moves: &[String],
) {
    CFG_LOG.with(|l| {
        let mut b = l.borrow_mut();
        let Some(v) = b.as_mut() else { return };
        if v.len() >= 24 {
            return;
        }
        let _ = pack;
        v.push(format!(
            "{name} ev={}/{}/{}/{}/{}/{} nat={nature} item={} abil={ability} moves={:?}",
            ev.h, ev.a, ev.b, ev.c, ev.d, ev.s,
            item.unwrap_or("None"),
            moves
        ));
    });
}

/// MCTSのルート統計を記録する（search.rs から呼ばれる。既定では何もしない）。
pub fn root_log_push(
    pack: &Pack,
    cands: &[crate::battle::Action],
    stats: &[(usize, i64, f64)],
    chosen_i: usize,
) {
    ROOT_LOG.with(|l| {
        let mut b = l.borrow_mut();
        let Some(v) = b.as_mut() else { return };
        let mut parts: Vec<String> = Vec::with_capacity(stats.len());
        for (ai_, n, q) in stats {
            parts.push(format!(
                "{}{}=n{} q{:.17}",
                if *ai_ == chosen_i { "*" } else { "" },
                act_str(pack, &cands[*ai_]),
                n,
                q
            ));
        }
        v.push(parts.join("  "));
    });
}

fn act_str(pack: &Pack, a: &crate::battle::Action) -> String {
    use crate::battle::ActKind;
    match a.kind {
        ActKind::Move => format!(
            "move {}{}",
            a.mv.as_ref().map(|m| pack.intern.resolve(m.name).to_string()).unwrap_or_default(),
            if a.do_mega { "+mega" } else { "" }
        ),
        ActKind::Switch => format!("switch->{}", a.switch_to),
        ActKind::Mega => "mega".to_string(),
        ActKind::Pass => "pass".to_string(),
    }
}

/// 両者 SearchAI + certain_ko_override でターンループを回す共通部
fn run_two_mcts(
    packr: &Pack,
    nets: [&NetW; 2],
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
            let burn = burn_turns();
            if burn > 0 && bt.turn <= burn {
                for sx in 0..2usize {
                    let (me, op) = crate::battle::split2(&mut bt.sides, sx);
                    let c = crate::search::candidate_actions(packr, me, op, &bt.field, false);
                    if !c.is_empty() {
                        out[sx] = c[rng.choice(c.len())].clone();
                    }
                }
                return out;
            }
            for sx in 0..2usize {
                let mut bl = bt.sides[sx].belief.0.take().unwrap();
                let ai: &mut SearchAI = if sx == 0 { ai1 } else { ai2 };
                let a = ai.choose(packr, nets[sx], &mut bt.sides, sx, &mut bt.field, &mut bl, rng);
                bt.sides[sx].belief.0 = Some(bl);
                let precise = ai.ko_precise;
                let (me, op) = crate::battle::split2(&mut bt.sides, sx);
                out[sx] = crate::ai::certain_ko_override_opt(packr, a, me, op, &mut bt.field, rng, precise);
            }
            ACT_LOG.with(|l| {
                if let Some(v) = l.borrow_mut().as_mut() {
                    v.push(format!("{} | {}", act_str(packr, &out[0]), act_str(packr, &out[1])));
                }
            });
            out
        },
        |bt| on_turn(packr, bt),
    )
}


/// simulator/learned_selection.py の学習選出（候補・相手の仮定・状態ベクトル）。MLP の推論と選択は Python 側（numpy）で行う
/// （Python と同じ行列積の丸め＝選出が完全一致するように）。state は CPython random.getstate()[1]（624語＋位置）。
/// 戻り: (候補＝自分6体の添字の並び, 相手の仮定＝相手6体の添字の並び×3, 状態ベクトル[候補×仮定×次元], 次元, 進めた乱数の状態)
#[allow(clippy::type_complexity, clippy::too_many_arguments)]
pub fn learned_select_states(
    pack: &mut Pack,
    ft: &crate::features::FeatTables,
    specs_a: &[String],
    specs_b: &[String],
    season: &str,
    n: usize,
    min_mega: usize,
    max_mega: usize,
    state: &[u32],
) -> (Vec<Vec<usize>>, Vec<Vec<usize>>, Vec<f64>, usize, Vec<u32>) {
    let mut a6: Vec<Poke> = specs_a.iter().map(|s| crate::poke::build_poke(pack, s, season)).collect();
    let mut b6: Vec<Poke> = specs_b.iter().map(|s| crate::poke::build_poke(pack, s, season)).collect();
    let packr: &Pack = pack;
    let pen: f64 = std::env::var("MEGA_PENALTY").ok().and_then(|v| v.parse().ok()).unwrap_or(50.0);
    let cell = std::cell::RefCell::new(CpyRandom::from_state(state));
    // 相手の仮定: ヒューリスティック選出の温度0＋温度1×2（Python の select_party_multi と同じ順・同じ乱数）
    let mut osels: Vec<Vec<usize>> = Vec::with_capacity(3);
    let nb = n.min(b6.len());
    for t in [0.0, 1.0, 1.0] {
        let mut sr = SharedRng(&cell);
        let mut srng = || cell.borrow_mut().random();
        osels.push(crate::ai::select_party(packr, &mut b6, &mut a6, nb, t, pen, &mut sr, &mut srng));
    }
    // 候補（3体＋先頭）。メガ1体ルール: min_mega..=max_mega 体
    let mut cands: Vec<Vec<usize>> = Vec::new();
    let na = a6.len();
    let mut combo = vec![0usize; n];
    fn rec(start: usize, k: usize, na: usize, n: usize, combo: &mut Vec<usize>, out: &mut Vec<Vec<usize>>) {
        if k == n {
            out.push(combo.clone());
            return;
        }
        for i in start..na {
            combo[k] = i;
            rec(i + 1, k + 1, na, n, combo, out);
        }
    }
    let mut combos = Vec::new();
    rec(0, 0, na, n, &mut combo, &mut combos);
    for c in combos {
        let nm = c.iter().filter(|&&i| a6[i].mega.is_some()).count();
        if nm < min_mega || nm > max_mega {
            continue;
        }
        for li in 0..n {
            let mut o = vec![c[li]];
            o.extend(c.iter().enumerate().filter(|(j, _)| *j != li).map(|(_, &i)| i));
            cands.push(o);
        }
    }
    let mut memo = crate::features::DmgMemo::default();
    let mut xs: Vec<f64> = Vec::new();
    let mut dim = 0usize;
    for c in &cands {
        for os in &osels {
            let mut sides = [
                Side { party: c.iter().map(|&i| a6[i].clone()).collect(), active_idx: 0, field_idx: 0, ..Default::default() },
                Side { party: os.iter().map(|&i| b6[i].clone()).collect(), active_idx: 0, field_idx: 1, ..Default::default() },
            ];
            let mut field = Field::default();
            memo.begin();
            let x = crate::features::encode_state(packr, ft, &mut sides, 0, &mut field, &mut memo, &mut crate::live::NoRng);
            memo.end();
            dim = x.len();
            xs.extend_from_slice(&x);
        }
    }
    let st = cell.into_inner().state();
    (cands, osels, xs, dim, st)
}
