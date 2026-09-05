//! simulator/ai.py の移植（HeuristicAI / GreedyAI / RandomAI / certain_ko_override / select_party）。
//!
//! Python の実挙動をそのまま再現する（＝AI 評価は calc_damage の副作用で実状態を汚す）。
//! R2 ハーネスは Battle.clone() 上で AI を動かしていたが、本番 Python はクローンしない。
//! ここでは本番 Python に合わせて実状態に対して評価する。
use crate::battle::{crit_chance, is_megastone, ActKind, Action, Side};
use crate::damage::{calc_damage, DMove, Field};
use crate::interner::Sym;
use crate::pack::{Cat, Pack};
use crate::poke::{mega_evolve_poke, Poke};
use crate::rng::BRng;

const AVG_HP: f64 = 170.0;

#[inline]
fn dmg_rng(rng: &mut dyn BRng) -> impl FnMut(u8) -> f64 + '_ {
    move |k: u8| if k == 0 { rng.random() } else { rng.choice(16) as f64 }
}

#[inline]
pub fn is_hazard(pack: &Pack, name: Sym) -> bool {
    let l = &pack.sy.l;
    name == l.ステルスロック || name == l.まきびし || name == pack.sy.ai.スパイク || name == l.どくびし
}

pub fn is_setup_move(pack: &Pack, name: Sym) -> bool {
    let l = &pack.sy.l;
    name == l.つるぎのまい
        || name == l.りゅうのまい
        || name == l.ちょうのまい
        || name == l.めいそう
        || name == l.わるだくみ
        || name == l.からをやぶる
        || name == l.てっぺき
        || name == l.ビルドアップ
        || name == l.ロックカット
        || name == l.こうそくいどう
        || name == l.せいちょう
        || name == l.とぐろをまく
        || name == l.コットンガード
        || name == l.はらだいこ
}

/// battle.py:44 is_trapped。`_bound_turns` は BattlePokemon に存在しない属性のため
/// getattr の既定 0 が常に使われる＝バインドでは交代不可にならない（Python の実挙動）。
pub fn is_trapped(pack: &Pack, poke: &Poke, opponent: Option<&Poke>) -> bool {
    if let Some(o) = opponent {
        if o.is_alive && o.ability == pack.sy.l.かげふみ && !poke.has_type(pack.tc.ゴースト) {
            return true;
        }
    }
    poke.trapped
}

/// ai.py `_effective_speed`
pub fn effective_speed(pack: &Pack, poke: &Poke, field: &Field) -> i64 {
    let l = &pack.sy.l;
    let mut spd = ((poke.eff_speed(pack) as f64)
        * crate::items::get_speed_item_multiplier(pack, poke.item))
    .floor() as i64;
    if field.weather == Some(pack.sy.we.rain) && poke.ability == l.すいすい {
        spd *= 2;
    }
    if field.weather == Some(pack.sy.we.sunny) && poke.ability == l.ようりょくそ {
        spd *= 2;
    }
    // battle.rs の速度順（実際に行動順を決める側）に揃える。
    // 以前は すなかき/ゆきかき が抜け、代わりに すながくれ（本来は回避率特性で速度に無関係）へ
    // ×1.5 を掛けていた。
    if field.weather == Some(pack.sy.we.sandstorm) && poke.ability == l.すなかき {
        spd *= 2;
    }
    if field.weather == Some(pack.sy.we.hail) && poke.ability == l.ゆきかき {
        spd *= 2;
    }
    if field.electric_terrain && poke.ability == l.サーフテール {
        spd *= 2;
    }
    spd
}

