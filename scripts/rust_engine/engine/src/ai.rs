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
        || name == l.ギアチェンジ
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

/// battle.py is_trapped。ゴーストタイプと きれいなぬけがら は常に交代できる。逃げられない状態・はいすいのじん・バインド・かげふみ
pub fn is_trapped(pack: &Pack, poke: &Poke, opponent: Option<&Poke>) -> bool {
    if poke.has_type(pack.tc.ゴースト) || poke.item == Some(pack.sy.l.きれいなぬけがら) {
        return false;
    }
    if let Some(o) = opponent {
        if o.is_alive && o.ability == pack.sy.l.かげふみ {
            return true;
        }
    }
    poke.trapped || poke.no_retreat || poke.bound_count > 0
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
    move_damage(pack, atk, def, mv, field, 0.5, HitMode::Exp, true, rng) * acc
}

#[derive(Clone, Copy, PartialEq, Eq)]
pub enum HitMode {
    Exp,
    Min,
    Max,
}

/// ai.py `_hit_plan`。連続技の [(何発目, 重み)]。正本は battle::calc_hits。
/// Exp=期待回数 / Min=必ず当たる回数（確定KO判定） / Max=最大回数（被弾の最悪値）。
pub fn hit_plan(pack: &Pack, mv: &DMove, atk: &Poke, mode: HitMode) -> Vec<(i64, f64)> {
    if !pack.env_multi_hit {
        return vec![(0, 1.0)];
    }
    let l = &pack.sy.l;
    let n = mv.name;
    let skill_link = atk.ability == l.スキルリンク;
    if n == l.ダブルキック || n == l.にどげり || n == l.ダブルウイング || n == l.ドラゴンアロー
        || n == l.スパークリングアリア || n == l.ダブルパンツァー || n == l.ツインビーム
        || n == l.ダブルアタック
    {
        return vec![(0, 2.0)];
    }
    if n == l.トリプルアクセル {
        return vec![(0, 1.0), (1, 1.0), (2, 1.0)];
    }
    let pick = |e: f64, lo: f64, hi: f64| match mode {
        HitMode::Exp => e,
        HitMode::Min => lo,
        HitMode::Max => hi,
    };
    if n == l.スケイルショット || n == l.みずしゅりけん || n == l.ロックブラスト
        || n == l.タネマシンガン || n == l.つららばり || n == l.ミサイルばり
        || n == l.ボーンラッシュ || n == l.あわ || n == l.スイープビンタ
    {
        // random.choices([2,3,4,5], weights=[3,3,1,1]) の期待値 = 3.0
        return vec![(0, if skill_link { 5.0 } else { pick(3.0, 2.0, 5.0) })];
    }
    if n == l.ネズミざん {
        return vec![(0, if skill_link { 10.0 } else { pick(6.513, 1.0, 10.0) })];
    }
    vec![(0, 1.0)]
}

/// ai.py `_expected_hits`（威力換算。トリプルアクセルは 20/40/60 で1発目の6倍）
pub fn expected_hits(pack: &Pack, mv: &DMove, atk: &Poke) -> f64 {
    if pack.env_multi_hit && mv.name == pack.sy.l.トリプルアクセル {
        return 6.0;
    }
    hit_plan(pack, mv, atk, HitMode::Exp).iter().map(|x| x.1).sum()
}

/// ai.py `_move_damage`。1回の技使用の合計ダメージ見積もり（姿変化・連続技・へんげんじざい込み、命中率なし）。
/// 発ごとの威力は multi_hit_index で決まる（前回の技の値が残っているので必ず設定して戻す）。
#[allow(clippy::too_many_arguments)]
pub fn move_damage(
    pack: &Pack,
    atk: &mut Poke,
    def: &mut Poke,
    mv: &DMove,
    field: &mut Field,
    roll: f64,
    mode: HitMode,
    crit_mix: bool,
    rng: &mut dyn BRng,
) -> f64 {
    let blade_applied = if pack.env_blade_forme
        && mv.category != Cat::Status
        && atk.ability == pack.sy.l.バトルスイッチ
        && !atk.in_blade_forme
    {
        crate::battle::aegislash_to_blade_pub(pack, atk);
        true
    } else {
        false
    };
    let saved = atk.multi_hit_index;
    let pc = if crit_mix { crit_chance(pack, atk, mv, Some(def)) } else { 0.0 };
    let mut total = 0.0f64;
    for (hi, w) in hit_plan(pack, mv, atk, mode) {
        atk.multi_hit_index = hi;
        let mut d = {
            let mut f = dmg_rng(rng);
            calc_damage(pack, atk, def, mv, field, false, Some(roll), None, &mut f) as f64
        };
        if pc > 0.0 {
            let dc = {
                let mut f = dmg_rng(rng);
                calc_damage(pack, atk, def, mv, field, true, Some(roll), None, &mut f) as f64
            };
            d = d * (1.0 - pc) + dc * pc;
        }
        total += d * w;
    }
    atk.multi_hit_index = saved;
    let l = &pack.sy.l;
    if (atk.ability == l.へんげんじざい || atk.ability == pack.sy.ai.リベロ)
        && mv.ty != crate::pack::NO_TY
        && !atk.has_type(mv.ty)
    {
        total *= 1.5;
    }
    if blade_applied {
        crate::battle::revert_blade_pub(atk);
        // ai.py _pre_move_forms_ctx は見積もりの後に _shield_* を消す（正準状態では0）。同じにする
        atk.shield_atk = 0;
        atk.shield_def = 0;
        atk.shield_spatk = 0;
        atk.shield_spdef = 0;
    }
    total
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
    goes_first_pri(pack, me, opp, my_pri, field, opp_max)
}

