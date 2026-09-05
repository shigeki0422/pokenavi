//! simulator/search_ai.py（本番構成 = mcts/regret/fast/qselect/downside-guard）の移植と、
//! simulator/alphazero.py の legal_actions_indexed / train_az2._net_ai の構成を写す。
use crate::ai::{
    self, filter_by_pp, filter_valid_by_lock, forced_charging_action, is_hazard, is_trapped,
    struggle, HazCtx,
};
use crate::battle::{ActKind, Action, Side};
use crate::damage::Field;
use crate::features::{encode_state_into, DmgMemo, FeatTables};
use crate::net::{NetScratch, NetW};
use crate::pack::{Cat, Pack};
use crate::rng::BRng;

pub const ACTION_DIM: usize = 12;

#[inline]
pub fn action_index(a: &Action) -> usize {
    if a.kind == ActKind::Switch {
        return 8 + a.switch_to as usize;
    }
    if a.move_idx >= 0 {
        return a.move_idx as usize + if a.do_mega { 4 } else { 0 };
    }
    11
}

/// alphazero.legal_actions_indexed（方策マスク用の列挙。設置技の除外は無い）
pub fn legal_actions_indexed(pack: &Pack, me_s: &Side, op_s: &Side) -> Vec<usize> {
    let me = me_s.active();
    let can_mega = me.mega.is_some() && !me.mega_evolved && !me_s.mega_used;
    let valid = filter_valid_by_lock(me);
    let pp_valid = filter_by_pp(&valid, me);
    let mut out = Vec::with_capacity(12);
    if pp_valid.is_empty() {
        out.push(11);
    } else {
        for (i, _) in &pp_valid {
            out.push(*i);
            if can_mega {
                out.push(4 + *i);
            }
        }
    }
    if !is_trapped(pack, me, Some(op_s.active())) {
        for (j, p) in me_s.party.iter().enumerate() {
            if j != me_s.active_idx && p.is_alive && j < 3 {
                out.push(8 + j);
            }
        }
    }
    out
}

/// SearchAI._candidate_actions
pub fn candidate_actions(pack: &Pack, me_s: &Side, op_s: &Side, field: &Field, collapse_mega: bool) -> Vec<Action> {
    let me = me_s.active();
    let can_mega = me.mega.is_some() && !me.mega_evolved && !me_s.mega_used;
    let mega_flags: &[bool] = if can_mega {
        if collapse_mega {
            &[true]
        } else {
            &[true, false]
        }
    } else {
        &[false]
    };
    let valid = filter_valid_by_lock(me);
    let pp_valid = filter_by_pp(&valid, me);
    let hz = HazCtx::of(op_s);
    let mut move_cands: Vec<(usize, crate::damage::DMove)> = pp_valid
        .iter()
        .filter(|(_, mv)| {
            !(mv.category == Cat::Status
                && is_hazard(pack, mv.name)
                && ai::hazard_value(pack, mv.name, &hz, field) <= 0.0)
        })
        .cloned()
        .collect();
    if move_cands.is_empty() {
        move_cands = pp_valid.clone();
    }
    let mut out: Vec<Action> = Vec::with_capacity(12);
    if pp_valid.is_empty() {
        for &dm in mega_flags {
            out.push(Action {
                kind: ActKind::Move,
                mv: Some(struggle(pack)),
                move_idx: -1,
                switch_to: -1,
                do_mega: dm,
            });
        }
    } else {
        for (i, mv) in &move_cands {
            for &dm in mega_flags {
                out.push(Action {
                    kind: ActKind::Move,
                    mv: Some(mv.clone()),
                    move_idx: *i as i64,
                    switch_to: -1,
                    do_mega: dm,
                });
            }
        }
    }
    if !is_trapped(pack, me, Some(op_s.active())) {
        for (i, p) in me_s.party.iter().enumerate() {
            if i != me_s.active_idx && p.is_alive {
                out.push(Action {
                    kind: ActKind::Switch,
                    mv: None,
                    move_idx: 0,
                    switch_to: i as i64,
                    do_mega: false,
                });
            }
        }
    }
    out
}