/// ai.py `expected_damage`
pub fn expected_damage(
    pack: &Pack,
    atk: &mut Poke,
    def: &mut Poke,
    mv: &DMove,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> f64 {
    if mv.category == Cat::Status || mv.power.is_none() {
        return 0.0;
    }
    let acc = (match mv.accuracy {
        Some(a) if a != 0 => a,
        _ => 100,
    }) as f64
        / 100.0;
    if pack.eff(mv.ty, def.type1, def.type2) == 0.0 {
        return 0.0;
    }
    let mut dmg = {
        let mut f = dmg_rng(rng);
        calc_damage(pack, atk, def, mv, field, false, Some(0.5), None, &mut f) as f64
    };
    let pc = crit_chance(pack, atk, mv, Some(def));
    if pc > 0.0 {
        let dc = {
            let mut f = dmg_rng(rng);
            calc_damage(pack, atk, def, mv, field, true, Some(0.5), None, &mut f) as f64
        };
        dmg = dmg * (1.0 - pc) + dc * pc;
    }
    let l = &pack.sy.l;
    if (atk.ability == l.へんげんじざい || atk.ability == pack.sy.ai.リベロ) && !atk.has_type(mv.ty)
    {
        dmg *= 1.5;
    }
    dmg * acc
}

/// ai.py `_best_expected_damage`
pub fn best_expected_damage(
    pack: &Pack,
    p: &mut Poke,
    opp: &mut Poke,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> f64 {
    let moves = p.moves.clone();
    let mut best = 0.0f64;
    let mut any = false;
    for mv in &moves {
        let v = expected_damage(pack, p, opp, mv, field, rng);
        if !any || v > best {
            best = v;
            any = true;
        }
    }
    if any {
        best
    } else {
        0.0
    }
}

/// ai.py `_matchup_score`
fn matchup_score(pack: &Pack, p: &Poke, opp: &Poke) -> i64 {
    let has_se = p.moves.iter().any(|mv| {
        mv.category != Cat::Status
            && mv.power.unwrap_or(0) != 0
            && pack.eff(mv.ty, opp.type1, opp.type2) >= 2.0
    });
    let mut opp_stab_max = f64::NEG_INFINITY;
    for t in [Some(opp.type1), opp.type2].into_iter().flatten() {
        let e = pack.eff(t, p.type1, p.type2);
        if e > opp_stab_max {
            opp_stab_max = e;
        }
    }
    if opp_stab_max == f64::NEG_INFINITY {
        opp_stab_max = 1.0;
    }
    let mut score = 0i64;
    if has_se {
        score += 2;
    }
    if opp_stab_max <= 0.5 {
        score += 2;
    } else if opp_stab_max <= 1.0 {
        score += 1;
    }
    score
}

/// ai.py `_is_likely_threatened`
fn is_likely_threatened(pack: &Pack, me: &Poke, opp: &Poke, known: &[Sym]) -> bool {
    for mv in &opp.moves {
        if known.contains(&mv.name) && pack.eff(mv.ty, me.type1, me.type2) >= 2.0 {
            return true;
        }
    }
    for t in [Some(opp.type1), opp.type2].into_iter().flatten() {
        if pack.eff(t, me.type1, me.type2) >= 2.0 {
            return true;
        }
    }
    false
}

/// ai.py `_best_switch_target`
fn best_switch_target(pack: &Pack, my: &Side, opp: &Side) -> Option<usize> {
    let me = my.active();
    let op = opp.active();
    if me.locked_move.is_some() || me.bound_count > 0 || me.switched_this_turn {
        return None;
    }
    let benched: Vec<usize> = (0..my.party.len())
        .filter(|&i| my.party[i].is_alive && i != my.active_idx)
        .collect();
    if benched.is_empty() {
        return None;
    }
    let known: Vec<Sym> = my
        .opp_view
        .pokemon
        .iter()
        .find(|k| k.name == op.name)
        .map(|k| k.known_moves.clone())
        .unwrap_or_default();
    if !is_likely_threatened(pack, me, op, &known) {
        return None;
    }
    let current = matchup_score(pack, me, op);
    let mut best_idx: Option<usize> = None;
    let mut best_score = current;
    let mut best_hp = 0.0f64;
    for &i in &benched {
        let p = &my.party[i];
        let s = matchup_score(pack, p, op);
        let hp_ratio = (p.hp as f64) / (if p.max_hp != 0 { p.max_hp } else { 1 } as f64);
        if s > best_score || (s == best_score && s > current && hp_ratio > best_hp) {
            best_score = s;
            best_idx = Some(i);
            best_hp = hp_ratio;
        }
    }
    best_idx
}

/// ai.py `_goes_first`
fn goes_first(pack: &Pack, me: &Poke, opp: &Poke, my_pri: i64, field: &Field) -> bool {
    let opp_max = opp.moves.iter().map(|m| m.priority).max().unwrap_or(0);
    if my_pri != opp_max {
        return my_pri > opp_max;
    }
    let my_spd = effective_speed(pack, me, field);
    let opp_spd = effective_speed(pack, opp, field);
    if !field.trick_room {
        my_spd >= opp_spd
    } else {
        my_spd <= opp_spd
    }
}

/// ai.py `_can_ko`
fn can_ko(
    pack: &Pack,
    atk: &mut Poke,
    def: &mut Poke,
    mv: &DMove,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> bool {
    if mv.power.unwrap_or(0) == 0 || mv.category == Cat::Status {
        return false;
    }
    if pack.eff(mv.ty, def.type1, def.type2) == 0.0 {
        return false;
    }
    let d = {
        let mut f = dmg_rng(rng);
        calc_damage(pack, atk, def, mv, field, false, Some(0.5), None, &mut f)
    };
    d >= def.hp
}

/// ai.py `_opp_priority_threatens`
fn opp_priority_threatens(
    pack: &Pack,
    me: &mut Poke,
    opp: &mut Poke,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> bool {
    let moves = opp.moves.clone();
    for mv in &moves {
        if mv.priority > 0 && mv.power.unwrap_or(0) != 0 {
            let d = {
                let mut f = dmg_rng(rng);
                calc_damage(pack, opp, me, mv, field, false, Some(1.0), None, &mut f)
            };
            if d >= me.hp {
                return true;
            }
        }
    }
    false
}

/// ai.py `_priority_ko_action`
fn priority_ko_action(
    pack: &Pack,
    me: &mut Poke,
    opp: &mut Poke,
    valid: &[(usize, DMove)],
    field: &mut Field,
    do_mega: bool,
    rng: &mut dyn BRng,
) -> Option<Action> {
    let mut cands: Vec<(usize, DMove)> = Vec::new();
    for (i, mv) in valid {
        if mv.priority > 0
            && mv.power.unwrap_or(0) != 0
            && goes_first(pack, me, opp, mv.priority, field)
            && can_ko(pack, me, opp, mv, field, rng)
        {
            cands.push((*i, mv.clone()));
        }
    }
    if cands.is_empty() {
        return None;
    }
    let mut best = 0usize;
    let mut bestv = f64::NEG_INFINITY;
    for (k, (_, mv)) in cands.iter().enumerate() {
        let v = expected_damage(pack, me, opp, mv, field, rng);
        if k == 0 || v > bestv {
            bestv = v;
            best = k;
        }
    }
    Some(Action {
        kind: ActKind::Move,
        mv: Some(cands[best].1.clone()),
        move_idx: cands[best].0 as i64,
        switch_to: -1,
        do_mega,
    })
}

/// ai.py `_forced_charging_action`（該当技が無ければ charging_move をクリアする＝副作用あり）
pub fn forced_charging_action(me: &mut Poke) -> Option<Action> {
    let cm = me.charging_move?;
    for (i, mv) in me.moves.iter().enumerate() {
        if mv.name == cm {
            return Some(Action {
                kind: ActKind::Move,
                mv: Some(mv.clone()),
                move_idx: i as i64,
                switch_to: -1,
                do_mega: false,
            });
        }
    }
    me.charging_move = None;
    None
}

/// ai.py `_filter_valid_by_lock`
pub fn filter_valid_by_lock(me: &Poke) -> Vec<(usize, DMove)> {
    let all: Vec<(usize, DMove)> =
        me.moves.iter().enumerate().map(|(i, m)| (i, m.clone())).collect();
    let mut valid = all.clone();
    if let Some(d) = me.disabled_move {
        valid.retain(|(_, mv)| mv.name != d);
    }
    let lock = me.choice_locked_move.or({
        if me.encore_count > 0 || me.lock_count > 0 {
            me.locked_move
        } else {
            None
        }
    });
    if let Some(lk) = lock {
        let locked: Vec<(usize, DMove)> =
            valid.iter().filter(|(_, mv)| mv.name == lk).cloned().collect();
        return if !locked.is_empty() { locked } else { valid };
    }
    if !valid.is_empty() {
        valid
    } else {
        all
    }
}

/// ai.py `_filter_by_pp`
pub fn filter_by_pp(valid: &[(usize, DMove)], me: &Poke) -> Vec<(usize, DMove)> {
    valid.iter().filter(|(i, _)| *i < me.pp.len() && me.pp[*i] > 0).cloned().collect()
}

/// ai.py `_get_struggle`
pub fn struggle(pack: &Pack) -> DMove {
    DMove {
        name: pack.sy.l.わるあがき,
        ty: pack.tc.ノーマル,
        category: Cat::Physical,
        power: Some(50),
        accuracy: Some(100),
        priority: 0,
        pp: Some(1),
    }
}

/// ai.py `should_mega_evolve`
#[inline]
fn should_mega(me: &Poke) -> bool {
    me.mega.is_some() && !me.mega_evolved
}

/// `_hazard_value` が読む相手サイドの情報（AI 評価中は不変）
#[derive(Clone, Copy)]
pub struct HazCtx {
    pub remaining: usize,
    pub field_idx: usize,
    pub sr_set: bool,
    pub sr_pending: bool,
}

impl HazCtx {
    pub fn of(opp: &Side) -> HazCtx {
        HazCtx {
            remaining: opp.party.iter().filter(|p| p.is_alive).count(),
            field_idx: opp.field_idx,
            sr_set: opp.stealth_rock_set,
            sr_pending: opp.sr_pending,
        }
    }
}

/// ai.py `_hazard_value`
pub fn hazard_value(pack: &Pack, name: Sym, opp: &HazCtx, field: &Field) -> f64 {
    let l = &pack.sy.l;
    let opp_remaining = opp.remaining;
    if opp_remaining <= 1 {
        return 0.0;
    }
    let entries = opp_remaining as f64;
    let oi = opp.field_idx;
    if name == l.ステルスロック {
        if opp.sr_set || opp.sr_pending || field.stealth_rock[oi] {
            return 0.0;
        }
        return entries * AVG_HP * 0.125;
    }
    if name == l.まきびし || name == pack.sy.ai.スパイク {
        let layers = field.spikes[oi];
        if layers >= 3 {
            return 0.0;
        }
        let d = [0.125, 1.0 / 6.0, 0.25][std::cmp::min(layers, 2) as usize];
        return entries * AVG_HP * d;
    }
    if name == l.どくびし {
        let layers = field.toxic_spikes[oi];
        if layers >= 2 {
            return 0.0;
        }
        return entries * AVG_HP * 0.09;
    }
    0.0
}

/// ai.py `_poison_immune`
fn poison_immune(pack: &Pack, opp: &Poke) -> bool {
    let l = &pack.sy.l;
    if opp.has_type(pack.tc.どく) || opp.has_type(pack.tc.はがね) {
        return true;
    }
    opp.ability == l.めんえき
        || opp.ability == l.きよめのしお
        || opp.ability == l.マジックガード
        || opp.ability == l.ポイズンヒール
}

/// ai.py `_wall_break_action`
fn wall_break_action(
    pack: &Pack,
    me: &mut Poke,
    opp: &mut Poke,
    valid: &[(usize, DMove)],
    field: &mut Field,
    do_mega: bool,
    rng: &mut dyn BRng,
) -> Option<Action> {
    let l = &pack.sy.l;
    let bounces = opp.ability == l.マジックミラー;
    for (i, mv) in valid {
        if mv.name == l.どくどく && opp.status.is_none() && !poison_immune(pack, opp) && !bounces {
            return Some(Action {
                kind: ActKind::Move,
                mv: Some(mv.clone()),
                move_idx: *i as i64,
                switch_to: -1,
                do_mega: false,
            });
        }
    }
    let opp_has_utility = opp.moves.iter().any(|m| m.category == Cat::Status);
    if opp_has_utility && !bounces {
        for (i, mv) in valid {
            if mv.name == l.ちょうはつ && opp.taunt_count == 0 {
                return Some(Action {
                    kind: ActKind::Move,
                    mv: Some(mv.clone()),
                    move_idx: *i as i64,
                    switch_to: -1,
                    do_mega: false,
                });
            }
        }
    }
    let opp_moves = opp.moves.clone();
    let mut opp_best = 0.0f64;
    let mut any = false;
    for m in &opp_moves {
        if m.power.unwrap_or(0) != 0 {
            let v = expected_damage(pack, opp, me, m, field, rng);
            if !any || v > opp_best {
                opp_best = v;
                any = true;
            }
        }
    }
    if !any {
        opp_best = 0.0;
    }
    let my_stages = (me.stage_attack
        + me.stage_sp_attack
        + me.stage_speed
        + me.stage_defense
        + me.stage_sp_defense) as i64;
    if opp_best < (me.hp as f64) * 0.4 && my_stages < 6 {
        for (i, mv) in valid {
            if is_setup_move(pack, mv.name) {
                return Some(Action {
                    kind: ActKind::Move,
                    mv: Some(mv.clone()),
                    move_idx: *i as i64,
                    switch_to: -1,
                    do_mega,
                });
            }
        }
    }
    None
}

#[derive(Clone, Copy, Debug)]
pub enum Ai {
    Greedy,
    Random,
    Heuristic { enable_tactics: bool, finish_priority: bool, wall_break: bool },
}

impl Ai {
    pub fn heuristic() -> Ai {
        Ai::Heuristic { enable_tactics: true, finish_priority: true, wall_break: true }
    }
}

#[inline]
fn mv_action(i: usize, mv: &DMove, do_mega: bool) -> Action {
    Action { kind: ActKind::Move, mv: Some(mv.clone()), move_idx: i as i64, switch_to: -1, do_mega }
}

/// 期待値最大（Python `max(key=...)` は最初の最大要素を返す）
fn argmax_expected(
    pack: &Pack,
    me: &mut Poke,
    opp: &mut Poke,
    cands: &[(usize, DMove)],
    field: &mut Field,
    rng: &mut dyn BRng,
) -> usize {
    let mut best = 0usize;
    let mut bestv = f64::NEG_INFINITY;
    for (k, (_, mv)) in cands.iter().enumerate() {
        let v = expected_damage(pack, me, opp, mv, field, rng);
        if k == 0 || v > bestv {
            bestv = v;
            best = k;
        }
    }
    best
}

/// GreedyAI.__call__
pub fn greedy_ai(
    pack: &Pack,
    my: &mut Side,
    opp: &mut Side,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> Action {
    let (mi, oi) = (my.active_idx, opp.active_idx);
    let mega_used = my.mega_used;
    let me = &mut my.party[mi];
    let op = &mut opp.party[oi];
    if !me.is_alive {
        return Action::default();
    }
    if let Some(a) = forced_charging_action(me) {
        return a;
    }
    let do_mega = should_mega(me) && !mega_used;
    if me.moves.is_empty() {
        return Action::default();
    }
    let valid = filter_valid_by_lock(me);
    let pp_valid = filter_by_pp(&valid, me);
    if pp_valid.is_empty() {
        return Action {
            kind: ActKind::Move,
            mv: Some(struggle(pack)),
            move_idx: -1,
            switch_to: -1,
            do_mega,
        };
    }
    let valid = pp_valid;

    let supereff: Vec<(usize, DMove)> = valid
        .iter()
        .filter(|(_, mv)| {
            mv.category != Cat::Status
                && mv.power.unwrap_or(0) != 0
                && pack.eff(mv.ty, op.type1, op.type2) >= 2.0
        })
        .cloned()
        .collect();
    if !supereff.is_empty() {
        let k = argmax_expected(pack, me, op, &supereff, field, rng);
        return mv_action(supereff[k].0, &supereff[k].1, do_mega);
    }
    let dmg_moves: Vec<(usize, DMove)> = valid
        .iter()
        .filter(|(_, mv)| mv.category != Cat::Status && mv.power.unwrap_or(0) != 0)
        .cloned()
        .collect();
    if !dmg_moves.is_empty() {
        let k = argmax_expected(pack, me, op, &dmg_moves, field, rng);
        return mv_action(dmg_moves[k].0, &dmg_moves[k].1, do_mega);
    }
    mv_action(valid[0].0, &valid[0].1, do_mega)
}

/// RandomAI.__call__
pub fn random_ai(
    pack: &Pack,
    my: &mut Side,
    _opp: &mut Side,
    _field: &mut Field,
    rng: &mut dyn BRng,
) -> Action {
    let mi = my.active_idx;
    let mega_used = my.mega_used;
    let me = &mut my.party[mi];
    if !me.is_alive {
        return Action::default();
    }
    if let Some(a) = forced_charging_action(me) {
        return a;
    }
    let do_mega = should_mega(me) && !mega_used;
    if me.moves.is_empty() {
        return Action::default();
    }
    let valid = filter_valid_by_lock(me);
    let pp_valid = filter_by_pp(&valid, me);
    if pp_valid.is_empty() {
        return Action {
            kind: ActKind::Move,
            mv: Some(struggle(pack)),
            move_idx: -1,
            switch_to: -1,
            do_mega,
        };
    }
    let k = rng.choice(pp_valid.len());
    mv_action(pp_valid[k].0, &pp_valid[k].1, do_mega)
}

/// HeuristicAI.__call__
pub fn heuristic_ai(
    pack: &Pack,
    my: &mut Side,
    opp: &mut Side,
    field: &mut Field,
    enable_tactics: bool,
    finish_priority: bool,
    wall_break: bool,
    rng: &mut dyn BRng,
) -> Action {
    let l = &pack.sy.l;
    let (mi, oi) = (my.active_idx, opp.active_idx);
    let mega_used = my.mega_used;
    let wish_count = my.wish_count;
    let (do_mega, valid) = {
        let me = &mut my.party[mi];
        if !me.is_alive {
            return Action::default();
        }
        if let Some(a) = forced_charging_action(me) {
            return a;
        }
        let do_mega = should_mega(me) && !mega_used;
        if me.moves.is_empty() {
            return Action::default();
        }
        let valid = filter_valid_by_lock(me);
        let pp_valid = filter_by_pp(&valid, me);
        if pp_valid.is_empty() {
            return Action {
                kind: ActKind::Move,
                mv: Some(struggle(pack)),
                move_idx: -1,
                switch_to: -1,
                do_mega,
            };
        }
        (do_mega, pp_valid)
    };

    // 交代判断
    {
        let trapped = is_trapped(pack, &my.party[mi], Some(&opp.party[oi]));
        let sw = if trapped { None } else { best_switch_target(pack, my, opp) };
        if let Some(idx) = sw {
            return Action {
                kind: ActKind::Switch,
                mv: None,
                move_idx: 0,
                switch_to: idx as i64,
                do_mega: false,
            };
        }
    }

    let bench_alive = (0..my.party.len()).any(|j| j != my.active_idx && my.party[j].is_alive);
    let haz = HazCtx::of(opp);
    let me = &mut my.party[mi];
    let op = &mut opp.party[oi];

    if enable_tactics {
        let has = |n: Sym| valid.iter().any(|(_, mv)| mv.name == n);
        let mut can_ko_now = false;
        for (_, mv) in valid.iter() {
            if mv.power.unwrap_or(0) != 0 && mv.category != Cat::Status {
                if can_ko(pack, me, op, mv, field, rng) {
                    can_ko_now = true;
                    break;
                }
            }
        }
        let opp_moves = op.moves.clone();
        let mut opp_best = 0.0f64;
        let mut any = false;
        for m in &opp_moves {
            if m.power.unwrap_or(0) != 0 {
                let v = expected_damage(pack, op, me, m, field, rng);
                if !any || v > opp_best {
                    opp_best = v;
                    any = true;
                }
            }
        }
        if !any {
            opp_best = 0.0;
        }
        if wish_count > 0 && has(l.まもる) && me.protect_consecutive == 0 && !can_ko_now {
            for (i, mv) in valid.iter() {
                if mv.name == l.まもる {
                    return Action {
                        kind: ActKind::Move,
                        mv: Some(mv.clone()),
                        move_idx: *i as i64,
                        switch_to: -1,
                        do_mega: false,
                    };
                }
            }
        }
        if wish_count == 0
            && (me.hp as f64) < (me.max_hp as f64) * 0.6
            && has(l.ねがいごと)
            && !can_ko_now
            && opp_best < me.hp as f64
        {
            for (i, mv) in valid.iter() {
                if mv.name == l.ねがいごと {
                    return Action {
                        kind: ActKind::Move,
                        mv: Some(mv.clone()),
                        move_idx: *i as i64,
                        switch_to: -1,
                        do_mega: false,
                    };
                }
            }
        }
        if has(l.バトンタッチ) && !can_ko_now && bench_alive {
            let boosts = (std::cmp::max(0, me.stage_attack)
                + std::cmp::max(0, me.stage_sp_attack)
                + std::cmp::max(0, me.stage_speed)) as i64;
            let setup_here: Vec<(usize, DMove)> =
                valid.iter().filter(|(_, mv)| is_setup_move(pack, mv.name)).cloned().collect();
            if boosts >= 2 || opp_best >= (me.hp as f64) * 0.5 {
                for (i, mv) in valid.iter() {
                    if mv.name == l.バトンタッチ {
                        return Action {
                            kind: ActKind::Move,
                            mv: Some(mv.clone()),
                            move_idx: *i as i64,
                            switch_to: -1,
                            do_mega: false,
                        };
                    }
                }
            }
            if opp_best < (me.hp as f64) * 0.45 && boosts < 4 && !setup_here.is_empty() {
                return mv_action(setup_here[0].0, &setup_here[0].1, do_mega);
            }
            if opp_best < (me.hp as f64) * 0.45
                && me.ability == l.かそく
                && me.stage_speed < 3
                && me.protect_consecutive == 0
                && has(l.まもる)
            {
                for (i, mv) in valid.iter() {
                    if mv.name == l.まもる {
                        return Action {
                            kind: ActKind::Move,
                            mv: Some(mv.clone()),
                            move_idx: *i as i64,
                            switch_to: -1,
                            do_mega: false,
                        };
                    }
                }
            }
        }
    }

    // 先制技 KO 判定
    let my_spd = effective_speed(pack, me, field);
    let opp_spd = effective_speed(pack, op, field);
    let i_go_second =
        if !field.trick_room { my_spd < opp_spd } else { my_spd > opp_spd };
    let opp_moves = op.moves.clone();
    let mut opp_normal_ko = false;
    for mv in &opp_moves {
        if mv.power.unwrap_or(0) != 0 && mv.category != Cat::Status {
            if can_ko(pack, op, me, mv, field, rng) {
                opp_normal_ko = true;
                break;
            }
        }
    }
    if i_go_second && opp_normal_ko {
        if let Some(a) = priority_ko_action(pack, me, op, &valid, field, do_mega, rng) {
            return a;
        }
    }
    if opp_priority_threatens(pack, me, op, field, rng) {
        if let Some(a) = priority_ko_action(pack, me, op, &valid, field, do_mega, rng) {
            return a;
        }
    }
    if finish_priority {
        if let Some(a) = priority_ko_action(pack, me, op, &valid, field, do_mega, rng) {
            return a;
        }
    }

    // 通常の技選択
    let hazard_candidates: Vec<(usize, DMove)> = valid
        .iter()
        .filter(|(_, mv)| mv.category == Cat::Status && is_hazard(pack, mv.name))
        .cloned()
        .collect();
    let dmg_moves: Vec<(usize, DMove)> = valid
        .iter()
        .filter(|(_, mv)| mv.category != Cat::Status && mv.power.unwrap_or(0) != 0)
        .cloned()
        .collect();
    if !hazard_candidates.is_empty() {
        let mut can_ko_now = false;
        for (_, mv) in dmg_moves.iter() {
            if can_ko(pack, me, op, mv, field, rng) {
                can_ko_now = true;
                break;
            }
        }
        if !can_ko_now {
            let mut best = 0usize;
            let mut bestv = f64::NEG_INFINITY;
            for (k, (_, mv)) in hazard_candidates.iter().enumerate() {
                let v = hazard_value(pack, mv.name, &haz, field);
                if k == 0 || v > bestv {
                    bestv = v;
                    best = k;
                }
            }
            if hazard_value(pack, hazard_candidates[best].1.name, &haz, field) > 0.0 {
                return Action {
                    kind: ActKind::Move,
                    mv: Some(hazard_candidates[best].1.clone()),
                    move_idx: hazard_candidates[best].0 as i64,
                    switch_to: -1,
                    do_mega: false,
                };
            }
        } else {
            let mut best_dmg = 0.0f64;
            let mut any = false;
            for (_, mv) in dmg_moves.iter() {
                let v = expected_damage(pack, me, op, mv, field, rng);
                if !any || v > best_dmg {
                    best_dmg = v;
                    any = true;
                }
            }
            if !any {
                best_dmg = 0.0;
            }
            for (i, mv) in hazard_candidates.iter() {
                if hazard_value(pack, mv.name, &haz, field) > best_dmg * 1.5 {
                    return Action {
                        kind: ActKind::Move,
                        mv: Some(mv.clone()),
                        move_idx: *i as i64,
                        switch_to: -1,
                        do_mega: false,
                    };
                }
            }
        }
    }

    let mut best_dmg = 0.0f64;
    {
        let mut any = false;
        for (_, mv) in dmg_moves.iter() {
            let v = expected_damage(pack, me, op, mv, field, rng);
            if !any || v > best_dmg {
                best_dmg = v;
                any = true;
            }
        }
        if !any {
            best_dmg = 0.0;
        }
    }
    if wall_break && best_dmg * 3.0 < op.hp as f64 {
        if let Some(a) = wall_break_action(pack, me, op, &valid, field, do_mega, rng) {
            return a;
        }
    }

    let supereff: Vec<(usize, DMove)> = dmg_moves
        .iter()
        .filter(|(_, mv)| pack.eff(mv.ty, op.type1, op.type2) >= 2.0)
        .cloned()
        .collect();
    if !supereff.is_empty() {
        let k = argmax_expected(pack, me, op, &supereff, field, rng);
        return mv_action(supereff[k].0, &supereff[k].1, do_mega);
    }
    if !dmg_moves.is_empty() {
        let k = argmax_expected(pack, me, op, &dmg_moves, field, rng);
        return mv_action(dmg_moves[k].0, &dmg_moves[k].1, do_mega);
    }
    mv_action(valid[0].0, &valid[0].1, do_mega)
}

/// ai.py `certain_ko_override`
pub fn certain_ko_override(
    pack: &Pack,
    act: Action,
    my: &mut Side,
    opp: &mut Side,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> Action {
    let l = &pack.sy.l;
    let (mi, oi) = (my.active_idx, opp.active_idx);
    {
        let me = &my.party[mi];
        let op = &opp.party[oi];
        if !me.is_alive || !op.is_alive {
            return act;
        }
    }
    if forced_charging_action(&mut my.party[mi]).is_some() {
        return act;
    }
    {
        let op = &opp.party[oi];
        let full = op.hp == op.max_hp;
        if full
            && (op.ability == l.マルチスケイル
                || op.ability == pack.sy.ai.ファントムガード
                || op.item == Some(l.きあいのタスキ)
                || op.ability == l.がんじょう)
        {
            return act;
        }
        // ばけのかわは満タンかどうかに関係なく1発目のダメージを無効化する（battle.rs:1294）ので、
        // 未破壊のうちは確定KOが成立しない。full 条件では捕まらないため個別に除外する。
        if op.ability == l.ばけのかわ && !op.disguise_broken {
            return act;
        }
    }
    let me = &mut my.party[mi];
    let op = &mut opp.party[oi];
    let valid = filter_by_pp(&filter_valid_by_lock(me), me);
    let mut best: Option<(usize, DMove)> = None;
    let mut bestd = -1i64;
    for (i, mv) in &valid {
        if mv.power.unwrap_or(0) == 0 || mv.category == Cat::Status {
            continue;
        }
        if pack.eff(mv.ty, op.type1, op.type2) == 0.0 {
            continue;
        }
        if !goes_first(pack, me, op, mv.priority, field) {
            continue;
        }
        let d = {
            let mut f = dmg_rng(rng);
            // 正規化ロール。最低ロールは 0.0（0.85 は実効 0.85+0.85*0.15=0.9775 ＝ほぼ最高値で、
            // 確定でないKOを確定と誤認する。実測: 介入の15.3%が該当）
            calc_damage(pack, me, op, mv, field, false, Some(0.0), None, &mut f)
        };
        if d >= op.hp && d > bestd {
            bestd = d;
            best = Some((*i, mv.clone()));
        }
    }
    let (bi, bmv) = match best {
        None => return act,
        Some(x) => x,
    };
    if act.kind == ActKind::Move && act.mv.as_ref().map(|m| m.name) == Some(bmv.name) {
        return act;
    }
    Action {
        kind: ActKind::Move,
        mv: Some(bmv),
        move_idx: bi as i64,
        switch_to: -1,
        do_mega: act.do_mega,
    }
}

/// AI ディスパッチ（certain_ko_override 付き）
pub fn decide(
    pack: &Pack,
    ai: Ai,
    my: &mut Side,
    opp: &mut Side,
    field: &mut Field,
    with_override: bool,
    rng: &mut dyn BRng,
) -> Action {
    let a = match ai {
        Ai::Greedy => greedy_ai(pack, my, opp, field, rng),
        Ai::Random => random_ai(pack, my, opp, field, rng),
        Ai::Heuristic { enable_tactics, finish_priority, wall_break } => heuristic_ai(
            pack,
            my,
            opp,
            field,
            enable_tactics,
            finish_priority,
            wall_break,
            rng,
        ),
    };
    if with_override {
        certain_ko_override(pack, a, my, opp, field, rng)
    } else {
        a
    }
}

// ───────────────────────── select_party ─────────────────────────

/// ai.py `_temp_sample_indices`（float の加算順まで再現）
pub fn temp_sample_indices(
    scores: &[f64],
    n: usize,
    temperature: f64,
    rng: &mut dyn FnMut() -> f64,
) -> Vec<usize> {
    let len = scores.len();
    let s = crate::pysum::pysum(scores.iter().copied());
    let m = s / len as f64;
    let var = crate::pysum::pysum(scores.iter().map(|v| (*v - m) * (*v - m)));
    let mut sd = (var / len as f64).sqrt();
    if sd == 0.0 {
        sd = 1.0;
    }
    let z: Vec<f64> = scores.iter().map(|v| (*v - m) / sd).collect();
    let mut pool: Vec<usize> = (0..len).collect();
    let mut chosen = Vec::new();
    for _ in 0..std::cmp::min(n, len) {
        let ws: Vec<f64> =
            pool.iter().map(|&i| (z[i] / f64::max(1e-6, temperature)).exp()).collect();
        let tot = crate::pysum::pysum_slice(&ws);
        let mut r = rng() * tot;
        let mut hit = None;
        for (k, _) in pool.iter().enumerate() {
            r -= ws[k];
            if r <= 0.0 {
                hit = Some(k);
                break;
            }
        }
        match hit {
            Some(k) => chosen.push(pool.remove(k)),
            None => chosen.push(pool.pop().unwrap()),
        }
    }
    chosen
}

/// ai.py `_order_by_lead`。`party` はインデックス列（呼び出し側の順序で渡す）。
fn order_by_lead(
    pack: &Pack,
    party: &mut Vec<usize>,
    pool: &[Poke],
    opp6: &[Poke],
    temperature: f64,
    rng: &mut dyn FnMut() -> f64,
) {
    if party.is_empty() || party.len() == 1 {
        return;
    }
    let lead_score = |pi: usize| -> f64 {
        let p = &pool[pi];
        let has_hazard =
            p.moves.iter().any(|mv| is_hazard(pack, mv.name) && mv.category == Cat::Status);
        let se_count = opp6
            .iter()
            .filter(|opp| {
                p.moves.iter().any(|mv| {
                    mv.category != Cat::Status
                        && mv.power.unwrap_or(0) != 0
                        && pack.eff(mv.ty, opp.type1, opp.type2) >= 2.0
                })
            })
            .count();
        (if has_hazard { 2.0 } else { 0.0 }) + se_count as f64
    };
    let scores: Vec<f64> = party.iter().map(|&i| lead_score(i)).collect();
    let lead_i;
    if temperature > 0.0 {
        let n = scores.len();
        let s = crate::pysum::pysum(scores.iter().copied());
        let m = s / n as f64;
        let var = crate::pysum::pysum(scores.iter().map(|v| (*v - m) * (*v - m)));
        let mut sd = (var / n as f64).sqrt();
        if sd == 0.0 {
            sd = 1.0;
        }
        let ws: Vec<f64> =
            scores.iter().map(|v| (((*v - m) / sd) / f64::max(1e-6, temperature)).exp()).collect();
        let tot = crate::pysum::pysum_slice(&ws);
        let pick = rng() * tot;
        let mut li = ws.len() - 1;
        let mut acc = 0.0f64;
        for (i, w) in ws.iter().enumerate() {
            acc += *w;
            if pick <= acc {
                li = i;
                break;
            }
        }
        lead_i = li;
    } else {
        let mut bi = 0usize;
        let mut bv = f64::NEG_INFINITY;
        for (i, v) in scores.iter().enumerate() {
            if i == 0 || *v > bv {
                bv = *v;
                bi = i;
            }
        }
        lead_i = bi;
    }
    if lead_i != 0 {
        party.swap(0, lead_i);
    }
}

/// ai.py `select_party`。返り値は party6 のインデックス（選出順、リード先頭）。
/// Python 同様、評価の副作用（きのみ消費等）で party6/opp6 を汚す。
///
/// rng（グローバル `random` 相当・calc_damage が消費）と srng（`rng=` 引数のインスタンス乱数・
/// 温度サンプリングが消費）は Python では別ストリームなので分離して受け取る。
pub fn select_party(
    pack: &Pack,
    party6: &mut Vec<Poke>,
    opp6: &mut Vec<Poke>,
    n: usize,
    temperature: f64,
    mega_penalty: f64,
    rng: &mut dyn BRng,
    srng: &mut dyn FnMut() -> f64,
) -> Vec<usize> {
    let mut dummy = Field::default();
    if party6.len() <= n {
        let mut idx: Vec<usize> = (0..party6.len()).collect();
        let pool = party6.clone();
        let opp = opp6.clone();
        order_by_lead(pack, &mut idx, &pool, &opp, temperature, srng);
        return idx;
    }

    // _poke_score
    fn poke_score(
        pack: &Pack,
        p: &mut Poke,
        opp6: &mut Vec<Poke>,
        field: &mut Field,
        rng: &mut dyn BRng,
    ) -> f64 {
        let my_hp = f64::max(1.0, p.max_hp as f64);
        let my_spd = effective_speed(pack, p, field);
        let mut val = 0.0f64;
        for oi in 0..opp6.len() {
            let opp_hp = f64::max(1.0, opp6[oi].max_hp as f64);
            let my_best = {
                let o = &mut opp6[oi];
                best_expected_damage(pack, p, o, field, rng)
            };
            let opp_best = {
                let o = &mut opp6[oi];
                best_expected_damage(pack, o, p, field, rng)
            };
            let faster = my_spd >= effective_speed(pack, &opp6[oi], field);
            let my_ko = my_best >= opp_hp;
            let opp_ko = opp_best >= my_hp;
            let mv = if my_ko && faster {
                2.0
            } else if my_ko && !opp_ko {
                1.3
            } else if opp_ko && !faster && !my_ko {
                -1.5
            } else {
                let mr = f64::min(my_best / opp_hp, 1.5);
                let orr = f64::min(opp_best / my_hp, 1.5);
                (mr - orr) + (if faster { 0.3 } else { -0.3 })
            };
            val += mv;
        }
        if p.moves.iter().any(|mv| is_hazard(pack, mv.name) && mv.category == Cat::Status) {
            val += 2.0;
        }
        val
    }

    let is_cap = |p: &Poke| p.mega.is_some() && !p.mega_evolved;
    let mega_caps: Vec<usize> = (0..party6.len()).filter(|&i| is_cap(&party6[i])).collect();
    let mut mbest: Option<usize> = None;
    if !mega_caps.is_empty() {
        let mut bv = f64::NEG_INFINITY;
        for (k, &i) in mega_caps.iter().enumerate() {
            let mut p = party6[i].clone();
            mega_evolve_poke(pack, &mut p);
            let v = poke_score(pack, &mut p, opp6, &mut dummy, rng);
            if k == 0 || v > bv {
                bv = v;
                mbest = Some(i);
            }
        }
    }

    let mut eff_score = |i: usize, party6: &mut Vec<Poke>, opp6: &mut Vec<Poke>| -> f64 {
        let cap = is_cap(&party6[i]);
        if Some(i) == mbest {
            let mut p = party6[i].clone();
            mega_evolve_poke(pack, &mut p);
            return poke_score(pack, &mut p, opp6, &mut dummy, rng);
        }
        let mut p = std::mem::take(&mut party6[i]);
        let v = poke_score(pack, &mut p, opp6, &mut dummy, rng);
        party6[i] = p;
        if cap {
            v - mega_penalty
        } else {
            v
        }
    };

    if temperature > 0.0 {
        let scores: Vec<f64> = (0..party6.len()).map(|i| eff_score(i, party6, opp6)).collect();
        let mut idx = temp_sample_indices(&scores, n, temperature, srng);
        let pool = party6.clone();
        let opp = opp6.clone();
        order_by_lead(pack, &mut idx, &pool, &opp, temperature, srng);
        return idx;
    }

    let scores: Vec<f64> = (0..party6.len()).map(|i| eff_score(i, party6, opp6)).collect();
    // sorted(enumerate(party6), key=..., reverse=True) は安定ソート（同点は元順）
    let mut indexed: Vec<usize> = (0..party6.len()).collect();
    indexed.sort_by(|&a, &b| scores[b].partial_cmp(&scores[a]).unwrap());

    let mut selected: Vec<usize> = Vec::new();
    let mut seen: Vec<(crate::pack::Ty, Option<crate::pack::Ty>)> = Vec::new();
    for &i in &indexed {
        if selected.len() >= n {
            break;
        }
        let tp = (party6[i].type1, party6[i].type2);
        if seen.iter().filter(|x| **x == tp).count() >= 2 {
            continue;
        }
        selected.push(i);
        seen.push(tp);
    }
    for &i in &indexed {
        if selected.len() >= n {
            break;
        }
        if !selected.contains(&i) {
            selected.push(i);
        }
    }
    selected.truncate(n);
    let pool = party6.clone();
    let opp = opp6.clone();
    order_by_lead(pack, &mut selected, &pool, &opp, 0.0, srng);
    selected
}

/// メガ石所持判定（select_party の外部利用向け）
pub fn has_megastone(pack: &Pack, p: &Poke) -> bool {
    is_megastone(pack, p.item)
}