/// 相手の最大優先度を外から与える版（本番経路は開示情報から推定した値を渡す）
fn goes_first_pri(
    pack: &Pack, me: &Poke, opp: &Poke, my_pri: i64, field: &Field, opp_max: i64,
) -> bool {
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
    move_damage(pack, atk, def, mv, field, 0.5, HitMode::Exp, false, rng) >= def.hp as f64
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
            let d = move_damage(pack, opp, me, mv, field, 1.0, HitMode::Max, false, rng);
            if d >= me.hp as f64 {
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

/// battle.py `forced_recharge_action`（反動ターンは交代も含めて行動を選べない。反動の技、無ければ先頭の技）
pub fn forced_recharge_action(me: &Poke) -> Option<Action> {
    if !me.recharge || !me.is_alive || me.moves.is_empty() {
        return None;
    }
    let i = me.moves.iter().position(|m| Some(m.name) == me.last_used_move).unwrap_or(0);
    Some(Action { kind: ActKind::Move, mv: Some(me.moves[i].clone()), move_idx: i as i64, switch_to: -1, do_mega: false })
}

/// ai.py `_forced_charging_action`（該当技が無ければ charging_move をクリアする＝副作用あり）
pub fn forced_charging_action(me: &mut Poke) -> Option<Action> {
    if let Some(a) = forced_recharge_action(me) {
        return Some(a);
    }
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
        // 縛られた技が使えないときはわるあがき（ai.py と同じ）。技自体を持っていない場合（決定化で入れ替わった等）は縛りなし扱い
        return if !locked.is_empty() || me.moves.iter().any(|m| m.name == lk) { locked } else { valid };
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
        // タイプなし（ゴーストにも当たる）・必中。ai.py `_get_struggle` と同じ
        ty: crate::pack::NO_TY,
        category: Cat::Physical,
        power: Some(50),
        accuracy: None,
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
    pub sr_pending: bool,
}

impl HazCtx {
    pub fn of(opp: &Side) -> HazCtx {
        HazCtx {
            remaining: opp.party.iter().filter(|p| p.is_alive).count(),
            field_idx: opp.field_idx,
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
        if opp.sr_pending || field.stealth_rock[oi] {
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
/// 事前分布のしきい値（ai.py `_ABIL_CERTAIN` / `_SASH_IGNORABLE` / `_MOVE_PRIOR_CERTAIN` と一致）
const ABIL_CERTAIN: f64 = 90.0;
const SASH_IGNORABLE: f64 = 10.0;
const MOVE_PRIOR_CERTAIN: f64 = 50.0;

/// my 側の観測（opp_view）と信念（belief）から、相手 op について読める特性/持ち物を返す。
/// 真値（op.ability / op.item）は読まない＝未開示情報のリークを作らない（REQUIREMENTS §4-1b）。
fn known_view(my: &mut Side, _pack: &Pack, op: &Poke) -> (Option<Sym>, Option<Sym>) {
    let k = my.opp_view.pokemon.iter().find(|k| k.name == op.name);
    (k.and_then(|k| k.known_ability), k.and_then(|k| k.known_item))
}

/// 相手種の事前分布を (特性, 持ち物, 技) で返す。信念が無ければ空。
fn priors_of(my: &mut Side, pack: &Pack, op: &Poke)
    -> (Vec<(String, f64)>, Vec<(String, f64)>, Vec<(String, f64)>) {
    let name = pack.intern.resolve(op.name).to_string();
    let mut bl = match my.belief.0.take() {
        None => return (Vec::new(), Vec::new(), Vec::new()),
        Some(b) => b,
    };
    let out = match bl.ensure(pack, &name, None, None) {
        Some(i) => {
            let pb = &bl.species[i].1;
            (pb.ability_prior.clone(), pb.item_prior.clone(), pb.move_prior.clone())
        }
        None => (Vec::new(), Vec::new(), Vec::new()),
    };
    my.belief.0 = Some(bl);
    out
}

/// ai.py `_survives_unknown`
/// Python は文字列で比較するので、こちらも intern.get() を挟まず文字列で揃える
/// （未 intern の名前が None に落ちると分岐が変わり Python と乖離する）。
fn survives_unknown(pack: &Pack, my: &mut Side, op: &Poke) -> bool {
    const SURVIVE: [&str; 3] = ["マルチスケイル", "ファントムガード", "がんじょう"];
    let (k_ab_sy, k_it_sy) = known_view(my, pack, op);
    let mut k_ab: Option<String> = k_ab_sy.map(|a| pack.intern.resolve(a).to_string());
    let k_it: Option<String> = k_it_sy.map(|i| pack.intern.resolve(i).to_string());
    let (ab_prior, it_prior, _) = priors_of(my, pack, op);
    if k_ab.is_none() {
        // Python の max() は同値なら「最初」を返す
        let top = ab_prior.iter().fold(None::<&(String, f64)>, |acc, x| match acc {
            Some(a) if a.1 >= x.1 => Some(a),
            _ => Some(x),
        });
        if let Some((n, r)) = top {
            if *r >= ABIL_CERTAIN {
                k_ab = Some(n.clone());
            }
        }
    }
    match &k_ab {
        Some(a) => {
            if SURVIVE.contains(&a.as_str()) {
                return true;
            }
        }
        None => {
            if ab_prior
                .iter()
                .any(|(n, r)| *r > 0.0 && SURVIVE.contains(&n.as_str()))
            {
                return true;
            }
        }
    }
    if k_it.as_deref() == Some("きあいのタスキ") {
        return true;
    }
    if k_it.is_none() {
        if it_prior.is_empty() {
            return true;
        }
        let sash = it_prior
            .iter()
            .find(|(n, _)| n == "きあいのタスキ")
            .map_or(0.0, |(_, r)| *r);
        if sash >= SASH_IGNORABLE {
            return true;
        }
    }
    false
}

/// ai.py `_disguise_intact`
fn disguise_intact(pack: &Pack, my: &mut Side, op: &Poke) -> bool {
    if op.disguise_broken {
        return false;
    }
    let (ab_prior, _, _) = priors_of(my, pack, op);
    if ab_prior.is_empty() {
        return false;
    }
    ab_prior
        .iter()
        .find(|(n, _)| n == "ばけのかわ")
        .map_or(false, |(_, r)| *r >= ABIL_CERTAIN)
}

/// ai.py `_opp_max_priority`（開示技＋使用率50%以上の技だけから推定）
fn opp_max_priority_known(pack: &Pack, my: &mut Side, op: &Poke) -> i64 {
    let mut known: Vec<Sym> = my
        .opp_view
        .pokemon
        .iter()
        .find(|k| k.name == op.name)
        .map(|k| k.known_moves.clone())
        .unwrap_or_default();
    let (_, _, mv_prior) = priors_of(my, pack, op);
    let mut known_s: Vec<String> =
        known.iter().map(|s| pack.intern.resolve(*s).to_string()).collect();
    for (n, r) in &mv_prior {
        if *r >= MOVE_PRIOR_CERTAIN {
            known_s.push(n.clone());
        }
    }
    op.moves
        .iter()
        .filter(|m| known_s.iter().any(|k| k == pack.intern.resolve(m.name)))
        .map(|m| m.priority)
        .max()
        .unwrap_or(0)
}

/// AI_KO_COND=0 で成功条件の確認を外す（A/B 用。既定 ON）
pub fn ko_cond_env() -> bool {
    std::env::var("AI_KO_COND").map(|v| v != "0").unwrap_or(true)
}

/// 監査40の AI 修正の既定（AI_FIX40=0 で旧挙動。ai.py / search_ai.py の _FIX40_ON と同じ）
pub fn fix40_env() -> bool {
    std::env::var("AI_FIX40").map(|v| v != "0").unwrap_or(true)
}

/// 監査200 C の AI 修正の既定（AI_FIX200=0 で旧挙動。search_ai.py の _FIX200_ON と同じ）
pub fn fix200_env() -> bool {
    std::env::var("AI_FIX200").map(|v| v != "0").unwrap_or(true)
}

/// 設置済み（上限まで）の設置技を外す AI 修正の既定（AI_FIXHZ=0 で旧挙動。search_ai.py の _FIXHZ_ON と同じ）
pub fn fixhz_env() -> bool {
    std::env::var("AI_FIXHZ").map(|v| v != "0").unwrap_or(true)
}

/// ai.py `_ko_hit_prob`: 確定KOの安全弁で使う命中率（公開情報）
fn ko_hit_prob(pack: &Pack, me: &Poke, op: &Poke, mv: &DMove, field: &Field) -> f64 {
    let acc = match mv.accuracy {
        None => return 1.0,
        Some(a) => a,
    };
    if me.lock_on || op.defenseless {
        return 1.0;
    }
    let s = &pack.sy;
    if me.ability == s.ab.ノーガード || op.ability == s.ab.ノーガード {
        return 1.0;
    }
    let w = crate::damage::effective_weather(pack, field, Some(me));
    let thunder = mv.name == s.mv.かみなり || mv.name == s.mv.ぼうふう;
    if (thunder && w == Some(s.we.rain)) || (mv.name == s.mv.ふぶき && w == Some(s.we.hail)) {
        return 1.0;
    }
    let l = &s.l;
    if mv.name == l.じわれ || mv.name == l.ぜったいれいど || mv.name == l.つのドリル || mv.name == l.ハサミギロチン {
        return if mv.name == l.ぜったいれいど && !me.has_type(pack.tc.こおり) { 0.20 } else { 0.30 };
    }
    let eva = if me.ability == s.ab.するどいめ || me.ability == s.ab.はっこう { 0 } else { op.stage_evasion };
    let mut p = (acc as f64) * crate::poke::acc_eva_stage(me.stage_accuracy - eva) / 100.0;
    if thunder && w == Some(s.we.sunny) {
        p = 0.5;
    }
    if me.ability == s.ab.ふくがん {
        p *= 1.3;
    }
    if me.ability == s.ab.はりきり && mv.category == Cat::Physical {
        p *= 0.8;
    }
    p *= crate::damage::get_evasion_item_mult(pack, op.item) * crate::damage::get_accuracy_evasion_item(pack, me.item);
    p.min(1.0)
}

pub fn certain_ko_override(
    pack: &Pack,
    act: Action,
    my: &mut Side,
    opp: &mut Side,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> Action {
    certain_ko_override_opt(pack, act, my, opp, field, rng, true, ko_cond_env(), fix40_env())
}

/// ai.py `_ko_move_fails`: 成功条件のある攻撃技で、確定KOの前提（撃てば当たる）が成り立たないか。
/// 相手の行動しだいで失敗する技（ふいうち・はやてがえし）と、威力が後で入る技（みらいよち）は常に除く。
fn ko_move_fails(pack: &Pack, me: &Poke, op: &Poke, mv: &DMove, field: &Field, fix40: bool) -> bool {
    let l = &pack.sy.l;
    let n = mv.name;
    if (n == l.ねこだまし || n == l.であいがしら) && me.turns_out > 0 {
        return true;
    }
    if fix40
        && ((n == l.でんこうそうげき && !me.has_type(pack.tc.でんき)) || (n == l.もえつきる && !me.has_type(pack.tc.ほのお)))
    {
        return true;
    }
    if n == l.ふいうち || n == l.はやてがえし || n == l.みらいよち {
        return true;
    }
    if n == l.ポルターガイスト && op.item.is_none() {
        return true;
    }
    if n == l.とっておき {
        let others: Vec<_> = me.moves.iter().map(|m| m.name).filter(|&x| x != l.とっておき).collect();
        if others.is_empty() || !others.iter().all(|x| me.used_moves.contains(x)) {
            return true;
        }
    }
    if n == l.アイアンローラー
        && !(field.grassy_terrain || field.electric_terrain || field.psychic_terrain || field.misty_terrain)
    {
        return true;
    }
    if field.psychic_terrain && mv.priority > 0 {
        let grounded = !(op.has_type(pack.tc.ひこう)
            || op.ability == l.ふゆう
            || op.magnet_rise
            || op.item == Some(pack.sy.it.ふうせん))
            || op.grounded;
        if grounded {
            return true;
        }
    }
    false
}

/// precise=false は 2026-09-28 以前の判定（姿変化・連続技なしの1発・A/B 用。env AI_KO_PRECISE=0）
/// cond=false は 2026-10-04 以前の判定（成功条件のある技も候補にする・A/B 用。env AI_KO_COND=0）
pub fn certain_ko_override_opt(
    pack: &Pack,
    act: Action,
    my: &mut Side,
    opp: &mut Side,
    field: &mut Field,
    rng: &mut dyn BRng,
    precise: bool,
    cond: bool,
    fix40: bool,
) -> Action {
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
    // 耐える系の判定は相手の真値ではなく opp_view（開示済み）＋使用率事前分布で行う。
    // 真値を読むと未開示のタスキ等を常に知っていることになり情報リーク（REQUIREMENTS §4-1b）。
    {
        let op = opp.party[oi].clone();
        let full = op.hp == op.max_hp;
        if full && survives_unknown(pack, my, &op) {
            return act;
        }
        // ばけのかわは満タンかどうかに関係なく1発目のダメージを無効化する（battle.rs:1294）ので、
        // 未破壊のうちは確定KOが成立しない。破壊済みかは実機で見える。
        if disguise_intact(pack, my, &op) {
            return act;
        }
    }
    let opp_pri = {
        let op = opp.party[oi].clone();
        opp_max_priority_known(pack, my, &op)
    };
    let me = &mut my.party[mi];
    let op = &mut opp.party[oi];
    let valid = filter_by_pp(&filter_valid_by_lock(me), me);
    let mut best: Option<(usize, DMove)> = None;
    let mut bestd = -1.0f64;
    let mut bestp = -1.0f64;
    let mut probs: Vec<(crate::interner::Sym, f64)> = Vec::new();
    for (i, mv) in &valid {
        if mv.power.unwrap_or(0) == 0 || mv.category == Cat::Status {
            continue;
        }
        if pack.eff(mv.ty, op.type1, op.type2) == 0.0 {
            continue;
        }
        if cond && ko_move_fails(pack, me, op, mv, field, fix40) {
            continue;
        }
        if !goes_first_pri(pack, me, op, mv.priority, field, opp_pri) {
            continue;
        }
        // 正規化ロール。最低ロールは 0.0（0.85 は実効 0.85+0.85*0.15=0.9775 ＝ほぼ最高値で、
        // 確定でないKOを確定と誤認する。実測: 介入の15.3%が該当）。
        // 姿変化（バトルスイッチ）と連続技の「必ず当たる回数」込み（ai.py _move_damage と同一）
        let (sm, so) = (crate::damage::EstSnap::take(me), crate::damage::EstSnap::take(op));
        let d = if precise {
            move_damage(pack, me, op, mv, field, 0.0, HitMode::Min, false, rng)
        } else {
            let mut f = dmg_rng(rng);
            calc_damage(pack, me, op, mv, field, false, Some(0.0), None, &mut f) as f64
        };
        sm.restore(me);
        so.restore(op);
        if d >= op.hp as f64 {
            let p = if fix40 { ko_hit_prob(pack, me, op, mv, field) } else { 1.0 };
            probs.push((mv.name, p));
            if p > bestp || (p == bestp && d > bestd) {
                bestp = p;
                bestd = d;
                best = Some((*i, mv.clone()));
            }
        }
    }
    let (bi, bmv) = match best {
        None => return act,
        Some(x) => x,
    };
    if act.kind == ActKind::Move && act.mv.as_ref().map(|m| m.name) == Some(bmv.name) {
        return act;
    }
    // 命中が確実でない技で上書きするのは、選んだ手が命中率の低い確定KO技だったときだけ（ai.py と同じ）
    if fix40 && bestp < 1.0 {
        let ap = if act.kind == ActKind::Move {
            act.mv.as_ref().and_then(|m| probs.iter().find(|(n, _)| *n == m.name).map(|x| x.1))
        } else {
            None
        };
        match ap {
            Some(a) if a < bestp => {}
            _ => return act,
        }
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
/// 呼び出し側のポケモンを壊さないための包み（Python: ai.select_party と同じ方針）。
/// 採点は expected_damage→calc_damage を通るので、半減きのみの消費（defender.item=None）・
/// かるわざ・溜め解除が「渡した個体そのもの」に残る。mcts_vs_dist は select_party の後に
/// `b6[i].clone()` で側2のパーティを作るため、消費済みの状態がそのまま対戦に入っていた。
/// 採点前を保存し、返す直前に必ず巻き戻す。
#[allow(clippy::too_many_arguments)]
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
    select_party_multi(pack, party6, opp6, n, &[temperature], mega_penalty, rng, srng).remove(0)
}

/// ai.py `select_party_multi`: select_party を温度の列の順に続けて呼んだのと同じ結果（採点は1回。rng＝採点のダメージ計算、
/// srng＝温度つきの抽選）
#[allow(clippy::too_many_arguments)]
pub fn select_party_multi(
    pack: &Pack,
    party6: &mut Vec<Poke>,
    opp6: &mut Vec<Poke>,
    n: usize,
    temperatures: &[f64],
    mega_penalty: f64,
    rng: &mut dyn BRng,
    srng: &mut dyn FnMut() -> f64,
) -> Vec<Vec<usize>> {
    let snap_p = party6.clone();
    let snap_o = opp6.clone();
    let out =
        select_party_inner(pack, party6, opp6, n, temperatures, mega_penalty, rng, srng);
    *party6 = snap_p;
    *opp6 = snap_o;
    out
}

/// select_party_multi と同じ結果を、1対面の最大期待ダメージ（best_expected_damage）を表から引いて計算する
/// （学習選出の高速版が、同じ2パーティの選出2回で表を共有する）。採点の副作用は「受け手の半減きのみ等の消費」だけを状態として追う。
/// 呼び出し側の条件: 全員無傷・能力ランク0・乱数を引く技なし・消費される持ち物とかるわざの組なし。
/// bed(攻め手がパーティ側か, 攻め手の添字, 攻め手がメガ後か, 攻め手の持ち物が消費済みか, 受け手の添字, 受け手がメガ後か, 受け手の持ち物が消費済みか)
/// → (値, 受け手の持ち物を消費したか)。bed が None（乱数を引いた等）なら None（srng は未消費。呼び出し側は元の実装へ）
#[allow(clippy::too_many_arguments, clippy::type_complexity)]
pub fn select_party_multi_tab(
    pack: &Pack,
    party6: &[Poke],
    opp6: &[Poke],
    n: usize,
    temperatures: &[f64],
    mega_penalty: f64,
    srng: &mut dyn FnMut() -> f64,
    bed: &mut dyn FnMut(bool, usize, bool, bool, usize, bool, bool) -> Option<(f64, bool)>,
) -> Option<Vec<Vec<usize>>> {
    if party6.len() <= n {
        return None;
    }
    let field = Field::default();
    let mut oc = vec![false; opp6.len()];
    let ospd: Vec<i64> = opp6.iter().map(|o| effective_speed(pack, o, &field)).collect();
    let mut score = |i: usize, mega: bool, oc: &mut Vec<bool>| -> Option<f64> {
        let pm;
        let p: &Poke = if mega {
            let mut q = party6[i].clone();
            mega_evolve_poke(pack, &mut q);
            pm = q;
            &pm
        } else {
            &party6[i]
        };
        let my_hp = f64::max(1.0, p.max_hp as f64);
        let my_spd = effective_speed(pack, p, &field);
        let mut pc = false;
        let mut val = 0.0f64;
        for oi in 0..opp6.len() {
            let opp_hp = f64::max(1.0, opp6[oi].max_hp as f64);
            let (my_best, c1) = bed(true, i, mega, pc, oi, false, oc[oi])?;
            if c1 {
                oc[oi] = true;
            }
            let (opp_best, c2) = bed(false, oi, false, oc[oi], i, mega, pc)?;
            if c2 {
                pc = true;
            }
            let faster = my_spd >= ospd[oi];
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
        Some(val)
    };
    let is_cap = |p: &Poke| p.mega.is_some() && !p.mega_evolved;
    let mut mbest: Option<usize> = None;
    let mut bv = f64::NEG_INFINITY;
    for (k, i) in (0..party6.len()).filter(|&i| is_cap(&party6[i])).enumerate() {
        let v = score(i, true, &mut oc)?;
        if k == 0 || v > bv {
            bv = v;
            mbest = Some(i);
        }
    }
    let mut scores = Vec::with_capacity(party6.len());
    for i in 0..party6.len() {
        let v = if Some(i) == mbest {
            score(i, true, &mut oc)?
        } else {
            let v = score(i, false, &mut oc)?;
            if is_cap(&party6[i]) {
                v - mega_penalty
            } else {
                v
            }
        };
        scores.push(v);
    }
    let mut p6 = party6.to_vec();
    let mut o6 = opp6.to_vec();
    Some(temperatures.iter().map(|&t| choose_by_scores(pack, &mut p6, &mut o6, &scores, n, t, srng)).collect())
}

#[allow(clippy::too_many_arguments)]
fn select_party_inner(
    pack: &Pack,
    party6: &mut Vec<Poke>,
    opp6: &mut Vec<Poke>,
    n: usize,
    temperatures: &[f64],
    mega_penalty: f64,
    rng: &mut dyn BRng,
    srng: &mut dyn FnMut() -> f64,
) -> Vec<Vec<usize>> {
    let mut dummy = Field::default();
    if party6.len() <= n {
        let mut out = Vec::new();
        for &temperature in temperatures {
            let mut idx: Vec<usize> = (0..party6.len()).collect();
            let pool = party6.clone();
            let opp = opp6.clone();
            order_by_lead(pack, &mut idx, &pool, &opp, temperature, srng);
            out.push(idx);
        }
        return out;
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

    let scores: Vec<f64> = (0..party6.len()).map(|i| eff_score(i, party6, opp6)).collect();
    temperatures.iter().map(|&t| choose_by_scores(pack, party6, opp6, &scores, n, t, srng)).collect()
}

/// ai.py `_choose_by_scores`
fn choose_by_scores(
    pack: &Pack,
    party6: &mut Vec<Poke>,
    opp6: &mut Vec<Poke>,
    scores: &[f64],
    n: usize,
    temperature: f64,
    srng: &mut dyn FnMut() -> f64,
) -> Vec<usize> {
    if temperature > 0.0 {
        let mut idx = temp_sample_indices(scores, n, temperature, srng);
        let pool = party6.clone();
        let opp = opp6.clone();
        order_by_lead(pack, &mut idx, &pool, &opp, temperature, srng);
        return idx;
    }
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

#[cfg(test)]
mod tests {
    use super::*;
    use crate::poke::build_poke;

    fn pack() -> Pack {
        Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"))
    }

    struct Z;
    impl BRng for Z {
        fn random(&mut self) -> f64 { 0.0 }
        fn choice(&mut self, _n: usize) -> usize { 0 }
        fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
        fn choices(&mut self) -> i64 { 2 }
    }

    /// test_all.py 26e と同じ: トリプルアクセルは発ごとの威力で合計し、残っている発数に左右されない。
    #[test]
    fn トリプルアクセルの見積もり() {
        let mut p = pack();
        let mut a = build_poke(&mut p, "マニューラ@いのちのたま:ようき:トリプルアクセル|はたきおとす|ねこだまし|つららおとし:0/32/0/0/0/32:プレッシャー", "M-6");
        let mut d = build_poke(&mut p, "ガブリアス@こだわりスカーフ:ようき:じしん|ドラゴンクロー|スケイルショット|つるぎのまい:0/32/0/0/0/32:さめはだ", "M-6");
        let pr: &Pack = &p;
        let mv = a.moves.iter().find(|m| pr.intern.resolve(m.name) == "トリプルアクセル").unwrap().clone();
        let mut f = Field::default();
        let mut r = Z;
        let pc = crit_chance(pr, &a, &mv, Some(&d));
        let mut want = 0.0;
        for i in 0..3 {
            a.multi_hit_index = i;
            let nc = calc_damage(pr, &mut a, &mut d, &mv, &mut f, false, Some(0.5), None, &mut |_| 0.0) as f64;
            let c = calc_damage(pr, &mut a, &mut d, &mv, &mut f, true, Some(0.5), None, &mut |_| 0.0) as f64;
            want += nc * (1.0 - pc) + c * pc;
        }
        want *= mv.accuracy.unwrap_or(100) as f64 / 100.0;
        a.multi_hit_index = 2;
        let got = expected_damage(pr, &mut a, &mut d, &mv, &mut f, &mut r);
        assert!((got - want).abs() < 1e-6, "got={got} want={want}");
        assert_eq!(a.multi_hit_index, 2, "発数は元に戻す");
        assert!((expected_hits(pr, &mv, &a) - 6.0).abs() < 1e-9);
    }

    /// 確定KOは連続技(2〜5発)を必ず当たる2発で判定する（test_all.py 26e と同じ）。
    #[test]
    fn 確定ko_連続技は2発で判定() {
        let mut p = pack();
        let g = build_poke(&mut p, "ガブリアス@こだわりスカーフ:ようき:スケイルショット|ステルスロック|つるぎのまい|まもる:0/32/0/0/0/32:さめはだ", "M-6");
        let s = build_poke(&mut p, "ヤドラン@ゴツゴツメット:ずぶとい:ねっとう|なまける|でんじは|トリック:32/0/32/0/0/0:さいせいりょく", "M-6");
        let pr: &Pack = &p;
        let mut my = Side { party: vec![g], active_idx: 0, ..Default::default() };
        let mut op = Side { party: vec![s], active_idx: 0, ..Default::default() };
        let mut f = Field::default();
        let mut r = Z;
        let mv = my.party[0].moves[0].clone();
        let one = {
            let (a, d) = (&mut my.party[0], &mut op.party[0]);
            calc_damage(pr, a, d, &mv, &mut f, false, Some(0.0), None, &mut |_| 0.0)
        };
        let st = Action { kind: ActKind::Move, mv: Some(my.party[0].moves[3].clone()), move_idx: 3, switch_to: -1, do_mega: false };
        op.party[0].hp = 2 * one;
        // 命中90の技なので、回数の判定だけを見るため命中の条件（監査40 #3）は外す
        let a = certain_ko_override_opt(pr, st.clone(), &mut my, &mut op, &mut f, &mut r, true, true, false);
        assert_eq!(a.move_idx, 0, "2発ぶんのHPなら確定");
        op.party[0].hp = 2 * one + 1;
        let a = certain_ko_override_opt(pr, st, &mut my, &mut op, &mut f, &mut r, true, true, false);
        assert_eq!(a.move_idx, 3, "3発目以降は当てにしない");
    }

    /// わるあがきはタイプなし・必中（ai.py `_get_struggle` と同じ。test_all.py 26g）。
    #[test]
    fn わるあがきはタイプなし() {
        let mut p = pack();
        let mut ind = build_poke(&mut p, "イエッサン(オス)@こだわりスカーフ:おくびょう:ワイドフォース|サイコキネシス|マジカルシャイン|トリック:0/0/0/32/0/32:サイコメイカー", "M-6");
        let mut gil = build_poke(&mut p, "ギルガルド@たべのこし:れいせい:シャドーボール|ラスターカノン|キングシールド|かげうち:32/0/2/32/0/0:バトルスイッチ", "M-6");
        let mut mas = build_poke(&mut p, "マスカーニャ@こだわりスカーフ:ようき:トリックフラワー|はたきおとす|とんぼがえり|トリプルアクセル:0/32/0/0/0/32:へんげんじざい", "M-6");
        let pr: &Pack = &p;
        let st = struggle(pr);
        assert!(st.ty == crate::pack::NO_TY && st.accuracy.is_none());
        let mut f = Field::default();
        let d = calc_damage(pr, &mut ind, &mut gil, &st, &mut f, false, Some(0.5), None, &mut |_| 0.0);
        assert!(d > 0, "ゴーストにも当たる");
        let t0 = mas.type1;
        crate::battle::apply_pre_move_forms(pr, &mut mas, &st);
        assert!(mas.type1 == t0 && !mas.protean_used, "へんげんじざいでタイプが変わらない");
    }

    /// 確定KOは成功条件のある技を、条件を満たさない局面で候補にしない（test_all.py 37 と同じ）
    #[test]
    fn 確定ko_初回だけの技と条件付きの技() {
        let mut p = pack();
        let gu = build_poke(&mut p, "グソクムシャ@きれいなぬけがら:いじっぱり:であいがしら|きゅうけつ|ふいうち|ねこだまし:32/32/0/0/0/0:ききかいひ", "M-6");
        let g = build_poke(&mut p, "ガブリアス@きれいなぬけがら:ようき:じしん:0/32/0/0/0/32:さめはだ", "M-6");
        let pr: &Pack = &p;
        let mut my = Side { party: vec![gu], active_idx: 0, ..Default::default() };
        let mut op = Side { party: vec![g], active_idx: 0, ..Default::default() };
        let mut f = Field::default();
        let mut r = Z;
        op.party[0].hp = 1;
        let st = Action { kind: ActKind::Move, mv: Some(my.party[0].moves[1].clone()), move_idx: 1, switch_to: -1, do_mega: false };
        let a = certain_ko_override_opt(pr, st.clone(), &mut my, &mut op, &mut f, &mut r, true, true, true);
        assert_eq!(a.move_idx, 0, "登場ターンは であいがしら");
        my.party[0].turns_out = 1;
        let a = certain_ko_override_opt(pr, st.clone(), &mut my, &mut op, &mut f, &mut r, true, true, true);
        assert_eq!(a.move_idx, 1, "2ターン目以降は であいがしら/ねこだまし/ふいうち を当てにしない");
        let a = certain_ko_override_opt(pr, st, &mut my, &mut op, &mut f, &mut r, true, false, true);
        assert_ne!(a.move_idx, 1, "旧判定（A/B 用）は上書きしていた");
    }

    /// 確定KOの見積もりで半減きのみを消費しない（実際の攻撃でだけ消費）
    #[test]
    fn 確定ko_見積もりで半減きのみを消費しない() {
        let mut p = pack();
        let g = build_poke(&mut p, "ガブリアス@きれいなぬけがら:ようき:じしん|つるぎのまい:0/32/0/0/0/32:さめはだ", "M-6");
        let e = build_poke(&mut p, "エンペルト@シュカのみ:ひかえめ:なみのり:32/0/0/32/0/0:げきりゅう", "M-6");
        let pr: &Pack = &p;
        let mut my = Side { party: vec![g], active_idx: 0, ..Default::default() };
        let mut op = Side { party: vec![e], active_idx: 0, ..Default::default() };
        let mut f = Field::default();
        let mut r = Z;
        op.party[0].hp = 10;
        let st = Action { kind: ActKind::Move, mv: Some(my.party[0].moves[1].clone()), move_idx: 1, switch_to: -1, do_mega: false };
        let a = certain_ko_override(pr, st, &mut my, &mut op, &mut f, &mut r);
        assert_eq!(a.move_idx, 0);
        assert_eq!(op.party[0].item, pr.intern.get("シュカのみ"), "シュカのみが残る");
    }

    /// Zメガ石もメガストーン（battle.py _is_megastone と同じ）
    #[test]
    fn zメガ石はメガストーン() {
        let p = pack();
        for (n, want) in [("ガブリアスナイトZ", true), ("アブソルナイトＺ", true), ("ボーマンダナイト", true),
                          ("いのちのたま", false)] {
            let sy = p.intern.get(n);
            assert_eq!(crate::battle::is_megastone(&p, sy), want && sy.is_some(), "{n}");
        }
    }
}
