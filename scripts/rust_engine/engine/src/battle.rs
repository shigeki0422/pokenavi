//! simulator/battle.py の移植。ログ文字列は生成しない（パリティ対象は状態のみ）。
//! Python の分岐順・early return をそのまま写す。
#![allow(clippy::too_many_arguments)]
use crate::abilities as ab;
use crate::damage::{
    calc_damage, check_hit, effective_move_type, effective_weather, is_contact_move, DMove, Field,
};
use crate::items as it;
use crate::oppview::OppView;
use crate::pack::{Cat, Pack, Ty};
use crate::poke::{apply_status, calc_stat, mega_evolve_poke, Poke};
use crate::rng::BRng;

pub const MAX_TURNS: i64 = 30;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum ActKind {
    Move,
    Switch,
    Mega,
    Pass,
}

#[derive(Clone, Debug)]
pub struct Action {
    pub kind: ActKind,
    pub mv: Option<DMove>,
    pub move_idx: i64,
    pub switch_to: i64,
    pub do_mega: bool,
}

impl Default for Action {
    fn default() -> Self {
        Action { kind: ActKind::Pass, mv: None, move_idx: 0, switch_to: -1, do_mega: false }
    }
}

/// belief は「対戦状態」ではなく意思決定者の知識。Python の
/// `OpponentBelief.__deepcopy__ -> None` / `Battle.clone()` / `_fast_clone_state` と同じく、
/// 複製時は必ず None になる（clone は探索用の複製にしか使わない）。
#[derive(Debug, Default)]
pub struct BeliefSlot(pub Option<Box<crate::belief::OpponentBelief>>);

impl Clone for BeliefSlot {
    fn clone(&self) -> Self {
        BeliefSlot(None)
    }
}

#[derive(Clone, Debug, Default)]
pub struct Side {
    pub belief: BeliefSlot,
    pub party: Vec<Poke>,
    /// 見せ合いで公開する6体ソース（隠れ選出のリサンプルで種名のみ使う）
    pub source6_names: Vec<crate::interner::Sym>,
    pub active_idx: usize,
    pub stealth_rock_set: bool,
    pub mega_used: bool,
    pub opp_view: OppView,
    pub field_idx: usize,
    pub reflect: bool,
    pub reflect_count: i64,
    pub light_screen: bool,
    pub light_screen_count: i64,
    pub aurora_veil: bool,
    pub aurora_veil_count: i64,
    pub tailwind: bool,
    pub tailwind_count: i64,
    pub wish_hp: i64,
    pub wish_count: i64,
    pub healing_wish: bool,
    pub safeguard: i64,
    pub future_sight_count: i64,
    pub future_sight_dmg: i64,
    pub future_sight_name: Option<u16>,
    pub sr_pending: bool,
    pub entry_pending: bool,
}

impl Side {
    #[inline]
    pub fn active(&self) -> &Poke {
        &self.party[self.active_idx]
    }
    #[inline]
    pub fn active_mut(&mut self) -> &mut Poke {
        let i = self.active_idx;
        &mut self.party[i]
    }
    pub fn has_alive(&self) -> bool {
        self.party.iter().any(|p| p.is_alive)
    }
    /// BattleSide.switch_to
    pub fn switch_to(&mut self, pack: &Pack, idx: usize) {
        let pi = self.active_idx;
        {
            let prev = &mut self.party[pi];
            ab::on_switch_out(pack, prev);
            if prev.transformed {
                if let Some(b) = prev.transform_backup.take() {
                    prev.attack = b.attack;
                    prev.defense = b.defense;
                    prev.sp_attack = b.sp_attack;
                    prev.sp_defense = b.sp_defense;
                    prev.speed = b.speed;
                    prev.ability = b.ability;
                    prev.moves = b.moves;
                    prev.pp = b.pp;
                }
                prev.transformed = false;
                prev.transform_backup = None;
            }
            prev.illusion_name = None;
            prev.stage_attack = 0;
            prev.stage_defense = 0;
            prev.stage_sp_attack = 0;
            prev.stage_sp_defense = 0;
            prev.stage_speed = 0;
            prev.stage_accuracy = 0;
            prev.stage_evasion = 0;
            prev.type1 = prev.base_type1;
            prev.type2 = prev.base_type2;
            prev.confused = false;
            prev.yawn_count = 0;
            prev.flinched = false;
            prev.protecting = false;
            prev.enduring = false;
            prev.grounded = false;
            prev.used_moves.clear();
            prev.ate_berry = false;
            prev.protect_consecutive = 0;
            prev.locked_move = None;
            prev.choice_locked_move = None;
            prev.disabled_move = None;
            prev.disabled_turns = 0;
            prev.lock_count = 0;
            prev.charging_move = None;
            prev.bound_count = 0;
            prev.throat_chop_count = 0;
            prev.substitute_hp = 0;
            prev.electromorphosis_charged = false;
            prev.gyaku_triggered = false;
            prev.protean_used = false;
            prev.barrier_done = false;
            prev.info_done = false;
            prev.recharge = false;
            prev.crit_stage = 0;
            prev.perish_count = 0;
            prev.destiny_bond = false;
            prev.cursed = false;
            prev.charged = false;
        }
        self.active_idx = idx;
        let baton = self.party[pi].baton_stages;
        if let Some(bs) = baton {
            for i in 0..7u8 {
                let v = bs[i as usize];
                self.party[idx].set_stage(i, v.clamp(-6, 6));
            }
            self.party[pi].baton_stages = None;
        }
        let fainted = self.party.iter().filter(|p| !p.is_alive).count() as i64;
        let a = &mut self.party[idx];
        a.turns_out = 0;
        a.times_hit = 0;
        a.switched_this_turn = true;
        a.fainted_allies = fainted;
    }
    pub fn next_alive_idx(&self) -> Option<usize> {
        self.party.iter().enumerate().find(|(i, p)| p.is_alive && *i != self.active_idx).map(|(i, _)| i)
    }
}

#[derive(Clone, Debug, Default)]
pub struct Battle {
    pub sides: [Side; 2],
    pub field: Field,
    pub turn: i64,
}

#[inline]
pub fn split2(sides: &mut [Side; 2], first: usize) -> (&mut Side, &mut Side) {
    let (a, b) = sides.split_at_mut(1);
    if first == 0 {
        (&mut a[0], &mut b[0])
    } else {
        (&mut b[0], &mut a[0])
    }
}

pub fn is_megastone(pack: &Pack, item: Option<u16>) -> bool {
    match item {
        None => false,
        Some(i) => {
            let s = pack.intern.resolve(i);
            s.ends_with("ナイト")
                || s.ends_with("ナイトＸ")
                || s.ends_with("ナイトＹ")
                || s.ends_with("ナイトX")
                || s.ends_with("ナイトY")
        }
    }
}

#[inline]
fn is_berry(pack: &Pack, item: Option<u16>) -> bool {
    matches!(item, Some(i) if pack.intern.resolve(i).ends_with("のみ"))
}

// ── おうごんのからだ が無効化する変化技 ────────────────────────────────────
fn gag_block(pack: &Pack, n: u16) -> bool {
    let l = &pack.sy.l;
    n == l.でんじは
        || n == l.おにび
        || n == l.どくどく
        || n == l.どくのこな
        || n == l.しびれごな
        || n == l.ねむりごな
        || n == l.キノコのほうし
        || n == l.さいみんじゅつ
        || n == l.あくび
        || n == l.へびにらみ
        || n == l.ちょうおんぱ
        || n == l.あやしいひかり
        || n == l.いばる
        || n == l.おだてる
        || n == l.ちょうはつ
        || n == l.アンコール
        || n == l.かなしばり
        || n == l.いちゃもん
        || n == l.やどりぎのタネ
        || n == l.メロメロ
        || n == l.くろいまなざし
        || n == l.なきごえ
        || n == l.にらみつける
        || n == l.あまえる
        || n == l.すなかけ
        || n == l.フラッシュ
        || n == l.あまいかおり
        || n == l.うそなき
        || n == l.ひっくりかえす
        || n == l.ワンダールーム
        || n == l.トリック
        || n == l.すりかえ
        || n == l.なかよくする
        || n == l.このゆびとまれ
        || n == l.とおせんぼう
        || n == l.くすぐる
        || n == l.テクスチャー2
}

// ── 行動優先度 ────────────────────────────────────────────────────────────
pub fn priority(pack: &Pack, action: &Action, poke: &Poke, field: &Field, rng: &mut dyn BRng) -> i64 {
    let l = &pack.sy.l;
    match action.kind {
        ActKind::Switch => return 6,
        ActKind::Mega => return 7,
        _ => {}
    }
    let mv = match &action.mv {
        None => return 0,
        Some(m) => m,
    };
    let mut base = mv.priority;
    if mv.name == l.グラススライダー && field.grassy_terrain {
        if !(poke.ability == l.ふゆう || poke.has_type(pack.tc.ひこう) || poke.magnet_rise) {
            base += 1;
        }
    }
    if poke.ability == l.はやてのつばさ && mv.ty == pack.tc.ひこう && poke.hp == poke.max_hp {
        base += 1;
    }
    if poke.ability == l.いたずらごころ && mv.category == Cat::Status {
        base += 1;
    }
    if it::has_quick_claw_trigger(pack, poke.item, rng) {
        base += 1;
    }
    base
}