/// train_az2._net_ai の nefn: (policy over legal, value=P(A勝))
pub struct NetCtx {
    pub ft: FeatTables,
    pub memo: DmgMemo,
    pub scratch: NetScratch,
    pub x: Vec<f64>,
}

impl NetCtx {
    pub fn new(pack: &Pack) -> NetCtx {
        NetCtx {
            ft: FeatTables::build(pack),
            memo: DmgMemo::default(),
            scratch: NetScratch::default(),
            x: Vec::with_capacity(905),
        }
    }
}

/// nefn(A,B,f): L=legal_actions_indexed(A,B,f) → net.evaluate(encode_state(A,B,f), L or [0])
pub fn net_eval(
    pack: &Pack,
    net: &NetW,
    ctx: &mut NetCtx,
    sides: &mut [Side; 2],
    first: usize,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> (Vec<(usize, f64)>, f64) {
    let legal = legal_actions_indexed(pack, &sides[first], &sides[1 - first]);
    let mut x = std::mem::take(&mut ctx.x);
    encode_state_into(pack, &ctx.ft, sides, first, field, &mut ctx.memo, rng, &mut x);
    let l: Vec<usize> = if legal.is_empty() { vec![0] } else { legal.clone() };
    let (p, v) = net.evaluate(&x, &l, &mut ctx.scratch);
    ctx.x = x;
    let pol: Vec<(usize, f64)> = if legal.is_empty() {
        Vec::new()
    } else {
        l.iter().copied().zip(p.iter().copied()).collect()
    };
    (pol, v)
}

/// G1/G2 ゲート用: x（905次元）も返す net_eval
pub fn net_eval_x(
    pack: &Pack,
    net: &NetW,
    ctx: &mut NetCtx,
    sides: &mut [Side; 2],
    first: usize,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> (Vec<f64>, Vec<(usize, f64)>, f64) {
    let legal = legal_actions_indexed(pack, &sides[first], &sides[1 - first]);
    let mut x = Vec::with_capacity(905);
    encode_state_into(pack, &ctx.ft, sides, first, field, &mut ctx.memo, rng, &mut x);
    let l: Vec<usize> = if legal.is_empty() { vec![0] } else { legal.clone() };
    let (p, v) = net.evaluate(&x, &l, &mut ctx.scratch);
    let pol: Vec<(usize, f64)> = if legal.is_empty() {
        Vec::new()
    } else {
        l.iter().copied().zip(p.iter().copied()).collect()
    };
    (x, pol, v)
}


// ══════════════════════════════════════════════════════════════════════════
//  SearchAI（本番構成: mcts=True / mcts_select="regret" / mcts_fast=True /
//            qselect / downside_guard / collapse_mega / HIDDEN_SELECTION=on）
// ══════════════════════════════════════════════════════════════════════════
use crate::battle::{Battle, BeliefSlot};
use crate::belief::{OpponentBelief, TplCache};
use crate::cpyrng::CpyRandom;
use crate::pysum::pysum;
use std::collections::HashMap;

#[derive(Default, Clone)]
struct Node {
    n: [HashMap<usize, i64>; 2],
    w: [HashMap<usize, f64>; 2],
    p: [HashMap<usize, f64>; 2],
    r: [HashMap<usize, f64>; 2],
    children: HashMap<(usize, usize), usize>,
    total: i64,
    expanded: bool,
    v: Option<f64>,
}

/// _sample_opp_config の1体分
#[derive(Clone, Debug)]
pub struct SampledCfg {
    pub ev: crate::pack::EvEntry,
    pub nature: String,
    pub item: Option<String>,
    pub ability: String,
    pub moves: Vec<String>,
}

pub struct SearchAI {
    pub season: String,
    pub rng: CpyRandom,
    pub mcts_sims: usize,
    pub mcts_fpu: f64,
    pub mcts_p_floor: f64,
    pub mcts_max_depth: usize,
    pub rm_prior_mix: f64,
    pub collapse_mega: bool,
    pub qselect: bool,
    pub qselect_frac: f64,
    pub qselect_min: i64,
    pub downside_guard: bool,
    pub downside_k: usize,
    pub downside_margin: f64,
    pub tree_roll: f64,
    pub hidden: bool,
    pub ctx: NetCtx,
    tpl: TplCache,
    nodes: Vec<Node>,
}

impl SearchAI {
    pub fn new(pack: &Pack, season: &str, seed: i128, sims: usize) -> SearchAI {
        SearchAI {
            season: season.to_string(),
            rng: CpyRandom::new(seed),
            mcts_sims: sims,
            mcts_fpu: 0.5,
            mcts_p_floor: 1e-3,
            mcts_max_depth: 60,
            rm_prior_mix: 0.25,
            collapse_mega: true,
            qselect: true,
            qselect_frac: 0.1,
            qselect_min: 10,
            downside_guard: true,
            downside_k: 8,
            downside_margin: 0.20,
            tree_roll: 0.85,
            hidden: true,
            ctx: NetCtx::new(pack),
            tpl: TplCache::default(),
            nodes: Vec::new(),
        }
    }

    fn new_node(&mut self) -> usize {
        self.nodes.push(Node::default());
        self.nodes.len() - 1
    }

    /// SearchAI.__call__（mcts 経路）
    #[allow(clippy::too_many_arguments)]
    pub fn choose(
        &mut self,
        pack: &Pack,
        net: &NetW,
        sides: &mut [Side; 2],
        me_idx: usize,
        field: &mut Field,
        belief: &mut OpponentBelief,
        grng: &mut dyn BRng,
    ) -> Action {
        let op_idx = 1 - me_idx;
        if !sides[me_idx].active().is_alive {
            return Action { kind: ActKind::Pass, ..Default::default() };
        }
        if let Some(a) = forced_charging_action(sides[me_idx].active_mut()) {
            return a;
        }
        let cands =
            candidate_actions(pack, &sides[me_idx], &sides[op_idx], field, self.collapse_mega);
        if cands.len() <= 1 {
            if let Some(a) = cands.into_iter().next() {
                return a;
            }
            // _fallback = HeuristicAI()（実運用では到達しない）
            let (me, op) = crate::battle::split2(sides, me_idx);
            return ai::decide(pack, ai::Ai::heuristic(), me, op, field, false, grng);
        }
        self.mcts_choose(pack, net, sides, me_idx, field, belief, &cands, grng)
    }

    #[allow(clippy::too_many_arguments)]
    fn mcts_choose(
        &mut self,
        pack: &Pack,
        net: &NetW,
        sides: &mut [Side; 2],
        me_idx: usize,
        field: &mut Field,
        belief: &mut OpponentBelief,
        cands: &[Action],
        grng: &mut dyn BRng,
    ) -> Action {
        let root = self.build_mcts_root(pack, net, sides, me_idx, field, belief, cands, grng);
        let my_is_s1 = me_idx == 0;
        // stats = [(a, n, q)]
        let mut stats: Vec<(usize, i64, f64)> = Vec::with_capacity(cands.len());
        for (ai_, a) in cands.iter().enumerate() {
            let ix = action_index(a);
            let n = self.nodes[root].n[0].get(&ix).copied().unwrap_or(0);
            let q = if n != 0 {
                self.nodes[root].w[0].get(&ix).copied().unwrap_or(0.0) / n as f64
            } else {
                -1.0
            };
            stats.push((ai_, n, q));
        }
        let chosen_i = if self.qselect {
            let mut maxn = 0i64;
            for (_, n, _) in &stats {
                if *n > maxn {
                    maxn = *n;
                }
            }
            let maxn = if maxn == 0 { 1 } else { maxn };
            let thr = std::cmp::max(self.qselect_min, (self.qselect_frac * maxn as f64) as i64);
            let elig: Vec<&(usize, i64, f64)> =
                stats.iter().filter(|x| x.1 >= thr).collect::<Vec<_>>();
            let src: Vec<&(usize, i64, f64)> =
                if elig.is_empty() { stats.iter().collect() } else { elig };
            let mut best = src[0];
            for x in src.iter().skip(1) {
                if x.2 > best.2 {
                    best = x;
                }
            }
            best.0
        } else {
            let mut best = &stats[0];
            for x in stats.iter().skip(1) {
                if x.1 > best.1 {
                    best = x;
                }
            }
            best.0
        };
        let mut chosen = cands[chosen_i].clone();
        if self.downside_guard {
            chosen = self.apply_downside_guard(
                pack, net, sides, me_idx, field, belief, cands, chosen, my_is_s1, grng,
            );
        }
        chosen
    }

    #[allow(clippy::too_many_arguments)]
    fn build_mcts_root(
        &mut self,
        pack: &Pack,
        net: &NetW,
        sides: &mut [Side; 2],
        me_idx: usize,
        field: &mut Field,
        belief: &mut OpponentBelief,
        cands: &[Action],
        grng: &mut dyn BRng,
    ) -> usize {
        belief.observe_disclosure(pack, &sides[me_idx].opp_view);
        let my_is_s1 = me_idx == 0;
        self.nodes.clear();
        let root = self.new_node();
        if cands.len() <= 1 {
            return root;
        }
        for _t in 0..self.mcts_sims {
            let mut cs: [Side; 2] = [sides[0].clone(), sides[1].clone()];
            let mut cfield = field.clone();
            let dopp = 1 - me_idx;
            if self.hidden {
                self.resample_hidden_bench(pack, &mut cs, dopp, &sides[me_idx].opp_view, grng);
            }
            let cfg = self.sample_opp_config(pack, &cs[dopp], belief);
            for (i, c) in cfg.iter().enumerate() {
                if let Some(c) = c {
                    self.determinize(pack, &mut cs[dopp].party[i], c);
                }
            }
            self.mcts_simulate(pack, net, root, &mut cs, &mut cfield, my_is_s1, grng);
        }
        root
    }

    /// SearchAI._resample_hidden_bench
    fn resample_hidden_bench(
        &mut self,
        pack: &Pack,
        cs: &mut [Side; 2],
        di: usize,
        opp_view: &crate::oppview::OppView,
        grng: &mut dyn BRng,
    ) {
        if cs[di].source6_names.len() <= cs[di].party.len() {
            return;
        }
        let mut seen: Vec<crate::interner::Sym> =
            opp_view.pokemon.iter().filter(|k| k.seen).map(|k| k.name).collect();
        let an = cs[di].active().name;
        if !seen.contains(&an) {
            seen.push(an);
        }
        let mut pool: Vec<crate::interner::Sym> =
            cs[di].source6_names.iter().copied().filter(|n| !seen.contains(n)).collect();
        // random.Random.shuffle（Fisher-Yates 下降・_randbelow）
        self.rng.shuffle(&mut pool);
        let mut pi = 0usize;
        for i in 0..cs[di].party.len() {
            if i == cs[di].active_idx {
                continue;
            }
            if seen.contains(&cs[di].party[i].name) || !cs[di].party[i].is_alive {
                continue;
            }
            if pi >= pool.len() {
                continue;
            }
            let name_sym = pool[pi];
            pi += 1;
            let name = pack.intern.resolve(name_sym).to_string();
            let tpl = match self.tpl.get(pack, &name, &self.season) {
                None => continue,
                Some(t) => t,
            };
            let spec = crate::poke::Spec {
                name: name.clone(),
                item: None,
                nature: None,
                moves: None,
                evs: None,
                ability: None,
            };
            let mut r: Option<&mut dyn BRng> = Some(grng);
            let b = crate::poke::build_from_template_rand(pack, &tpl, &spec, &mut r);
            cs[di].party[i] = crate::poke::to_poke(pack, &b);
        }
    }

    /// SearchAI._sample_opp_config
    fn sample_opp_config(
        &mut self,
        pack: &Pack,
        opp_side: &Side,
        belief: &mut OpponentBelief,
    ) -> Vec<Option<SampledCfg>> {
        let mut out = Vec::with_capacity(opp_side.party.len());
        for p in &opp_side.party {
            let name = pack.intern.resolve(p.name).to_string();
            let bi = belief.ensure(pack, &name, None, None);
            let bi = match bi {
                None => {
                    out.push(None);
                    continue;
                }
                Some(i) => i,
            };
            let pb = &belief.species[bi].1;
            let (ev, nature) = pb.sample_spread(&mut self.rng);
            let item = pb.sample_item(&mut self.rng);
            let ability = pb.sample_ability(&mut self.rng);
            let moves = pb.sample_moves(&mut self.rng, 4);
            out.push(Some(SampledCfg { ev, nature, item, ability, moves }));
        }
        out
    }

    /// SearchAI._determinize
    fn determinize(&mut self, pack: &Pack, poke: &mut crate::poke::Poke, c: &SampledCfg) {
        let name = pack.intern.resolve(poke.name).to_string();
        let tpl = match self.tpl.get(pack, &name, &self.season) {
            None => return,
            Some(t) => t,
        };
        if !poke.mega_evolved && !poke.transformed {
            let nat_sym = pack.intern.get(&c.nature);
            let nm = |k: u8| -> f64 {
                match nat_sym.and_then(|s| pack.nature_mods.get(&s)) {
                    Some(&(up, dn)) => {
                        if up == k {
                            1.1
                        } else if dn == k {
                            0.9
                        } else {
                            1.0
                        }
                    }
                    None => 1.0,
                }
            };
            let frac = if poke.max_hp != 0 { poke.hp as f64 / poke.max_hp as f64 } else { 1.0 };
            let e = &c.ev;
            poke.max_hp = crate::poke::calc_hp(tpl.base[0], e.h);
            poke.attack = crate::poke::calc_stat(tpl.base[1], e.a, 31, nm(0));
            poke.defense = crate::poke::calc_stat(tpl.base[2], e.b, 31, nm(1));
            poke.sp_attack = crate::poke::calc_stat(tpl.base[3], e.c, 31, nm(2));
            poke.sp_defense = crate::poke::calc_stat(tpl.base[4], e.d, 31, nm(3));
            poke.speed = crate::poke::calc_stat(tpl.base[5], e.s, 31, nm(4));
            poke.nature = nat_sym.unwrap_or(poke.nature);
            poke.evs = [e.h, e.a, e.b, e.c, e.d, e.s];
            poke.hp = if poke.is_alive {
                std::cmp::max(1, (frac * poke.max_hp as f64).round_ties_even() as i64)
            } else {
                0
            };
        }
        if let Some(it) = &c.item {
            poke.item = pack.intern.get(it);
        }
        if !c.ability.is_empty() {
            if let Some(a) = pack.intern.get(&c.ability) {
                poke.ability = a;
            }
        }
        let mut mvs: Vec<crate::damage::DMove> = Vec::new();
        for m in &c.moves {
            if let Some(&idx) = pack.move_by_name.get(m) {
                let md = &pack.moves[idx];
                mvs.push(crate::damage::DMove {
                    name: md.name,
                    ty: md.ty,
                    category: md.category,
                    power: md.power,
                    accuracy: md.accuracy,
                    priority: md.priority,
                    pp: md.pp,
                });
            }
        }
        if !mvs.is_empty() {
            let names: Vec<crate::interner::Sym> = mvs.iter().map(|m| m.name).collect();
            poke.pp = mvs.iter().map(|m| m.pp.unwrap_or(5)).collect();
            poke.moves = mvs;
            for slot in [
                &mut poke.last_used_move,
                &mut poke.choice_locked_move,
                &mut poke.locked_move,
                &mut poke.disabled_move,
                &mut poke.charging_move,
            ] {
                if let Some(x) = *slot {
                    if !names.contains(&x) {
                        *slot = None;
                    }
                }
            }
        }
    }

    /// SearchAI._advance_turn（固定ロール tree_roll で1ターン解決）
    fn advance_turn(
        &mut self,
        pack: &Pack,
        cs: &mut [Side; 2],
        cfield: &mut Field,
        a_me: &Action,
        a_op: &Action,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) -> i64 {
        let (a1, a2) = if my_is_s1 { (a_me, a_op) } else { (a_op, a_me) };
        let mut b = Battle {
            sides: [std::mem::take(&mut cs[0]), std::mem::take(&mut cs[1])],
            field: std::mem::take(cfield),
            turn: 0,
        };
        b.sides[0].field_idx = 0;
        b.sides[1].field_idx = 1;
        let prev = b.field.roll_override;
        b.field.roll_override = Some(self.tree_roll);
        let acts = [a1.clone(), a2.clone()];
        let mut used = false;
        let w = b.run_loop_lim(
            pack,
            grng,
            1,
            |_bt, _rng| {
                assert!(!used, "resume(max_turns=1) は1回だけ行動を要求するはず");
                used = true;
                [acts[0].clone(), acts[1].clone()]
            },
            |_| {},
        );
        b.field.roll_override = prev;
        cs[0] = std::mem::take(&mut b.sides[0]);
        cs[1] = std::mem::take(&mut b.sides[1]);
        *cfield = b.field;
        w
    }

    /// SearchAI._mcts_leaf_value（net_eval あり）
    fn leaf_value(
        &mut self,
        pack: &Pack,
        net: &NetW,
        cs: &mut [Side; 2],
        cfield: &mut Field,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) -> f64 {
        let (_, v1) = net_eval(pack, net, &mut self.ctx, cs, 0, cfield, grng);
        if my_is_s1 {
            v1
        } else {
            1.0 - v1
        }
    }

    /// SearchAI._expand_with_value（葉のencode+forwardを2回に統合・memo有効）
    #[allow(clippy::too_many_arguments)]
    fn expand_with_value(
        &mut self,
        pack: &Pack,
        net: &NetW,
        node: usize,
        cs: &mut [Side; 2],
        cfield: &mut Field,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) -> f64 {
        // Python: ev(me,op) → ev(op,me) → ev(cs1,cs2)（3つ目はメモヒット）
        let (fa, fb) = if my_is_s1 { (0usize, 1usize) } else { (1usize, 0usize) };
        self.ctx.memo.begin();
        let (pol_a, val_a) = net_eval(pack, net, &mut self.ctx, cs, fa, cfield, grng);
        let (pol_b, val_b) = net_eval(pack, net, &mut self.ctx, cs, fb, cfield, grng);
        self.ctx.memo.end();
        let nd = &mut self.nodes[node];
        nd.p[0] = pol_a.iter().copied().collect();
        nd.p[1] = pol_b.iter().copied().collect();
        nd.expanded = true;
        let v1 = if my_is_s1 { val_a } else { val_b };
        if my_is_s1 {
            v1
        } else {
            1.0 - v1
        }
    }

    /// SearchAI._select（mcts_select="regret"）
    fn select(&mut self, node: usize, side: usize, cands: &[Action]) -> (usize, usize, f64) {
        let mut items: Vec<(usize, usize, f64, f64)> = Vec::with_capacity(cands.len());
        {
            let nd = &self.nodes[node];
            for (k, a) in cands.iter().enumerate() {
                let ix = action_index(a);
                let n = nd.n[side].get(&ix).copied().unwrap_or(0);
                let q = if n != 0 {
                    nd.w[side].get(&ix).copied().unwrap_or(0.0) / n as f64
                } else {
                    self.mcts_fpu
                };
                let p = f64::max(
                    nd.p[side].get(&ix).copied().unwrap_or(self.mcts_p_floor),
                    self.mcts_p_floor,
                );
                items.push((ix, k, q, p));
            }
        }
        let psum = {
            let t = pysum(items.iter().map(|x| x.3));
            if t == 0.0 {
                1.0
            } else {
                t
            }
        };
        // regret-matching
        let mut sig: Vec<f64> = Vec::with_capacity(items.len());
        {
            let nd = &self.nodes[node];
            let pos: Vec<f64> =
                items.iter().map(|x| f64::max(0.0, nd.r[side].get(&x.0).copied().unwrap_or(0.0))).collect();
            let z = pysum(pos.iter().copied());
            if z > 0.0 {
                for v in &pos {
                    sig.push(v / z);
                }
            } else {
                for _ in 0..items.len() {
                    sig.push(1.0 / items.len() as f64);
                }
            }
        }
        let lam = self.rm_prior_mix;
        for (i, it) in items.iter().enumerate() {
            sig[i] = (1.0 - lam) * sig[i] + lam * (it.3 / psum);
        }
        let v = pysum(items.iter().enumerate().map(|(i, it)| sig[i] * it.2));
        {
            let nd = &mut self.nodes[node];
            for it in items.iter() {
                let e = nd.r[side].entry(it.0).or_insert(0.0);
                *e += it.2 - v;
            }
        }
        // _sample
        let r = self.rng.random();
        let mut acc = 0.0f64;
        for (i, it) in items.iter().enumerate() {
            acc += sig[i];
            if r <= acc {
                return (it.0, it.1, sig[i]);
            }
        }
        let last = items.len() - 1;
        (items[last].0, items[last].1, sig[last])
    }

    #[allow(clippy::too_many_arguments)]
    fn mcts_simulate(
        &mut self,
        pack: &Pack,
        net: &NetW,
        root: usize,
        cs: &mut [Side; 2],
        cfield: &mut Field,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) {
        if !self.nodes[root].expanded {
            self.expand_with_value(pack, net, root, cs, cfield, my_is_s1, grng);
        }
        let mut node = root;
        let mut path: Vec<(usize, usize, usize)> = Vec::new();
        let mut depth = 0usize;
        let v: f64;
        let me_i = if my_is_s1 { 0usize } else { 1 };
        let op_i = 1 - me_i;
        loop {
            let my_cands =
                candidate_actions(pack, &cs[me_i], &cs[op_i], cfield, self.collapse_mega);
            let opp_cands =
                candidate_actions(pack, &cs[op_i], &cs[me_i], cfield, self.collapse_mega);
            if my_cands.is_empty() || opp_cands.is_empty() {
                v = self.leaf_value(pack, net, cs, cfield, my_is_s1, grng);
                break;
            }
            let (ix_me, k_me, _sg_me) = self.select(node, 0, &my_cands);
            let (ix_op, k_op, _sg_op) = self.select(node, 1, &opp_cands);
            path.push((node, ix_me, ix_op));
            let winner = self.advance_turn(
                pack,
                cs,
                cfield,
                &my_cands[k_me],
                &opp_cands[k_op],
                my_is_s1,
                grng,
            );
            depth += 1;
            if winner != 0 {
                v = if (winner == 1) == my_is_s1 { 1.0 } else { 0.0 };
                break;
            }
            let key = (ix_me, ix_op);
            match self.nodes[node].children.get(&key).copied() {
                None => {
                    let child = self.new_node();
                    self.nodes[node].children.insert(key, child);
                    let vv = self.expand_with_value(pack, net, child, cs, cfield, my_is_s1, grng);
                    self.nodes[child].v = Some(vv);
                    v = vv;
                    break;
                }
                Some(child) => {
                    node = child;
                    if depth >= self.mcts_max_depth {
                        v = self.leaf_value(pack, net, cs, cfield, my_is_s1, grng);
                        break;
                    }
                }
            }
        }
        // backup（nextturn_lambda=0 なので v_root == v）
        for (nd_i, im, io) in path {
            let nd = &mut self.nodes[nd_i];
            nd.total += 1;
            *nd.n[0].entry(im).or_insert(0) += 1;
            *nd.w[0].entry(im).or_insert(0.0) += v;
            *nd.n[1].entry(io).or_insert(0) += 1;
            *nd.w[1].entry(io).or_insert(0.0) += 1.0 - v;
        }
    }

    /// SearchAI._downside_value
    #[allow(clippy::too_many_arguments)]
    fn downside_value(
        &mut self,
        pack: &Pack,
        net: &NetW,
        sides: &[Side; 2],
        me_idx: usize,
        field: &Field,
        belief: &mut OpponentBelief,
        a: &Action,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) -> f64 {
        belief.observe_disclosure(pack, &sides[me_idx].opp_view);
        let di = 1 - me_idx;
        let mut worst = 1.0f64;
        for _k in 0..self.downside_k {
            let mut b: [Side; 2] = [sides[0].clone(), sides[1].clone()];
            let mut bf = field.clone();
            if self.hidden {
                self.resample_hidden_bench(pack, &mut b, di, &sides[me_idx].opp_view, grng);
            }
            let cfg = self.sample_opp_config(pack, &b[di], belief);
            for (i, c) in cfg.iter().enumerate() {
                if let Some(c) = c {
                    self.determinize(pack, &mut b[di].party[i], c);
                }
            }
            let all = candidate_actions(pack, &b[di], &b[me_idx], &bf, self.collapse_mega);
            let moves: Vec<Action> =
                all.iter().filter(|x| x.kind == ActKind::Move).cloned().collect();
            let opp_cands = if moves.is_empty() { all } else { moves };
            let mut v_type = 1.0f64;
            for oa in &opp_cands {
                let mut c: [Side; 2] = [b[0].clone(), b[1].clone()];
                let mut cf = bf.clone();
                let winner = self.advance_turn(pack, &mut c, &mut cf, a, oa, my_is_s1, grng);
                let v = if winner != 0 {
                    if (winner == 1) == my_is_s1 {
                        1.0
                    } else {
                        0.0
                    }
                } else {
                    self.leaf_value(pack, net, &mut c, &mut cf, my_is_s1, grng)
                };
                if v < v_type {
                    v_type = v;
                }
            }
            if v_type < worst {
                worst = v_type;
            }
            let _ = &mut bf;
        }
        worst
    }

    /// SearchAI._apply_downside_guard
    #[allow(clippy::too_many_arguments)]
    fn apply_downside_guard(
        &mut self,
        pack: &Pack,
        net: &NetW,
        sides: &[Side; 2],
        me_idx: usize,
        field: &Field,
        belief: &mut OpponentBelief,
        root_my: &[Action],
        chosen: Action,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) -> Action {
        let switches: Vec<Action> =
            root_my.iter().filter(|a| a.kind == ActKind::Switch).cloned().collect();
        if switches.is_empty() {
            return chosen;
        }
        let chosen_is_switch = chosen.kind == ActKind::Switch;
        let mut cand: Vec<Action> = Vec::new();
        if !chosen_is_switch {
            cand.push(chosen.clone());
        }
        cand.extend(switches.iter().cloned());
        let mut ds: Vec<f64> = Vec::with_capacity(cand.len());
        for a in &cand {
            let v =
                self.downside_value(pack, net, sides, me_idx, field, belief, a, my_is_s1, grng);
            ds.push(v);
        }
        let off = if chosen_is_switch { 0 } else { 1 };
        let mut bi = 0usize;
        for j in 1..switches.len() {
            if ds[off + j] > ds[off + bi] {
                bi = j;
            }
        }
        let base = if chosen_is_switch {
            // chosen は switches のどれか（値一致）＝ Python は id(chosen) で引く
            let mut k = 0usize;
            for (j, s) in switches.iter().enumerate() {
                if s.switch_to == chosen.switch_to {
                    k = j;
                    break;
                }
            }
            ds[k]
        } else {
            ds[0]
        };
        if ds[off + bi] - base >= self.downside_margin {
            return switches[bi].clone();
        }
        chosen
    }
}

/// Side に belief を設定する補助
pub fn set_belief(side: &mut Side, b: OpponentBelief) {
    side.belief = BeliefSlot(Some(Box::new(b)));
}