/// _speed_order: true なら side1（sides[0] 相当の第1引数）が先攻
pub fn speed_order(
    pack: &Pack,
    s1: &Side,
    a1: &Action,
    s2: &Side,
    a2: &Action,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> bool {
    let l = &pack.sy.l;
    let we = &pack.sy.we;
    let p1 = s1.active();
    let p2 = s2.active();
    let pri1 = priority(pack, a1, p1, field, rng);
    let pri2 = priority(pack, a2, p2, field, rng);
    if pri1 != pri2 {
        return pri1 > pri2;
    }
    let stall1 = p1.ability == l.あとだし;
    let stall2 = p2.ability == l.あとだし;
    if stall1 != stall2 {
        return stall2;
    }
    let qd1 = p1.ability == l.クイックドロウ && rng.random() < 0.30;
    let qd2 = p2.ability == l.クイックドロウ && rng.random() < 0.30;
    if qd1 && !qd2 {
        return true;
    }
    if qd2 && !qd1 {
        return false;
    }

    let mut spd1 = p1.eff_speed(pack);
    let mut spd2 = p2.eff_speed(pack);

    field.weather_negated = p1.ability == l.ノーてんき || p2.ability == l.ノーてんき;
    let w1 = effective_weather(pack, field, Some(p1));
    let w2 = effective_weather(pack, field, Some(p2));

    let m1 = if p1.ability != l.ぶきよう { it::get_speed_item_multiplier(pack, p1.item) } else { 1.0 };
    let m2 = if p2.ability != l.ぶきよう { it::get_speed_item_multiplier(pack, p2.item) } else { 1.0 };
    spd1 = ((spd1 as f64) * m1).floor() as i64;
    spd2 = ((spd2 as f64) * m2).floor() as i64;

    if s1.tailwind {
        spd1 *= 2;
    }
    if s2.tailwind {
        spd2 *= 2;
    }
    if w1 == Some(we.rain) && p1.ability == l.すいすい {
        spd1 *= 2;
    }
    if w2 == Some(we.rain) && p2.ability == l.すいすい {
        spd2 *= 2;
    }
    if w1 == Some(we.sunny) && p1.ability == l.ようりょくそ {
        spd1 *= 2;
    }
    if w2 == Some(we.sunny) && p2.ability == l.ようりょくそ {
        spd2 *= 2;
    }
    if w1 == Some(we.sandstorm) && p1.ability == l.すなかき {
        spd1 *= 2;
    }
    if w2 == Some(we.sandstorm) && p2.ability == l.すなかき {
        spd2 *= 2;
    }
    if w1 == Some(we.hail) && p1.ability == l.ゆきかき {
        spd1 *= 2;
    }
    if w2 == Some(we.hail) && p2.ability == l.ゆきかき {
        spd2 *= 2;
    }
    if field.electric_terrain {
        if p1.ability == l.サーフテール {
            spd1 *= 2;
        }
        if p2.ability == l.サーフテール {
            spd2 *= 2;
        }
    }
    if p1.ability == l.はやあし && p1.status.is_some() {
        spd1 = ((spd1 as f64) * 1.5) as i64;
    }
    if p2.ability == l.はやあし && p2.status.is_some() {
        spd2 = ((spd2 as f64) * 1.5) as i64;
    }
    if spd1 == spd2 {
        return rng.random() < 0.5;
    }
    if !field.trick_room {
        spd1 > spd2
    } else {
        spd1 < spd2
    }
}

// ── 入場効果 ──────────────────────────────────────────────────────────────
/// _entry_effects。party は イリュージョン 用（同一 side の手持ち）。
pub fn entry_effects(
    pack: &Pack,
    side: &mut Side,
    side_idx: usize,
    field: &mut Field,
    opponent: &mut Poke,
) {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    let pi = side.active_idx;
    {
        let poke = &mut side.party[pi];
        poke.turns_out = 0;
        poke.times_hit = 0;
        poke.pivot_out = false;
        poke.force_switch = false;

        let immune_to_ground = poke.has_type(pack.tc.ひこう)
            || poke.ability == l.ふゆう
            || poke.ability == l.うなぎのぼり;

        if field.stealth_rock[side_idx] && poke.ability != l.マジックガード {
            let eff = pack.eff(pack.tc.いわ, poke.type1, poke.type2);
            let dmg = std::cmp::max(1, ((poke.max_hp as f64) * eff / 8.0).floor() as i64);
            poke.take_damage(dmg);
        }
        if field.spikes[side_idx] > 0 && !immune_to_ground && poke.ability != l.マジックガード {
            let rate = match field.spikes[side_idx] {
                1 => 1.0 / 8.0,
                2 => 1.0 / 6.0,
                _ => 1.0 / 4.0,
            };
            let dmg = std::cmp::max(1, ((poke.max_hp as f64) * rate).floor() as i64);
            poke.take_damage(dmg);
        }
        if field.toxic_spikes[side_idx] > 0 && !immune_to_ground && poke.ability != l.マジックガード {
            if poke.has_type(pack.tc.どく) {
                field.toxic_spikes[side_idx] = 0;
            } else if !poke.has_type(pack.tc.はがね) {
                let layers = field.toxic_spikes[side_idx];
                let status = if layers >= 2 { st.badpoison } else { st.poison };
                apply_status(pack, poke, status, false);
            }
        }
        if field.sticky_web[side_idx] && !immune_to_ground {
            poke.stage_speed = std::cmp::max(-6, poke.stage_speed - 1);
        }
        if poke.ability == l.がんじょう && !poke.is_alive {
            poke.hp = 1;
            poke.is_alive = true;
        }
    }
    // イリュージョン（party の末尾から生存かつ自分でない個体）
    let ill = {
        let poke = &side.party[pi];
        if poke.ability == l.イリュージョン {
            let mut found = None;
            for (i, p) in side.party.iter().enumerate().rev() {
                if p.is_alive && i != pi {
                    found = Some(p.name);
                    break;
                }
            }
            found
        } else {
            None
        }
    };
    if let Some(nm) = ill {
        side.party[pi].illusion_name = Some(nm);
    }
    ab::entry_ability(pack, &mut side.party[pi], opponent, field, 5);
}

// ── 交代先選択（エンジン内蔵ヒューリスティック）────────────────────────────
fn eff_spd_for_switch(pack: &Pack, p: &Poke, field: &Field, has_field: bool) -> f64 {
    let l = &pack.sy.l;
    let we = &pack.sy.we;
    let mut s = p.speed as f64;
    if p.item == Some(l.こだわりスカーフ) {
        s *= 1.5;
    }
    if p.status == Some(pack.sy.st.paralysis) && p.ability != l.はやあし {
        s *= 0.5;
    }
    if has_field {
        let w = effective_weather(pack, field, Some(p));
        let a = p.ability;
        if (a == l.すいすい && w == Some(we.rain))
            || (a == l.すなかき && w == Some(we.sandstorm))
            || (a == l.ようりょくそ && w == Some(we.sunny))
            || (a == l.ゆきかき && (w == Some(we.hail) || w == Some(pack.sy.l.snow)))
        {
            s *= 2.0;
        }
    }
    s
}

/// _best_faint_switch
pub fn best_faint_switch(
    pack: &Pack,
    side: &mut Side,
    opp: &mut Poke,
    field: &mut Field,
    has_field: bool,
    rng: &mut dyn BRng,
) -> Option<usize> {
    let benched: Vec<usize> = (0..side.party.len())
        .filter(|&i| side.party[i].is_alive && i != side.active_idx)
        .collect();
    if benched.is_empty() {
        return None;
    }
    let mut fld_default = Field::default();
    let fld: &mut Field = if has_field { field } else { &mut fld_default };

    let opp_spd = eff_spd_for_switch(pack, opp, fld, has_field);
    let mut best_i = benched[0];
    let mut best_score = f64::NEG_INFINITY;
    for (k, &i) in benched.iter().enumerate() {
        // _can_revenge
        let mut rev = 0.0;
        // ばけのかわ未破壊なら1発目は通らないので反撃KOは成立しない
        let disguised = opp.ability == pack.sy.l.ばけのかわ && !opp.disguise_broken;
        if !disguised && eff_spd_for_switch(pack, &side.party[i], fld, has_field) > opp_spd {
            let mut best = 0.0f64;
            let nmv = side.party[i].moves.len();
            for mi in 0..nmv {
                let mv = side.party[i].moves[mi].clone();
                if mv.category != Cat::Status && mv.power.unwrap_or(0) > 0 {
                    let d = calc_damage(
                        pack,
                        &mut side.party[i],
                        opp,
                        &mv,
                        fld,
                        false,
                        Some(0.0),   // 最低ロール（0.85 は実効0.9775＝ほぼ最高値）
                        None,
                        &mut |k| if k == 0 { rng.random() } else { rng.choice(16) as f64 },
                    );
                    if (d as f64) > best {
                        best = d as f64;
                    }
                }
            }
            if best >= opp.hp as f64 {
                rev = 100000.0;
            }
        }
        let p = &side.party[i];
        let has_se = p.moves.iter().any(|mv| {
            mv.category != Cat::Status
                && mv.power.unwrap_or(0) != 0
                && pack.eff(mv.ty, opp.type1, opp.type2) >= 2.0
        });
        let mut opp_max_eff = f64::NEG_INFINITY;
        for t in [Some(opp.type1), opp.type2].into_iter().flatten() {
            let e = pack.eff(t, p.type1, p.type2);
            if e > opp_max_eff {
                opp_max_eff = e;
            }
        }
        if opp_max_eff == f64::NEG_INFINITY {
            opp_max_eff = 1.0;
        }
        let mut sc = 0.0f64;
        if has_se {
            sc += 2.0;
        }
        if opp_max_eff <= 0.5 {
            sc += 2.0;
        } else if opp_max_eff <= 1.0 {
            sc += 1.0;
        } else if opp_max_eff >= 2.0 {
            sc -= 2.0;
        }
        let score = rev + sc * 1000.0 + (p.hp as f64) / (std::cmp::max(1, p.max_hp) as f64) * 10.0;
        if k == 0 || score > best_score {
            best_score = score;
            best_i = i;
        }
    }
    Some(best_i)
}

/// _choose_pivot_target
pub fn choose_pivot_target(
    pack: &Pack,
    side: &mut Side,
    opp: &mut Poke,
    is_baton: bool,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> Option<usize> {
    let benched: Vec<usize> = (0..side.party.len())
        .filter(|&i| side.party[i].is_alive && i != side.active_idx)
        .collect();
    if benched.is_empty() {
        return None;
    }
    if is_baton {
        let mut best_i = benched[0];
        let mut best = f64::NEG_INFINITY;
        for (k, &i) in benched.iter().enumerate() {
            let p = &side.party[i];
            let mut v = std::cmp::max(p.attack, p.sp_attack) as f64;
            if p.mega.is_some() {
                v *= 1.2;
            }
            if k == 0 || v > best {
                best = v;
                best_i = i;
            }
        }
        return Some(best_i);
    }
    // Python: _choose_pivot_target は _best_faint_switch(side, opp) を field 無しで呼ぶ
    // （battle.py:438）＝空の BattleField で評価する。
    let _ = field;
    let mut empty = Field::default();
    best_faint_switch(pack, side, opp, &mut empty, false, rng)
}

// ── ギルガルド フォルム ───────────────────────────────────────────────────
fn aegislash_to_blade(pack: &Pack, p: &mut Poke) {
    if p.in_blade_forme {
        return;
    }
    p.shield_atk = p.attack;
    p.shield_def = p.defense;
    p.shield_spatk = p.sp_attack;
    p.shield_spdef = p.sp_defense;
    let nature = p.nature;
    let nat = |k: u8| -> f64 {
        match pack.nature_mods.get(&nature) {
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
    p.attack = calc_stat(150, p.evs[1], 31, nat(0));
    p.defense = calc_stat(50, p.evs[2], 31, nat(1));
    p.sp_attack = calc_stat(150, p.evs[3], 31, nat(2));
    p.sp_defense = calc_stat(50, p.evs[4], 31, nat(3));
    if p.ability == pack.sy.l.はりきり {
        p.attack = ((p.attack as f64) * 1.5).floor() as i64;
    }
    p.in_blade_forme = true;
}

fn aegislash_to_shield(p: &mut Poke) {
    if !p.in_blade_forme {
        return;
    }
    p.attack = p.shield_atk;
    p.defense = p.shield_def;
    p.sp_attack = p.shield_spatk;
    p.sp_defense = p.shield_spdef;
    p.in_blade_forme = false;
}

// ── 急所・連続ヒット ──────────────────────────────────────────────────────
fn is_high_crit(pack: &Pack, n: u16) -> bool {
    let l = &pack.sy.l;
    n == l.きょうふのつるぎ || n == l.からじしボム || n == l.スラッシュ || n == l.カタストロフィ
        || n == l.シャドークロー || n == l.ナイトスラッシュ || n == l.クロスポイズン
        || n == l.サイコカッター || n == l.リーフブレード || n == l._3ぼんのや
        || n == l.ストーンエッジ || n == l.ブレイズキック || n == l.クラブハンマー
        || n == l.クロスチョップ || n == l.つじぎり || n == l.ドリルライナー
        || n == l.アクアカッター || n == l.エアカッター || n == l.ゴッドバード
}

pub fn crit_chance(pack: &Pack, attacker: &Poke, mv: &DMove, defender: Option<&Poke>) -> f64 {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    if let Some(d) = defender {
        if d.ability == l.シェルアーマー || d.ability == l.カブトアーマー {
            return 0.0;
        }
    }
    if attacker.ability == l.ひとでなし {
        if let Some(d) = defender {
            if d.status == Some(st.poison) || d.status == Some(st.badpoison) {
                return 1.0;
            }
        }
    }
    if mv.name == l.トリックフラワー {
        return 1.0;
    }
    let mut stage = 0i64;
    if is_high_crit(pack, mv.name) {
        stage = 1;
    }
    if attacker.ability == l.きょううん {
        stage += 1;
    }
    stage += crate::damage::get_crit_stage_bonus(pack, attacker.item);
    stage += attacker.crit_stage;
    match std::cmp::min(stage, 3) {
        0 => 1.0 / 24.0,
        1 => 1.0 / 8.0,
        2 => 1.0 / 2.0,
        _ => 1.0,
    }
}

fn check_critical(pack: &Pack, attacker: &Poke, mv: &DMove, defender: &Poke, rng: &mut dyn BRng) -> bool {
    rng.random() < crit_chance(pack, attacker, mv, Some(defender))
}

fn calc_hits(pack: &Pack, mv: &DMove, attacker: &Poke, rng: &mut dyn BRng) -> i64 {
    let l = &pack.sy.l;
    let n = mv.name;
    let skill_link = attacker.ability == l.スキルリンク;
    if n == l.ダブルキック
        || n == l.にどげり
        || n == l.ダブルウイング
        || n == l.ドラゴンアロー
        || n == l.スパークリングアリア
        || n == l.ダブルパンツァー
        || n == l.ツインビーム
        || n == l.ダブルアタック
    {
        return 2;
    }
    if n == l.トリプルアクセル {
        return 3;
    }
    if n == l.スケイルショット
        || n == l.みずしゅりけん
        || n == l.ロックブラスト
        || n == l.タネマシンガン
        || n == l.つららばり
        || n == l.ミサイルばり
        || n == l.ボーンラッシュ
        || n == l.あわ
        || n == l.スイープビンタ
    {
        if skill_link {
            return 5;
        }
        return rng.choices();
    }
    if n == l.ネズミざん {
        if skill_link {
            return 10;
        }
        let mut hits = 1;
        while hits < 10 && rng.random() < 0.90 {
            hits += 1;
        }
        return hits;
    }
    1
}

// ══════════════════════════════════════════════════════════════════════════
//  _execute_move
// ══════════════════════════════════════════════════════════════════════════
pub fn execute_move(
    pack: &Pack,
    sides: &mut [Side; 2],
    field: &mut Field,
    aidx: usize,
    action: &Action,
    opp_action: Option<&Action>,
    rng: &mut dyn BRng,
) {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    let we = &pack.sy.we;
    let didx = 1 - aidx;
    let mv: DMove = match &action.mv {
        None => return,
        Some(m) => m.clone(),
    };
    let n = mv.name;
    let (ai, di) = (sides[aidx].active_idx, sides[didx].active_idx);

    macro_rules! A {
        () => {
            sides[aidx].party[ai]
        };
    }
    macro_rules! D {
        () => {
            sides[didx].party[di]
        };
    }
    macro_rules! two {
        () => {{
            let (a, b) = sides.split_at_mut(1);
            if aidx == 0 {
                (&mut a[0].party[ai], &mut b[0].party[di])
            } else {
                (&mut b[0].party[ai], &mut a[0].party[di])
            }
        }};
    }

    A!().flinched = false;
    A!().last_used_move = Some(n);
    A!().last_move_obj = Some(mv.clone());
    if n != l.とっておき {
        let nm = A!().name;
        let _ = nm;
        if !A!().used_moves.contains(&n) {
            A!().used_moves.push(n);
        }
    }
    {
        let an = A!().name;
        sides[didx].opp_view.on_move(an, n);
    }

    if A!().recharge {
        A!().recharge = false;
        return;
    }

    // ねごと（ダメージ技の再実行）
    if n == l.ねごと {
        if A!().status != Some(st.sleep) {
            return;
        }
        let usable: Vec<usize> = (0..A!().moves.len())
            .filter(|&i| A!().moves[i].category != Cat::Status)
            .collect();
        if usable.is_empty() {
            return;
        }
        let k = rng.choice(usable.len());
        let selected = A!().moves[usable[k]].clone();
        let saved_status = A!().status;
        let saved_count = A!().sleep_count;
        A!().status = None;
        let fake = Action { kind: ActKind::Move, mv: Some(selected), ..Default::default() };
        execute_move(pack, sides, field, aidx, &fake, opp_action, rng);
        if sides[aidx].party[ai].status.is_none() {
            sides[aidx].party[ai].status = saved_status;
            sides[aidx].party[ai].sleep_count = saved_count;
        }
        return;
    }

    if mv.category == Cat::Status && A!().taunt_count > 0 {
        A!().taunt_count = std::cmp::max(0, A!().taunt_count - 1);
        return;
    }

    if A!().throat_chop_count > 0 && pack.flags(n).sound {
        return;
    }

    if A!().encore_count > 0 && A!().locked_move.is_some() {
        A!().encore_count -= 1;
        if A!().encore_count == 0 {
            A!().locked_move = None;
        }
    }

    if A!().disabled_move == Some(n) {
        return;
    }

    if A!().status == Some(st.paralysis) && rng.random() < 0.25 {
        return;
    }

    if A!().status == Some(st.sleep) {
        A!().sleep_count -= if A!().ability == l.はやおき { 2 } else { 1 };
        if A!().sleep_count > 0 {
            if n == l.いびき || n == l.ねごと {
                // 使える
            } else {
                A!().charging_move = None;
                return;
            }
        } else {
            A!().status = None;
        }
    }

    if A!().status == Some(st.freeze) {
        if n == l.もえつきる || n == l.ねっとう || n == l.ねっさのだいち || n == l.せいなるほのお {
            A!().status = None;
        } else if rng.random() < 0.2 {
            A!().status = None;
        } else {
            return;
        }
    }

    if A!().confused && rng.random() < 0.33 {
        let (atk, def) = (A!().attack, A!().defense);
        let self_dmg = std::cmp::max(
            1,
            ((((((2.0f64 * 50.0 / 5.0 + 2.0).floor()) * 40.0 * atk as f64 / def as f64).floor())
                / 50.0)
                + 2.0)
                .floor() as i64,
        );
        A!().take_damage(self_dmg);
        return;
    }

    // まもる系
    if n == l.まもる || n == l.キングシールド || n == l.ニードルガード || n == l.みきり
        || n == l.こらえる || n == l.トーチカ
    {
        let cnt = A!().protect_consecutive;
        let success_rate = (1.0f64 / 3.0).powi(cnt as i32);
        if cnt > 0 && rng.random() >= success_rate {
            A!().protect_consecutive += 1;
            return;
        }
        if n == l.こらえる {
            A!().enduring = true;
            A!().protect_consecutive += 1;
            return;
        }
        A!().protecting = true;
        A!().protect_move = Some(n);
        A!().protect_consecutive += 1;
        if n == l.キングシールド && A!().ability == l.バトルスイッチ {
            aegislash_to_shield(&mut A!());
        }
        return;
    } else {
        A!().protect_consecutive = 0;
    }

    // スクリーン技
    if n == l.リフレクター {
        if !sides[aidx].reflect {
            sides[aidx].reflect = true;
            sides[aidx].reflect_count = if A!().item == Some(l.ひかりのねんど) { 8 } else { 5 };
        }
        return;
    }
    if n == l.ひかりのかべ {
        if !sides[aidx].light_screen {
            sides[aidx].light_screen = true;
            sides[aidx].light_screen_count =
                if A!().item == Some(l.ひかりのねんど) { 8 } else { 5 };
        }
        return;
    }
    if n == l.オーロラベール {
        if effective_weather(pack, field, Some(&A!())) != Some(we.hail) {
            return;
        }
        if !sides[aidx].aurora_veil {
            sides[aidx].aurora_veil = true;
            sides[aidx].aurora_veil_count =
                if A!().item == Some(l.ひかりのねんど) { 8 } else { 5 };
        }
        return;
    }
    if n == l.おいかぜ {
        if !sides[aidx].tailwind {
            sides[aidx].tailwind = true;
            sides[aidx].tailwind_count = 3;
        }
        return;
    }
    if n == l.まきびし {
        let oi = sides[didx].field_idx;
        if field.spikes[oi] < 3 {
            field.spikes[oi] += 1;
        }
        return;
    }
    if n == l.ステルスロック {
        if !sides[didx].stealth_rock_set && !sides[didx].sr_pending {
            sides[didx].sr_pending = true;
        }
        return;
    }
    if n == l.トリックルーム {
        if field.trick_room {
            field.trick_room = false;
            field.trick_room_count = 0;
        } else {
            field.trick_room = true;
            field.trick_room_count = 5;
        }
        return;
    }
    // 天候技
    {
        let wt = |rock: u16, a: &Poke| -> i64 {
            if a.item == Some(rock) {
                8
            } else {
                5
            }
        };
        if n == l.あまごい {
            field.weather = Some(we.rain);
            field.weather_count = wt(l.しめったいわ, &A!());
            return;
        }
        if n == l.にほんばれ {
            field.weather = Some(we.sunny);
            field.weather_count = wt(l.あついいわ, &A!());
            return;
        }
        if n == l.すなあらし {
            field.weather = Some(we.sandstorm);
            field.weather_count = wt(l.さらさらいわ, &A!());
            return;
        }
        if n == l.あられ {
            field.weather = Some(we.hail);
            field.weather_count = wt(l.つめたいいわ, &A!());
            return;
        }
        if n == l.ゆきげしき {
            field.weather = Some(we.hail);
            field.weather_count = wt(l.つめたいいわ, &A!());
            return;
        }
        if n == l.さむいギャグ {
            field.weather = Some(we.hail);
            field.weather_count = wt(l.つめたいいわ, &A!());
            A!().pivot_out = true;
            return;
        }
    }

    // 変化技
    if mv.category == Cat::Status {
        if A!().ability == l.いたずらごころ && D!().has_type(pack.tc.あく) {
            return;
        }
        let hit = {
            let (a, d) = two!();
            check_hit(pack, a, d, &mv, field, &mut || rng.random())
        };
        if !hit {
            return;
        }
        if D!().ability == l.おうごんのからだ && gag_block(pack, n) {
            return;
        }
        apply_status_move(pack, sides, field, aidx, &mv, rng);
        return;
    }

    // ── 攻撃技の前処理 ──
    if (n == l.ねこだまし || n == l.であいがしら) && A!().turns_out > 0 {
        return;
    }
    if n == l.ふいうち {
        let opp_is_attacking = match opp_action {
            Some(oa) => {
                oa.kind == ActKind::Move
                    && oa.mv.as_ref().map(|m| m.category != Cat::Status).unwrap_or(false)
            }
            None => false,
        };
        if !opp_is_attacking {
            return;
        }
    }
    if pack.flags(n).sound && D!().ability == l.ぼうおん {
        return;
    }
    if n == l.ポルターガイスト && D!().item.is_none() {
        return;
    }
    if n == l.なげつける {
        if A!().item.is_none() {
            return;
        }
        A!().last_flung_item = A!().item;
        A!().item = None;
    }
    if mv.priority > 0 && (D!().ability == l.じょおうのいげん || D!().ability == l.テイルアーマー) {
        return;
    }
    if (n == l.だいばくはつ || n == l.じばく || n == l.ミストバースト)
        && (A!().ability == l.しめりけ || D!().ability == l.しめりけ)
    {
        return;
    }
    if A!().ability == l.バトルスイッチ && mv.category != Cat::Status {
        aegislash_to_blade(pack, &mut A!());
    }
    if A!().ability == l.へんげんじざい && !A!().protean_used {
        let new_type = mv.ty;
        if A!().type1 != new_type || A!().type2.is_some() {
            A!().type1 = new_type;
            A!().type2 = None;
            A!().protean_used = true;
        }
    }

    // 一撃必殺
    if n == l.ぜったいれいど || n == l.ハサミギロチン || n == l.つのドリル || n == l.じわれ {
        if n == l.ぜったいれいど && D!().has_type(pack.tc.こおり) {
            return;
        }
        if n == l.じわれ && D!().has_type(pack.tc.ひこう) {
            return;
        }
        if (n == l.つのドリル || n == l.ハサミギロチン) && D!().has_type(pack.tc.ゴースト) {
            return;
        }
        let hit = {
            let (a, d) = two!();
            check_hit(pack, a, d, &mv, field, &mut || rng.random())
        };
        if !hit {
            return;
        }
        if D!().item == Some(l.きあいのタスキ) && D!().hp == D!().max_hp {
            D!().item = None;
            it::on_item_consumed(pack, &mut D!());
            D!().hp = 1;
        } else if D!().ability == l.がんじょう && D!().hp == D!().max_hp {
            D!().hp = 1;
        } else if D!().item == Some(l.きあいのハチマキ) && rng.random() < 0.10 {
            D!().hp = 1;
        } else {
            let overkill = D!().hp;
            D!().hp = 0;
            D!().is_alive = false;
            {
                let (a, d) = two!();
                ab::on_defender_ko(pack, a, d, overkill);
            }
            ab::on_ko(pack, &mut A!());
        }
        return;
    }

    // 溜め技
    if n == l.ソーラービーム || n == l.ソーラーブレード || n == l.あなをほる || n == l.そらをとぶ
        || n == l.ダイビング || n == l.エレクトロビーム || n == l.ゴッドバード
        || n == l.とびはねる || n == l.メテオビーム || n == l.ゴーストダイブ
    {
        let w = effective_weather(pack, field, Some(&A!()));
        let mut instant =
            (n == l.ソーラービーム || n == l.ソーラーブレード) && w == Some(we.sunny);
        instant = instant || (n == l.エレクトロビーム && w == Some(we.rain));
        if !instant {
            if A!().charging_move.is_none() {
                A!().charging_move = Some(n);
                if n == l.エレクトロビーム || n == l.メテオビーム {
                    A!().stage_sp_attack = std::cmp::min(6, A!().stage_sp_attack + 1);
                }
                return;
            } else {
                A!().charging_move = None;
            }
        }
        if instant && n == l.エレクトロビーム {
            A!().stage_sp_attack = std::cmp::min(6, A!().stage_sp_attack + 1);
        }
    }

    if n == l.くちばしキャノン {
        A!().beak_primed = false;
    }
    if (n == l.フェイント || n == l.ゴーストダイブ) && D!().protecting {
        D!().protecting = false;
    }
    A!().pierce_quarter = false;
    if D!().protecting
        && is_contact_move(pack, &mv)
        && (A!().ability == l.ふかしのこぶし || A!().ability == l.かんつうドリル)
    {
        D!().protecting = false;
        A!().pierce_quarter = true;
    }
    if n == l.きあいパンチ && A!().took_damage_this_turn {
        return;
    }
    if n == l.もえつきる && !A!().has_type(pack.tc.ほのお) {
        return;
    }
    if n == l.ゲップ && !A!().ate_berry {
        return;
    }
    if (n == l.いびき || n == l.ねごと) && A!().status != Some(st.sleep) {
        return;
    }
    if n == l.デカハンマー {
        if A!().deka_last {
            A!().deka_last = false;
            return;
        }
        A!().deka_last = true;
    } else {
        A!().deka_last = false;
    }
    if n == l.とっておき {
        let others: Vec<u16> =
            A!().moves.iter().map(|m| m.name).filter(|&x| x != l.とっておき).collect();
        let used = A!().used_moves.clone();
        if others.is_empty() || !others.iter().all(|x| used.contains(x)) {
            return;
        }
    }
    if n == l.はやてがえし {
        let opp_pri = match opp_action {
            Some(oa) if oa.kind == ActKind::Move => {
                oa.mv.as_ref().map(|m| m.priority).unwrap_or(0)
            }
            _ => 0,
        };
        if opp_pri <= 0 {
            return;
        }
    }
    if n == l.アイアンローラー {
        if !(field.grassy_terrain
            || field.electric_terrain
            || field.psychic_terrain
            || field.misty_terrain)
        {
            return;
        }
    }
    if n == l.みらいよち {
        if sides[didx].future_sight_count > 0 {
            return;
        }
        let d = {
            let (a, dd) = two!();
            // 正規化ロール（実ロール = 0.85 + x*0.15）。平均ロール0.925は Some(0.5)。
            // Some(0.925) は実効0.98875＝ほぼ最高値になる。
            calc_damage(pack, a, dd, &mv, field, false, Some(0.5), None, &mut |k| {
                if k == 0 {
                    rng.random()
                } else {
                    rng.choice(16) as f64
                }
            })
        };
        sides[didx].future_sight_dmg = d;
        sides[didx].future_sight_count = 2;
        sides[didx].future_sight_name = Some(A!().name);
        return;
    }

    // 命中判定
    let hit = {
        let (a, d) = two!();
        check_hit(pack, a, d, &mv, field, &mut || rng.random())
    };
    if !hit {
        if D!().protecting {
            let pmove = D!().protect_move;
            if pmove == Some(l.キングシールド)
                && is_contact_move(pack, &mv)
                && A!().ability != l.えんかく
                && !ab::is_mold(pack, &A!())
            {
                A!().stage_attack = std::cmp::max(-6, A!().stage_attack - 1);
            }
            if pmove == Some(l.トーチカ)
                && is_contact_move(pack, &mv)
                && A!().ability != l.えんかく
                && D!().is_alive
                && A!().is_alive
            {
                apply_status(pack, &mut A!(), st.poison, false);
            }
            if pmove == Some(l.ニードルガード)
                && is_contact_move(pack, &mv)
                && A!().ability != l.えんかく
                && A!().is_alive
            {
                let nd = std::cmp::max(1, A!().max_hp / 8);
                A!().take_damage(nd);
            }
        } else {
            A!().move_failed_this_turn = true;
            if n == l.とびひざげり || n == l.とびげり || n == l.かかとおとし || n == l.サンダーダイブ
            {
                let recoil = std::cmp::max(1, A!().max_hp / 2);
                A!().take_damage(recoil);
            }
        }
        return;
    }

    // タイプ無効
    let eff_type = {
        let a = &A!();
        effective_move_type(pack, a, &mv, field)
    };
    let mut eff = pack.eff(eff_type, D!().type1, D!().type2);
    if n == l.フリーズドライ && D!().has_type(pack.tc.みず) {
        eff = f64::max(eff, 2.0);
    }
    if eff == 0.0 {
        return;
    }

    // ばけのかわ
    if D!().ability == l.ばけのかわ && !D!().disguise_broken {
        D!().disguise_broken = true;
        let pen = std::cmp::max(1, ((D!().max_hp as f64) / 8.0).floor() as i64);
        D!().take_damage(pen);
        if (n == l.ボルトチェンジ || n == l.とんぼがえり || n == l.クイックターン) && A!().is_alive
        {
            A!().pivot_out = true;
        }
        return;
    }

    // カウンター系
    if n == l.カウンター || n == l.ミラーコート || n == l.メタルバースト || n == l.ほうふく {
        let mut ret_dmg = if n == l.カウンター {
            A!().last_physical_dmg_received * 2
        } else if n == l.ミラーコート {
            A!().last_special_dmg_received * 2
        } else {
            (((A!().last_physical_dmg_received + A!().last_special_dmg_received) as f64) * 1.5)
                .floor() as i64
        };
        if ret_dmg <= 0 {
            return;
        }
        if D!().item == Some(l.きあいのタスキ) && D!().hp == D!().max_hp && ret_dmg >= D!().hp {
            ret_dmg = D!().hp - 1;
            D!().item = None;
            it::on_item_consumed(pack, &mut D!());
            let dn = D!().name;
            sides[aidx].opp_view.on_item(dn, l.きあいのタスキ);
        }
        if D!().ability == l.がんじょう && D!().hp == D!().max_hp && ret_dmg >= D!().hp {
            ret_dmg = D!().hp - 1;
        }
        if D!().item == Some(l.きあいのハチマキ) && ret_dmg >= D!().hp && rng.random() < 0.10 {
            ret_dmg = D!().hp - 1;
        }
        D!().take_damage(ret_dmg);
        if !D!().is_alive {
            {
                let (a, d) = two!();
                ab::on_defender_ko(pack, a, d, ret_dmg);
            }
            ab::on_ko(pack, &mut A!());
        }
        return;
    }

    let critical = {
        let (a, d) = (&sides[aidx].party[ai], &sides[didx].party[di]);
        let c = crit_chance(pack, a, &mv, Some(d));
        rng.random() < c
    };
    let mut hits = calc_hits(pack, &mv, &A!(), rng);

    let screen_breaker = n == l.かわらわり || n == l.レイジングブル || n == l.サイコファング;
    let mut screen_mult = 1.0f64;
    if !critical && !ab::is_mold(pack, &A!()) && A!().ability != l.すりぬけ && !screen_breaker {
        if mv.category == Cat::Physical && (sides[didx].reflect || sides[didx].aurora_veil) {
            screen_mult = 0.5;
        } else if mv.category == Cat::Special
            && (sides[didx].light_screen || sides[didx].aurora_veil)
        {
            screen_mult = 0.5;
        }
    }

    let mut total_dmg: i64 = 0;
    for hit_i in 0..hits {
        if !D!().is_alive {
            break;
        }
        A!().multi_hit_index = hit_i;
        let ro = field.roll_override;
        let mut dmg = {
            let (a, d) = two!();
            calc_damage(pack, a, d, &mv, field, critical, None, ro, &mut |k| {
                if k == 0 {
                    rng.random()
                } else {
                    rng.choice(16) as f64
                }
            })
        };
        if screen_mult < 1.0 {
            dmg = std::cmp::max(1, ((dmg as f64) * screen_mult).floor() as i64);
        }
        if A!().pierce_quarter {
            dmg = std::cmp::max(1, dmg / 4);
        }

        let sub_hp = D!().substitute_hp;
        if sub_hp > 0 && n != l.ぼうふう && n != l.ハイパーボイス {
            if dmg >= sub_hp {
                D!().substitute_hp = 0;
            } else {
                D!().substitute_hp = sub_hp - dmg;
            }
            total_dmg += dmg;
            continue;
        }

        if D!().item == Some(l.きあいのタスキ) && D!().hp == D!().max_hp && dmg >= D!().hp {
            dmg = D!().hp - 1;
            D!().item = None;
            it::on_item_consumed(pack, &mut D!());
            let dn = D!().name;
            sides[aidx].opp_view.on_item(dn, l.きあいのタスキ);
        }
        if D!().ability == l.がんじょう && D!().hp == D!().max_hp && dmg >= D!().hp {
            dmg = D!().hp - 1;
            let dn = D!().name;
            sides[aidx].opp_view.on_ability(dn, l.がんじょう);
        }
        if D!().item == Some(l.きあいのハチマキ) && dmg >= D!().hp && rng.random() < 0.10 {
            dmg = D!().hp - 1;
            let dn = D!().name;
            sides[aidx].opp_view.on_item(dn, l.きあいのハチマキ);
        }

        D!().take_damage(dmg);
        total_dmg += dmg;
        if dmg > 0 {
            D!().took_damage_this_turn = true;
        }
        if D!().illusion_name.is_some() {
            D!().illusion_name = None;
        }
        if mv.category == Cat::Physical {
            D!().last_physical_dmg_received += dmg;
        } else if mv.category == Cat::Special {
            D!().last_special_dmg_received += dmg;
        }
        if A!().item == Some(l.いのちのたま) && mv.category != Cat::Status {
            let recoil = std::cmp::max(1, ((A!().max_hp as f64) / 10.0).floor() as i64);
            A!().take_damage(recoil);
            let an = A!().name;
            sides[didx].opp_view.on_item(an, l.いのちのたま);
        }
        {
            let (a, d) = two!();
            ab::rough_skin_recoil(pack, a, d, &mv);
        }
        if D!().beak_primed && is_contact_move(pack, &mv) && A!().is_alive {
            apply_status(pack, &mut A!(), st.burn, false);
        }
        if (n == l.ついばむ || n == l.むしくい) && A!().is_alive && is_berry(pack, D!().item) {
            let berry = D!().item.unwrap();
            D!().item = None;
            A!().ate_berry = true;
            if berry == l.オボンのみ {
                let h = A!().max_hp / 4;
                A!().hp = std::cmp::min(A!().max_hp, A!().hp + h);
            } else if berry == l.オレンのみ {
                A!().hp = std::cmp::min(A!().max_hp, A!().hp + 10);
            } else if berry == l.ラムのみ || berry == l.カゴのみ {
                A!().status = None;
                A!().bad_poison_count = 0;
                A!().sleep_count = 0;
                A!().confused = false;
            } else if berry == l.モモンのみ
                && (A!().status == Some(st.poison) || A!().status == Some(st.badpoison))
            {
                A!().status = None;
                A!().bad_poison_count = 0;
            } else if berry == l.チーゴのみ && A!().status == Some(st.burn) {
                A!().status = None;
            } else {
                let sidx = if berry == l.カムラのみ {
                    Some(4u8)
                } else if berry == l.サルのみ {
                    Some(2u8)
                } else if berry == l.リュガのみ {
                    Some(1u8)
                } else if berry == l.タラプのみ {
                    Some(3u8)
                } else {
                    None
                };
                if let Some(sx) = sidx {
                    let v = A!().stage(sx);
                    A!().set_stage(sx, std::cmp::min(6, v + 1));
                }
            }
        }
        if D!().is_alive {
            let (a, d) = two!();
            ab::on_after_hit(pack, a, d, &mv, rng);
        }
        if D!().is_alive && A!().ability == l.ポイズンタッチ && is_contact_move(pack, &mv) {
            if rng.random() < 0.30 {
                let ok = apply_status(pack, &mut D!(), st.poison, false);
                if ok {
                    it::try_cure_berry(pack, &mut D!());
                }
            }
        }
        if D!().item == Some(l.じゃくてんほけん) {
            let ec = pack.eff(eff_type, D!().type1, D!().type2);
            if ec >= 2.0 {
                D!().stage_attack = std::cmp::min(6, D!().stage_attack + 2);
                D!().stage_sp_attack = std::cmp::min(6, D!().stage_sp_attack + 2);
                D!().item = None;
            }
        }
        if !D!().is_alive {
            {
                let (a, d) = two!();
                ab::on_defender_ko(pack, a, d, dmg);
            }
            ab::on_ko(pack, &mut A!());
        }
    }

    if critical && D!().is_alive && D!().ability == l.いかりのつぼ {
        D!().stage_attack = 6;
    }

    if (n == l.だいばくはつ || n == l.じばく) && A!().is_alive {
        let hp = A!().hp;
        A!().take_damage(hp);
        A!().is_alive = false;
    }
    if !D!().is_alive && D!().destiny_bond && A!().is_alive {
        let hp = A!().hp;
        A!().take_damage(hp);
        A!().is_alive = false;
    }
    if A!().item == Some(l.かいがらのすず) && total_dmg > 0 && A!().is_alive {
        let heal = std::cmp::max(1, ((total_dmg as f64) / 8.0).floor() as i64);
        A!().hp = std::cmp::min(A!().max_hp, A!().hp + heal);
    }
    // HP吸収技
    {
        let rate = if n == l.ギガドレイン
            || n == l.メガドレイン
            || n == l.すいとる
            || n == l.ドレインパンチ
            || n == l.きゅうけつ
            || n == l.パラボラチャージ
            || n == l.むねんのつるぎ
            || n == l.ウッドホーン
            || n == l.シャカシャカほう
        {
            Some(0.5)
        } else if n == l.ドレインキッス {
            Some(0.75)
        } else {
            None
        };
        if let Some(r) = rate {
            if total_dmg > 0 && A!().is_alive {
                let mut heal = std::cmp::max(1, ((total_dmg as f64) * r).floor() as i64);
                if A!().item == Some(l.おおきなねっこ) {
                    heal = ((heal as f64) * 1.3).floor() as i64;
                }
                A!().hp = std::cmp::min(A!().max_hp, A!().hp + heal);
            }
        }
    }

    if D!().is_alive && D!().ability == l.のろわれボディ && rng.random() < 0.30 {
        if A!().disabled_move.is_none() {
            A!().disabled_move = Some(n);
            A!().disabled_turns = 3;
        }
    }
    if D!().ability == l.すなはき && total_dmg > 0 && field.weather != Some(we.sandstorm) {
        field.weather = Some(we.sandstorm);
        field.weather_count = 5;
    }
    if D!().ability == l.どくげしょう && mv.category == Cat::Physical && total_dmg > 0 {
        let fi = sides[aidx].field_idx;
        if field.toxic_spikes[fi] < 2 {
            field.toxic_spikes[fi] += 1;
        }
    }

    // はたきおとす
    if n == l.はたきおとす && D!().is_alive && D!().item.is_some() {
        let itm = D!().item.unwrap();
        if is_megastone(pack, Some(itm)) {
            // 失敗
        } else if D!().ability == l.ねんちゃく {
            // 失敗
        } else {
            let dn = D!().name;
            sides[aidx].opp_view.on_item(dn, itm);
            D!().item = None;
        }
    }

    // いかりのまえば
    if n == l.いかりのまえば && D!().is_alive {
        if D!().has_type(pack.tc.ゴースト) {
            return;
        }
        let mut fang = std::cmp::max(1, D!().hp / 2);
        if D!().item == Some(l.きあいのタスキ) && D!().hp == D!().max_hp && fang >= D!().hp {
            fang = D!().hp - 1;
            D!().item = None;
            it::on_item_consumed(pack, &mut D!());
        }
        if D!().ability == l.がんじょう && D!().hp == D!().max_hp && fang >= D!().hp {
            fang = D!().hp - 1;
        }
        if D!().item == Some(l.きあいのハチマキ) && fang >= D!().hp && rng.random() < 0.10 {
            fang = D!().hp - 1;
        }
        D!().take_damage(fang);
        total_dmg += fang;
    }
    if n == l.ちきゅうなげ && D!().is_alive {
        if D!().has_type(pack.tc.ゴースト) {
            return;
        }
        D!().take_damage(50);
        total_dmg += 50;
    }
    if n == l.ナイトヘッド && D!().is_alive {
        if D!().has_type(pack.tc.ノーマル) {
            return;
        }
        D!().take_damage(50);
        total_dmg += 50;
    }
    if n == l.いのちがけ && D!().is_alive {
        let dmg = A!().hp;
        D!().take_damage(dmg);
        total_dmg += dmg;
        let hp = A!().hp;
        A!().take_damage(hp);
        A!().is_alive = false;
    }
    if n == l.はきだす && D!().is_alive {
        if A!().stockpile_count <= 0 {
            return;
        }
        let power = match A!().stockpile_count {
            1 => 100,
            2 => 200,
            _ => 300,
        };
        let mut spit = mv.clone();
        spit.power = Some(power);
        let ro2 = field.roll_override;
        let sd = {
            let (a, d) = two!();
            calc_damage(pack, a, d, &spit, field, false, None, ro2, &mut |k| {
                if k == 0 {
                    rng.random()
                } else {
                    rng.choice(16) as f64
                }
            })
        };
        D!().take_damage(sd);
        total_dmg += sd;
        let sc = A!().stockpile_count;
        for stx in [1u8, 3u8] {
            let v = A!().stage(stx);
            A!().set_stage(stx, std::cmp::max(-6, v - sc as i32));
        }
        A!().stockpile_count = 0;
    }
    if n == l.ふくろだたき && D!().is_alive {
        let cnt = sides[aidx].party.iter().filter(|p| p.is_alive && p.status.is_none()).count()
            as i64;
        hits = std::cmp::max(1, cnt);
        let base = std::cmp::max(1, A!().attack / 10);
        let fd = base * hits;
        D!().take_damage(fd);
        total_dmg += fd;
    }
    if n == l.がむしゃら && D!().is_alive {
        if D!().has_type(pack.tc.ゴースト) {
            return;
        }
        let target_hp = A!().hp;
        if D!().hp > target_hp {
            let extra = D!().hp - target_hp;
            D!().take_damage(extra);
            total_dmg += extra;
        }
    }
    if n == l.すてゼリフ && D!().is_alive {
        for stx in [0u8, 2u8] {
            let dab = D!().ability;
            if dab != l.クリアボディ && dab != l.しろいけむり && dab != l.かがくへんかガス {
                let v = D!().stage(stx);
                D!().set_stage(stx, std::cmp::max(-6, v - 1));
            }
        }
        if A!().is_alive {
            A!().pivot_out = true;
        }
    }
    if (n == l.ボルトチェンジ || n == l.とんぼがえり || n == l.クイックターン) && A!().is_alive {
        A!().pivot_out = true;
    }
    if (n == l.ドラゴンテール || n == l.ほえる || n == l.ふきとばし || n == l.ともえなげ)
        && D!().is_alive
    {
        D!().force_switch = true;
    }

    if total_dmg > 0 {
        let (dn, dhp, dmax) = (D!().name, D!().hp, D!().max_hp);
        let an = A!().name;
        sides[aidx].opp_view.on_hp_change(dn, dhp, dmax, total_dmg, Some(n), Some(an));
        // 推定器(任意): 観測した被ダメージ割合で EV/性格をベイズ更新（battle.py:1384）
        if sides[aidx].belief.0.is_some() {
            let frac = crate::oppview::round3(total_dmg as f64 / dmax as f64);
            let mut bl = sides[aidx].belief.0.take().unwrap();
            let mut att = std::mem::take(&mut sides[aidx].party[ai]);
            bl.observe_damage(pack, dn, &mut att, &mv, frac, field, false, rng);
            sides[aidx].party[ai] = att;
            sides[aidx].belief.0 = Some(bl);
        }
    }

    if total_dmg > 0 {
        if n == l.ひけん_ちえなみ {
            let idx = sides[didx].field_idx;
            if field.spikes[idx] < 3 {
                field.spikes[idx] += 1;
            }
        } else if n == l.がんせきアックス {
            let idx = sides[didx].field_idx;
            if !field.stealth_rock[idx] {
                field.stealth_rock[idx] = true;
            }
        }
    }

    if (n == l.ギガインパクト
        || n == l.ブラストバーン
        || n == l.はかいこうせん
        || n == l.ハイドロカノン
        || n == l.ハードプラント
        || n == l.がんせきほう)
        && A!().is_alive
    {
        A!().recharge = true;
    }

    if n == l.うちおとす && total_dmg > 0 && D!().is_alive {
        D!().grounded = true;
        D!().magnet_rise = false;
        let cm = D!().charging_move;
        if cm == Some(l.そらをとぶ) || cm == Some(l.とびはねる) {
            D!().charging_move = None;
        }
    }
    if n == l.クリアスモッグ && total_dmg > 0 && D!().is_alive {
        for i in 0..5u8 {
            D!().set_stage(i, 0);
        }
    }
    if (n == l.こうそくスピン || n == l.キラースピン) && total_dmg > 0 && A!().is_alive {
        if A!().bound_count > 0 {
            A!().bound_count = 0;
        }
        if A!().seeded {
            A!().seeded = false;
        }
    }
    if n == l.こうそくスピン && total_dmg > 0 && A!().is_alive {
        let mi = sides[aidx].field_idx;
        if field.stealth_rock[mi] {
            field.stealth_rock[mi] = false;
        }
        if field.spikes[mi] > 0 {
            field.spikes[mi] = 0;
        }
        if field.toxic_spikes[mi] > 0 {
            field.toxic_spikes[mi] = 0;
        }
        A!().stage_speed = std::cmp::min(6, A!().stage_speed + 1);
    }
    if n == l.キラースピン && total_dmg > 0 && D!().is_alive {
        if apply_status(pack, &mut D!(), st.poison, false) {
            it::try_cure_berry(pack, &mut D!());
        }
    }
    if (n == l.アイススピナー || n == l.アイアンローラー) && total_dmg > 0 {
        if field.electric_terrain {
            field.electric_terrain = false;
            field.electric_terrain_count = 0;
        }
        if field.psychic_terrain {
            field.psychic_terrain = false;
            field.psychic_terrain_count = 0;
        }
        if field.misty_terrain {
            field.misty_terrain = false;
            field.misty_terrain_count = 0;
        }
        if field.grassy_terrain {
            field.grassy_terrain = false;
            field.grassy_terrain_count = 0;
        }
    }
    if (n == l.どろぼう || n == l.ほしがる) && total_dmg > 0 && A!().is_alive {
        if A!().item.is_none() && D!().item.is_some() {
            let itm = D!().item.unwrap();
            if is_megastone(pack, Some(itm)) || D!().ability == l.ねんちゃく {
                // 奪えない
            } else {
                A!().item = Some(itm);
                D!().item = None;
            }
        }
    }
    if A!().ability == l.マジシャン
        && total_dmg > 0
        && A!().is_alive
        && A!().item.is_none()
        && D!().item.is_some()
        && !is_megastone(pack, D!().item)
        && D!().ability != l.ねんちゃく
    {
        A!().item = D!().item;
        D!().item = None;
    }
    if D!().ability == l.わるいてぐせ
        && is_contact_move(pack, &mv)
        && A!().ability != l.えんかく
        && D!().is_alive
        && D!().item.is_none()
        && A!().item.is_some()
        && !is_megastone(pack, A!().item)
        && A!().ability != l.ねんちゃく
    {
        D!().item = A!().item;
        A!().item = None;
    }
    if (n == l.レイジングブル || n == l.かわらわり || n == l.サイコファング) && total_dmg > 0 {
        if sides[didx].reflect {
            sides[didx].reflect = false;
            sides[didx].reflect_count = 0;
        }
        if sides[didx].light_screen {
            sides[didx].light_screen = false;
            sides[didx].light_screen_count = 0;
        }
        if sides[didx].aurora_veil {
            sides[didx].aurora_veil = false;
            sides[didx].aurora_veil_count = 0;
        }
    }

    let dsg = sides[didx].safeguard;
    {
        let (a, d) = two!();
        apply_secondary(pack, a, d, &mv, total_dmg, field, dsg, rng);
    }
    {
        let (a, d) = two!();
        apply_recoil(pack, a, d, &mv, total_dmg);
    }

    // おやこあい
    if A!().ability == l.おやこあい && hits == 1 && total_dmg > 0 && D!().is_alive {
        let mut pb = std::cmp::max(1, ((total_dmg as f64) * 0.25).floor() as i64);
        if D!().item == Some(l.きあいのタスキ) && D!().hp == D!().max_hp && pb >= D!().hp {
            pb = D!().hp - 1;
            D!().item = None;
            it::on_item_consumed(pack, &mut D!());
        }
        if D!().ability == l.がんじょう && D!().hp == D!().max_hp && pb >= D!().hp {
            pb = D!().hp - 1;
        }
        if D!().item == Some(l.きあいのハチマキ) && pb >= D!().hp && rng.random() < 0.10 {
            pb = D!().hp - 1;
        }
        D!().take_damage(pb);
        if D!().is_alive {
            {
                let (a, d) = two!();
                ab::on_after_hit(pack, a, d, &mv, rng);
            }
            let dsg2 = sides[didx].safeguard;
            let (a, d) = two!();
            apply_secondary(pack, a, d, &mv, pb, field, dsg2, rng);
        }
        {
            let (a, d) = two!();
            ab::rough_skin_recoil(pack, a, d, &mv);
        }
        {
            let (a, d) = two!();
            apply_recoil(pack, a, d, &mv, pb);
        }
        if !D!().is_alive {
            {
                let (a, d) = two!();
                ab::on_defender_ko(pack, a, d, pb);
            }
            ab::on_ko(pack, &mut A!());
        }
    }
}

// ══════════════════════════════════════════════════════════════════════════
//  _apply_status_move
// ══════════════════════════════════════════════════════════════════════════
#[derive(Clone, Copy)]
enum Deb {
    Status(u16),
    Confused,
    Stage(u8, i32),
    Infatuation,
    Torment,
    Trapped,
    AbilitySuppressed,
    AbilityChange(u16),
    TypeAdd(Ty),
    TypeSet(Ty),
    PpReduce(i64),
}

fn opponent_debuffs(pack: &Pack, n: u16) -> Option<(Vec<Deb>,)> {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    use Deb::*;
    let v: Vec<Deb> = if n == l.いかりのこな {
        vec![]
    } else if n == l.どくどく {
        vec![Status(st.badpoison)]
    } else if n == l.でんじは {
        vec![Status(st.paralysis)]
    } else if n == l.おにび {
        vec![Status(st.burn)]
    } else if n == l.ねむりごな || n == l.さいみんじゅつ || n == l.うたう {
        vec![Status(st.sleep)]
    } else if n == l.あやしいひかり || n == l.ちょうおんぱ || n == l.てんしのキッス {
        vec![Confused]
    } else if n == l.へびにらみ || n == l.しびれごな {
        vec![Status(st.paralysis)]
    } else if n == l.わたほうし || n == l.こわいかお || n == l.いとをはく {
        vec![Stage(4, -2)]
    } else if n == l.フェザーダンス || n == l.あまえる {
        vec![Stage(0, -2)]
    } else if n == l.かいでんぱ {
        vec![Stage(2, -2)]
    } else if n == l.つぶらなひとみ {
        vec![Stage(0, -1)]
    } else if n == l.どくのいと {
        vec![Status(st.poison), Stage(4, -2)]
    } else if n == l.いやなおと {
        vec![Stage(1, -2)]
    } else if n == l.うそなき || n == l.きんぞくおん {
        vec![Stage(3, -2)]
    } else if n == l.あまいかおり {
        vec![Stage(6, -2)]
    } else if n == l.どくのこな {
        vec![Status(st.poison)]
    } else if n == l.おたけび || n == l.なみだめ {
        vec![Stage(0, -1), Stage(2, -1)]
    } else if n == l.くすぐる {
        vec![Stage(0, -1), Stage(1, -1)]
    } else if n == l.いばる {
        vec![Stage(0, 2), Confused]
    } else if n == l.おだてる {
        vec![Stage(2, 1), Confused]
    } else if n == l.メロメロ {
        vec![Infatuation]
    } else if n == l.いちゃもん {
        vec![Torment]
    } else if n == l.くろいまなざし || n == l.とおせんぼう || n == l.かげぬい {
        vec![Trapped]
    } else if n == l.いえき {
        vec![AbilitySuppressed]
    } else if n == l.シンプルビーム {
        vec![AbilityChange(l.たんじゅん)]
    } else if n == l.なやみのタネ {
        vec![AbilityChange(l.ふみん)]
    } else if n == l.ハロウィン {
        vec![TypeAdd(pack.tc.ゴースト)]
    } else if n == l.もりののろい {
        vec![TypeAdd(pack.tc.くさ)]
    } else if n == l.うらみ {
        vec![PpReduce(4)]
    } else if n == l.ぶきみなじゅもん {
        vec![PpReduce(3)]
    } else if n == l.デコレーション {
        vec![Stage(0, 2), Stage(2, 2)]
    } else if n == l.ハバネロエキス {
        vec![Stage(1, -2), Stage(0, 2)]
    } else if n == l.まほうのこな {
        vec![TypeSet(pack.tc.エスパー)]
    } else {
        return None;
    };
    Some((v,))
}

/// SELF_BOOSTS
fn self_boosts(pack: &Pack, n: u16) -> Option<Vec<(u8, i32)>> {
    let l = &pack.sy.l;
    let v = if n == l.つるぎのまい {
        vec![(0u8, 2i32)]
    } else if n == l.わるだくみ {
        vec![(2, 2)]
    } else if n == l.りゅうのまい {
        vec![(0, 1), (4, 1)]
    } else if n == l.からをやぶる {
        vec![(0, 2), (2, 2), (4, 2), (1, -1), (3, -1)]
    } else if n == l.めいそう {
        vec![(2, 1), (3, 1)]
    } else if n == l.ちょうのまい {
        vec![(2, 1), (3, 1), (4, 1)]
    } else if n == l.はいすいのじん {
        vec![(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
    } else if n == l.コスモパワー {
        vec![(1, 1), (3, 1)]
    } else if n == l.てっぺき {
        vec![(1, 2)]
    } else if n == l.ビルドアップ {
        vec![(0, 1), (1, 1)]
    } else if n == l.こうそくいどう || n == l.ロックカット {
        vec![(4, 2)]
    } else if n == l.ドわすれ {
        vec![(3, 2)]
    } else if n == l.コットンガード {
        vec![(1, 3)]
    } else if n == l.とぐろをまく {
        vec![(0, 1), (1, 1), (5, 1)]
    } else if n == l.ちいさくなる {
        vec![(6, 2)]
    } else if n == l.とける || n == l.たてこもる {
        vec![(1, 2)]
    } else if n == l.かげぶんしん {
        vec![(6, 1)]
    } else {
        return None;
    };
    Some(v)
}

pub fn apply_status_move(
    pack: &Pack,
    sides: &mut [Side; 2],
    field: &mut Field,
    aidx: usize,
    mv: &DMove,
    rng: &mut dyn BRng,
) {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    let we = &pack.sy.we;
    let didx = 1 - aidx;
    let n = mv.name;
    let (ai, di) = (sides[aidx].active_idx, sides[didx].active_idx);
    macro_rules! A {
        () => {
            sides[aidx].party[ai]
        };
    }
    macro_rules! D {
        () => {
            sides[didx].party[di]
        };
    }

    // マジックミラー（個別処理される対人変化技）
    if (n == l.ちょうはつ || n == l.アンコール || n == l.やどりぎのタネ)
        && D!().ability == l.マジックミラー
    {
        if A!().ability != l.マジックミラー {
            apply_status_move(pack, sides, field, didx, mv, rng);
        }
        return;
    }

    if n == l.ひっくりかえす {
        if D!().ability == l.マジックミラー && A!().ability != l.マジックミラー {
            apply_status_move(pack, sides, field, didx, mv, rng);
            return;
        }
        for i in 0..7u8 {
            let v = D!().stage(i);
            if v != 0 {
                D!().set_stage(i, -v);
            }
        }
        return;
    }

    if n == l.みがわり {
        let cost = A!().max_hp / 4;
        if A!().hp <= cost {
        } else if A!().substitute_hp > 0 {
        } else {
            A!().hp -= cost;
            A!().substitute_hp = cost;
        }
        return;
    }

    if n == l.すてゼリフ {
        let dab = D!().ability;
        if dab != l.クリアボディ && dab != l.しろいけむり && dab != l.かがくへんかガス {
            for stx in [0u8, 2u8] {
                let v = D!().stage(stx);
                D!().set_stage(stx, std::cmp::max(-6, v - 1));
            }
        }
        A!().pivot_out = true;
        return;
    }

    if n == l.たくわえる {
        if A!().stockpile_count >= 3 {
            return;
        }
        A!().stockpile_count += 1;
        for stx in [1u8, 3u8] {
            let v = A!().stage(stx);
            if v < 6 {
                A!().set_stage(stx, v + 1);
            }
        }
        return;
    }

    if n == l.のみこむ {
        if A!().stockpile_count <= 0 {
            return;
        }
        let ratio = match A!().stockpile_count {
            1 => 0.25,
            2 => 0.5,
            _ => 1.0,
        };
        let heal = if ratio >= 1.0 {
            A!().max_hp
        } else {
            std::cmp::max(1, ((A!().max_hp as f64) * ratio).floor() as i64)
        };
        A!().hp = std::cmp::min(A!().max_hp, A!().hp + heal);
        let sc = A!().stockpile_count;
        for stx in [1u8, 3u8] {
            let v = A!().stage(stx);
            A!().set_stage(stx, std::cmp::max(-6, v - sc as i32));
        }
        A!().stockpile_count = 0;
        return;
    }

    // 回復技
    if n == l.なまける
        || n == l.じこさいせい
        || n == l.あさのひざし
        || n == l.こうごうせい
        || n == l.つきのひかり
        || n == l.はねやすめ
        || n == l.タマゴうみ
        || n == l.ミルクのみ
    {
        if A!().heal_block_count > 0 {
            return;
        }
        let heal = if n == l.あさのひざし || n == l.こうごうせい || n == l.つきのひかり {
            let ew = effective_weather(pack, field, Some(&A!()));
            if ew == Some(we.sunny) {
                A!().max_hp * 2 / 3
            } else if ew == Some(we.rain) || ew == Some(we.sandstorm) || ew == Some(we.hail) {
                A!().max_hp / 4
            } else {
                A!().max_hp / 2
            }
        } else {
            A!().max_hp / 2
        };
        A!().hp = std::cmp::min(A!().max_hp, A!().hp + heal);
        if n == l.はねやすめ && A!().has_type(pack.tc.ひこう) {
            A!().roost_types = Some((A!().type1, A!().type2));
            let mut rem: Vec<Ty> = Vec::new();
            if A!().type1 != pack.tc.ひこう {
                rem.push(A!().type1);
            }
            if let Some(t2) = A!().type2 {
                if t2 != pack.tc.ひこう {
                    rem.push(t2);
                }
            }
            A!().type1 = if rem.is_empty() { pack.tc.ノーマル } else { rem[0] };
            A!().type2 = if rem.len() > 1 { Some(rem[1]) } else { None };
        }
        return;
    }

    if n == l.ねむる {
        if A!().heal_block_count > 0 {
            return;
        }
        if A!().hp >= A!().max_hp {
            return;
        }
        A!().hp = A!().max_hp;
        A!().status = Some(st.sleep);
        A!().sleep_count = 2;
        A!().bad_poison_count = 0;
        return;
    }

    if n == l.はらだいこ {
        if A!().hp <= A!().max_hp / 2 {
            return;
        }
        let cost = A!().max_hp / 2;
        A!().hp = std::cmp::max(1, A!().hp - cost);
        A!().stage_attack = 6;
        return;
    }

    if n == l.いたみわけ {
        let avg = (A!().hp + D!().hp) / 2;
        A!().hp = std::cmp::min(A!().max_hp, avg);
        D!().hp = std::cmp::min(D!().max_hp, avg);
        if D!().hp <= 0 {
            D!().hp = 0;
            D!().is_alive = false;
        }
        return;
    }

    if n == l.やどりぎのタネ {
        if !D!().has_type(pack.tc.くさ) {
            D!().seeded = true;
        }
        return;
    }

    if n == l.あくび {
        if D!().status.is_none() && D!().yawn_count == 0 {
            let dab = D!().ability;
            if dab != l.ふみん && dab != l.やるき {
                D!().yawn_count = 2;
            }
        }
        return;
    }

    if n == l.アンコール {
        if D!().ability == l.アロマベール {
        } else if D!().last_used_move.is_some() && D!().encore_count == 0 {
            D!().encore_count = 3;
            D!().locked_move = D!().last_used_move;
        }
        return;
    }

    if n == l.ちょうはつ {
        if D!().ability == l.アロマベール {
        } else if D!().taunt_count == 0 {
            D!().taunt_count = 3;
        }
        return;
    }

    if n == l.きあいだめ {
        A!().crit_stage = std::cmp::min(3, A!().crit_stage + 2);
        return;
    }
    if n == l.ドラゴンエール {
        let bonus = if A!().has_type(pack.tc.ドラゴン) { 2 } else { 1 };
        A!().crit_stage = std::cmp::min(3, A!().crit_stage + bonus);
        return;
    }

    if n == l.せいちょう {
        let amt = if effective_weather(pack, field, Some(&A!())) == Some(we.sunny) { 2 } else { 1 };
        for stx in [0u8, 2u8] {
            let v = A!().stage(stx);
            A!().set_stage(stx, std::cmp::min(6, v + amt));
        }
        return;
    }

    if n == l.はいすいのじん && A!().trapped {
        return;
    }

    if let Some(boosts) = self_boosts(pack, n) {
        for (attr, delta) in boosts {
            let d = if A!().ability == l.あまのじゃく { -delta } else { delta };
            let val = A!().stage(attr);
            let new_val = (val + d).clamp(-6, 6);
            A!().set_stage(attr, new_val);
            if new_val != val {
                if d > 0 && D!().is_alive && D!().ability == l.びんじょう {
                    let ov = D!().stage(attr);
                    D!().set_stage(attr, std::cmp::min(6, ov + d));
                }
            }
        }
        if n == l.ちいさくなる {
            A!().minimized = true;
        }
        if n == l.はいすいのじん {
            A!().trapped = true;
        }
        return;
    }

    // SELF_STATE
    if n == l.ねをはる {
        A!().rooted = true;
        return;
    }
    if n == l.アクアリング {
        A!().aqua_ring = true;
        return;
    }
    if n == l.でんじふゆう {
        A!().magnet_rise = true;
        return;
    }
    if n == l.ロックオン {
        A!().lock_on = true;
        return;
    }
    if n == l.ふういん {
        A!().sealed = true;
        return;
    }

    if n == l.とおぼえ {
        A!().stage_attack = std::cmp::min(6, A!().stage_attack + 1);
        return;
    }

    if n == l.つぼをつく {
        let k = rng.choice(7) as u8;
        let v = A!().stage(k);
        A!().set_stage(k, std::cmp::min(6, v + 2));
        return;
    }

    if n == l.じゅうりょく {
        field.gravity = 5;
        return;
    }
    if n == l.マジックルーム {
        field.magic_room = 5;
        return;
    }
    if n == l.ワンダールーム {
        field.wonder_room = 5;
        return;
    }

    if n == l.しんぴのまもり {
        sides[aidx].safeguard = 5;
        return;
    }

    if n == l.ミラータイプ {
        let (t1, t2) = (D!().type1, D!().type2);
        A!().type1 = t1;
        A!().type2 = t2;
        return;
    }

    if n == l.なかまづくり {
        let a = A!().ability;
        D!().ability = a;
        return;
    }
    if n == l.なりきり {
        let d = D!().ability;
        A!().ability = d;
        return;
    }
    if n == l.スキルスワップ {
        let (a, d) = (A!().ability, D!().ability);
        A!().ability = d;
        D!().ability = a;
        return;
    }

    if n == l.じこあんじ {
        for i in 0..7u8 {
            let v = D!().stage(i);
            A!().set_stage(i, v);
        }
        return;
    }

    if n == l.スピードスワップ {
        let (a, d) = (A!().speed, D!().speed);
        A!().speed = d;
        D!().speed = a;
        return;
    }
    if n == l.パワースワップ {
        for i in [0u8, 2u8] {
            let (a, d) = (A!().stage(i), D!().stage(i));
            A!().set_stage(i, d);
            D!().set_stage(i, a);
        }
        return;
    }
    if n == l.ガードスワップ {
        for i in [1u8, 3u8] {
            let (a, d) = (A!().stage(i), D!().stage(i));
            A!().set_stage(i, d);
            D!().set_stage(i, a);
        }
        return;
    }
    if n == l.パワートリック {
        let (a, b) = (A!().attack, A!().defense);
        A!().attack = b;
        A!().defense = a;
        return;
    }
    if n == l.ガードシェア {
        for i in [1u8, 3u8] {
            let avg = (A!().raw_stat(i) + D!().raw_stat(i)) / 2;
            A!().set_raw_stat(i, avg);
            D!().set_raw_stat(i, avg);
        }
        return;
    }
    if n == l.パワーシェア {
        for i in [0u8, 2u8] {
            let avg = (A!().raw_stat(i) + D!().raw_stat(i)) / 2;
            A!().set_raw_stat(i, avg);
            D!().set_raw_stat(i, avg);
        }
        return;
    }
    if n == l.すりかえ {
        if is_megastone(pack, A!().item) || is_megastone(pack, D!().item) {
            return;
        }
        let (a, d) = (A!().item, D!().item);
        A!().item = d;
        D!().item = a;
        return;
    }
    if n == l.グラスフィールド {
        field.grassy_terrain = true;
        field.grassy_terrain_count = 5;
        return;
    }
    if n == l.リサイクル {
        let consumed = A!().last_consumed_item;
        if A!().item.is_none() && consumed.is_some() {
            A!().item = consumed;
            A!().last_consumed_item = None;
        }
        return;
    }
    if n == l.まねっこ || n == l.さいはい {
        let mut copy_mv = D!().last_move_obj.clone();
        if copy_mv.is_none() {
            let lum = D!().last_used_move;
            copy_mv = D!().moves.iter().find(|m| Some(m.name) == lum).cloned();
        }
        if let Some(cm) = copy_mv {
            let cn = cm.name;
            let uncopyable = cn == l.まねっこ
                || cn == l.さいはい
                || cn == l.オウムがえし
                || cn == l.ものまね
                || cn == l.スケッチ
                || cn == l.へんしん
                || cn == l.わるあがき;
            if !uncopyable {
                let act = Action { kind: ActKind::Move, mv: Some(cm), ..Default::default() };
                execute_move(pack, sides, field, aidx, &act, None, rng);
            }
        }
        return;
    }
    if n == l.ねごと {
        if A!().status == Some(st.sleep) {
            let cands: Vec<usize> =
                (0..A!().moves.len()).filter(|&i| A!().moves[i].name != l.ねごと).collect();
            if !cands.is_empty() {
                let k = rng.choice(cands.len());
                let chosen = A!().moves[cands[k]].clone();
                let act = Action { kind: ActKind::Move, mv: Some(chosen), ..Default::default() };
                execute_move(pack, sides, field, aidx, &act, None, rng);
            }
        }
        return;
    }
    if n == l.そうでん {
        D!().electrified = true;
        return;
    }

    // メロメロ（性別なしのため必ず失敗）
    if n == l.メロメロ {
        return;
    }
    if n == l.でんじは && D!().has_type(pack.tc.じめん) {
        return;
    }
    let is_powder = n == l.ねむりごな
        || n == l.しびれごな
        || n == l.どくのこな
        || n == l.キノコのほうし
        || n == l.わたほうし
        || n == l.いかりのこな
        || n == l.まほうのこな;
    if is_powder
        && (D!().has_type(pack.tc.くさ)
            || D!().ability == l.ぼうじん
            || D!().item == Some(l.ぼうじんゴーグル))
    {
        return;
    }

    if let Some((debs,)) = opponent_debuffs(pack, n) {
        if D!().ability == l.マジックミラー {
            if A!().ability != l.マジックミラー {
                apply_status_move(pack, sides, field, didx, mv, rng);
            }
            return;
        }
        let sg = sides[didx].safeguard > 0;
        for deb in debs {
            match deb {
                Deb::Status(val) => {
                    if sg {
                        continue;
                    }
                    let dab = D!().ability;
                    if val == st.sleep
                        && (dab == l.ふみん || dab == l.やるき || dab == l.スイートベール)
                    {
                        continue;
                    }
                    if dab == l.リーフガード
                        && effective_weather(pack, field, Some(&D!())) == Some(we.sunny)
                    {
                        continue;
                    }
                    let corr = A!().ability == l.ふしょく;
                    let ok = apply_status(pack, &mut D!(), val, corr);
                    if ok {
                        if val == st.sleep {
                            D!().sleep_count = rng.randint(1, 3);
                        }
                        it::try_cure_berry(pack, &mut D!());
                        if D!().ability == l.シンクロ
                            && (val == st.poison
                                || val == st.badpoison
                                || val == st.paralysis
                                || val == st.burn)
                            && A!().is_alive
                        {
                            apply_status(pack, &mut A!(), val, false);
                        }
                    }
                }
                Deb::Confused => {
                    if sg {
                    } else if D!().ability == l.マイペース {
                    } else {
                        D!().confused = true;
                        it::try_cure_berry(pack, &mut D!());
                    }
                }
                Deb::Stage(attr, val) => {
                    let v = if D!().ability == l.あまのじゃく { -val } else { val };
                    let dab = D!().ability;
                    if v < 0
                        && (dab == l.クリアボディ
                            || dab == l.しろいけむり
                            || dab == l.かがくへんかガス)
                    {
                        continue;
                    }
                    let old_v = D!().stage(attr);
                    let new_v = (old_v + v).clamp(-6, 6);
                    D!().set_stage(attr, new_v);
                    if new_v != old_v && v < 0 {
                        ab::on_stat_lowered(pack, &mut D!());
                    }
                }
                Deb::Infatuation => {
                    D!().infatuation = true;
                }
                Deb::Torment => {
                    D!().torment = true;
                }
                Deb::Trapped => {
                    D!().trapped = true;
                }
                Deb::AbilitySuppressed => {
                    D!().ability_suppressed = true;
                }
                Deb::AbilityChange(v) => {
                    D!().ability = v;
                }
                Deb::TypeAdd(t) => {
                    if D!().type1 != t && D!().type2 != Some(t) {
                        if D!().type2.is_none() {
                            D!().type2 = Some(t);
                        } else {
                            D!().type1 = t;
                        }
                    }
                }
                Deb::TypeSet(t) => {
                    D!().type1 = t;
                    D!().type2 = None;
                }
                Deb::PpReduce(v) => {
                    if let Some(lum) = D!().last_used_move {
                        let np = D!().pp.len();
                        for i in 0..D!().moves.len() {
                            if D!().moves[i].name == lum && i < np {
                                D!().pp[i] = std::cmp::max(0, D!().pp[i] - v);
                                break;
                            }
                        }
                    }
                }
            }
        }
        return;
    }

    // 強制交代
    if n == l.ほえる || n == l.ふきとばし {
        let mut blocked = false;
        let dab = D!().ability;
        if dab == l.マジックミラー {
            blocked = true;
            if A!().ability != l.マジックミラー {
                A!().force_switch = true;
            }
        } else if dab == l.おうごんのからだ {
            blocked = true;
        } else if dab == l.きゅうばん {
            blocked = true;
        } else if n == l.ほえる && dab == l.ぼうおん {
            blocked = true;
        } else if n == l.ふきとばし && dab == l.かぜのり {
            blocked = true;
        }
        if !blocked {
            for i in 0..7u8 {
                D!().set_stage(i, 0);
            }
            D!().force_switch = true;
        }
        return;
    }

    if n == l.くろいきり {
        for i in 0..7u8 {
            A!().set_stage(i, 0);
            D!().set_stage(i, 0);
        }
        return;
    }

    if n == l.みちづれ {
        if A!().destiny_bond_last_turn {
            return;
        }
        A!().destiny_bond = true;
        A!().destiny_bond_last_turn = true;
        return;
    }

    if n == l.ほろびのうた {
        if A!().perish_count == 0 {
            A!().perish_count = 3;
        }
        if D!().perish_count == 0 {
            D!().perish_count = 3;
        }
        return;
    }

    if n == l.ねがいごと {
        if sides[aidx].wish_count == 0 {
            sides[aidx].wish_hp = A!().max_hp / 2;
            sides[aidx].wish_count = 2;
        }
        return;
    }

    if n == l.いやしのねがい {
        sides[aidx].healing_wish = true;
        let hp = A!().hp;
        A!().take_damage(hp);
        A!().is_alive = false;
        return;
    }

    if n == l.おきみやげ {
        for stx in [0u8, 2u8] {
            let dab = D!().ability;
            if dab != l.クリアボディ && dab != l.しろいけむり && dab != l.かがくへんかガス {
                let old_v = D!().stage(stx);
                D!().set_stage(stx, std::cmp::max(-6, old_v - 2));
            }
        }
        let hp = A!().hp;
        A!().take_damage(hp);
        A!().is_alive = false;
        return;
    }

    if n == l.どくびし {
        let idx = sides[didx].field_idx;
        if field.toxic_spikes[idx] < 2 {
            field.toxic_spikes[idx] += 1;
        }
        return;
    }
    if n == l.ねばねばネット {
        let idx = sides[didx].field_idx;
        if !field.sticky_web[idx] {
            field.sticky_web[idx] = true;
        }
        return;
    }
    if n == l.きりばらい {
        let dab = D!().ability;
        if dab != l.クリアボディ && dab != l.しろいけむり && dab != l.かがくへんかガス {
            D!().stage_evasion = std::cmp::max(-6, D!().stage_evasion - 1);
        }
        for sx in [aidx, didx] {
            let idx = sides[sx].field_idx;
            field.spikes[idx] = 0;
            field.toxic_spikes[idx] = 0;
            field.sticky_web[idx] = false;
            field.stealth_rock[idx] = false;
            sides[sx].reflect = false;
            sides[sx].light_screen = false;
            sides[sx].aurora_veil = false;
        }
        return;
    }
    if n == l.おかたづけ {
        for sx in [aidx, didx] {
            let idx = sides[sx].field_idx;
            field.spikes[idx] = 0;
            field.toxic_spikes[idx] = 0;
            field.sticky_web[idx] = false;
        }
        A!().stage_attack = std::cmp::min(6, A!().stage_attack + 1);
        A!().stage_speed = std::cmp::min(6, A!().stage_speed + 1);
        return;
    }
    if n == l.みずびたし {
        D!().type1 = pack.tc.みず;
        D!().type2 = None;
        return;
    }
    if n == l.のろい {
        if A!().has_type(pack.tc.ゴースト) {
            let cost = std::cmp::max(1, A!().max_hp / 4);
            A!().take_damage(cost);
            D!().cursed = true;
        } else {
            A!().stage_attack = std::cmp::min(6, A!().stage_attack + 1);
            A!().stage_defense = std::cmp::min(6, A!().stage_defense + 1);
            A!().stage_speed = std::cmp::max(-6, A!().stage_speed - 1);
        }
        return;
    }
    if n == l.バトンタッチ {
        let mut bs = [0i32; 7];
        for i in 0..7u8 {
            bs[i as usize] = A!().stage(i);
        }
        A!().baton_stages = Some(bs);
        A!().pivot_out = true;
        return;
    }
    if n == l.トリック {
        if is_megastone(pack, A!().item) || is_megastone(pack, D!().item) {
            return;
        }
        let (a, d) = (A!().item, D!().item);
        A!().item = d;
        D!().item = a;
        return;
    }
    if n == l.ミストフィールド {
        field.misty_terrain = true;
        field.misty_terrain_count = 5;
        return;
    }
    if n == l.エレキフィールド {
        field.electric_terrain = true;
        field.electric_terrain_count = 5;
        return;
    }
    if n == l.サイコフィールド {
        field.psychic_terrain = true;
        field.psychic_terrain_count = 5;
        return;
    }
    if n == l.じゅうでん {
        A!().charged = true;
        A!().stage_sp_defense = std::cmp::min(6, A!().stage_sp_defense + 1);
        return;
    }
    if n == l.しっぽきり {
        let cost = A!().max_hp / 2;
        let sub_hp = A!().max_hp / 4;
        if A!().hp > cost && A!().substitute_hp == 0 {
            A!().hp -= cost;
            A!().substitute_hp = sub_hp;
            A!().pivot_out = true;
        }
        return;
    }
    if n == l.ちからをすいとる {
        let heal = D!().eff_stat(0);
        A!().hp = std::cmp::min(A!().max_hp, A!().hp + heal);
        let dab = D!().ability;
        if dab != l.クリアボディ && dab != l.しろいけむり && dab != l.かがくへんかガス {
            D!().stage_attack = std::cmp::max(-6, D!().stage_attack - 1);
        }
        return;
    }
    if n == l.ほおばる {
        if is_berry(pack, A!().item) {
            A!().item = None;
            A!().ate_berry = true;
            A!().stage_defense = std::cmp::min(6, A!().stage_defense + 2);
        }
        return;
    }
    if n == l.かなしばり {
        if D!().last_used_move.is_some() && D!().disabled_move.is_none() {
            D!().disabled_move = D!().last_used_move;
            D!().disabled_turns = 4;
        }
        return;
    }
    if n == l.ソウルビート {
        let cost = std::cmp::max(1, A!().max_hp / 3);
        if A!().hp > cost {
            A!().hp -= cost;
            for i in 0..5u8 {
                let v = A!().stage(i);
                A!().set_stage(i, std::cmp::min(6, v + 1));
            }
        }
        return;
    }
    if n == l.へんしん {
        if A!().transformed {
            return;
        }
        let bak = crate::poke::TransformBackup {
            attack: A!().attack,
            defense: A!().defense,
            sp_attack: A!().sp_attack,
            sp_defense: A!().sp_defense,
            speed: A!().speed,
            ability: A!().ability,
            moves: A!().moves.clone(),
            pp: A!().pp.clone(),
        };
        A!().transform_backup = Some(Box::new(bak));
        let (dat, ddf, dsa, dsd, dsp, dab, dt1, dt2) = (
            D!().attack,
            D!().defense,
            D!().sp_attack,
            D!().sp_defense,
            D!().speed,
            D!().ability,
            D!().type1,
            D!().type2,
        );
        let dmoves = D!().moves.clone();
        let dstages: [i32; 7] = {
            let mut s = [0i32; 7];
            for i in 0..7u8 {
                s[i as usize] = D!().stage(i);
            }
            s
        };
        A!().attack = dat;
        A!().defense = ddf;
        A!().sp_attack = dsa;
        A!().sp_defense = dsd;
        A!().speed = dsp;
        A!().ability = dab;
        A!().type1 = dt1;
        A!().type2 = dt2;
        A!().pp = dmoves.iter().map(|m| std::cmp::min(5, m.pp.unwrap_or(5))).collect();
        A!().moves = dmoves;
        for i in 0..7u8 {
            A!().set_stage(i, dstages[i as usize]);
        }
        A!().transformed = true;
        return;
    }
}

// ══════════════════════════════════════════════════════════════════════════
//  _apply_secondary / _apply_recoil
// ══════════════════════════════════════════════════════════════════════════

/// STATUS_EFFECTS: (状態 or None=confused, 確率)
fn status_effects(pack: &Pack, n: u16) -> Option<(Option<u16>, f64)> {
    let l = &pack.sy.l;
    let s = &pack.sy.st;
    let r = if n == l._10まんボルト {
        (Some(s.paralysis), 0.10)
    } else if n == l.かみなり {
        (Some(s.paralysis), 0.30)
    } else if n == l.ボルテッカー {
        (Some(s.paralysis), 0.10)
    } else if n == l.でんきショック {
        (Some(s.paralysis), 0.10)
    } else if n == l.スパーク {
        (Some(s.paralysis), 0.30)
    } else if n == l.りゅうのいぶき {
        (Some(s.paralysis), 0.30)
    } else if n == l.ほうでん {
        (Some(s.paralysis), 0.30)
    } else if n == l.かみなりのキバ {
        (Some(s.paralysis), 0.10)
    } else if n == l.かみなりパンチ {
        (Some(s.paralysis), 0.10)
    } else if n == l.ほっぺすりすり {
        (Some(s.paralysis), 1.00)
    } else if n == l.でんじほう {
        (Some(s.paralysis), 1.00)
    } else if n == l.のしかかり {
        (Some(s.paralysis), 0.30)
    } else if n == l.とびはねる {
        (Some(s.paralysis), 0.30)
    } else if n == l.かえんほうしゃ {
        (Some(s.burn), 0.10)
    } else if n == l.フレアドライブ {
        (Some(s.burn), 0.10)
    } else if n == l.だいもんじ {
        (Some(s.burn), 0.10)
    } else if n == l.かえんぐるま {
        (Some(s.burn), 0.10)
    } else if n == l.ねっとう {
        (Some(s.burn), 0.30)
    } else if n == l.ほのおのキバ {
        (Some(s.burn), 0.10)
    } else if n == l.ほのおのパンチ {
        (Some(s.burn), 0.10)
    } else if n == l.ブレイズキック {
        (Some(s.burn), 0.10)
    } else if n == l.ふんえん {
        (Some(s.burn), 0.30)
    } else if n == l.ねっぷう {
        (Some(s.burn), 0.10)
    } else if n == l.ねっさのだいち {
        (Some(s.burn), 0.30)
    } else if n == l.ひゃっきやこう {
        (Some(s.burn), 0.30)
    } else if n == l.れんごく {
        (Some(s.burn), 1.00)
    } else if n == l.シャカシャカほう {
        (Some(s.burn), 0.20)
    } else if n == l.れいとうビーム {
        (Some(s.freeze), 0.10)
    } else if n == l.ふぶき {
        (Some(s.freeze), 0.10)
    } else if n == l.アイスビーム {
        (Some(s.freeze), 0.10)
    } else if n == l.こおりのキバ {
        (Some(s.freeze), 0.10)
    } else if n == l.れいとうパンチ {
        (Some(s.freeze), 0.10)
    } else if n == l.どくづき {
        (Some(s.poison), 0.30)
    } else if n == l.クロスポイズン {
        (Some(s.poison), 0.10)
    } else if n == l.どくどくのキバ {
        (Some(s.badpoison), 0.50)
    } else if n == l.ヘドロばくだん {
        (Some(s.poison), 0.30)
    } else if n == l.ヘドロウェーブ {
        (Some(s.poison), 0.10)
    } else if n == l.ダストシュート {
        (Some(s.poison), 0.30)
    } else if n == l.シェルアームズ {
        (Some(s.poison), 0.20)
    } else if n == l.どくばりセンボン {
        (Some(s.poison), 0.50)
    } else if n == l.ウォーターパルス {
        (None, 0.20)
    } else if n == l.みずのはどう {
        (None, 0.20)
    } else if n == l.ダイナミックフル {
        (None, 0.10)
    } else if n == l.ぼうふう {
        (None, 0.30)
    } else if n == l.ばくれつパンチ {
        (None, 1.00)
    } else if n == l.かかとおとし {
        (None, 0.30)
    } else {
        return None;
    };
    Some(r)
}

/// DEF_DOWNS: (stat, delta, prob)
fn def_downs(pack: &Pack, n: u16) -> Option<(u8, i32, f64)> {
    let l = &pack.sy.l;
    let r = if n == l.かみくだく {
        (1u8, -1i32, 0.20)
    } else if n == l.クラッシュクロー {
        (1, -1, 0.50)
    } else if n == l.バークアウト {
        (2, -1, 1.00)
    } else if n == l.こごえるかぜ {
        (4, -1, 1.00)
    } else if n == l.がんせきふうじ {
        (4, -1, 1.00)
    } else if n == l.じならし {
        (4, -1, 1.00)
    } else if n == l.バブルこうせん {
        (4, -1, 0.10)
    } else if n == l.バブルだま {
        (4, -1, 0.10)
    } else if n == l.キャタストロフィ {
        (1, -1, 0.20)
    } else if n == l.マッドショット {
        (4, -1, 1.00)
    } else if n == l.アクアブレイク {
        (1, -1, 0.20)
    } else if n == l.ワタシらしく {
        (2, -1, 1.00)
    } else if n == l.ルミナコリジョン {
        (3, -2, 1.00)
    } else if n == l.マジカルフレイム {
        (2, -1, 1.00)
    } else if n == l.エレキネット {
        (4, -1, 1.00)
    } else if n == l.シャドーボール {
        (3, -1, 0.20)
    } else if n == l.サイコキネシス {
        (3, -1, 0.10)
    } else if n == l.エナジーボール {
        (3, -1, 0.10)
    } else if n == l.むしのさざめき {
        (3, -1, 0.10)
    } else if n == l.じゃれつく {
        (0, -1, 0.10)
    } else if n == l.ムーンフォース {
        (2, -1, 0.30)
    } else if n == l.ナイトバースト {
        (5, -1, 0.40)
    } else if n == l.だくりゅう {
        (5, -1, 1.00)
    } else if n == l.どろかけ {
        (5, -1, 1.00)
    } else if n == l.アイアンテール {
        (1, -1, 0.30)
    } else if n == l.トロピカルキック {
        (0, -1, 1.00)
    } else if n == l.はいよるいちげき {
        (2, -1, 1.00)
    } else if n == l.ひやみず {
        (0, -1, 1.00)
    } else if n == l.むしのていこう {
        (2, -1, 1.00)
    } else if n == l.Gのちから {
        (1, -1, 1.00)
    } else if n == l.とびつく {
        (4, -1, 1.00)
    } else if n == l.りんごさん {
        (3, -1, 1.00)
    } else if n == l.きあいだま {
        (3, -1, 0.10)
    } else if n == l.アシッドボム {
        (3, -2, 1.00)
    } else if n == l.シェルブレード {
        (1, -1, 0.50)
    } else if n == l._3ぼんのや {
        (1, -1, 0.50)
    } else if n == l.だいちのちから {
        (3, -1, 0.10)
    } else if n == l.とびかかる {
        (0, -1, 1.00)
    } else if n == l.ラスターカノン {
        (3, -1, 0.10)
    } else if n == l.ほのおのムチ {
        (1, -1, 1.00)
    } else if n == l.ブレイククロー {
        (1, -1, 0.50)
    } else if n == l.ローキック {
        (4, -1, 1.00)
    } else if n == l.ワイドブレイカー {
        (0, -1, 1.00)
    } else if n == l.ソウルクラッシュ {
        (2, -1, 1.00)
    } else {
        return None;
    };
    Some(r)
}

/// SELF_EFFECTS（KO時に発動するサブセットは self_effects_ko）
fn self_effects(pack: &Pack, n: u16) -> Option<Vec<(u8, i32, f64)>> {
    let l = &pack.sy.l;
    let v = if n == l.インファイト || n == l.クローズコンバット {
        vec![(1u8, -1i32, 1.0f64), (3, -1, 1.0)]
    } else if n == l.ばかぢから {
        vec![(0, -1, 1.0), (1, -1, 1.0)]
    } else if n == l.りゅうせいぐん
        || n == l.リーフストーム
        || n == l.オーバーヒート
        || n == l.サイコブースト
        || n == l.ゴールドラッシュ
    {
        vec![(2, -2, 1.0)]
    } else if n == l.だいばくはつ || n == l.じばく {
        vec![]
    } else if n == l.フレアソング {
        vec![(2, 1, 1.0)]
    } else if n == l.ほのおのまい {
        vec![(2, 1, 0.50)]
    } else if n == l.チャージビーム {
        vec![(2, 1, 0.70)]
    } else if n == l.ニトロチャージ || n == l.アクアステップ || n == l.くさわけ {
        vec![(4, 1, 1.0)]
    } else if n == l.コメットパンチ {
        vec![(0, 1, 0.20)]
    } else if n == l.アームハンマー {
        vec![(4, -1, 1.0)]
    } else if n == l.アーマーキャノン {
        vec![(1, -1, 1.0), (3, -1, 1.0)]
    } else if n == l.オーラぐるま {
        vec![(4, 1, 1.0)]
    } else if n == l.バリアーラッシュ {
        vec![(1, 1, 1.0)]
    } else if n == l.はがねのつばさ {
        vec![(1, 1, 0.10)]
    } else if n == l.ぶちかまし {
        vec![(1, -1, 1.0), (3, -1, 1.0)]
    } else if n == l.アイスハンマー {
        vec![(4, -1, 1.0)]
    } else if n == l.スケイルノイズ {
        vec![(1, -1, 1.0)]
    } else if n == l.スケイルショット {
        vec![(1, -1, 1.0), (4, 1, 1.0)]
    } else {
        return None;
    };
    Some(v)
}

fn self_effects_ko(pack: &Pack, n: u16) -> Option<Vec<(u8, i32, f64)>> {
    let l = &pack.sy.l;
    let v = if n == l.インファイト || n == l.クローズコンバット {
        vec![(1u8, -1i32, 1.0f64), (3, -1, 1.0)]
    } else if n == l.ばかぢから {
        vec![(0, -1, 1.0), (1, -1, 1.0)]
    } else if n == l.りゅうせいぐん
        || n == l.リーフストーム
        || n == l.オーバーヒート
        || n == l.サイコブースト
        || n == l.ゴールドラッシュ
    {
        vec![(2, -2, 1.0)]
    } else if n == l.アームハンマー {
        vec![(4, -1, 1.0)]
    } else if n == l.アーマーキャノン {
        vec![(1, -1, 1.0), (3, -1, 1.0)]
    } else if n == l.とどめばり {
        vec![(0, 3, 1.0)]
    } else {
        return None;
    };
    Some(v)
}

fn flinch_prob(pack: &Pack, n: u16) -> Option<f64> {
    let l = &pack.sy.l;
    let p = if n == l.エアスラッシュ {
        0.30
    } else if n == l.アイアンヘッド {
        0.20
    } else if n == l._3ぼんのや {
        0.30
    } else if n == l.がんせきおとし {
        0.30
    } else if n == l.いわなだれ {
        0.30
    } else if n == l.ほのおのキバ || n == l.かみなりのキバ || n == l.こおりのキバ {
        0.10
    } else if n == l.ウォーターフォール || n == l.たきのぼり {
        0.20
    } else if n == l.あくのはどう {
        0.20
    } else if n == l.かみつく {
        0.30
    } else if n == l.しねんのずつき {
        0.20
    } else if n == l.ねこだまし {
        1.00
    } else if n == l.スピードスター {
        0.0
    } else if n == l.いびき {
        0.30
    } else if n == l.じんつうりき {
        0.10
    } else if n == l.つららおとし || n == l.ひょうざんおろし {
        0.30
    } else if n == l.ゴッドバード {
        0.30
    } else if n == l.ドラゴンダイブ {
        0.20
    } else if n == l.はやてがえし {
        1.00
    } else {
        return None;
    };
    Some(p)
}

pub fn apply_secondary(
    pack: &Pack,
    attacker: &mut Poke,
    defender: &mut Poke,
    mv: &DMove,
    dmg: i64,
    field: &Field,
    def_safeguard: i64,
    rng: &mut dyn BRng,
) {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    let we = &pack.sy.we;
    let n = mv.name;

    if !defender.is_alive {
        if let Some(effs) = self_effects_ko(pack, n) {
            for (stat, delta, prob) in effs {
                if rng.random() < prob {
                    let old_val = attacker.stage(stat);
                    let new_val = (old_val + delta).clamp(-6, 6);
                    attacker.set_stage(stat, new_val);
                }
            }
        }
        return;
    }

    if dmg > 0 {
        defender.times_hit += 1;
    }

    let force_no_secondary = attacker.ability == l.ちからずく || defender.ability == l.りんぷん;

    if n == l.じごくづき && dmg > 0 && defender.is_alive {
        defender.throat_chop_count = 2;
    }

    let is_bind = n == l.まきつく
        || n == l.しめつける
        || n == l.まとわりつく
        || n == l.ほのおのうず
        || n == l.うずしお
        || n == l.すなじごく
        || n == l.トラバサミ;
    if is_bind && dmg > 0 && defender.is_alive && defender.bound_count == 0 {
        defender.bound_count = rng.randint(4, 5);
    }

    if n == l.なげつける && defender.is_alive && !force_no_secondary {
        let flung = attacker.last_flung_item;
        let s2 = if flung == Some(l.どくバリ) {
            Some(st.poison)
        } else if flung == Some(l.もうどくだま) {
            Some(st.badpoison)
        } else {
            None
        };
        if let Some(sv) = s2 {
            let ok = apply_status(pack, defender, sv, false);
            if ok {
                it::try_cure_berry(pack, defender);
            }
        }
    }

    let sg_sec = def_safeguard > 0;
    if let Some((effect, prob)) = status_effects(pack, n) {
        if !force_no_secondary && !sg_sec {
            let sunny_freeze = effect == Some(st.freeze)
                && effective_weather(pack, field, Some(defender)) == Some(we.sunny);
            if sunny_freeze {
                // 何もしない
            } else if rng.random() < prob {
                match effect {
                    None => {
                        if defender.ability != l.マイペース {
                            defender.confused = true;
                            it::try_cure_berry(pack, defender);
                        }
                    }
                    Some(e) => {
                        let ok = apply_status(pack, defender, e, false);
                        if ok {
                            it::try_cure_berry(pack, defender);
                        }
                    }
                }
            }
        }
    }

    if n == l.トライアタック && !force_no_secondary && rng.random() < 0.20 {
        let idx = rng.choice(3);
        let effect = [st.paralysis, st.burn, st.freeze][idx];
        if !(effect == st.freeze
            && effective_weather(pack, field, Some(defender)) == Some(we.sunny))
        {
            let ok = apply_status(pack, defender, effect, false);
            if ok {
                it::try_cure_berry(pack, defender);
            }
        }
    }

    if (n == l.しっとのほのお || n == l.みわくのボイス) && !force_no_secondary {
        let any_up = (0..7u8).any(|i| defender.stage(i) > 0);
        if any_up {
            if n == l.みわくのボイス {
                if defender.ability != l.マイペース {
                    defender.confused = true;
                    it::try_cure_berry(pack, defender);
                }
            } else if apply_status(pack, defender, st.burn, false) {
                it::try_cure_berry(pack, defender);
            }
        }
    }

    if defender.ability == l.りんぷん {
        return;
    }

    if let Some((stat, delta0, prob)) = def_downs(pack, n) {
        if !force_no_secondary {
            let mut delta = delta0;
            if defender.ability == l.あまのじゃく {
                delta = -delta;
            }
            let mut blocked = false;
            if delta < 0 {
                let dab = defender.ability;
                if dab == l.ミラーアーマー && rng.random() < prob {
                    let ov = attacker.stage(stat);
                    attacker.set_stage(stat, std::cmp::max(-6, ov + delta));
                    return;
                }
                if dab == l.クリアボディ || dab == l.しろいけむり || dab == l.かがくへんかガス {
                    return;
                }
                if stat == 1 && dab == l.はとむね {
                    return;
                }
                if stat == 0 && dab == l.かいりきバサミ {
                    return;
                }
                if stat == 5 && (dab == l.するどいめ || dab == l.はっこう) {
                    return;
                }
            }
            let _ = blocked;
            blocked = false;
            let _ = blocked;
            if rng.random() < prob {
                let old_val = defender.stage(stat);
                let new_val = (old_val + delta).clamp(-6, 6);
                defender.set_stage(stat, new_val);
                if new_val != old_val && delta < 0 {
                    ab::on_stat_lowered(pack, defender);
                }
            }
        }
    }

    if n == l.げんしのちから && !force_no_secondary && rng.random() < 0.10 {
        for i in 0..5u8 {
            let v = attacker.stage(i);
            if v < 6 {
                attacker.set_stage(i, v + 1);
            }
        }
    }
    if let Some(effs) = self_effects(pack, n) {
        for (stat, delta, prob) in effs {
            if rng.random() < prob {
                let d = if attacker.ability == l.あまのじゃく { -delta } else { delta };
                let old_val = attacker.stage(stat);
                let new_val = (old_val + d).clamp(-6, 6);
                attacker.set_stage(stat, new_val);
                if new_val != old_val {
                    if d < 0 {
                        ab::on_stat_lowered(pack, attacker);
                    }
                    if d > 0 && defender.is_alive && defender.ability == l.びんじょう {
                        let ov = defender.stage(stat);
                        defender.set_stage(stat, std::cmp::min(6, ov + d));
                    }
                }
            }
        }
    }

    if n == l.ぶきみなじゅもん && defender.is_alive {
        if let Some(lum) = defender.last_used_move {
            let np = defender.pp.len();
            for i in 0..defender.moves.len() {
                if defender.moves[i].name == lum && i < np {
                    defender.pp[i] = std::cmp::max(0, defender.pp[i] - 3);
                    break;
                }
            }
        }
    }

    if let Some(fp) = flinch_prob(pack, n) {
        if fp > 0.0 && !force_no_secondary && rng.random() < fp {
            if defender.ability != l.せいしんりょく && defender.ability != l.どんかん {
                defender.flinched = true;
            }
        }
    }

    if n == l.フェイタルクロー && defender.is_alive && !force_no_secondary && rng.random() < 0.30 {
        let idx = rng.choice(3);
        let chosen = [st.poison, st.paralysis, st.sleep][idx];
        let ok = apply_status(pack, defender, chosen, false);
        if ok {
            if chosen == st.sleep {
                defender.sleep_count = rng.randint(1, 3);
            }
            it::try_cure_berry(pack, defender);
        }
    }

    if n == l.かげぬい && dmg > 0 && defender.is_alive {
        defender.trapped = true;
    }

    if n == l.ねっとう || n == l.ねっさのだいち {
        if defender.is_alive && defender.status == Some(st.freeze) {
            defender.status = None;
        }
    }
    if n == l.ねっとう || n == l.もえつきる || n == l.ねっさのだいち {
        if attacker.status == Some(st.freeze) {
            attacker.status = None;
        }
    }
    if n == l.もえつきる && attacker.has_type(pack.tc.ほのお) {
        let mut rem: Vec<Ty> = Vec::new();
        if attacker.type1 != pack.tc.ほのお {
            rem.push(attacker.type1);
        }
        if let Some(t2) = attacker.type2 {
            if t2 != pack.tc.ほのお {
                rem.push(t2);
            }
        }
        attacker.type1 = if rem.is_empty() { pack.tc.ノーマル } else { rem[0] };
        attacker.type2 = if rem.len() > 1 { Some(rem[1]) } else { None };
    }

    if n == l.しおづけ && defender.is_alive && !force_no_secondary && !defender.salted {
        defender.salted = true;
    }
    if n == l.みずあめボム && defender.is_alive && !force_no_secondary {
        defender.syrup_count = 3;
    }
    if n == l.サイコノイズ && defender.is_alive && !force_no_secondary {
        defender.heal_block_count = 2;
    }
    if n == l.うたかたのアリア && defender.is_alive && defender.status == Some(st.burn) {
        defender.status = None;
    }
    if n == l.ミストバースト && attacker.is_alive {
        attacker.hp = 0;
        attacker.is_alive = false;
    }

    let is_rage = n == l.げきりん || n == l.あばれる || n == l.はなびらのまい || n == l.だいふんげき;
    if is_rage {
        if attacker.locked_move.is_none() {
            attacker.locked_move = Some(n);
            attacker.lock_count = rng.randint(2, 3);
        } else {
            attacker.lock_count -= 1;
            if attacker.lock_count <= 0 {
                attacker.locked_move = None;
                attacker.lock_count = 0;
                if attacker.ability != l.マイペース {
                    attacker.confused = true;
                    it::try_cure_berry(pack, attacker);
                }
            }
        }
    }
    if n == l.さわぐ {
        if attacker.locked_move.is_none() {
            attacker.locked_move = Some(n);
            attacker.lock_count = rng.randint(2, 3);
        } else {
            attacker.lock_count -= 1;
            if attacker.lock_count <= 0 {
                attacker.locked_move = None;
                attacker.lock_count = 0;
            }
        }
    }

    attacker.last_used_move = Some(n);
}

pub fn apply_recoil(pack: &Pack, attacker: &mut Poke, _defender: &mut Poke, mv: &DMove, dmg: i64) {
    let l = &pack.sy.l;
    let n = mv.name;
    if (attacker.ability == l.いしあたま || attacker.ability == l.ロックヘッド)
        && n != l.わるあがき
    {
        return;
    }
    if n == l.わるあがき {
        let recoil = std::cmp::max(1, ((attacker.max_hp as f64) / 4.0).floor() as i64);
        attacker.take_damage(recoil);
        return;
    }
    if attacker.ability == l.ロックヘッド || attacker.ability == l.マジックガード {
        return;
    }
    if n == l.てっていこうせん {
        let recoil = std::cmp::max(1, attacker.max_hp / 2);
        attacker.take_damage(recoil);
        return;
    }
    let rate = if n == l.すてみタックル
        || n == l.フレアドライブ
        || n == l.ボルテッカー
        || n == l.ウェーブタックル
        || n == l.ブレイブバード
        || n == l.ウッドハンマー
    {
        Some(1.0 / 3.0)
    } else if n == l.もろはのずつき || n == l.はめつのひかり {
        Some(1.0 / 2.0)
    } else if n == l.ワイルドボルト {
        Some(1.0 / 4.0)
    } else {
        None
    };
    if let Some(r) = rate {
        let recoil = std::cmp::max(1, ((dmg as f64) * r).floor() as i64);
        attacker.take_damage(recoil);
    }
}

// ══════════════════════════════════════════════════════════════════════════
//  Battle（ターンループ）
// ══════════════════════════════════════════════════════════════════════════

fn entry_effects_side(pack: &Pack, sides: &mut [Side; 2], field: &mut Field, sx: usize) {
    let (me, opp) = split2(sides, sx);
    let si = me.field_idx;
    let oi = opp.active_idx;
    entry_effects(pack, me, si, field, &mut opp.party[oi]);
}

impl Battle {
    pub fn new(s1: Side, s2: Side, field: Field) -> Battle {
        let mut b = Battle { sides: [s1, s2], field, turn: 0 };
        b.sides[0].field_idx = 0;
        b.sides[1].field_idx = 1;
        b
    }

    fn apply_healing_wish(&mut self, sx: usize) {
        let s = &mut self.sides[sx];
        if s.healing_wish && s.active().is_alive {
            let i = s.active_idx;
            s.party[i].hp = s.party[i].max_hp;
            s.party[i].status = None;
            s.healing_wish = false;
        }
    }

    /// _faint_switch（chooser 未設定＝実戦ハーネスと同じ _best_faint_switch 経路）
    fn faint_switch(&mut self, pack: &Pack, fx: usize, rng: &mut dyn BRng) {
        let ox = 1 - fx;
        loop {
            if self.sides[fx].active().is_alive || !self.sides[fx].has_alive() {
                break;
            }
            let next_idx = {
                let Battle { sides, field, .. } = self;
                let (me, opp) = split2(sides, fx);
                let oi = opp.active_idx;
                best_faint_switch(pack, me, &mut opp.party[oi], field, true, rng)
            };
            let next_idx = match next_idx {
                None => break,
                Some(i) => i,
            };
            self.sides[fx].switch_to(pack, next_idx);
            {
                let Battle { sides, field, .. } = self;
                entry_effects_side(pack, sides, field, fx);
            }
            let nm = self.sides[fx].active().clone();
            self.sides[ox].opp_view.on_enter(&nm);
        }
    }

    fn info_abilities_on_entry(&mut self, pack: &Pack) {
        let l = &pack.sy.l;
        for mx in 0..2usize {
            let ox = 1 - mx;
            let (alive, done, abil) = {
                let me = self.sides[mx].active();
                (me.is_alive, me.info_done, me.ability)
            };
            if !alive || done {
                continue;
            }
            if abil != l.おみとおし && abil != l.きけんよち && abil != l.よちむ {
                continue;
            }
            self.sides[mx].active_mut().info_done = true;
            if abil == l.おみとおし {
                let (on, oitem) = {
                    let o = self.sides[ox].active();
                    (o.name, o.item)
                };
                if let Some(itm) = oitem {
                    self.sides[mx].opp_view.on_item(on, itm);
                }
            }
            if abil == l.きけんよち {
                let (mt1, mt2) = {
                    let me = self.sides[mx].active();
                    (me.type1, me.type2)
                };
                let mut threat = false;
                {
                    let o = self.sides[ox].active();
                    for mvx in o.moves.iter() {
                        if mvx.category == Cat::Status {
                            continue;
                        }
                        if mvx.name == l.じわれ
                            || mvx.name == l.つのドリル
                            || mvx.name == l.ハサミギロチン
                            || mvx.name == l.ぜったいれいど
                        {
                            threat = true;
                            break;
                        }
                        if pack.eff(mvx.ty, mt1, mt2) > 1.0 {
                            threat = true;
                            break;
                        }
                    }
                }
                if threat {
                    let on = self.sides[ox].active().name;
                    self.sides[mx].opp_view.on_anticipation(on);
                }
            }
        }
    }

    /// _do_action
    fn do_action(
        &mut self,
        pack: &Pack,
        mx: usize,
        action: &Action,
        opp_action: Option<&Action>,
        defer_self_faint: bool,
        rng: &mut dyn BRng,
    ) {
        let ox = 1 - mx;
        let l = &pack.sy.l;
        if action.kind == ActKind::Switch {
            let idx = action.switch_to;
            if idx >= 0 && (idx as usize) < self.sides[mx].party.len()
                && self.sides[mx].party[idx as usize].is_alive
            {
                self.sides[mx].switch_to(pack, idx as usize);
                {
                    let Battle { sides, field, .. } = self;
                    entry_effects_side(pack, sides, field, mx);
                }
                self.apply_healing_wish(mx);
                let nm = self.sides[mx].active().clone();
                self.sides[ox].opp_view.on_enter(&nm);
                self.faint_switch(pack, mx, rng);
            }
            return;
        }

        if action.kind == ActKind::Move && action.mv.is_some() {
            {
                let Battle { sides, field, .. } = self;
                execute_move(pack, sides, field, mx, action, opp_action, rng);
            }
            // PP消費
            let mi = action.move_idx;
            {
                let opp_alive = self.sides[ox].active().is_alive;
                let opp_pressure = self.sides[ox].active().ability == l.プレッシャー;
                let s = &mut self.sides[mx];
                let ai = s.active_idx;
                if mi >= 0 && (mi as usize) < s.party[ai].pp.len() {
                    let mut cost = 1;
                    if action.mv.as_ref().map(|m| m.category != Cat::Status).unwrap_or(false)
                        && opp_alive
                        && opp_pressure
                    {
                        cost = 2;
                    }
                    let v = s.party[ai].pp[mi as usize];
                    s.party[ai].pp[mi as usize] = std::cmp::max(0, v - cost);
                }
            }
            // こだわり縛り
            {
                let s = &mut self.sides[mx];
                let ai = s.active_idx;
                if it::is_choice_item(pack, s.party[ai].item)
                    && s.party[ai].choice_locked_move.is_none()
                {
                    s.party[ai].choice_locked_move = action.mv.as_ref().map(|m| m.name);
                }
            }
            // ステルスロック pending
            if self.sides[ox].sr_pending {
                self.sides[ox].sr_pending = false;
                self.sides[ox].stealth_rock_set = true;
                let fi = self.sides[ox].field_idx;
                self.field.stealth_rock[fi] = true;
            }

            self.faint_switch(pack, ox, rng);
            if !defer_self_faint {
                self.faint_switch(pack, mx, rng);
            }

            // ピボット
            let piv = self.sides[mx].active().is_alive && self.sides[mx].active().pivot_out;
            if piv {
                self.sides[mx].active_mut().pivot_out = false;
                let is_baton =
                    action.mv.as_ref().map(|m| m.name == l.バトンタッチ).unwrap_or(false);
                let next_idx = {
                    let Battle { sides, field, .. } = self;
                    let (me, opp) = split2(sides, mx);
                    let oi = opp.active_idx;
                    choose_pivot_target(pack, me, &mut opp.party[oi], is_baton, field, rng)
                };
                if let Some(ni) = next_idx {
                    self.sides[mx].switch_to(pack, ni);
                    {
                        let Battle { sides, field, .. } = self;
                        entry_effects_side(pack, sides, field, mx);
                    }
                    self.apply_healing_wish(mx);
                    let nm = self.sides[mx].active().clone();
                    self.sides[ox].opp_view.on_enter(&nm);
                    self.faint_switch(pack, mx, rng);
                }
            }

            // 強制交代
            let fsw = self.sides[ox].active().is_alive && self.sides[ox].active().force_switch;
            if fsw {
                self.sides[ox].active_mut().force_switch = false;
                let benched: Vec<usize> = (0..self.sides[ox].party.len())
                    .filter(|&i| {
                        self.sides[ox].party[i].is_alive && i != self.sides[ox].active_idx
                    })
                    .collect();
                if !benched.is_empty() {
                    let k = rng.choice(benched.len());
                    let new_idx = benched[k];
                    self.sides[ox].switch_to(pack, new_idx);
                    {
                        let Battle { sides, field, .. } = self;
                        entry_effects_side(pack, sides, field, ox);
                    }
                    let nm = self.sides[ox].active().clone();
                    self.sides[mx].opp_view.on_enter(&nm);
                    self.faint_switch(pack, ox, rng);
                }
            }
        }
    }

    fn end_of_turn(&mut self, pack: &Pack, rng: &mut dyn BRng) {
        let l = &pack.sy.l;
        let st = &pack.sy.st;
        let we = &pack.sy.we;
        self.sides[0].active_mut().flinched = false;
        self.sides[1].active_mut().flinched = false;
        self.field.weather_negated = self.sides[0].active().ability == l.ノーてんき
            || self.sides[1].active().ability == l.ノーてんき;
        if self.field.weather.is_some() && self.field.weather_count > 0 {
            self.field.weather_count -= 1;
            if self.field.weather_count == 0 {
                self.field.weather = None;
            }
        }

        for sx in 0..2usize {
            let ox = 1 - sx;
            if !self.sides[sx].active().is_alive {
                continue;
            }
            // 天候ダメ
            {
                let Battle { sides, field, .. } = self;
                let p = sides[sx].active_mut();
                if effective_weather(pack, field, Some(p)) == Some(we.sandstorm) {
                    let bad = |t: Ty| t == pack.tc.いわ || t == pack.tc.はがね || t == pack.tc.じめん;
                    let t1ok = !bad(p.type1);
                    let t2ok = match p.type2 {
                        None => true,
                        Some(t) => !bad(t),
                    };
                    let a = p.ability;
                    let abok = a != l.すなかき
                        && a != l.すながくれ
                        && a != l.すなのちから
                        && a != l.ぼうじん
                        && a != l.マジックガード;
                    if t1ok && t2ok && abok {
                        let dmg = std::cmp::max(1, p.max_hp / 16);
                        p.take_damage(dmg);
                    }
                }
            }
            // 状態異常
            {
                let p = self.sides[sx].active_mut();
                if p.ability != l.マジックガード {
                    if p.status == Some(st.burn) {
                        let dmg = std::cmp::max(1, p.max_hp / 16);
                        p.take_damage(dmg);
                    } else if p.status == Some(st.poison) || p.status == Some(st.badpoison) {
                        if p.ability == l.ポイズンヒール {
                            let heal = std::cmp::max(1, p.max_hp / 8);
                            p.hp = std::cmp::min(p.max_hp, p.hp + heal);
                        } else if p.status == Some(st.poison) {
                            let dmg = std::cmp::max(1, p.max_hp / 8);
                            p.take_damage(dmg);
                        } else {
                            p.bad_poison_count += 1;
                            let dmg = std::cmp::max(1, p.max_hp * p.bad_poison_count / 16);
                            p.take_damage(dmg);
                        }
                    }
                }
            }
            if !self.sides[sx].active().is_alive {
                continue;
            }
            // ねをはる/アクアリング
            {
                let p = self.sides[sx].active_mut();
                if (p.rooted || p.aqua_ring) && p.is_alive {
                    let heal = std::cmp::max(1, p.max_hp / 16);
                    p.hp = std::cmp::min(p.max_hp, p.hp + heal);
                }
            }
            // たべのこし / くろいヘドロ
            {
                let (item, is_poison) = {
                    let p = self.sides[sx].active();
                    (p.item, p.has_type(pack.tc.どく))
                };
                if item == Some(l.たべのこし) {
                    let (nm, healed) = {
                        let p = self.sides[sx].active_mut();
                        let heal = std::cmp::max(1, p.max_hp / 16);
                        let old = p.hp;
                        p.hp = std::cmp::min(p.max_hp, p.hp + heal);
                        (p.name, p.hp > old)
                    };
                    if healed {
                        self.sides[ox].opp_view.on_item(nm, l.たべのこし);
                    }
                } else if item == Some(l.くろいヘドロ) {
                    if is_poison {
                        let (nm, healed) = {
                            let p = self.sides[sx].active_mut();
                            let heal = std::cmp::max(1, p.max_hp / 16);
                            let old = p.hp;
                            p.hp = std::cmp::min(p.max_hp, p.hp + heal);
                            (p.name, p.hp > old)
                        };
                        if healed {
                            self.sides[ox].opp_view.on_item(nm, l.くろいヘドロ);
                        }
                    } else {
                        let p = self.sides[sx].active_mut();
                        let dmg = std::cmp::max(1, p.max_hp / 16);
                        p.take_damage(dmg);
                    }
                }
            }

            let berry_blocked = self.sides[ox].active().is_alive
                && self.sides[ox].active().ability == l.きんちょうかん;

            // オボンのみ
            if !berry_blocked {
                let trig = {
                    let p = self.sides[sx].active();
                    p.item == Some(l.オボンのみ) && p.hp <= p.max_hp / 2
                };
                if trig {
                    let nm = {
                        let p = self.sides[sx].active_mut();
                        let heal = p.max_hp / 4;
                        p.hp = std::cmp::min(p.max_hp, p.hp + heal);
                        p.last_berry = Some(l.オボンのみ);
                        p.item = None;
                        p.ate_berry = true;
                        it::on_item_consumed(pack, p);
                        p.name
                    };
                    self.sides[ox].opp_view.on_item(nm, l.オボンのみ);
                }
            }
            // オレンのみ
            if !berry_blocked {
                let trig = {
                    let p = self.sides[sx].active();
                    p.item == Some(l.オレンのみ) && p.hp <= p.max_hp / 2
                };
                if trig {
                    let nm = {
                        let p = self.sides[sx].active_mut();
                        p.hp = std::cmp::min(p.max_hp, p.hp + 10);
                        p.last_berry = Some(l.オレンのみ);
                        p.item = None;
                        p.ate_berry = true;
                        it::on_item_consumed(pack, p);
                        p.name
                    };
                    self.sides[ox].opp_view.on_item(nm, l.オレンのみ);
                }
            }
            if !berry_blocked {
                it::try_cure_berry(pack, self.sides[sx].active_mut());
            }
            it::try_white_herb(pack, self.sides[sx].active_mut());
            it::try_mental_herb(pack, self.sides[sx].active_mut());
            it::try_leppa_berry(pack, self.sides[sx].active_mut());
            if !berry_blocked {
                it::apply_hp_berry(pack, self.sides[sx].active_mut());
            }
            {
                let Battle { sides, field, .. } = self;
                ab::end_of_turn_ability(pack, sides[sx].active_mut(), field, rng);
            }
            // やどりぎのタネ
            {
                let seeded = {
                    let p = self.sides[sx].active();
                    p.seeded && p.is_alive
                };
                if seeded {
                    let drain = {
                        let p = self.sides[sx].active_mut();
                        let d = std::cmp::max(1, p.max_hp / 8);
                        p.take_damage(d);
                        d
                    };
                    let o = self.sides[ox].active_mut();
                    if o.is_alive {
                        o.hp = std::cmp::min(o.max_hp, o.hp + drain);
                    }
                }
            }
            // しおづけ
            {
                let p = self.sides[sx].active_mut();
                if p.salted && p.is_alive {
                    let ws = p.has_type(pack.tc.みず) || p.has_type(pack.tc.はがね);
                    let rate = if ws { 1.0 / 8.0 } else { 1.0 / 16.0 };
                    let dmg = std::cmp::max(1, ((p.max_hp as f64) * rate).floor() as i64);
                    p.take_damage(dmg);
                }
            }
            // あくび
            {
                let p = self.sides[sx].active_mut();
                if p.yawn_count > 0 {
                    p.yawn_count -= 1;
                    if p.yawn_count == 0 && p.status.is_none() {
                        if p.ability != l.ふみん && p.ability != l.やるき {
                            p.status = Some(st.sleep);
                            p.sleep_count = rng.randint(1, 3);
                        }
                    }
                }
            }
            // バインド
            {
                let p = self.sides[sx].active_mut();
                if p.bound_count > 0 && p.is_alive {
                    let d = std::cmp::max(1, p.max_hp / 8);
                    p.take_damage(d);
                    p.bound_count -= 1;
                }
            }
            {
                let p = self.sides[sx].active_mut();
                if p.throat_chop_count > 0 {
                    p.throat_chop_count -= 1;
                }
                if p.taunt_count > 0 {
                    p.taunt_count -= 1;
                }
                if p.encore_count > 0 {
                    p.encore_count -= 1;
                    if p.encore_count == 0 {
                        p.locked_move = None;
                    }
                }
                if p.disabled_turns > 0 {
                    p.disabled_turns -= 1;
                    if p.disabled_turns == 0 {
                        p.disabled_move = None;
                    }
                }
                p.protecting = false;
                p.enduring = false;
                if p.last_used_move != Some(l.みちづれ) {
                    p.destiny_bond_last_turn = false;
                }
                if let Some((t1, t2)) = p.roost_types {
                    p.type1 = t1;
                    p.type2 = t2;
                    p.roost_types = None;
                }
                if p.syrup_count > 0 {
                    p.syrup_count -= 1;
                }
                if p.heal_block_count > 0 {
                    p.heal_block_count -= 1;
                }
                p.move_failed_last = p.move_failed_this_turn;
                p.move_failed_this_turn = false;
                if p.switched_this_turn {
                    p.switched_this_turn = false;
                } else {
                    p.turns_out += 1;
                }
            }
        }

        // ものひろい
        for mx in 0..2usize {
            let ox = 1 - mx;
            let take = {
                let mp = self.sides[mx].active();
                let op = self.sides[ox].active();
                mp.is_alive && mp.ability == l.ものひろい && mp.item.is_none() && op.last_berry.is_some()
            };
            if take {
                let b = self.sides[ox].active().last_berry;
                self.sides[mx].active_mut().item = b;
                self.sides[ox].active_mut().last_berry = None;
            }
        }

        if self.field.trick_room && self.field.trick_room_count > 0 {
            self.field.trick_room_count -= 1;
            if self.field.trick_room_count == 0 {
                self.field.trick_room = false;
            }
        }

        // フィールドカウント（misty / electric / psychic の順）
        {
            let f = &mut self.field;
            if f.misty_terrain {
                f.misty_terrain_count -= 1;
                if f.misty_terrain_count <= 0 {
                    f.misty_terrain = false;
                    f.misty_terrain_count = 0;
                }
            }
            if f.electric_terrain {
                f.electric_terrain_count -= 1;
                if f.electric_terrain_count <= 0 {
                    f.electric_terrain = false;
                    f.electric_terrain_count = 0;
                }
            }
            if f.psychic_terrain {
                f.psychic_terrain_count -= 1;
                if f.psychic_terrain_count <= 0 {
                    f.psychic_terrain = false;
                    f.psychic_terrain_count = 0;
                }
            }
        }

        // ねがいごと
        for sx in 0..2usize {
            if self.sides[sx].wish_count > 0 {
                self.sides[sx].wish_count -= 1;
                if self.sides[sx].wish_count == 0 && self.sides[sx].active().is_alive {
                    let wh = self.sides[sx].wish_hp;
                    let p = self.sides[sx].active_mut();
                    let heal = std::cmp::min(wh, p.max_hp - p.hp);
                    p.hp += heal;
                }
            }
        }
        // みらいよち
        for sx in 0..2usize {
            if self.sides[sx].future_sight_count > 0 {
                self.sides[sx].future_sight_count -= 1;
                if self.sides[sx].future_sight_count == 0 && self.sides[sx].active().is_alive {
                    let fs = self.sides[sx].future_sight_dmg;
                    self.sides[sx].active_mut().take_damage(fs);
                }
            }
        }
        // ほろびのうた・のろい
        for sx in 0..2usize {
            let p = self.sides[sx].active_mut();
            if !p.is_alive {
                continue;
            }
            if p.perish_count > 0 {
                p.perish_count -= 1;
                if p.perish_count == 0 {
                    let hp = p.hp;
                    p.take_damage(hp);
                    p.is_alive = false;
                }
            }
            if p.cursed && p.is_alive {
                let d = std::cmp::max(1, p.max_hp / 4);
                p.take_damage(d);
            }
        }
        // スクリーン・おいかぜ
        for sx in 0..2usize {
            let s = &mut self.sides[sx];
            if s.reflect_count > 0 {
                s.reflect_count -= 1;
                if s.reflect_count == 0 {
                    s.reflect = false;
                }
            }
            if s.light_screen_count > 0 {
                s.light_screen_count -= 1;
                if s.light_screen_count == 0 {
                    s.light_screen = false;
                }
            }
            if s.aurora_veil_count > 0 {
                s.aurora_veil_count -= 1;
                if s.aurora_veil_count == 0 {
                    s.aurora_veil = false;
                }
            }
            if s.tailwind_count > 0 {
                s.tailwind_count -= 1;
                if s.tailwind_count == 0 {
                    s.tailwind = false;
                }
            }
        }
        for sx in 0..2usize {
            let p = self.sides[sx].active_mut();
            p.last_physical_dmg_received = 0;
            p.last_special_dmg_received = 0;
        }
        self.faint_switch(pack, 0, rng);
        self.faint_switch(pack, 1, rng);
    }

    /// run（見せ合い＋初手入場）。preview は [(name, base_t1, base_t2, t1, t2)]
    pub fn start(
        &mut self,
        pack: &Pack,
        pv_for_s1: &[(u16, Ty, Option<Ty>, Ty, Option<Ty>)],
        pv_for_s2: &[(u16, Ty, Option<Ty>, Ty, Option<Ty>)],
    ) {
        self.sides[0].opp_view.team_preview(pv_for_s1);
        self.sides[1].opp_view.team_preview(pv_for_s2);
        {
            let Battle { sides, field, .. } = self;
            entry_effects_side(pack, sides, field, 0);
            entry_effects_side(pack, sides, field, 1);
        }
    }

    /// _turn_loop の行動リプレイ版。acts[t] = [side1の行動, side2の行動]
    pub fn run_replay(
        &mut self,
        pack: &Pack,
        acts: &[[Action; 2]],
        rng: &mut dyn BRng,
        on_turn: impl FnMut(&Battle),
    ) -> i64 {
        self.run_loop(
            pack,
            rng,
            |bt, _rng| {
                let ti = (bt.turn - 1) as usize;
                if ti >= acts.len() {
                    panic!("行動リプレイ不足: turn={} acts={}", bt.turn, acts.len());
                }
                [acts[ti][0].clone(), acts[ti][1].clone()]
            },
            on_turn,
        )
    }

    /// _turn_loop（AI 駆動版）。ai_x = (AI種別, certain_ko_override を掛けるか)
    pub fn run_with_ai(
        &mut self,
        pack: &Pack,
        ai1: (crate::ai::Ai, bool),
        ai2: (crate::ai::Ai, bool),
        rng: &mut dyn BRng,
        on_turn: impl FnMut(&Battle),
    ) -> i64 {
        self.run_loop(
            pack,
            rng,
            |bt, rng| {
                let a1 = {
                    let Battle { sides, field, .. } = bt;
                    let (s1, s2) = split2(sides, 0);
                    crate::ai::decide(pack, ai1.0, s1, s2, field, ai1.1, rng)
                };
                let a2 = {
                    let Battle { sides, field, .. } = bt;
                    let (s2, s1) = split2(sides, 1);
                    crate::ai::decide(pack, ai2.0, s2, s1, field, ai2.1, rng)
                };
                [a1, a2]
            },
            on_turn,
        )
    }

    /// _turn_loop 本体（行動の供給元だけを差し替え可能にしたもの）
    pub fn run_loop(
        &mut self,
        pack: &Pack,
        rng: &mut dyn BRng,
        get_acts: impl FnMut(&mut Battle, &mut dyn BRng) -> [Action; 2],
        on_turn: impl FnMut(&Battle),
    ) -> i64 {
        self.run_loop_lim(pack, rng, MAX_TURNS, get_acts, on_turn)
    }

    /// `resume(max_turns=n)` 相当（limit = min(n, MAX_TURNS)）
    pub fn run_loop_lim(
        &mut self,
        pack: &Pack,
        rng: &mut dyn BRng,
        max_turns: i64,
        mut get_acts: impl FnMut(&mut Battle, &mut dyn BRng) -> [Action; 2],
        mut on_turn: impl FnMut(&Battle),
    ) -> i64 {
        let l = &pack.sy.l;
        let limit = std::cmp::min(max_turns, MAX_TURNS);
        while self.turn < limit {
            self.turn += 1;
            if !self.sides[0].has_alive() {
                return 2;
            }
            if !self.sides[1].has_alive() {
                return 1;
            }
            // バリアフリー
            for bx in 0..2usize {
                let trig = self.sides[bx].active().ability == l.バリアフリー
                    && !self.sides[bx].active().barrier_done;
                if trig {
                    self.sides[bx].active_mut().barrier_done = true;
                    for sx in 0..2usize {
                        let s = &mut self.sides[sx];
                        if s.reflect || s.light_screen || s.aurora_veil {
                            s.reflect = false;
                            s.light_screen = false;
                            s.aurora_veil = false;
                            s.reflect_count = 0;
                            s.light_screen_count = 0;
                            s.aurora_veil_count = 0;
                        }
                    }
                }
            }
            self.field.weather_negated = self.sides[0].active().ability == l.ノーてんき
                || self.sides[1].active().ability == l.ノーてんき;
            self.info_abilities_on_entry(pack);

            let [action1, action2] = get_acts(self, rng);
            let chooser1 = self.sides[0].active_idx;
            let chooser2 = self.sides[1].active_idx;

            // メガ進化
            for sx in 0..2usize {
                let a = if sx == 0 { &action1 } else { &action2 };
                let ok = a.do_mega
                    && !self.sides[sx].active().mega_evolved
                    && !self.sides[sx].mega_used;
                if ok {
                    mega_evolve_poke(pack, self.sides[sx].active_mut());
                    self.sides[sx].mega_used = true;
                    let Battle { sides, field, .. } = self;
                    let (me, opp) = split2(sides, sx);
                    let mi = me.active_idx;
                    let oi = opp.active_idx;
                    ab::entry_ability(
                        pack,
                        &mut me.party[mi],
                        &mut opp.party[oi],
                        field,
                        MAX_TURNS,
                    );
                }
            }

            for sx in 0..2usize {
                let a = if sx == 0 { &action1 } else { &action2 };
                let primed =
                    a.mv.as_ref().map(|m| m.name == l.くちばしキャノン).unwrap_or(false);
                let p = self.sides[sx].active_mut();
                p.beak_primed = primed;
                p.took_damage_this_turn = false;
            }

            let p1_first = {
                let Battle { sides, field, .. } = self;
                let (s1, s2) = (&sides[0], &sides[1]);
                speed_order(pack, s1, &action1, s2, &action2, field, rng)
            };
            let (fx, ox) = if p1_first { (0usize, 1usize) } else { (1usize, 0usize) };
            let (first_action, second_action) =
                if p1_first { (&action1, &action2) } else { (&action2, &action1) };
            let second_chooser = if ox == 0 { chooser1 } else { chooser2 };

            self.do_action(pack, fx, first_action, Some(second_action), true, rng);
            if !self.sides[ox].has_alive() {
                on_turn(self);
                break;
            }

            if self.sides[ox].active_idx != second_chooser {
                // 行動権喪失
            } else if !self.sides[fx].active().is_alive {
                // 相手不在
            } else if self.sides[ox].active().flinched {
                if self.sides[ox].active().ability == l.ふくつのこころ {
                    let p = self.sides[ox].active_mut();
                    p.stage_speed = std::cmp::min(6, p.stage_speed + 1);
                }
                self.sides[ox].active_mut().flinched = false;
            } else {
                self.sides[ox].active_mut().acts_second = true;
                self.do_action(pack, ox, second_action, Some(first_action), false, rng);
                if self.sides[ox].active().is_alive {
                    self.sides[ox].active_mut().acts_second = false;
                }
            }
            if !self.sides[fx].has_alive() {
                on_turn(self);
                break;
            }

            self.end_of_turn(pack, rng);
            on_turn(self);
        }
        if !self.sides[0].has_alive() {
            return 2;
        }
        if !self.sides[1].has_alive() {
            return 1;
        }
        0
    }
}
