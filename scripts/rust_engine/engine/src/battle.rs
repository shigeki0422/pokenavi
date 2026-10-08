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
            prev.entry_moves.clear();
            prev.ate_berry = false;
            prev.protect_consecutive = 0;
            prev.locked_move = None;
            prev.encore_count = 0;
            prev.taunt_count = 0;
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
            prev.defenseless = false;
            prev.octolocked = false;
            prev.crit_stage = 0;
            prev.perish_count = 0;
            prev.destiny_bond = false;
            prev.cursed = false;
            prev.charged = false;
            prev.bad_poison_count = 0;
            prev.trapped = false;
            prev.no_retreat = false;
            prev.last_used_move = None;
            prev.last_move_obj = None;
            prev.magnet_rise = false;
            prev.levitate_turns = 0;
            prev.minimized = false;
            prev.lock_on = false;
            prev.seeded = false;
            prev.rooted = false;
            prev.aqua_ring = false;
            prev.infatuation = false;
            prev.torment = false;
            prev.heal_block_count = 0;
            prev.syrup_count = 0;
            prev.ability_suppressed = false;
            prev.acts_second = false;
        }
        let shed_sub = std::mem::take(&mut self.party[pi].shed_tail_sub);
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
        if shed_sub > 0 {
            a.substitute_hp = shed_sub;
        }
        a.turns_out = 0;
        a.switched_this_turn = true;
        a.fainted_allies = fainted;
    }
    pub fn next_alive_idx(&self) -> Option<usize> {
        self.party.iter().enumerate().find(|(i, p)| p.is_alive && *i != self.active_idx).map(|(i, _)| i)
    }
}

/// 1v1判定の「ダメージレース」表示用の記録（analysis::sim_pair だけが有効にする。既定は None で何もしない）。
/// (区切り, 行動した側, 両者のHP, 両者の持ち物, 両者のばけのかわが剥がれているか)。
/// 区切り: 0=ターン開始 1=行動後 2=ひるんで動けず 3=ターン終了処理後。
/// .5 能力ランク(攻撃・防御・特攻・特防・素早さ) / .6 状態異常 / .7 天候 は1v1の再生表示用。
pub type RaceMark = (u8, usize, [i64; 2], [Option<crate::interner::Sym>; 2], [bool; 2], [[i32; 5]; 2],
                     [Option<crate::interner::Sym>; 2], Option<crate::interner::Sym>);
thread_local! {
    pub static RACE_LOG: std::cell::RefCell<Option<Vec<RaceMark>>> = const { std::cell::RefCell::new(None) };
}

thread_local! {
    /// RACE_LOG が有効な間だけ、HPが動いた原因を積む (区切りの番号, 側, 原因, 量(正=ダメージ/負=回復))。
    /// 区切りの番号は積んだ時点の RACE_LOG の長さ＝次に積まれる区切りまでの区間に属する。
    pub static RACE_CAUSES: std::cell::RefCell<Vec<(usize, usize, &'static str, i64)>> = const { std::cell::RefCell::new(Vec::new()) };
}

/// HPが動いた原因を記録する（判定の経過表示用。RACE_LOG が無効なら何もしない＝対戦の挙動は変えない）。
pub fn race_cause(side: usize, kind: &'static str, amount: i64) {
    if amount == 0 { return; }
    RACE_LOG.with(|r| {
        if let Some(v) = r.borrow().as_ref() {
            let k = v.len();
            RACE_CAUSES.with(|c| c.borrow_mut().push((k, side, kind, amount)));
        }
    });
}

fn race_mark(b: &Battle, phase: u8, actor: usize) {
    RACE_LOG.with(|r| {
        if let Some(v) = r.borrow_mut().as_mut() {
            let (p0, p1) = (b.sides[0].active(), b.sides[1].active());
            let stg = |p: &Poke| [p.stage(0), p.stage(1), p.stage(2), p.stage(3), p.stage(4)];
            v.push((phase, actor, [p0.hp, p1.hp], [p0.item, p1.item], [p0.disguise_broken, p1.disguise_broken],
                    [stg(p0), stg(p1)], [p0.status, p1.status], b.field.weather));
        }
    });
}

#[derive(Clone, Debug, Default)]
pub struct Battle {
    pub sides: [Side; 2],
    pub field: Field,
    pub turn: i64,
    /// 前回の行動選択時の持ち物（battle.py の _item_snap）。空＝未取得
    pub item_snap: Vec<Vec<Option<crate::interner::Sym>>>,
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
                // M-6 の Zメガ石（battle.py _is_megastone と同じ。抜けていて、ガブリアスナイトZ 等を
                // はたきおとす・トリックで奪えてしまい、型プールの読みでもメガ後の特性で型を全部弾いていた）
                || s.ends_with("ナイトＺ")
                || s.ends_with("ナイトZ")
        }
    }
}

#[inline]
fn is_berry(pack: &Pack, item: Option<u16>) -> bool {
    matches!(item, Some(i) if pack.intern.resolve(i).ends_with("のみ"))
}

// ── おうごんのからだ が無効化する変化技 ────────────────────────────────────
fn gag_block(pack: &Pack, n: u16) -> bool {
    pack.flags(n).foe_status
}

// ── 行動優先度 ────────────────────────────────────────────────────────────
pub fn priority(pack: &Pack, action: &Action, poke: &Poke, field: &Field, rng: &mut dyn BRng) -> i64 {
    let mut base = priority_base(pack, action, poke, field);
    if !matches!(action.kind, ActKind::Switch | ActKind::Mega) && action.mv.is_some()
        && it::has_quick_claw_trigger(pack, poke.item, rng)
    {
        base += 1;
    }
    base
}

/// 乱数を使わない部分の優先度（せんせいのツメ以外。battle.py の _priority_base）
pub fn priority_base(pack: &Pack, action: &Action, poke: &Poke, field: &Field) -> i64 {
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
        if !(poke.ability == l.ふゆう
            || poke.has_type(pack.tc.ひこう)
            || poke.magnet_rise
            || poke.item == Some(pack.sy.it.ふうせん))
            || poke.grounded
        {
            base += 1;
        }
    }
    if poke.ability == l.はやてのつばさ && mv.ty == pack.tc.ひこう && poke.hp == poke.max_hp {
        base += 1;
    }
    if poke.ability == l.いたずらごころ && mv.category == Cat::Status {
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
        if let Some(f) = field.speed_tie_p1_first {
            return f;
        }
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
        poke.pivot_out = false;
        poke.force_switch = false;

        let immune_to_ground = poke.has_type(pack.tc.ひこう)
            || poke.ability == l.ふゆう
            || poke.ability == l.うなぎのぼり
            || poke.item == Some(pack.sy.it.ふうせん);

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
                apply_status(pack, poke, status, false, Some(&*field));
            }
        }
        if field.sticky_web[side_idx] && !immune_to_ground {
            poke.stage_speed = std::cmp::max(-6, poke.stage_speed - 1);
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
    ab::entry_ability(pack, &mut side.party[pi], opponent, field);
    // 継続中のフィールドに登場したときもシードを発動する（設置時の発動は技・特性の側）
    it::try_terrain_seed(pack, &mut side.party[pi], field);
    // しろいハーブ: 能力が下がった直後に発動（ねばねばネット・いかく 等）
    it::try_white_herb(pack, &mut side.party[pi]);
    it::try_white_herb(pack, opponent);
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
                    let (sp, so) = (
                        crate::damage::EstSnap::take(&side.party[i]),
                        crate::damage::EstSnap::take(opp),
                    );
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
                    sp.restore(&mut side.party[i]);
                    so.restore(opp);
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
    // ブレードフォルムは第9世代(SV)で A/C=140（150 は第8世代以前の値）
    p.attack = calc_stat(140, p.evs[1], 31, nat(0));
    p.defense = calc_stat(50, p.evs[2], 31, nat(1));
    p.sp_attack = calc_stat(140, p.evs[3], 31, nat(2));
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
        || n == l.ねらいうち || n == l.きりさく
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
    // 必ず急所に当たる技（正本: simulator/battle.py ALWAYS_CRIT_MOVES）
    if mv.name == l.トリックフラワー || mv.name == l.やまあらし || mv.name == l.こおりのいぶき {
        return 1.0;
    }
    let mut stage = 0i64;
    if is_high_crit(pack, mv.name) {
        stage = 1;
    }
    if attacker.ability == l.きょううん {
        stage += 1;
    }
    stage += crate::damage::get_crit_stage_bonus(
        pack,
        attacker.item,
        Some(pack.intern.resolve(attacker.name)),
    );
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

/// 1v1判定の「最大打点1発」の候補から外す技。対戦本体では通常どおり動く。
///   反射技  : 相手が出した技の種類と威力で威力が決まるので、成功前提だと過大評価になる
///   HP依存技: 撃ち続けても倒しきれず（相手のHPを自分のHPまで／半分に削るだけ）、
///             かつ双方の残HPに強く依存するので、最大打点の比較には向かない
/// ちきゅうなげ・ナイトヘッドは固定ダメージで倒しきれるため対象外にしない。
pub fn is_excluded_from_matchup(pack: &Pack, mv: &DMove) -> bool {
    let l = &pack.sy.l;
    mv.name == l.カウンター || mv.name == l.ミラーコート || mv.name == l.メタルバースト
        || mv.name == l.がむしゃら || mv.name == l.いかりのまえば
}

/// 1発ごとに命中判定があり、外れるとそこで止まる技。
/// 分析（1v1判定）は必中を仮定するので、これらは常に最大回数で当たる扱いになる。
/// 回数そのものが乱数で決まる 2〜5回の技（みずしゅりけん等）とは別扱い。
/// 技を撃つ直前に走る、攻撃側の姿・タイプの変化。
/// ダメージ計算より前に効くので、分析側が calc_damage を直に呼ぶとここを取りこぼす
/// （マスカーニャのへんげんじざいで全技にSTABが乗る分、ギルガルドのバトルスイッチで
///  攻撃が50→150になる分が、表示ダメージにだけ反映されない事故が起きた）。
/// 対戦本体（execute_move）と分析（analysis::move_damage）で共有する。
/// ai.rs の見積もりから姿変化を一時適用するための公開ラッパ（正本: simulator/ai.py）。
pub fn aegislash_to_blade_pub(pack: &Pack, p: &mut Poke) {
    aegislash_to_blade(pack, p);
}

/// 一時適用した姿変化を元に戻す。
pub fn revert_blade_pub(p: &mut Poke) {
    if !p.in_blade_forme {
        return;
    }
    p.attack = p.shield_atk;
    p.defense = p.shield_def;
    p.sp_attack = p.shield_spatk;
    p.sp_defense = p.shield_spdef;
    p.in_blade_forme = false;
}

pub fn apply_pre_move_forms(pack: &Pack, attacker: &mut Poke, mv: &DMove) {
    let l = &pack.sy.l;
    if attacker.ability == l.バトルスイッチ && mv.category != Cat::Status {
        aegislash_to_blade(pack, attacker);
    }
    // タイプなしの技（わるあがき）ではタイプが変わらない（battle.py と同じ）
    if (attacker.ability == l.へんげんじざい || attacker.ability == pack.sy.ai.リベロ)
        && !attacker.protean_used
        && mv.ty != crate::pack::NO_TY
    {
        let new_type = mv.ty;
        if attacker.type1 != new_type || attacker.type2.is_some() {
            attacker.type1 = new_type;
            attacker.type2 = None;
            attacker.protean_used = true;
        }
    }
}

/// 「何発目か」を反映して1発ぶんのダメージを計算する。
///
/// multi_hit_index の更新を呼び出し側に任せると、対戦本体と分析側で
/// 反映漏れが起きる（実際に分析側だけトリプルアクセルの威力が20固定になり、
/// 「78〜97% なのに確定1」という食い違いを出した）。
/// 対戦本体（execute_move）と分析（analysis::move_damage）はここを共有する。
pub fn hit_damage(
    pack: &Pack,
    attacker: &mut Poke,
    defender: &mut Poke,
    mv: &DMove,
    field: &mut Field,
    hit_i: i64,
    critical: bool,
    roll_override: Option<f64>,
    rng: &mut dyn BRng,
) -> i64 {
    attacker.multi_hit_index = hit_i;
    calc_damage(pack, attacker, defender, mv, field, critical, None, roll_override, &mut |k| {
        if k == 0 {
            rng.random()
        } else {
            rng.choice(16) as f64
        }
    })
}

pub fn is_accuracy_chained(pack: &Pack, mv: &DMove) -> bool {
    mv.name == pack.sy.l.トリプルアクセル || mv.name == pack.sy.l.ネズミざん
}

/// 連続技か（calc_hits が2回以上を返しうる技）。乱数を使わない判定。
pub fn is_multi_hit(pack: &Pack, mv: &DMove) -> bool {
    let l = &pack.sy.l;
    let n = mv.name;
    [l.ダブルキック, l.にどげり, l.ダブルウイング, l.ドラゴンアロー, l.スパークリングアリア, l.ダブルパンツァー,
     l.ツインビーム, l.ダブルアタック, l.トリプルアクセル, l.スケイルショット, l.みずしゅりけん, l.ロックブラスト,
     l.タネマシンガン, l.つららばり, l.ミサイルばり, l.ボーンラッシュ, l.あわ, l.スイープビンタ, l.ネズミざん].contains(&n)
}

pub fn calc_hits(pack: &Pack, mv: &DMove, attacker: &Poke, rng: &mut dyn BRng) -> i64 {
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
        if skill_link {
            return 3;
        }
        let mut hits = 1;
        while hits < 3 && rng.hit_continue() < 0.90 {
            hits += 1;
        }
        return hits;
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
        while hits < 10 && rng.hit_continue() < 0.90 {
            hits += 1;
        }
        return hits;
    }
    1
}

// ══════════════════════════════════════════════════════════════════════════
//  _execute_move
// ══════════════════════════════════════════════════════════════════════════
/// `dmg_out` にはこの技が与えた合計ダメージが入る（早期returnした場合は0のまま）。
/// 分析側が「その技のダメージ」を知るための出力で、対戦の挙動には影響しない。
/// 分析が calc_damage を直に呼ぶと、ここに至るまでの前処理
/// （へんげんじざいのタイプ変更・バトルスイッチ・急所判定・連続回数）を取りこぼす。
/// とびひざげり系: 外れ・まもる・無効で最大HPの1/2の反動（battle.py _crash_recoil と同じ）
/// 浮いている（じめん技・じわれ が当たらない）。battle.py _airborne
pub fn airborne(pack: &Pack, p: &Poke, field: &Field, attacker: Option<&Poke>) -> bool {
    if p.grounded || field.gravity > 0 {
        return false;
    }
    let lev = p.ability == pack.sy.l.ふゆう
        && !attacker.map(|a| crate::damage::should_ignore_ability(pack, a)).unwrap_or(false);
    p.has_type(pack.tc.ひこう) || lev || p.magnet_rise || p.item == Some(pack.sy.it.ふうせん)
}

/// かいふくふうじ 中は回復できない。battle.py _can_heal
#[inline]
pub fn can_heal(p: &Poke) -> bool {
    p.heal_block_count <= 0
}

/// 覚えている技の残りPP（覚えていなければ0）。battle.py _move_pp
pub fn move_pp(p: &Poke, name: u16) -> i64 {
    for (i, m) in p.moves.iter().enumerate() {
        if m.name == name && i < p.pp.len() {
            return p.pp[i];
        }
    }
    0
}

/// 場を離れたポケモンが相手に掛けていた拘束を解く。battle.py _release_by_leaving
#[inline]
fn release_by_leaving(opp: &mut Poke) {
    opp.bound_count = 0;
    opp.trapped = false;
    opp.octolocked = false;
}

/// 相手の変化技による能力低下（すてゼリフ・おきみやげ・ちからをすいとる）。battle.py _foe_stat_drop
fn foe_stat_drop(pack: &Pack, attacker: &mut Poke, defender: &mut Poke, drops: &[(u8, i32)]) -> bool {
    let l = &pack.sy.l;
    if defender.ability == l.ミラーアーマー {
        for &(stat, delta) in drops {
            ab::reflect_stat_drop(pack, attacker, stat, delta);
        }
        return true;
    }
    let mut changed = false;
    let mut lowered = false;
    for &(stat, delta) in drops {
        let d = if defender.ability == l.あまのじゃく { -delta } else { delta };
        let dab = defender.ability;
        if d < 0
            && (dab == l.クリアボディ || dab == l.しろいけむり || dab == l.かがくへんかガス
                || (stat == 0 && dab == l.かいりきバサミ)
                || (stat == 1 && dab == l.はとむね))
        {
            continue;
        }
        let old = defender.stage(stat);
        let new = (old + d).clamp(-6, 6);
        if new != old {
            defender.set_stage(stat, new);
            changed = true;
            lowered = lowered || d < 0;
        }
    }
    if lowered {
        ab::on_stat_lowered(pack, defender);
    }
    changed
}

fn crash_recoil(pack: &Pack, a: &mut Poke, n: u16) {
    let l = &pack.sy.l;
    if (n == l.とびひざげり || n == l.とびげり || n == l.かかとおとし || n == l.サンダーダイブ) && a.is_alive
        && a.ability != l.マジックガード
    {
        let recoil = std::cmp::max(1, a.max_hp / 2);
        a.take_damage(recoil);
    }
}

pub fn execute_move(
    pack: &Pack,
    sides: &mut [Side; 2],
    field: &mut Field,
    aidx: usize,
    action: &Action,
    opp_action: Option<&Action>,
    rng: &mut dyn BRng,
    dmg_out: &mut i64,
) {
    let ai = sides[aidx].active_idx;
    execute_move_inner(pack, sides, field, aidx, action, opp_action, rng, dmg_out);
    // 自分が倒れる技（だいばくはつ・じばく・ミストバースト）は、外れ・まもる・タイプ無効・ばけのかわ等で技が途中で終わっても、
    // 使った時点で自分は倒れる（実機どおり。battle.py _execute_move と同じ）
    if let Some(p) = sides[aidx].party.get_mut(ai) {
        if p.selfko_pending {
            p.selfko_pending = false;
            if p.is_alive {
                let hp = p.hp;
                p.take_damage(hp);
                p.is_alive = false;
            }
        }
    }
}

#[allow(clippy::too_many_arguments)]
fn execute_move_inner(
    pack: &Pack,
    sides: &mut [Side; 2],
    field: &mut Field,
    aidx: usize,
    action: &Action,
    opp_action: Option<&Action>,
    rng: &mut dyn BRng,
    dmg_out: &mut i64,
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

    A!().defenseless = false;
    A!().flinched = false;
    if n != l.みちづれ {
        A!().destiny_bond = false;
    }
    A!().last_used_move = Some(n);
    A!().last_move_obj = Some(mv.clone());
    // 間に別の技（変化技を含む）を使えば次の デカハンマー は出せる（battle.py と同じ）
    if n != l.デカハンマー {
        A!().deka_last = false;
    }
    if n != l.とっておき {
        let nm = A!().name;
        let _ = nm;
        if !A!().used_moves.contains(&n) {
            A!().used_moves.push(n);
        }
    }
    // 自分の技だけを「判明した技」にする（わるあがき・まねっこのコピーは除く。battle.py と同じ）
    if A!().moves.iter().any(|m| m.name == n) {
        let an = A!().name;
        sides[didx].opp_view.on_move(an, n);
        // 交代せずに違う技を打った＝こだわりアイテムではない（battle.py と同じ）
        if !A!().via_call {
            // 持ち物が途中で変わったら数え直す（battle.py と同じ）
            if A!().entry_moves.is_empty() || A!().entry_item != A!().item {
                A!().entry_moves.clear();
                A!().entry_item = A!().item;
            }
            if !A!().entry_moves.contains(&n) {
                A!().entry_moves.push(n);
            }
            if A!().entry_moves.len() >= 2 && sides[didx].belief.0.is_some() {
                let mut bl = sides[didx].belief.0.take().unwrap();
                bl.observe_absent_item(pack, an, &["こだわりスカーフ", "こだわりハチマキ", "こだわりメガネ"]);
                sides[didx].belief.0 = Some(bl);
            }
            // 技選びの観測（battle.py と同じ条件）
            if sides[didx].belief.0.is_some() && mv.category != Cat::Status && mv.priority <= 0
                && A!().choice_locked_move.is_none() && A!().encore_count == 0 && A!().lock_count == 0
            {
                let own_def = D!().clone();
                let subj = crate::belief::pub_state(&A!());
                let mut bl = sides[didx].belief.0.take().unwrap();
                bl.observe_choice(pack, an, &mv, own_def, field, subj);
                sides[didx].belief.0 = Some(bl);
            }
        }
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
        A!().sleep_count -= if A!().ability == l.はやおき { 2 } else { 1 };
        if A!().sleep_count <= 0 {
            A!().status = None;
            return;
        }
        A!().sleep_acts += 1;
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
        sides[aidx].party[ai].via_call = true;
        execute_move(pack, sides, field, aidx, &fake, opp_action, rng, &mut 0);
        sides[aidx].party[ai].via_call = false;
        if sides[aidx].party[ai].status.is_none() {
            sides[aidx].party[ai].status = saved_status;
            sides[aidx].party[ai].sleep_count = saved_count;
        }
        return;
    }

    if mv.category == Cat::Status && A!().taunt_count > 0 {
        return;
    }

    if A!().throat_chop_count > 0 && pack.flags(n).sound {
        return;
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
            A!().sleep_acts += 1;
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
        if n == l.もえつきる || n == l.ねっとう || n == l.ねっさのだいち || n == l.せいなるほのお
            || n == l.かえんボール
        {
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
            sides[aidx].tailwind_count = 4;
        }
        return;
    }
    let bounce = D!().ability == l.マジックミラー && A!().ability != l.マジックミラー;
    if n == l.まきびし {
        let oi = if bounce { sides[aidx].field_idx } else { sides[didx].field_idx };
        if field.spikes[oi] < 3 {
            field.spikes[oi] += 1;
        }
        return;
    }
    if n == l.ステルスロック {
        if bounce {
            let ai2 = sides[aidx].field_idx;
            if !field.stealth_rock[ai2] {
                field.stealth_rock[ai2] = true;
                sides[aidx].stealth_rock_set = true;
            }
            return;
        }
        if !field.stealth_rock[sides[didx].field_idx] && !sides[didx].sr_pending {
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
        // 同じ天候では失敗（battle.py と同じ）
        let same = (n == l.あまごい && field.weather == Some(we.rain))
            || (n == l.にほんばれ && field.weather == Some(we.sunny))
            || (n == l.すなあらし && field.weather == Some(we.sandstorm))
            || ((n == l.あられ || n == l.ゆきげしき) && field.weather == Some(we.hail));
        if same {
            return;
        }
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
            if field.weather != Some(we.hail) {
                field.weather = Some(we.hail);
                field.weather_count = wt(l.つめたいいわ, &A!());
            }
            A!().pivot_out = true;
            return;
        }
    }

    // 変化技
    if mv.category == Cat::Status {
        if A!().ability == l.いたずらごころ && pack.flags(n).foe_status && D!().has_type(pack.tc.あく) {
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
        if D!().substitute_hp > 0 && gag_block(pack, n) && !pack.flags(n).sub_bypass && !pack.flags(n).sound
            && A!().ability != l.すりぬけ && D!().ability != l.マジックミラー
        {
            return;
        }
        let pending = matches!(opp_action, Some(oa) if oa.kind == ActKind::Move) && !A!().acts_second;
        apply_status_move(pack, sides, field, aidx, &mv, rng, pending);
        return;
    }

    // ── 攻撃技の前処理 ──
    if (n == l.ねこだまし || n == l.であいがしら) && A!().turns_out > 0 {
        return;
    }
    if n == l.ふいうち {
        let opp_is_attacking = field.assume_opp_attacks || match opp_action {
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
        it::on_item_consumed(pack, &mut A!());
    }
    if mv.priority > 0 && (D!().ability == l.じょおうのいげん || D!().ability == l.テイルアーマー) {
        return;
    }
    if (n == l.だいばくはつ || n == l.じばく || n == l.ミストバースト)
        && (A!().ability == l.しめりけ || D!().ability == l.しめりけ)
    {
        return;
    }
    if n == l.だいばくはつ || n == l.じばく || n == l.ミストバースト {
        A!().selfko_pending = true;
    }
    apply_pre_move_forms(pack, &mut A!(), &mv);

    // 一撃必殺
    if n == l.ぜったいれいど || n == l.ハサミギロチン || n == l.つのドリル || n == l.じわれ {
        if n == l.ぜったいれいど && D!().has_type(pack.tc.こおり) {
            return;
        }
        if n == l.じわれ && airborne(pack, &D!(), field, Some(&A!())) {
            return;
        }
        if (n == l.つのドリル || n == l.ハサミギロチン) && D!().has_type(pack.tc.ゴースト) {
            return;
        }
        // がんじょうは一撃必殺技を完全に無効化する（HP満タンのまま）。タスキのように1で耐えるのではない。
        // かたやぶり系は貫通する。
        if D!().ability == l.がんじょう
            && A!().ability != l.かたやぶり
            && A!().ability != l.ターボブレイズ
            && A!().ability != l.テラボルテージ
        {
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
    if n == l.でんこうそうげき && !A!().has_type(pack.tc.でんき) {
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
    if field.psychic_terrain && mv.priority > 0 && mv.category != Cat::Status {
        let d_grounded = !(D!().has_type(pack.tc.ひこう)
            || D!().ability == l.ふゆう
            || D!().magnet_rise
            || D!().item == Some(pack.sy.it.ふうせん))
            || D!().grounded;
        if d_grounded {
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
            {
                A!().stage_attack = std::cmp::max(-6, A!().stage_attack - 1);
            }
            if pmove == Some(l.トーチカ)
                && is_contact_move(pack, &mv)
                && A!().ability != l.えんかく
                && D!().is_alive
                && A!().is_alive
            {
                apply_status(pack, &mut A!(), st.poison, false, Some(&*field));
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
        }
        crash_recoil(pack, &mut A!(), n);
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
    // きもったま: ノーマル・かくとう技はゴーストにも当たる（ダメージ計算側はもとから等倍扱い。ここで弾いて当たらなかった）
    if eff == 0.0 && !crate::damage::scrappy_override(pack, &A!(), eff_type, &D!()) {
        crash_recoil(pack, &mut A!(), n);
        return;
    }

    // 特性・ふうせんで無効（ダメージ0の命中ではなく「効かない」。接触の反応・技の追加効果・反動は起きない。battle.py と同じ）
    let mold = crate::damage::should_ignore_ability(pack, &A!());
    let ab_immune = !mold
        && crate::damage::check_move_immunity(pack, &D!(), eff_type, n)
        && !crate::damage::scrappy_override(pack, &A!(), eff_type, &D!());
    let bal_immune = D!().item == Some(pack.sy.it.ふうせん) && eff_type == pack.tc.じめん && !D!().grounded;
    if ab_immune || bal_immune {
        if ab_immune {
            // 特性で無効になったことは表示される（HPが満タンで回復しなくても特性は判明。battle.py と同じ）
            let (dn, dab) = (D!().name, D!().ability);
            sides[aidx].opp_view.on_ability(dn, dab);
            ab::on_absorb(pack, &mut D!(), eff_type);
        }
        crash_recoil(pack, &mut A!(), n);
        return;
    }

    // ばけのかわ: 1発目のダメージだけを防ぐ（連続技の2発目以降は通る。ねこだましのひるみは防げない＝実機どおり）
    let mut disguise_ate_first = false;
    if D!().ability == l.ばけのかわ && !D!().disguise_broken && !mold {
        D!().disguise_broken = true;
        {
            let dn = D!().name;
            sides[aidx].opp_view.on_ability(dn, l.ばけのかわ);
        }
        let pen = std::cmp::max(1, ((D!().max_hp as f64) / 8.0).floor() as i64);
        let hd0 = D!().hp;
        D!().take_damage(pen);
        race_cause(didx, "disguise", hd0 - D!().hp);
        if n == l.ねこだまし && D!().is_alive && D!().ability != l.せいしんりょく && D!().ability != l.どんかん {
            D!().flinched = true;
        }
        disguise_ate_first = is_multi_hit(pack, &mv) && D!().is_alive;
        if !disguise_ate_first {
            // いのちのたま: ばけのかわに当たってダメージが0でも反動を受ける（実機どおり。battle.py と同一）
            if A!().item == Some(l.いのちのたま) && mv.category != Cat::Status && A!().is_alive
                && A!().ability != l.マジックガード
            {
                let recoil = std::cmp::max(1, ((A!().max_hp as f64) / 10.0).floor() as i64);
                let h0 = A!().hp;
                A!().take_damage(recoil);
                race_cause(aidx, "lifeorb", h0 - A!().hp);
                let an = A!().name;
                sides[didx].opp_view.on_item(an, l.いのちのたま);
                let nerv = D!().is_alive && D!().ability == l.きんちょうかん;
                let hb0 = A!().hp;
                if let Some(bb) = hp_berry_now(pack, &mut A!(), nerv) {
                    race_cause(aidx, "berry", hb0 - A!().hp);
                    let an = A!().name;
                    sides[didx].opp_view.on_item(an, bb);
                }
            }
            if (n == l.ボルトチェンジ || n == l.とんぼがえり || n == l.クイックターン) && A!().is_alive
            {
                A!().pivot_out = true;
            }
            return;
        }
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
        if D!().ability == l.がんじょう && D!().hp == D!().max_hp && ret_dmg >= D!().hp && !mold {
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

    let mut critical = {
        let (a, d) = (&sides[aidx].party[ai], &sides[didx].party[di]);
        let c = crit_chance(pack, a, &mv, Some(d));
        rng.random() < c
    };
    let mut any_crit = critical;
    let mut hits = calc_hits(pack, &mv, &A!(), rng);
    // 型の逆算用に、行動前の両者の見えている状態を控える（battle.py の _pre_att/_pre_def）
    // 写しは信念を持つ実戦だけで取る（探索中の複製には信念が無い。battle.py と同じ）
    let has_bl = sides[aidx].belief.0.is_some() || sides[didx].belief.0.is_some();
    let pre_att = if has_bl { Some(crate::belief::pub_state(&A!())) } else { None };
    let pre_def = if has_bl { Some(crate::belief::pub_state(&D!())) } else { None };

    let screen_breaker = n == l.かわらわり || n == l.レイジングブル || n == l.サイコファング;
    let screen_of = |crit: bool, sides: &[Side], att_ab: crate::interner::Sym| -> f64 {
        if !crit && att_ab != l.すりぬけ && !screen_breaker {
            if mv.category == Cat::Physical && (sides[didx].reflect || sides[didx].aurora_veil) {
                return 0.5;
            } else if mv.category == Cat::Special
                && (sides[didx].light_screen || sides[didx].aurora_veil)
            {
                return 0.5;
            }
        }
        1.0
    };
    let mut screen_mult = screen_of(critical, &sides[..], A!().ability);
    let chained = is_accuracy_chained(pack, &mv);

    let mut total_dmg: i64 = 0;
    // 実際に減らしたHP（残りHPで頭打ち）。反動・吸収・かいがらのすずの基準。
    let mut dealt_hp: i64 = 0;
    let (mut sub_hits, mut real_hits) = (0i64, 0i64);
    for hit_i in 0..hits {
        if !D!().is_alive {
            break;
        }
        if disguise_ate_first && hit_i == 0 {
            continue;
        }
        if hit_i > 0 && chained {
            critical = {
                let (a, d) = (&sides[aidx].party[ai], &sides[didx].party[di]);
                let c = crit_chance(pack, a, &mv, Some(d));
                rng.random() < c
            };
            screen_mult = screen_of(critical, &sides[..], A!().ability);
            any_crit = any_crit || critical;
        }
        let ro = field.roll_override;
        let mut dmg = {
            let (a, d) = two!();
            hit_damage(pack, a, d, &mv, field, hit_i, critical, ro, rng)
        };
        if screen_mult < 1.0 {
            dmg = std::cmp::max(1, ((dmg as f64) * screen_mult).floor() as i64);
        }
        if A!().pierce_quarter {
            dmg = std::cmp::max(1, dmg / 4);
        }

        let sub_hp = D!().substitute_hp;
        if sub_hp > 0 && !pack.flags(n).sound && A!().ability != l.すりぬけ {
            // みがわり が受けた攻撃: 追加効果・接触の反応・防御側の持ち物/特性は起きない（battle.py と同じ）
            if dmg >= sub_hp {
                D!().substitute_hp = 0;
            } else {
                D!().substitute_hp = sub_hp - dmg;
            }
            total_dmg += dmg;
            dealt_hp += std::cmp::min(dmg, sub_hp);
            sub_hits += 1;
            if A!().item == Some(pack.sy.it.ノーマルジュエル) && eff_type == pack.tc.ノーマル {
                A!().item = None;
                it::on_item_consumed(pack, &mut A!());
            }
            if A!().item == Some(l.いのちのたま) && A!().ability != l.マジックガード && hit_i == hits - 1 {
                let recoil = std::cmp::max(1, ((A!().max_hp as f64) / 10.0).floor() as i64);
                let h0 = A!().hp;
                A!().take_damage(recoil);
                race_cause(aidx, "lifeorb", h0 - A!().hp);
                let an = A!().name;
                sides[didx].opp_view.on_item(an, l.いのちのたま);
                let nerv = D!().is_alive && D!().ability == l.きんちょうかん;
                let hb0 = A!().hp;
                if let Some(bb) = hp_berry_now(pack, &mut A!(), nerv) {
                    race_cause(aidx, "berry", hb0 - A!().hp);
                    let an = A!().name;
                    sides[didx].opp_view.on_item(an, bb);
                }
            }
            continue;
        }
        real_hits += 1;

        if D!().item == Some(l.きあいのタスキ) && D!().hp == D!().max_hp && dmg >= D!().hp {
            dmg = D!().hp - 1;
            D!().item = None;
            it::on_item_consumed(pack, &mut D!());
            let dn = D!().name;
            sides[aidx].opp_view.on_item(dn, l.きあいのタスキ);
        }
        if D!().ability == l.がんじょう && D!().hp == D!().max_hp && dmg >= D!().hp && !mold {
            dmg = D!().hp - 1;
            let dn = D!().name;
            sides[aidx].opp_view.on_ability(dn, l.がんじょう);
        }
        if D!().item == Some(l.きあいのハチマキ) && dmg >= D!().hp && rng.random() < 0.10 {
            dmg = D!().hp - 1;
            let dn = D!().name;
            sides[aidx].opp_view.on_item(dn, l.きあいのハチマキ);
        }

        let hp0 = D!().hp;
        D!().take_damage(dmg);
        // 再生表示用: 残りHPで頭打ちにする前の技のダメージ（とどめの一撃も技そのものの値を見せる）
        race_cause(didx, "rawmove", dmg);
        total_dmg += dmg;
        dealt_hp += hp0 - D!().hp;
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
        // ノーマルジュエル: ノーマル技を撃つと消費（威力補正は pack.type_boost）。
        // 消費は実戦経路だけで行う。calc_damage の中でやるとAIの見積りを呼ぶだけで無くなる。
        if A!().item == Some(pack.sy.it.ノーマルジュエル)
            && eff_type == pack.tc.ノーマル
            && mv.category != Cat::Status
        {
            A!().item = None;
            it::on_item_consumed(pack, &mut A!());
        }

        // レッドカード: ダメージを与えてきた相手を追い出す（消費）。持ち主は防御側。
        // マジックミラーと同じ force_switch を使う＝処理タイミングも既存と揃える。
        if D!().item == Some(pack.sy.it.レッドカード) && total_dmg > 0 && A!().is_alive {
            let has_bench = (0..sides[aidx].party.len())
                .any(|i| sides[aidx].party[i].is_alive && i != sides[aidx].active_idx);
            if has_bench {
                D!().item = None;
                it::on_item_consumed(pack, &mut D!());
                if A!().ability != l.ばんけん {
                    A!().force_switch = true;
                }
            }
        }

        // ききかいひ: HPが1/2以下になると手持ちに戻る（この技で1/2を跨いだ時のみ）
        if D!().ability == l.ききかいひ
            && total_dmg > 0
            && D!().is_alive
            && D!().hp * 2 <= D!().max_hp
            && (D!().hp + total_dmg) * 2 > D!().max_hp
        {
            let has_bench = (0..sides[didx].party.len())
                .any(|i| sides[didx].party[i].is_alive && i != sides[didx].active_idx);
            if has_bench {
                D!().pivot_out = true;
            }
        }

        // だっしゅつボタン: ダメージを受けた自分が手持ちに戻る（消費）。
        // 交代先は選べる想定なので、ランダム交代ではなくピボット扱いにする。
        if D!().item == Some(pack.sy.it.だっしゅつボタン) && total_dmg > 0 && D!().is_alive {
            let has_bench = (0..sides[didx].party.len())
                .any(|i| sides[didx].party[i].is_alive && i != sides[didx].active_idx);
            if has_bench {
                D!().item = None;
                it::on_item_consumed(pack, &mut D!());
                D!().pivot_out = true;
            }
        }

        // ふうせん: 技のダメージを受けると割れて無くなる
        if D!().item == Some(pack.sy.it.ふうせん) && total_dmg > 0 {
            D!().item = None;
            it::on_item_consumed(pack, &mut D!());
            let dn = D!().name;
            sides[aidx].opp_view.on_item(dn, pack.sy.it.ふうせん);
        }

        // いのちのたま: 技1回につき1回（連続技は最後に当てた発の後）
        if A!().item == Some(l.いのちのたま) && mv.category != Cat::Status && A!().ability != l.マジックガード
            && (hit_i == hits - 1 || !D!().is_alive)
        {
            let recoil = std::cmp::max(1, ((A!().max_hp as f64) / 10.0).floor() as i64);
            let h0 = A!().hp;
            A!().take_damage(recoil);
            race_cause(aidx, "lifeorb", h0 - A!().hp);
            let an = A!().name;
            sides[didx].opp_view.on_item(an, l.いのちのたま);
            {
            let nerv = D!().is_alive && D!().ability == l.きんちょうかん;
            let hb0 = A!().hp;
            if let Some(bb) = hp_berry_now(pack, &mut A!(), nerv) {
                race_cause(aidx, "berry", hb0 - A!().hp);
                let an = A!().name;
                sides[didx].opp_view.on_item(an, bb);
            }
        }
        }
        {
            let helmet = D!().item == Some(l.ゴツゴツメット);
            let h0 = A!().hp;
            let (a, d) = two!();
            ab::rough_skin_recoil(pack, a, d, &mv, field);
            race_cause(aidx, if helmet { "helmet" } else { "roughskin" }, h0 - a.hp);
        }
        {
            let nerv = D!().is_alive && D!().ability == l.きんちょうかん;
            let hb0 = A!().hp;
            if let Some(bb) = hp_berry_now(pack, &mut A!(), nerv) {
                race_cause(aidx, "berry", hb0 - A!().hp);
                let an = A!().name;
                sides[didx].opp_view.on_item(an, bb);
            }
        }
        // 接触して初めて分かる防御側の持ち物/特性を開示（条件は rough_skin_recoil と一致）
        if A!().ability != l.えんかく && is_contact_move(pack, &mv) {
            let (dn, dit, dab) = (D!().name, D!().item, D!().ability);
            if dit == Some(l.ゴツゴツメット) {
                sides[aidx].opp_view.on_item(dn, l.ゴツゴツメット);
            } else if sides[aidx].belief.0.is_some() {
                // 否定的観測（battle.py と 1:1）: 接触技を当てたのに反動が無かった＝ゴツゴツメットではない
                let mut bl = sides[aidx].belief.0.take().unwrap();
                bl.observe_absent_item(pack, dn, &["ゴツゴツメット"]);
                sides[aidx].belief.0 = Some(bl);
            }
            if dab == l.さめはだ || dab == l.てつのとげ {
                sides[aidx].opp_view.on_ability(dn, dab);
            }
        }
        if D!().beak_primed && is_contact_move(pack, &mv) && A!().is_alive {
            apply_status(pack, &mut A!(), st.burn, false, Some(&*field));
        }
        if (n == l.ついばむ || n == l.むしくい) && A!().is_alive && is_berry(pack, D!().item) {
            let berry = D!().item.unwrap();
            D!().item = None;
            it::on_item_consumed(pack, &mut D!());
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
            ab::on_after_hit(pack, a, d, &mv, field, rng);
        }
        if D!().is_alive && A!().ability == l.ポイズンタッチ && is_contact_move(pack, &mv) {
            if rng.random() < 0.30 {
                let ok = apply_status(pack, &mut D!(), st.poison, false, Some(&*field));
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
                it::on_item_consumed(pack, &mut D!());
            }
        }
        if !D!().is_alive {
            {
                let (a, d) = two!();
                ab::on_defender_ko(pack, a, d, dmg);
            }
            ab::on_ko(pack, &mut A!());
        }
        // 連続技の途中でHPが半分以下になったら、次のヒットの前にオボンのみ等を食べる（最後のヒットの後は下の従来の位置）
        if hit_i < hits - 1 && D!().is_alive {
            let nerv = A!().is_alive && A!().ability == l.きんちょうかん;
            let hb0 = D!().hp;
            if let Some(bb) = hp_berry_now(pack, &mut D!(), nerv) {
                race_cause(didx, "berry", hb0 - D!().hp);
                let dn = D!().name;
                sides[aidx].opp_view.on_item(dn, bb);
            }
        }
    }

    let sub_absorbed = sub_hits > 0 && real_hits == 0;
    if any_crit && D!().is_alive && D!().ability == l.いかりのつぼ && !sub_absorbed {
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
    if A!().item == Some(l.かいがらのすず) && dealt_hp > 0 && A!().is_alive && can_heal(&A!()) {
        let heal = std::cmp::max(1, ((dealt_hp as f64) / 8.0).floor() as i64);
        let h0 = A!().hp;
        A!().hp = std::cmp::min(A!().max_hp, A!().hp + heal);
        race_cause(aidx, "shellbell", h0 - A!().hp);
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
            if dealt_hp > 0 && A!().is_alive && D!().ability == l.ヘドロえき {
                // マジックガード は ヘドロえき のダメージを受けない（回復もしない）
                if A!().ability != l.マジックガード {
                    let dm = std::cmp::max(1, ((dealt_hp as f64) * r).floor() as i64);
                    let h0 = A!().hp;
                    A!().take_damage(dm);
                    race_cause(aidx, "liquidooze", h0 - A!().hp);
                    let nerv = D!().is_alive && D!().ability == l.きんちょうかん;
                    let hb0 = A!().hp;
                    if let Some(bb) = hp_berry_now(pack, &mut A!(), nerv) {
                        race_cause(aidx, "berry", hb0 - A!().hp);
                        let an = A!().name;
                        sides[didx].opp_view.on_item(an, bb);
                    }
                }
            } else if dealt_hp > 0 && A!().is_alive && can_heal(&A!()) {
                let mut heal = std::cmp::max(1, ((dealt_hp as f64) * r).floor() as i64);
                if A!().item == Some(l.おおきなねっこ) {
                    heal = ((heal as f64) * 1.3).floor() as i64;
                }
                let h0 = A!().hp;
                A!().hp = std::cmp::min(A!().max_hp, A!().hp + heal);
                race_cause(aidx, "drain", h0 - A!().hp);
            }
        }
    }

    if D!().is_alive && D!().ability == l.のろわれボディ && !sub_absorbed && rng.random() < 0.30 {
        if A!().disabled_move.is_none() {
            A!().disabled_move = Some(n);
            A!().disabled_turns = 3;
        }
    }
    if D!().ability == l.こぼれダネ && total_dmg > 0 && !sub_absorbed && !field.grassy_terrain {
        it::set_terrain(field, 1, 5);
        {
            let (dp, ap) = { let (x, y) = two!(); (y, x) };
            crate::items::try_terrain_seed(pack, dp, field);
            crate::items::try_terrain_seed(pack, ap, field);
        }
    }

    if D!().ability == l.すなはき && total_dmg > 0 && !sub_absorbed && field.weather != Some(we.sandstorm) {
        field.weather = Some(we.sandstorm);
        field.weather_count = 5;
    }
    if D!().ability == l.どくげしょう && mv.category == Cat::Physical && total_dmg > 0 && !sub_absorbed {
        let fi = sides[aidx].field_idx;
        if field.toxic_spikes[fi] < 2 {
            field.toxic_spikes[fi] += 1;
        }
    }

    // はたきおとす
    if n == l.はたきおとす && D!().is_alive && D!().item.is_some() && !sub_absorbed {
        let itm = D!().item.unwrap();
        if is_megastone(pack, Some(itm)) {
            // 失敗
        } else if D!().ability == l.ねんちゃく {
            // 失敗
        } else {
            let dn = D!().name;
            sides[aidx].opp_view.on_item(dn, itm);
            D!().item = None;
            it::on_item_consumed(pack, &mut D!());
        }
    }

    // 固定ダメージ技（いかりのまえば・ちきゅうなげ 等）が みがわり に当たったら みがわり が受ける（battle.py _to_sub）
    macro_rules! to_sub {
        ($d:expr) => {{
            let dd: i64 = $d;
            let sh = D!().substitute_hp;
            if sub_absorbed && sh > 0 {
                D!().substitute_hp = std::cmp::max(0, sh - dd);
                total_dmg += dd;
                true
            } else {
                false
            }
        }};
    }
    // いかりのまえば
    if n == l.いかりのまえば && D!().is_alive && !to_sub!(std::cmp::max(1, D!().hp / 2)) {
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
        if !to_sub!(50) {
            D!().take_damage(50);
            total_dmg += 50;
        }
    }
    if n == l.ナイトヘッド && D!().is_alive {
        if D!().has_type(pack.tc.ノーマル) {
            return;
        }
        if !to_sub!(50) {
            D!().take_damage(50);
            total_dmg += 50;
        }
    }
    if n == l.いのちがけ && D!().is_alive {
        let dmg = A!().hp;
        if !to_sub!(dmg) {
            D!().take_damage(dmg);
            total_dmg += dmg;
        }
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
            if !to_sub!(extra) {
                D!().take_damage(extra);
                total_dmg += extra;
            }
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
    if n == l.くらいつく && total_dmg > 0 && D!().is_alive && !sub_absorbed {
        D!().trapped = true;
        A!().trapped = true;
    }

    if n == l.きょけんとつげき && A!().is_alive {
        A!().defenseless = true;
    }

    if (n == l.ドラゴンテール || n == l.ほえる || n == l.ふきとばし || n == l.ともえなげ)
        && D!().is_alive
        && !sub_absorbed
    {
        D!().force_switch = true;
    }

    if total_dmg > 0 && !sub_absorbed && !field.no_view {
        let (dn, dhp, dmax) = (D!().name, D!().hp, D!().max_hp);
        let an = A!().name;
        sides[aidx].opp_view.on_hp_change(dn, dhp, dmax, total_dmg, Some(n), Some(an));
        // 推定器(任意): 観測した被ダメージ割合で EV/性格をベイズ更新（battle.py:1384）
        // 観測がダメージ式1回分と一致する場合だけ使う（連続技・急所・倒した/耐えた一撃は除く。battle.py と同じ）
        let obs_ok = hits == 1 && !critical && D!().is_alive && D!().hp > 1;
        if obs_ok && sides[aidx].belief.0.is_some() {
            let frac = (crate::belief::hp_pct(dhp + total_dmg, dmax) - crate::belief::hp_pct(dhp, dmax)) as f64;
            let mut bl = sides[aidx].belief.0.take().unwrap();
            let mut att = std::mem::take(&mut sides[aidx].party[ai]);
            bl.observe_damage(pack, dn, &mut att, &mv, frac, field, false, rng,
                              pre_def.as_ref(), pre_att.as_ref());
            sides[aidx].party[ai] = att;
            sides[aidx].belief.0 = Some(bl);
        }
        // 与ダメージ観測（belief.py と 1:1）: 殴られた側は「自分がどれだけ減ったか」から
        // 相手の攻撃側 EV/性格を絞る。被ダメージ観測は相手の耐久しか絞れない。
        if obs_ok && sides[didx].belief.0.is_some() {
            let frac = total_dmg as f64;
            let mut bl = sides[didx].belief.0.take().unwrap();
            let mut def = std::mem::take(&mut sides[didx].party[di]);
            bl.observe_damage_dealt(pack, an, &mut def, &mv, frac, field, false, rng,
                                    pre_att.as_ref(), pre_def.as_ref());
            sides[didx].party[di] = def;
            sides[didx].belief.0 = Some(bl);
        }
    }

    // オボンのみ/オレンのみ: 被弾でHPが半分以下になった直後（与ダメージの観測の後＝見える減り方は回復前）
    {
        let nerv = A!().is_alive && A!().ability == l.きんちょうかん;
        let hb0 = D!().hp;
        if let Some(bb) = hp_berry_now(pack, &mut D!(), nerv) {
            race_cause(didx, "berry", hb0 - D!().hp);
            let dn = D!().name;
            sides[aidx].opp_view.on_item(dn, bb);
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
        || n == l.がんせきほう
        || n == l.スターアサルト)
        && A!().is_alive
    {
        A!().recharge = true;
    }

    if n == l.うちおとす && total_dmg > 0 && D!().is_alive && !sub_absorbed {
        D!().grounded = true;
        D!().magnet_rise = false;
        let cm = D!().charging_move;
        if cm == Some(l.そらをとぶ) || cm == Some(l.とびはねる) {
            D!().charging_move = None;
        }
    }
    if n == l.クリアスモッグ && total_dmg > 0 && D!().is_alive && !sub_absorbed {
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
    if (n == l.こうそくスピン || n == l.キラースピン) && total_dmg > 0 && A!().is_alive {
        let mi = sides[aidx].field_idx;
        field.stealth_rock[mi] = false;
        field.spikes[mi] = 0;
        field.toxic_spikes[mi] = 0;
        field.sticky_web[mi] = false;
        if n == l.こうそくスピン {
            A!().stage_speed = std::cmp::min(6, A!().stage_speed + 1);
        }
    }
    if n == l.キラースピン && total_dmg > 0 && D!().is_alive && !sub_absorbed {
        if apply_status(pack, &mut D!(), st.poison, false, Some(&*field)) {
            it::try_cure_berry(pack, &mut D!());
        }
    }
    *dmg_out = total_dmg;
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
    if (n == l.どろぼう || n == l.ほしがる) && total_dmg > 0 && A!().is_alive && !sub_absorbed {
        if A!().item.is_none() && D!().item.is_some() {
            let itm = D!().item.unwrap();
            if is_megastone(pack, Some(itm)) || D!().ability == l.ねんちゃく {
                // 奪えない
            } else {
                A!().item = Some(itm);
                D!().item = None;
                it::on_item_consumed(pack, &mut D!());
            }
        }
    }
    if A!().ability == l.マジシャン
        && total_dmg > 0
        && !sub_absorbed
        && A!().is_alive
        && A!().item.is_none()
        && D!().item.is_some()
        && !is_megastone(pack, D!().item)
        && D!().ability != l.ねんちゃく
    {
        A!().item = D!().item;
        D!().item = None;
        it::on_item_consumed(pack, &mut D!());
    }
    if D!().ability == l.わるいてぐせ
        && !sub_absorbed
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
        it::on_item_consumed(pack, &mut A!());
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
        apply_secondary(pack, a, d, &mv, total_dmg, field, dsg, rng, sub_absorbed);
    }
    {
        let (a, d) = two!();
        let h0 = a.hp;
        apply_recoil(pack, a, d, &mv, dealt_hp);
        race_cause(aidx, "recoil", h0 - a.hp);
    }
    {
        let nerv = D!().is_alive && D!().ability == l.きんちょうかん;
        let ha0 = A!().hp;
        if let Some(bb) = hp_berry_now(pack, &mut A!(), nerv) {
            race_cause(aidx, "berry", ha0 - A!().hp);
            let an = A!().name;
            sides[didx].opp_view.on_item(an, bb);
        }
    }

    // おやこあい（2発目も みがわり が残っていれば みがわり が受ける）
    let pb_sub = D!().substitute_hp;
    if A!().ability == l.おやこあい && hits == 1 && total_dmg > 0 && D!().is_alive && pb_sub > 0
        && !pack.flags(n).sound && A!().ability != l.すりぬけ
    {
        let pb = std::cmp::max(1, ((total_dmg as f64) * 0.25).floor() as i64);
        D!().substitute_hp = std::cmp::max(0, pb_sub - pb);
        {
            let (a, d) = two!();
            let h0 = a.hp;
            apply_recoil(pack, a, d, &mv, std::cmp::min(pb, pb_sub));
            race_cause(aidx, "recoil", h0 - a.hp);
        }
        let nerv = D!().is_alive && D!().ability == l.きんちょうかん;
        let hb0 = A!().hp;
        if let Some(bb) = hp_berry_now(pack, &mut A!(), nerv) {
            race_cause(aidx, "berry", hb0 - A!().hp);
            let an = A!().name;
            sides[didx].opp_view.on_item(an, bb);
        }
    } else if A!().ability == l.おやこあい && hits == 1 && total_dmg > 0 && D!().is_alive {
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
        let pb0 = D!().hp;
        D!().take_damage(pb);
        race_cause(didx, "rawmove", pb);
        let pb_dealt = pb0 - D!().hp;
        {
            let nerv = A!().is_alive && A!().ability == l.きんちょうかん;
            let hb0 = D!().hp;
            if let Some(bb) = hp_berry_now(pack, &mut D!(), nerv) {
                race_cause(didx, "berry", hb0 - D!().hp);
                let dn = D!().name;
                sides[aidx].opp_view.on_item(dn, bb);
            }
        }
        if D!().is_alive {
            {
                let (a, d) = two!();
                ab::on_after_hit(pack, a, d, &mv, field, rng);
            }
            let dsg2 = sides[didx].safeguard;
            let (a, d) = two!();
            apply_secondary(pack, a, d, &mv, pb, field, dsg2, rng, false);
        }
        {
            let helmet = D!().item == Some(l.ゴツゴツメット);
            let h0 = A!().hp;
            let (a, d) = two!();
            ab::rough_skin_recoil(pack, a, d, &mv, field);
            race_cause(aidx, if helmet { "helmet" } else { "roughskin" }, h0 - a.hp);
        }
        {
            let (a, d) = two!();
            let h0 = a.hp;
            apply_recoil(pack, a, d, &mv, pb_dealt);
            race_cause(aidx, "recoil", h0 - a.hp);
        }
        {
            let nerv = D!().is_alive && D!().ability == l.きんちょうかん;
            let hb0 = A!().hp;
            if let Some(bb) = hp_berry_now(pack, &mut A!(), nerv) {
                race_cause(aidx, "berry", hb0 - A!().hp);
                let an = A!().name;
                sides[didx].opp_view.on_item(an, bb);
            }
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
pub fn self_boosts(pack: &Pack, n: u16) -> Option<Vec<(u8, i32)>> {
    let l = &pack.sy.l;
    let v = if n == l.つるぎのまい {
        vec![(0u8, 2i32)]
    } else if n == l.わるだくみ {
        vec![(2, 2)]
    } else if n == l.りゅうのまい {
        vec![(0, 1), (4, 1)]
    } else if n == l.ギアチェンジ {
        vec![(0, 1), (4, 2)]
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

/// battle.py `_has_bench`: 交代できる控え（場に出ていない生存個体）がいるか
fn has_bench(side: &Side) -> bool {
    side.party.iter().enumerate().any(|(i, p)| p.is_alive && i != side.active_idx)
}

pub fn apply_status_move(
    pack: &Pack,
    sides: &mut [Side; 2],
    field: &mut Field,
    aidx: usize,
    mv: &DMove,
    rng: &mut dyn BRng,
    target_pending: bool,
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
    if (n == l.ちょうはつ || n == l.アンコール || n == l.やどりぎのタネ || n == l.あくび
        || n == l.どくびし || n == l.ねばねばネット)
        && D!().ability == l.マジックミラー
    {
        if A!().ability != l.マジックミラー {
            apply_status_move(pack, sides, field, didx, mv, rng, false);
        }
        return;
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
    // すてゼリフ を跳ね返すと使った側の能力が下がる（どちらも交代しない）
    if n == l.すてゼリフ && D!().ability == l.マジックミラー && A!().ability != l.マジックミラー {
        let (a, d) = two!();
        foe_stat_drop(pack, d, a, &[(0, -1), (2, -1)]);
        return;
    }

    if n == l.ひっくりかえす {
        if D!().ability == l.マジックミラー && A!().ability != l.マジックミラー {
            apply_status_move(pack, sides, field, didx, mv, rng, false);
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
        // 能力が変わらなければ交代しない（ミラーアーマー で跳ね返されたときは交代する）
        let changed = {
            let (a, d) = two!();
            foe_stat_drop(pack, a, d, &[(0, -1), (2, -1)])
        };
        if changed {
            A!().pivot_out = true;
        }
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
        if A!().stockpile_count <= 0 || !can_heal(&A!()) {
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
        let aab = A!().ability;
        if aab == l.ふみん || aab == l.やるき || aab == l.スイートベール || aab == l.きよめのしお
            || crate::damage::terrain_blocks_sleep(pack, &A!(), field)
        {
            return;
        }
        A!().hp = A!().max_hp;
        A!().status = Some(st.sleep);
        A!().sleep_count = 3;
        A!().sleep_acts = 0;
        A!().sleep_rest = true;
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
        let dab = D!().ability;
        if D!().status.is_none() && D!().yawn_count == 0
            && dab != l.ふみん && dab != l.やるき && dab != l.スイートベール && dab != l.きよめのしお
            && !(dab == l.リーフガード && effective_weather(pack, field, Some(&D!())) == Some(we.sunny))
            && !crate::damage::terrain_blocks_sleep(pack, &D!(), field)
            && sides[didx].safeguard == 0
        {
            D!().yawn_count = 2;
        }
        return;
    }

    if n == l.アンコール {
        if D!().ability == l.アロマベール {
        } else if let Some(lm) = D!().last_used_move {
            if D!().encore_count == 0 && !pack.flags(lm).encore_fail && move_pp(&D!(), lm) > 0 {
                D!().encore_count = if target_pending { 3 } else { 4 };
                D!().locked_move = Some(lm);
            }
        }
        return;
    }

    if n == l.ちょうはつ {
        if D!().ability == l.アロマベール {
        } else if D!().taunt_count == 0 {
            D!().taunt_count = if target_pending || D!().switched_this_turn { 3 } else { 4 };
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

    if n == l.はいすいのじん && A!().no_retreat {
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
            A!().no_retreat = true;
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
        // 使ったターンを含め5ターン（交代で終わる）
        if A!().magnet_rise || A!().grounded || A!().rooted || field.gravity > 0 {
            return;
        }
        A!().magnet_rise = true;
        A!().levitate_turns = 5;
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
        // 入れ替わった持ち物は両者に見える（battle.py と同じ）
        let (an, dn) = (A!().name, D!().name);
        sides[aidx].opp_view.on_item_swapped(dn, a);
        sides[didx].opp_view.on_item_swapped(an, d);
        if a.is_some() && A!().item.is_none() {
            it::on_item_consumed(pack, &mut A!());
        }
        if d.is_some() && D!().item.is_none() {
            it::on_item_consumed(pack, &mut D!());
        }
        return;
    }
    // 同じフィールドでは失敗
    if (n == l.グラスフィールド && field.grassy_terrain)
        || (n == l.ミストフィールド && field.misty_terrain)
        || (n == l.エレキフィールド && field.electric_terrain)
        || (n == l.サイコフィールド && field.psychic_terrain)
    {
        return;
    }
    if n == l.グラスフィールド {
        let tt = it::terrain_turns(pack, A!().item);
        it::set_terrain(field, 1, tt);
        it::try_terrain_seed(pack, &mut A!(), field);
        it::try_terrain_seed(pack, &mut D!(), field);
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
                execute_move(pack, sides, field, aidx, &act, None, rng, &mut 0);
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
                sides[aidx].party[ai].via_call = true;
                execute_move(pack, sides, field, aidx, &act, None, rng, &mut 0);
                sides[aidx].party[ai].via_call = false;
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
                apply_status_move(pack, sides, field, didx, mv, rng, false);
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
                    if val == st.sleep && crate::damage::terrain_blocks_sleep(pack, &D!(), field) {
                        continue;
                    }
                    if dab == l.リーフガード
                        && effective_weather(pack, field, Some(&D!())) == Some(we.sunny)
                    {
                        continue;
                    }
                    let corr = A!().ability == l.ふしょく;
                    let ok = apply_status(pack, &mut D!(), val, corr, Some(&*field));
                    if ok {
                        if val == st.sleep {
                            D!().sleep_count = rng.randint(2, 4);
                            D!().sleep_acts = 0;
                            D!().sleep_rest = false;
                        }
                        it::try_cure_berry(pack, &mut D!());
                        if D!().ability == l.シンクロ
                            && (val == st.poison
                                || val == st.badpoison
                                || val == st.paralysis
                                || val == st.burn)
                            && A!().is_alive
                        {
                            apply_status(pack, &mut A!(), val, false, Some(&*field));
                        }
                    }
                }
                Deb::Confused => {
                    if sg {
                    } else if D!().ability == l.マイペース {
                    } else if crate::damage::misty_blocks(pack, &D!(), Some(&*field)) {
                    } else {
                        D!().confused = true;
                        it::try_cure_berry(pack, &mut D!());
                    }
                }
                Deb::Stage(attr, val) => {
                    if val < 0 && D!().ability == l.ミラーアーマー {
                        ab::reflect_stat_drop(pack, &mut A!(), attr, val);
                        continue;
                    }
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
            if A!().ability != l.マジックミラー && has_bench(&sides[aidx]) {
                A!().force_switch = true;
            }
        } else if dab == l.おうごんのからだ {
            blocked = true;
        } else if dab == l.きゅうばん || dab == l.ばんけん {
            blocked = true;
        } else if n == l.ほえる && dab == l.ぼうおん {
            blocked = true;
        } else if n == l.ふきとばし && dab == l.かぜのり {
            blocked = true;
        }
        if !blocked && has_bench(&sides[didx]) {
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
            A!().perish_count = 4;
        }
        if D!().perish_count == 0 && D!().ability != l.ぼうおん {
            D!().perish_count = 4;
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

    if n == l.たこがため {
        D!().trapped = true;
        D!().octolocked = true;
        return;
    }

    if n == l.コートチェンジ {
        let (ax, dx) = (sides[aidx].field_idx, sides[didx].field_idx);
        field.stealth_rock.swap(ax, dx);
        field.spikes.swap(ax, dx);
        field.toxic_spikes.swap(ax, dx);
        field.sticky_web.swap(ax, dx);
        let (a, b) = sides.split_at_mut(1);
        let (sa, sd) = if aidx == 0 { (&mut a[0], &mut b[0]) } else { (&mut b[0], &mut a[0]) };
        std::mem::swap(&mut sa.reflect, &mut sd.reflect);
        std::mem::swap(&mut sa.reflect_count, &mut sd.reflect_count);
        std::mem::swap(&mut sa.light_screen, &mut sd.light_screen);
        std::mem::swap(&mut sa.light_screen_count, &mut sd.light_screen_count);
        std::mem::swap(&mut sa.aurora_veil, &mut sd.aurora_veil);
        std::mem::swap(&mut sa.aurora_veil_count, &mut sd.aurora_veil_count);
        std::mem::swap(&mut sa.tailwind, &mut sd.tailwind);
        std::mem::swap(&mut sa.tailwind_count, &mut sd.tailwind_count);
        std::mem::swap(&mut sa.safeguard, &mut sd.safeguard);
        std::mem::swap(&mut sa.stealth_rock_set, &mut sd.stealth_rock_set);
        return;
    }

    if n == l.さいきのいのり {
        let tgt = (0..sides[aidx].party.len()).find(|&i| !sides[aidx].party[i].is_alive);
        match tgt {
            None => return,
            Some(i) => {
                let mhp = sides[aidx].party[i].max_hp;
                sides[aidx].party[i].is_alive = true;
                sides[aidx].party[i].hp = std::cmp::max(1, mhp / 2);
                sides[aidx].party[i].status = None;
                return;
            }
        }
    }

    if n == l.いやしのねがい {
        sides[aidx].healing_wish = true;
        let hp = A!().hp;
        A!().take_damage(hp);
        A!().is_alive = false;
        return;
    }

    if n == l.おきみやげ {
        {
            let (a, d) = two!();
            foe_stat_drop(pack, a, d, &[(0, -2), (2, -2)]);
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
            field.stealth_rock[idx] = false;
            sides[sx].stealth_rock_set = false;
        }
        A!().substitute_hp = 0;
        D!().substitute_hp = 0;
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
        // 入れ替わった持ち物は両者に見える（battle.py と同じ）
        let (an, dn) = (A!().name, D!().name);
        sides[aidx].opp_view.on_item_swapped(dn, a);
        sides[didx].opp_view.on_item_swapped(an, d);
        if a.is_some() && A!().item.is_none() {
            it::on_item_consumed(pack, &mut A!());
        }
        if d.is_some() && D!().item.is_none() {
            it::on_item_consumed(pack, &mut D!());
        }
        return;
    }
    if n == l.ミストフィールド {
        let tt = it::terrain_turns(pack, A!().item);
        it::set_terrain(field, 3, tt);
        it::try_terrain_seed(pack, &mut A!(), field);
        it::try_terrain_seed(pack, &mut D!(), field);
        return;
    }
    if n == l.エレキフィールド {
        let tt = it::terrain_turns(pack, A!().item);
        it::set_terrain(field, 0, tt);
        it::try_terrain_seed(pack, &mut A!(), field);
        it::try_terrain_seed(pack, &mut D!(), field);
        return;
    }
    if n == l.サイコフィールド {
        let tt = it::terrain_turns(pack, A!().item);
        it::set_terrain(field, 2, tt);
        it::try_terrain_seed(pack, &mut A!(), field);
        it::try_terrain_seed(pack, &mut D!(), field);
        return;
    }
    if n == l.じゅうでん {
        A!().charged = true;
        A!().stage_sp_defense = std::cmp::min(6, A!().stage_sp_defense + 1);
        return;
    }
    if n == l.しっぽきり {
        let cost = (A!().max_hp + 1) / 2;
        let sub_hp = A!().max_hp / 4;
        if A!().hp > cost && A!().substitute_hp == 0 && has_bench(&sides[aidx]) {
            A!().hp -= cost;
            A!().shed_tail_sub = sub_hp;
            A!().pivot_out = true;
        }
        return;
    }
    if n == l.ちからをすいとる {
        if D!().stage_attack <= -6 || !can_heal(&A!()) {
            return;
        }
        let heal = D!().eff_stat(0);
        A!().hp = std::cmp::min(A!().max_hp, A!().hp + heal);
        let (a, d) = two!();
        foe_stat_drop(pack, a, d, &[(0, -1)]);
        return;
    }
    if n == l.ほおばる {
        if is_berry(pack, A!().item) {
            A!().item = None;
            A!().ate_berry = true;
            A!().stage_defense = std::cmp::min(6, A!().stage_defense + 2);
            it::on_item_consumed(pack, &mut A!());
        }
        return;
    }
    if n == l.かなしばり {
        let lum = D!().last_used_move;
        if lum.is_some() && D!().disabled_move.is_none() && move_pp(&D!(), lum.unwrap()) > 0 {
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
    } else if n == l.かえんボール {
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
    } else if n == l.ドラムアタック {
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
    } else if n == l.うらみつらみ {
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
    } else if n == l.びりびりちくちく {
        0.30
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
    sub_hit: bool,
) {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    let we = &pack.sy.we;
    let n = mv.name;
    // みがわり が受けたときは相手への効果は起きず、自分への効果だけ起きる（battle.py と同じ）
    let tgt = !sub_hit;

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
        // ミストバースト: 相手を倒しても自分は倒れる（以前はこの早期 return で自分が残っていた。battle.py と同じ）
        if n == l.ミストバースト && attacker.is_alive {
            attacker.hp = 0;
            attacker.is_alive = false;
        }
        return;
    }

    if dmg > 0 && tgt {
        defender.times_hit += 1;
    }

    let force_no_secondary = attacker.ability == l.ちからずく || defender.ability == l.りんぷん;

    if n == l.じごくづき && dmg > 0 && defender.is_alive && tgt {
        defender.throat_chop_count = 2;
    }

    let is_bind = n == l.まきつく
        || n == l.しめつける
        || n == l.まとわりつく
        || n == l.ほのおのうず
        || n == l.うずしお
        || n == l.すなじごく
        || n == l.トラバサミ;
    if is_bind && dmg > 0 && defender.is_alive && defender.bound_count == 0 && tgt {
        defender.bound_count = rng.randint(4, 5);
        // しめつけバンドを持つのは「縛った側」。EOTで相手を辿らずに済むよう束縛時に控える。
        defender.bound_by_band = attacker.item == Some(pack.sy.it.しめつけバンド);
    }

    if n == l.なげつける && defender.is_alive && !force_no_secondary && tgt {
        let flung = attacker.last_flung_item;
        let s2 = if flung == Some(l.どくバリ) {
            Some(st.poison)
        } else if flung == Some(l.もうどくだま) {
            Some(st.badpoison)
        } else {
            None
        };
        if let Some(sv) = s2 {
            let ok = apply_status(pack, defender, sv, false, Some(&*field));
            if ok {
                it::try_cure_berry(pack, defender);
            }
        }
    }

    let sg_sec = def_safeguard > 0;
    if let Some((effect, prob)) = status_effects(pack, n) {
        if !force_no_secondary && !sg_sec && tgt {
            let sunny_freeze = effect == Some(st.freeze)
                && effective_weather(pack, field, Some(defender)) == Some(we.sunny);
            if sunny_freeze {
                // 何もしない
            } else if rng.random() < prob {
                match effect {
                    None => {
                        if defender.ability != l.マイペース && !crate::damage::misty_blocks(pack, defender, Some(field)) {
                            defender.confused = true;
                            it::try_cure_berry(pack, defender);
                        }
                    }
                    Some(e) => {
                        let ok = apply_status(pack, defender, e, false, Some(&*field));
                        if ok {
                            it::try_cure_berry(pack, defender);
                        }
                    }
                }
            }
        }
    }

    if n == l.トライアタック && !force_no_secondary && tgt && rng.random() < 0.20 {
        let idx = rng.choice(3);
        let effect = [st.paralysis, st.burn, st.freeze][idx];
        if !(effect == st.freeze
            && effective_weather(pack, field, Some(defender)) == Some(we.sunny))
        {
            let ok = apply_status(pack, defender, effect, false, Some(&*field));
            if ok {
                it::try_cure_berry(pack, defender);
            }
        }
    }

    if (n == l.しっとのほのお || n == l.みわくのボイス) && !force_no_secondary && tgt {
        let any_up = (0..7u8).any(|i| defender.stage(i) > 0);
        if any_up {
            if n == l.みわくのボイス {
                if defender.ability != l.マイペース && !crate::damage::misty_blocks(pack, defender, Some(field)) {
                    defender.confused = true;
                    it::try_cure_berry(pack, defender);
                }
            } else if apply_status(pack, defender, st.burn, false, Some(&*field)) {
                it::try_cure_berry(pack, defender);
            }
        }
    }

    if defender.ability == l.りんぷん {
        return;
    }

    if let Some((stat, delta0, prob)) = def_downs(pack, n) {
        if !force_no_secondary && tgt {
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

    if n == l.ぶきみなじゅもん && defender.is_alive && tgt {
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
        if fp > 0.0 && !force_no_secondary && tgt && rng.random() < fp {
            if defender.ability != l.せいしんりょく && defender.ability != l.どんかん {
                defender.flinched = true;
            }
        }
    }

    if n == l.フェイタルクロー && defender.is_alive && !force_no_secondary && tgt && rng.random() < 0.30 {
        let idx = rng.choice(3);
        let chosen = [st.poison, st.paralysis, st.sleep][idx];
        let ok = !(chosen == st.sleep && crate::damage::terrain_blocks_sleep(pack, defender, field))
            && apply_status(pack, defender, chosen, false, Some(&*field));
        if ok {
            if chosen == st.sleep {
                defender.sleep_count = rng.randint(2, 4);
                defender.sleep_acts = 0;
                defender.sleep_rest = false;
            }
            it::try_cure_berry(pack, defender);
        }
    }

    if n == l.かげぬい && dmg > 0 && defender.is_alive && tgt {
        defender.trapped = true;
    }

    if (n == l.ねっとう || n == l.ねっさのだいち) && tgt {
        if defender.is_alive && defender.status == Some(st.freeze) {
            defender.status = None;
        }
    }
    if n == l.ねっとう || n == l.もえつきる || n == l.ねっさのだいち || n == l.かえんボール {
        if attacker.status == Some(st.freeze) {
            attacker.status = None;
        }
    }
    if n == l.でんこうそうげき && attacker.has_type(pack.tc.でんき) {
        let mut rem: Vec<Ty> = Vec::new();
        if attacker.type1 != pack.tc.でんき {
            rem.push(attacker.type1);
        }
        if let Some(t2) = attacker.type2 {
            if t2 != pack.tc.でんき {
                rem.push(t2);
            }
        }
        attacker.type1 = if rem.is_empty() { pack.tc.ノーマル } else { rem[0] };
        attacker.type2 = if rem.len() > 1 { Some(rem[1]) } else { None };
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

    if n == l.しおづけ && defender.is_alive && !force_no_secondary && tgt && !defender.salted {
        defender.salted = true;
    }
    if n == l.みずあめボム && defender.is_alive && !force_no_secondary && tgt {
        defender.syrup_count = 3;
    }
    if n == l.サイコノイズ && defender.is_alive && !force_no_secondary && tgt {
        defender.heal_block_count = 2;
    }
    if n == l.うたかたのアリア && defender.is_alive && defender.status == Some(st.burn) && tgt {
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
                if attacker.ability != l.マイペース && !crate::damage::misty_blocks(pack, attacker, Some(field)) {
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

/// オボンのみ/オレンのみ: HPが半分以下になった直後に発動する（実機どおり。ターン終了まで待たない）。
/// 被弾直後・反動/いのちのたま/ゴツゴツメット等で減った直後に呼ぶ。発動したらそのきのみを返す（開示は呼び出し側）。
/// opp_nervous: 相手が場にいて きんちょうかん。battle.py `_hp_berry_now` と同一。
pub fn hp_berry_now(pack: &Pack, p: &mut Poke, opp_nervous: bool) -> Option<crate::interner::Sym> {
    let l = &pack.sy.l;
    if !p.is_alive || p.hp > p.max_hp / 2 || opp_nervous || !can_heal(p) {
        return None;
    }
    let berry = p.item?;
    let heal = if berry == l.オボンのみ { p.max_hp / 4 } else if berry == l.オレンのみ { 10 } else { return None };
    p.hp = std::cmp::min(p.max_hp, p.hp + heal);
    p.last_berry = Some(berry);
    p.item = None;
    p.ate_berry = true;
    it::on_item_consumed(pack, p);
    Some(berry)
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
        let mut b = Battle { sides: [s1, s2], field, turn: 0, item_snap: Vec::new() };
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
            release_by_leaving(self.sides[1 - fx].active_mut());
            {
                let Battle { sides, field, .. } = self;
                entry_effects_side(pack, sides, field, fx);
            }
            self.apply_healing_wish(fx);
            let nm = self.sides[fx].active().clone();
            self.sides[ox].opp_view.on_enter(pack, &nm);
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
                release_by_leaving(self.sides[1 - mx].active_mut());
                {
                    let Battle { sides, field, .. } = self;
                    entry_effects_side(pack, sides, field, mx);
                }
                self.apply_healing_wish(mx);
                let nm = self.sides[mx].active().clone();
                self.sides[ox].opp_view.on_enter(pack, &nm);
                self.faint_switch(pack, mx, rng);
            }
            return;
        }

        if action.kind == ActKind::Move && action.mv.is_some() {
            let enc_action;
            // アンコールされた技のPPが尽きたらアンコールは解ける（わるあがき等をその技に差し替えない）
            {
                let a = self.sides[mx].active_mut();
                if a.encore_count > 0 {
                    if let Some(lm) = a.locked_move {
                        if move_pp(a, lm) <= 0 {
                            a.encore_count = 0;
                            a.locked_move = None;
                        }
                    }
                }
            }
            let action = {
                let a = self.sides[mx].active();
                let cur = action.mv.as_ref().map(|m| m.name);
                match a.locked_move {
                    Some(lm) if a.encore_count > 0 && cur != Some(lm) => {
                        match a.moves.iter().position(|m| m.name == lm) {
                            Some(ei) => {
                                enc_action = Action {
                                    kind: ActKind::Move,
                                    mv: Some(a.moves[ei].clone()),
                                    move_idx: ei as i64,
                                    do_mega: action.do_mega,
                                    ..Default::default()
                                };
                                &enc_action
                            }
                            None => action,
                        }
                    }
                    _ => action,
                }
            };
            {
                let Battle { sides, field, .. } = self;
                execute_move(pack, sides, field, mx, action, opp_action, rng, &mut 0);
            }
            it::try_white_herb(pack, self.sides[mx].active_mut());
            it::try_white_herb(pack, self.sides[ox].active_mut());
            // メンタルハーブ: 行動制限を受けた直後に発動
            it::try_mental_herb(pack, self.sides[mx].active_mut());
            it::try_mental_herb(pack, self.sides[ox].active_mut());
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
                    release_by_leaving(self.sides[1 - mx].active_mut());
                    {
                        let Battle { sides, field, .. } = self;
                        entry_effects_side(pack, sides, field, mx);
                    }
                    self.apply_healing_wish(mx);
                    let nm = self.sides[mx].active().clone();
                    self.sides[ox].opp_view.on_enter(pack, &nm);
                    self.faint_switch(pack, mx, rng);
                }
            }

            // だっしゅつボタン: ダメージを受けた側（=相手）が引っ込む。交代先は戦略的に選ぶ。
            // 攻撃側の pivot_out（とんぼがえり等）は上で処理済み。防御側に立つのは本アイテムのみ。
            let opiv = self.sides[ox].active().is_alive && self.sides[ox].active().pivot_out;
            if opiv {
                self.sides[ox].active_mut().pivot_out = false;
                let next_idx = {
                    let Battle { sides, field, .. } = self;
                    let (me, opp) = split2(sides, ox);
                    let oi = opp.active_idx;
                    choose_pivot_target(pack, me, &mut opp.party[oi], false, field, rng)
                };
                if let Some(ni) = next_idx {
                    self.sides[ox].switch_to(pack, ni);
                    release_by_leaving(self.sides[1 - ox].active_mut());
                    {
                        let Battle { sides, field, .. } = self;
                        entry_effects_side(pack, sides, field, ox);
                    }
                    self.apply_healing_wish(ox);
                    let nm = self.sides[ox].active().clone();
                    self.sides[mx].opp_view.on_enter(pack, &nm);
                    self.faint_switch(pack, ox, rng);
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
                    release_by_leaving(self.sides[1 - ox].active_mut());
                    {
                        let Battle { sides, field, .. } = self;
                        entry_effects_side(pack, sides, field, ox);
                    }
                    let nm = self.sides[ox].active().clone();
                    self.sides[mx].opp_view.on_enter(pack, &nm);
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

        // 天候ダメ・持ち物・状態異常・拘束等は素早さの速い側から（battle.py と同一）。同速は side0 が先
        // （分析の speed_tie_p1_first=Some(false) のときだけ side1 が先）。
        let eot_order = {
            let s0 = crate::ai::effective_speed(pack, self.sides[0].active(), &self.field);
            let s1 = crate::ai::effective_speed(pack, self.sides[1].active(), &self.field);
            if s1 > s0 || (s1 == s0 && self.field.speed_tie_p1_first == Some(false)) { [1usize, 0] } else { [0usize, 1] }
        };
        for sx in eot_order {
            let ox = 1 - sx;
            if !self.sides[sx].active().is_alive {
                continue;
            }
            let eot_h0 = self.sides[sx].active().hp;
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
            let eot_h1 = self.sides[sx].active().hp;
            race_cause(sx, "sandstorm", eot_h0 - eot_h1);
            let status_kind = match self.sides[sx].active().status {
                Some(x) if x == st.burn => "burn",
                Some(x) if x == st.badpoison => "badpoison",
                _ => "poison",
            };
            // 状態異常
            {
                let p = self.sides[sx].active_mut();
                if p.ability != l.マジックガード {
                    if p.status == Some(st.burn) {
                        let dmg = std::cmp::max(1, p.max_hp / 16);
                        p.take_damage(dmg);
                    } else if p.status == Some(st.poison) || p.status == Some(st.badpoison) {
                        if p.ability == l.ポイズンヒール {
                            if can_heal(p) {
                                let heal = std::cmp::max(1, p.max_hp / 8);
                                p.hp = std::cmp::min(p.max_hp, p.hp + heal);
                            }
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
            race_cause(sx, status_kind, eot_h1 - self.sides[sx].active().hp);
            if !self.sides[sx].active().is_alive {
                continue;
            }
            // ねをはる/アクアリング
            {
                let p = self.sides[sx].active_mut();
                if (p.rooted || p.aqua_ring) && p.is_alive && can_heal(p) {
                    let heal = std::cmp::max(1, p.max_hp / 16);
                    p.hp = std::cmp::min(p.max_hp, p.hp + heal);
                }
            }
            let eot_h2 = self.sides[sx].active().hp;
            // グラスフィールド: 地面にいるポケモンはターン終了時に最大HPの1/16回復
            if self.field.grassy_terrain {
                let gravity = self.field.gravity > 0;
                let p = self.sides[sx].active_mut();
                let airborne = p.has_type(pack.tc.ひこう) || p.ability == l.ふゆう || p.magnet_rise
                    || p.item == Some(pack.sy.it.ふうせん);
                if p.is_alive && p.hp < p.max_hp && can_heal(p) && (!airborne || p.grounded || gravity) {
                    let heal = std::cmp::max(1, p.max_hp / 16);
                    p.hp = std::cmp::min(p.max_hp, p.hp + heal);
                }
            }
            race_cause(sx, "grassy", eot_h2 - self.sides[sx].active().hp);
            let eot_h3 = self.sides[sx].active().hp;
            // たべのこし / くろいヘドロ
            {
                let (item, is_poison, healable, mg) = {
                    let p = self.sides[sx].active();
                    (p.item, p.has_type(pack.tc.どく), can_heal(p), p.ability == l.マジックガード)
                };
                if item == Some(l.たべのこし) && healable {
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
                            let heal = if healable { std::cmp::max(1, p.max_hp / 16) } else { 0 };
                            let old = p.hp;
                            p.hp = std::cmp::min(p.max_hp, p.hp + heal);
                            (p.name, p.hp > old)
                        };
                        if healed {
                            self.sides[ox].opp_view.on_item(nm, l.くろいヘドロ);
                        }
                    } else if !mg {
                        let p = self.sides[sx].active_mut();
                        let dmg = std::cmp::max(1, p.max_hp / 16);
                        p.take_damage(dmg);
                    }
                }
            }

            {
                let it_now = self.sides[sx].active().item;
                let kind = if it_now == Some(l.くろいヘドロ) { "sludge" } else { "leftovers" };
                race_cause(sx, kind, eot_h3 - self.sides[sx].active().hp);
            }
            // 否定的観測（belief.py と 1:1）: HPが満タンでないのにターン終了で回復しなかった
            // ＝回復持ち物ではない。満タンだと回復が起きなくても何も分からないので除外する。
            {
                let (nm, hp, mx, alive, item, healable) = {
                    let p = self.sides[sx].active();
                    (p.name, p.hp, p.max_hp, p.is_alive, p.item, can_heal(p))
                };
                let not_recov = item != Some(l.たべのこし) && item != Some(l.くろいヘドロ);
                if self.sides[ox].belief.0.is_some() && hp < mx && alive && not_recov && healable {
                    let mut bl = self.sides[ox].belief.0.take().unwrap();
                    bl.observe_absent_item(pack, nm, &["たべのこし", "くろいヘドロ"]);
                    self.sides[ox].belief.0 = Some(bl);
                }
            }

            let berry_blocked = self.sides[ox].active().is_alive
                && self.sides[ox].active().ability == l.きんちょうかん;

            let item_before_berry = self.sides[sx].active().item;
            let eot_h4 = self.sides[sx].active().hp;
            // オボンのみ
            if !berry_blocked {
                let trig = {
                    let p = self.sides[sx].active();
                    p.item == Some(l.オボンのみ) && p.hp <= p.max_hp / 2 && can_heal(p)
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
                    p.item == Some(l.オレンのみ) && p.hp <= p.max_hp / 2 && can_heal(p)
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
            race_cause(sx, "berry", eot_h4 - self.sides[sx].active().hp);
            // 否定的観測（battle.py と 1:1）: 表示HPが半分を確実に下回ったのにきのみが発動しなかった
            // ＝オボンのみ/オレンのみではない。境目（50%付近）ときんちょうかんの時は推論しない
            {
                let (nm, hp, mx, alive, healable) = {
                    let p = self.sides[sx].active();
                    (p.name, p.hp, p.max_hp, p.is_alive, can_heal(p))
                };
                if self.sides[ox].belief.0.is_some() && !berry_blocked && alive && healable
                    && item_before_berry != Some(l.オボンのみ) && item_before_berry != Some(l.オレンのみ)
                    && hp <= mx / 2 && hp * 100 < mx * 49
                {
                    let mut bl = self.sides[ox].belief.0.take().unwrap();
                    bl.observe_absent_item(pack, nm, &["オボンのみ", "オレンのみ"]);
                    self.sides[ox].belief.0 = Some(bl);
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
                    p.seeded && p.is_alive && p.ability != l.マジックガード
                };
                if seeded {
                    let drain = {
                        let p = self.sides[sx].active_mut();
                        let d = std::cmp::max(1, p.max_hp / 8);
                        let h0 = p.hp;
                        p.take_damage(d);
                        race_cause(sx, "leechseed", h0 - p.hp);
                        d
                    };
                    let o = self.sides[ox].active_mut();
                    if o.is_alive && can_heal(o) {
                        let h0 = o.hp;
                        o.hp = std::cmp::min(o.max_hp, o.hp + drain);
                        race_cause(ox, "leechseed", h0 - o.hp);
                    }
                }
            }
            // たこがため（ターン終わりにB/D-1）
            {
                let p = self.sides[sx].active_mut();
                if p.octolocked && p.is_alive {
                    p.stage_defense = std::cmp::max(-6, p.stage_defense - 1);
                    p.stage_sp_defense = std::cmp::max(-6, p.stage_sp_defense - 1);
                }
            }
            // しおづけ
            {
                let p = self.sides[sx].active_mut();
                if p.salted && p.is_alive && p.ability != l.マジックガード {
                    let ws = p.has_type(pack.tc.みず) || p.has_type(pack.tc.はがね);
                    let rate = if ws { 1.0 / 8.0 } else { 1.0 / 16.0 };
                    let dmg = std::cmp::max(1, ((p.max_hp as f64) * rate).floor() as i64);
                    let h0 = p.hp;
                    p.take_damage(dmg);
                    race_cause(sx, "saltcure", h0 - p.hp);
                }
            }
            // あくび
            {
                let p = self.sides[sx].active_mut();
                if p.yawn_count > 0 {
                    p.yawn_count -= 1;
                    if p.yawn_count == 0 && p.status.is_none()
                        && !crate::damage::terrain_blocks_sleep(pack, p, &self.field)
                        && !(p.ability == l.リーフガード
                            && effective_weather(pack, &self.field, Some(&*p)) == Some(pack.sy.we.sunny))
                        && apply_status(pack, p, st.sleep, false, Some(&self.field))
                    {
                        p.sleep_count = rng.randint(2, 4);
                        p.sleep_acts = 0;
                        p.sleep_rest = false;
                    }
                }
            }
            // バインド（拘束した側が倒れていれば解ける）
            if !self.sides[ox].active().is_alive {
                self.sides[sx].active_mut().bound_count = 0;
            }
            {
                let p = self.sides[sx].active_mut();
                if p.bound_count > 0 && p.is_alive {
                    if p.ability != l.マジックガード {
                        let d = std::cmp::max(1, p.max_hp / if p.bound_by_band { 6 } else { 8 });
                        let h0 = p.hp;
                        p.take_damage(d);
                        race_cause(sx, "bind", h0 - p.hp);
                    }
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
                // でんじふゆう: 使ったターンを含め5ターン
                if p.levitate_turns > 0 {
                    p.levitate_turns -= 1;
                    if p.levitate_turns == 0 {
                        p.magnet_rise = false;
                    }
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
            if f.grassy_terrain {
                f.grassy_terrain_count -= 1;
                if f.grassy_terrain_count <= 0 {
                    f.grassy_terrain = false;
                    f.grassy_terrain_count = 0;
                }
            }
        }

        // ねがいごと
        for sx in 0..2usize {
            if self.sides[sx].wish_count > 0 {
                self.sides[sx].wish_count -= 1;
                if self.sides[sx].wish_count == 0 && self.sides[sx].active().is_alive
                    && can_heal(self.sides[sx].active())
                {
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
            if p.cursed && p.is_alive && p.ability != l.マジックガード {
                let d = std::cmp::max(1, p.max_hp / 4);
                let h0 = p.hp;
                p.take_damage(d);
                race_cause(sx, "curse", h0 - p.hp);
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
        // ターン終了後に出たポケモンは次のターンの頭から場にいる扱い（実機の activeTurns。battle.py と同じ）
        for sx in 0..2usize {
            self.sides[sx].active_mut().switched_this_turn = false;
        }
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
        // 先発も「場に出た」（battle.py の run と同じ。隠れ選出の引き直しから外す）
        let a0 = self.sides[0].active().clone();
        let a1 = self.sides[1].active().clone();
        // LEAD_SEEN=0（側2は LEAD_SEEN_2）で旧挙動＝先発を記録しない。A/B 専用
        let on = |k: &str| std::env::var(k).map(|v| v != "0").unwrap_or(true);
        if on("LEAD_SEEN_2") {
            self.sides[1].opp_view.on_enter(pack, &a0);
        }
        if on("LEAD_SEEN") {
            self.sides[0].opp_view.on_enter(pack, &a1);
        }
        // 入場時効果は素早さの速い側から（遅い側の天候・フィールドが後から上書きする）。同速は side0 が先（battle.py と同一）
        {
            let s0 = crate::ai::effective_speed(pack, self.sides[0].active(), &self.field);
            let s1 = crate::ai::effective_speed(pack, self.sides[1].active(), &self.field);
            let order = if s1 > s0 { [1usize, 0] } else { [0usize, 1] };
            let Battle { sides, field, .. } = self;
            for sx in order {
                entry_effects_side(pack, sides, field, sx);
            }
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
    /// battle.py の _sync_item_loss（前回の行動選択時から持ち物が無くなった個体を相手の opp_view へ）
    /// 側 `sx` のメガシンカ（まだなら）。メガ後の特性の入場効果（ひでり等）もここで発動する。
    pub fn mega_one(&mut self, pack: &Pack, sx: usize) {
        let ok = !self.sides[sx].active().mega_evolved && !self.sides[sx].mega_used;
        if !ok {
            return;
        }
        mega_evolve_poke(pack, self.sides[sx].active_mut());
        self.sides[sx].mega_used = true;
        // メガ進化は実機で形態が見える＝メガ石と進化後の特性がその場で確定する
        if !self.field.no_view {
            let ox = 1 - sx;
            let (mn, mit, mab) = {
                let p = self.sides[sx].active();
                (p.name, p.item, p.ability)
            };
            if let Some(itm) = mit {
                self.sides[ox].opp_view.on_item(mn, itm);
            }
            self.sides[ox].opp_view.on_ability(mn, mab);
        }
        let Battle { sides, field, .. } = self;
        let (me, opp) = split2(sides, sx);
        let mi = me.active_idx;
        let oi = opp.active_idx;
        ab::entry_ability(pack, &mut me.party[mi], &mut opp.party[oi], field);
        it::try_white_herb(pack, &mut me.party[mi]);
        it::try_white_herb(pack, &mut opp.party[oi]);
    }

    fn sync_item_loss(&mut self) {
        let cur: Vec<Vec<Option<crate::interner::Sym>>> =
            self.sides.iter().map(|s| s.party.iter().map(|p| p.item).collect()).collect();
        if !self.item_snap.is_empty() {
            for si in 0..2usize {
                let vi = 1 - si;
                for pi in 0..self.sides[si].party.len() {
                    let prev = self.item_snap[si].get(pi).copied().flatten();
                    if let Some(it) = prev {
                        if self.sides[si].party[pi].item.is_none() {
                            let nm = self.sides[si].party[pi].name;
                            self.sides[vi].opp_view.on_item_lost(nm, it);
                        }
                    }
                }
            }
        }
        self.item_snap = cur;
    }

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
            if !self.field.no_view {
                self.sync_item_loss();
            }

            let [action1, action2] = get_acts(self, rng);
            let chooser1 = self.sides[0].active_idx;
            let chooser2 = self.sides[1].active_idx;

            // メガ進化: 素早さの速い側から（遅い側の ひでり 等が後から上書きする）。同速は side0 が先（battle.py と同一）
            let mega_order = {
                let s0 = crate::ai::effective_speed(pack, self.sides[0].active(), &self.field);
                let s1 = crate::ai::effective_speed(pack, self.sides[1].active(), &self.field);
                if s1 > s0 { [1usize, 0] } else { [0usize, 1] }
            };
            for sx in mega_order {
                let a = if sx == 0 { &action1 } else { &action2 };
                if a.do_mega {
                    self.mega_one(pack, sx);
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
            // 行動順の観測（belief.py `_observe_order` と 1:1）。優先度が違うと速度の
            // 情報にならないので見送る。交代は速度と無関係（先に処理される）ので対象外。
            {
                let both_move = action1.kind == ActKind::Move && action2.kind == ActKind::Move;
                // 特性込みの優先度で比べ、速度以外で順番が決まる場面は観測しない（battle.py と同じ）
                let same_pr = both_move && {
                    let Battle { sides, field, .. } = &*self;
                    priority_base(pack, &action1, sides[0].active(), field)
                        == priority_base(pack, &action2, sides[1].active(), field)
                };
                let speed_decides = {
                    let (a0, a1) = (self.sides[0].active().ability, self.sides[1].active().ability);
                    let bad = [l.あとだし, l.クイックドロウ, l.はやあし, l.ぶきよう];
                    !self.field.trick_room && !self.sides[0].tailwind && !self.sides[1].tailwind
                        && !bad.contains(&a0) && !bad.contains(&a1)
                };
                if same_pr && speed_decides {
                    for sx in 0..2usize {
                        let me_first = if sx == 0 { p1_first } else { !p1_first };
                        if self.sides[sx].belief.0.is_none() {
                            continue;
                        }
                        let (my_spd, opp_name, opp_st) = {
                            let Battle { sides, field, .. } = self;
                            (
                                crate::ai::effective_speed(pack, sides[sx].active(), field),
                                sides[1 - sx].active().name,
                                crate::belief::pub_state(sides[1 - sx].active()),
                            )
                        };
                        let mut bl = self.sides[sx].belief.0.take().unwrap();
                        bl.observe_order(pack, opp_name, my_spd, !me_first, &self.field, Some(&opp_st));
                        self.sides[sx].belief.0 = Some(bl);
                    }
                }
            }
            let (fx, ox) = if p1_first { (0usize, 1usize) } else { (1usize, 0usize) };
            let (first_action, second_action) =
                if p1_first { (&action1, &action2) } else { (&action2, &action1) };
            let second_chooser = if ox == 0 { chooser1 } else { chooser2 };

            race_mark(self, 0, fx);
            self.do_action(pack, fx, first_action, Some(second_action), true, rng);
            race_mark(self, 1, fx);
            if !self.sides[ox].has_alive() {
                if self.field.eot_on_last_faint {
                    self.end_of_turn(pack, rng);
                    race_mark(self, 3, 0);
                }
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
                race_mark(self, 2, ox);
            } else {
                self.sides[ox].active_mut().acts_second = true;
                self.do_action(pack, ox, second_action, Some(first_action), false, rng);
                race_mark(self, 1, ox);
                if self.sides[ox].active().is_alive {
                    self.sides[ox].active_mut().acts_second = false;
                }
            }
            if !self.sides[fx].has_alive() && !self.field.eot_on_last_faint {
                on_turn(self);
                break;
            }
            if !self.sides[fx].has_alive() {
                self.end_of_turn(pack, rng);
                race_mark(self, 3, 0);
                on_turn(self);
                break;
            }

            self.end_of_turn(pack, rng);
            race_mark(self, 3, 0);
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

/// 監査5（2026-10-04）の修正。test_all.py 37 と同じ局面
#[cfg(test)]
mod fix5_tests {
    use super::*;
    use crate::poke::build_poke;

    fn pack() -> Pack {
        Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"))
    }

    struct Z;
    impl BRng for Z {
        fn random(&mut self) -> f64 { 0.99 }
        fn choice(&mut self, _n: usize) -> usize { 0 }
        fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
        fn choices(&mut self) -> i64 { 2 }
    }

    const N: &str = "きれいなぬけがら";

    fn sides(p: &mut Pack, a: &[&str], b: &[&str]) -> [Side; 2] {
        let pa: Vec<Poke> = a.iter().map(|s| build_poke(p, s, "M-6")).collect();
        let pb: Vec<Poke> = b.iter().map(|s| build_poke(p, s, "M-6")).collect();
        [Side { party: pa, active_idx: 0, field_idx: 0, ..Default::default() },
         Side { party: pb, active_idx: 0, field_idx: 1, ..Default::default() }]
    }

    fn mv_of(p: &Pack, poke: &Poke, n: &str) -> Action {
        let (i, m) = poke.moves.iter().enumerate().find(|(_, m)| p.intern.resolve(m.name) == n).unwrap();
        Action { kind: ActKind::Move, mv: Some(m.clone()), move_idx: i as i64, switch_to: -1, do_mega: false }
    }

    #[test]
    fn 継続中のフィールドへの登場でシードが発動() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("オオニューラ@サイコシード:ようき:インファイト:0/32/0/0/0/32:かるわざ")],
                          &[&format!("ガブリアス@{N}:ようき:じしん:0/32/0/0/0/32:さめはだ")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        it::set_terrain(&mut f, 2, 5);
        let mut opp = s[1].party[0].clone();
        entry_effects(pr, &mut s[0], 0, &mut f, &mut opp);
        let o = &s[0].party[0];
        assert!(o.item.is_none() && o.stage_sp_defense == 1, "サイコシード発動");
        assert_eq!(o.stage_speed, 2, "かるわざ");
        let mut s2 = sides(&mut p, &[&format!("オオニューラ@サイコシード:ようき:インファイト:0/32/0/0/0/32:かるわざ")],
                           &[&format!("ガブリアス@{N}:ようき:じしん:0/32/0/0/0/32:さめはだ")]);
        let pr: &Pack = &p;
        let mut f2 = Field::default();
        it::set_terrain(&mut f2, 1, 5);
        entry_effects(pr, &mut s2[0], 0, &mut f2, &mut opp);
        assert!(s2[0].party[0].item.is_some(), "別のフィールドでは発動しない");
    }

    #[test]
    fn ふうせんは設置物の接地判定() {
        let mut p = pack();
        let mut s = sides(&mut p, &["ガブリアス@ふうせん:ようき:じしん:0/32/0/0/0/32:さめはだ"],
                          &[&format!("カバルドン@{N}:わんぱく:じしん:32/0/32/0/0/0:すなおこし")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        f.spikes[0] = 3;
        f.sticky_web[0] = true;
        let mut opp = s[1].party[0].clone();
        entry_effects(pr, &mut s[0], 0, &mut f, &mut opp);
        let g = &s[0].party[0];
        assert!(g.hp == g.max_hp && g.stage_speed == 0);
    }

    #[test]
    fn フィールドは1つだけ() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("ゴリランダー@{N}:いじっぱり:グラスフィールド:32/32/0/0/0/0:グラスメイカー")],
                          &[&format!("ガブリアス@{N}:ようき:じしん:0/32/0/0/0/32:さめはだ")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        it::set_terrain(&mut f, 2, 5);
        let a = mv_of(pr, &s[0].party[0], "グラスフィールド");
        let mut d = 0;
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert!(f.grassy_terrain && !f.psychic_terrain && f.psychic_terrain_count == 0);
    }

    #[test]
    fn ほえるは控えがいなければ失敗() {
        let mut p = pack();
        let hip = format!("カバルドン@{N}:わんぱく:ほえる:32/0/32/0/0/0:すなおこし");
        let gab = format!("ガブリアス@{N}:ようき:じしん:0/32/0/0/0/32:さめはだ");
        let mut s = sides(&mut p, &[&hip], &[&gab]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        s[1].party[0].stage_attack = 2;
        let a = mv_of(pr, &s[0].party[0], "ほえる");
        let mut d = 0;
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert!(s[1].party[0].stage_attack == 2 && !s[1].party[0].force_switch, "控え無し: 失敗");
        let mut s = sides(&mut p, &[&hip], &[&gab, &gab.replace("ガブリアス", "ボーマンダ").replace("さめはだ", "いかく")]);
        let pr: &Pack = &p;
        s[1].party[0].stage_attack = 2;
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert!(s[1].party[0].stage_attack == 0 && s[1].party[0].force_switch, "控えあり: 成功");
    }

    #[test]
    fn キラースピンは設置物を除去し素早さは上がらない() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("キラフロル@{N}:ひかえめ:キラースピン|こうそくスピン:32/0/0/32/0/0:どくげしょう")],
                          &[&format!("カバルドン@{N}:わんぱく:じしん:32/0/32/0/0/0:すなおこし")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        f.stealth_rock[0] = true;
        f.spikes[0] = 2;
        f.toxic_spikes[0] = 1;
        f.sticky_web[0] = true;
        f.stealth_rock[1] = true;
        s[0].party[0].seeded = true;
        let a = mv_of(pr, &s[0].party[0], "キラースピン");
        let mut d = 0;
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert!(d > 0);
        assert!(!f.stealth_rock[0] && f.spikes[0] == 0 && f.toxic_spikes[0] == 0 && !f.sticky_web[0]);
        assert!(f.stealth_rock[1], "相手側は残る");
        assert!(!s[0].party[0].seeded && s[0].party[0].stage_speed == 0);
        f.sticky_web[0] = true;
        let a = mv_of(pr, &s[0].party[0], "こうそくスピン");
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert!(!f.sticky_web[0] && s[0].party[0].stage_speed == 1);
    }

    #[test]
    fn ねむるは3回目の行動で起きる() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("カビゴン@{N}:わんぱく:ねむる|のしかかり|ねごと:32/0/32/0/0/0:あついしぼう")],
                          &[&format!("カバルドン@{N}:わんぱく:じしん:32/0/32/0/0/0:すなおこし")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        let sleep = pr.sy.st.sleep;
        s[0].party[0].hp = 10;
        let a = mv_of(pr, &s[0].party[0], "ねむる");
        let mut d = 0;
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert!(s[0].party[0].status == Some(sleep) && s[0].party[0].sleep_count == 3);
        let b = mv_of(pr, &s[0].party[0], "のしかかり");
        execute_move(pr, &mut s, &mut f, 0, &b, None, &mut Z, &mut d);
        execute_move(pr, &mut s, &mut f, 0, &b, None, &mut Z, &mut d);
        assert!(s[0].party[0].status == Some(sleep) && s[1].party[0].hp == s[1].party[0].max_hp);
        execute_move(pr, &mut s, &mut f, 0, &b, None, &mut Z, &mut d);
        assert!(s[0].party[0].status.is_none());
        s[0].party[0].status = Some(sleep);
        s[0].party[0].sleep_count = 1;
        let c = mv_of(pr, &s[0].party[0], "ねごと");
        execute_move(pr, &mut s, &mut f, 0, &c, None, &mut Z, &mut d);
        assert!(s[0].party[0].status.is_none(), "ねごともカウンタを減らす");
        s[0].party[0].hp = 10;
        it::set_terrain(&mut f, 0, 5);
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert!(s[0].party[0].status.is_none() && s[0].party[0].hp == 10, "フィールドで接地ならねむる失敗");
    }

    #[test]
    fn あくびの失敗条件() {
        let mut p = pack();
        let hip = format!("カバルドン@{N}:わんぱく:あくび:32/0/32/0/0/0:すなおこし");
        let gab = format!("ガブリアス@{N}:ようき:じしん:0/32/0/0/0/32:さめはだ");
        let mut s = sides(&mut p, &[&hip], &[&gab]);
        let pr: &Pack = &p;
        let a = mv_of(pr, &s[0].party[0], "あくび");
        let mut d = 0;
        let mut f = Field::default();
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert_eq!(s[1].party[0].yawn_count, 2);
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert_eq!(s[1].party[0].yawn_count, 2, "ねむけ中は失敗");
        for t in 0..2usize {
            let mut s = sides(&mut p, &[&hip], &[&gab]);
            let pr: &Pack = &p;
            let mut f = Field::default();
            f.electric_terrain = t == 0;
            f.misty_terrain = t == 1;
            execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
            assert_eq!(s[1].party[0].yawn_count, 0, "フィールドで接地なら失敗");
        }
        let mut s = sides(&mut p, &[&hip], &[&gab]);
        let pr: &Pack = &p;
        s[1].safeguard = 3;
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert_eq!(s[1].party[0].yawn_count, 0, "しんぴのまもり");
        let mut s = sides(&mut p, &[&hip], &[&gab]);
        let pr: &Pack = &p;
        s[1].party[0].status = Some(pr.sy.st.burn);
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert_eq!(s[1].party[0].yawn_count, 0, "状態異常");
    }

    #[test]
    fn グラススライダーはふうせんで先制にならない() {
        let mut p = pack();
        let s = sides(&mut p, &[&format!("ゴリランダー@ふうせん:いじっぱり:グラススライダー:32/32/0/0/0/0:グラスメイカー")],
                      &[&format!("ガブリアス@{N}:ようき:じしん:0/32/0/0/0/32:さめはだ")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        it::set_terrain(&mut f, 1, 5);
        let mut g = s[0].party[0].clone();
        let a = mv_of(pr, &g, "グラススライダー");
        assert_eq!(priority_base(pr, &a, &g, &f), 0);
        g.item = None;
        assert_eq!(priority_base(pr, &a, &g, &f), 1);
    }
}

/// 監査40（2026-10-04）の修正。test_all.py 39 と同じ局面
#[cfg(test)]
mod fix40_tests {
    use super::*;
    use crate::poke::build_poke;

    fn pack() -> Pack {
        Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"))
    }

    struct Z;
    impl BRng for Z {
        fn random(&mut self) -> f64 { 0.5 }
        fn choice(&mut self, _n: usize) -> usize { 0 }
        fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
        fn choices(&mut self) -> i64 { 2 }
    }

    const N: &str = "きれいなぬけがら";
    const DUM: &str = "カビゴン@きれいなぬけがら:わんぱく:のろい|ボディプレス:32/0/32/0/0/0:あついしぼう";

    fn sides(p: &mut Pack, a: &[&str], b: &[&str]) -> [Side; 2] {
        let pa: Vec<Poke> = a.iter().map(|s| build_poke(p, s, "M-6")).collect();
        let pb: Vec<Poke> = b.iter().map(|s| build_poke(p, s, "M-6")).collect();
        [Side { party: pa, active_idx: 0, field_idx: 0, ..Default::default() },
         Side { party: pb, active_idx: 0, field_idx: 1, ..Default::default() }]
    }

    fn mv_of(p: &Pack, poke: &Poke, n: &str) -> Action {
        let (i, m) = poke.moves.iter().enumerate().find(|(_, m)| p.intern.resolve(m.name) == n).unwrap();
        Action { kind: ActKind::Move, mv: Some(m.clone()), move_idx: i as i64, switch_to: -1, do_mega: false }
    }

    #[test]
    fn audit40_1_メガ進化の天候は5ターン() {
        let mut p = pack();
        let [a, b] = sides(&mut p, &["リザードン@リザードナイトY:ひかえめ:はねやすめ:0/0/0/32/0/32:もうか"], &[DUM]);
        let pr: &Pack = &p;
        let mut bt = Battle::new(a, b, Field::default());
        bt.mega_one(pr, 0);
        assert_eq!(bt.field.weather, Some(pr.sy.we.sunny));
        assert_eq!(bt.field.weather_count, 5);
    }

    #[test]
    fn audit40_7_ミラーアーマーはいかくを跳ね返す() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("ボーマンダ@{N}:いじっぱり:すてみタックル:0/32/0/0/0/32:いかく")],
                          &[&format!("アーマーガア@{N}:わんぱく:ボディプレス:32/0/32/0/0/0:ミラーアーマー")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        let mut opp = s[1].party[0].clone();
        entry_effects(pr, &mut s[0], 0, &mut f, &mut opp);
        assert_eq!(s[0].party[0].stage_attack, -1);
        assert_eq!(opp.stage_attack, 0);
    }

    #[test]
    fn audit40_11_ほろびのうたのカウントは4() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("ゲンガー@{N}:おくびょう:ほろびのうた:32/0/0/0/0/32:のろわれボディ")], &[DUM]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        let a = mv_of(pr, &s[0].party[0], "ほろびのうた");
        let mut d = 0;
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert_eq!((s[0].party[0].perish_count, s[1].party[0].perish_count), (4, 4));
    }

    #[test]
    fn audit40_8_とびひざげりはタイプ無効でも反動() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("エースバーン@{N}:ようき:とびひざげり:0/32/0/0/0/32:もうか")],
                          &[&format!("ゲンガー@{N}:おくびょう:のろい:32/0/0/0/0/32:のろわれボディ")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        let a = mv_of(pr, &s[0].party[0], "とびひざげり");
        let mut d = 0;
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        let e = &s[0].party[0];
        assert_eq!(e.max_hp - e.hp, e.max_hp / 2);
    }

    #[test]
    fn audit40_15_特性で無効の技は効かない() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("パーモット@{N}:ようき:でんこうそうげき:0/32/0/0/0/32:てつのこぶし")],
                          &[&format!("ライチュウ@{N}:おくびょう:わるだくみ:0/0/0/32/0/32:ひらいしん")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        let a = mv_of(pr, &s[0].party[0], "でんこうそうげき");
        let mut d = 0;
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert!(s[0].party[0].has_type(pr.tc.でんき), "タイプは残る");
        assert_eq!(s[1].party[0].stage_sp_attack, 1);
        let mut s = sides(&mut p, &[&format!("ゴリランダー@{N}:いじっぱり:10まんばりき:32/32/0/0/0/0:グラスメイカー")],
                          &["ウォッシュロトム@ゴツゴツメット:ずぶとい:おにび:32/0/32/0/0/0:ふゆう"]);
        let pr: &Pack = &p;
        let a = mv_of(pr, &s[0].party[0], "10まんばりき");
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert_eq!(s[0].party[0].hp, s[0].party[0].max_hp, "ゴツゴツメットは発動しない");
    }

    #[test]
    fn audit40_みがわりとミストフィールドは状態異常を防ぐ() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("ヒートロトム@{N}:ずぶとい:おにび|でんじは|ちょうはつ:32/0/32/0/0/0:ふゆう")],
                          &[&format!("ゲンガー@{N}:おくびょう:みがわり:32/0/0/0/0/32:のろわれボディ")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        s[1].party[0].substitute_hp = 40;
        let mut d = 0;
        for m in ["おにび", "でんじは"] {
            let a = mv_of(pr, &s[0].party[0], m);
            execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        }
        assert!(s[1].party[0].status.is_none());
        let a = mv_of(pr, &s[0].party[0], "ちょうはつ");
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert!(s[1].party[0].taunt_count > 0, "ちょうはつ は貫通");
        let mut s = sides(&mut p, &[&format!("ブラッキー@{N}:ずぶとい:でんじは|あやしいひかり:32/0/32/0/0/0:せいしんりょく")], &[DUM]);
        let pr: &Pack = &p;
        f.misty_terrain = true;
        f.misty_terrain_count = 5;
        for m in ["でんじは", "あやしいひかり"] {
            let a = mv_of(pr, &s[0].party[0], m);
            execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        }
        assert!(s[1].party[0].status.is_none() && !s[1].party[0].confused);
    }

    fn names(p: &Pack, c: &[Action]) -> Vec<String> {
        c.iter().map(|a| match &a.mv { Some(m) => p.intern.resolve(m.name).to_string(), None => "sw".to_string() }).collect()
    }

    fn cands(s: &Side) -> Vec<Action> {
        let me = s.active();
        let mut v: Vec<Action> = me.moves.iter().enumerate()
            .map(|(i, m)| Action { kind: ActKind::Move, mv: Some(m.clone()), move_idx: i as i64, switch_to: -1, do_mega: false })
            .collect();
        for (i, p) in s.party.iter().enumerate() {
            if i != s.active_idx && p.is_alive {
                v.push(Action { kind: ActKind::Switch, mv: None, move_idx: 0, switch_to: i as i64, do_mega: false });
            }
        }
        v
    }

    #[test]
    fn audit40_19_必ず失敗する手と効果の無い手を候補から外す() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("グソクムシャ@{N}:いじっぱり:であいがしら|アクアブレイク|じこさいせい|つるぎのまい:32/32/0/0/0/0:ききかいひ"), DUM],
                          &[DUM]);
        let pr: &Pack = &p;
        let f = Field::default();
        s[0].party[0].turns_out = 1;
        s[0].party[0].stage_attack = 6;
        let c = crate::search::prune_futile_moves(pr, &s[0], &s[1], &f, cands(&s[0]));
        assert_eq!(names(pr, &c), vec!["アクアブレイク", "sw"]);
        let mut s = sides(&mut p, &[&format!("カバルドン@{N}:わんぱく:ほえる|あくび|じしん|でんじは:32/0/32/0/0/0:すなおこし")], &[DUM]);
        let pr: &Pack = &p;
        s[1].party[0].status = Some(pr.sy.st.paralysis);
        let c = crate::search::prune_futile_moves(pr, &s[0], &s[1], &f, cands(&s[0]));
        assert_eq!(names(pr, &c), vec!["じしん"]);
        let mut s = sides(&mut p, &[&format!("カバルドン@{N}:わんぱく:じしん|がんせきふうじ:32/0/32/0/0/0:すなおこし")],
                          &["サーフゴー@ふうせん:ひかえめ:シャドーボール:0/0/0/32/0/32:おうごんのからだ"]);
        let pr: &Pack = &p;
        let g = s[1].party[0].clone();
        s[0].opp_view.on_enter(pr, &g);
        let c = crate::search::prune_futile_moves(pr, &s[0], &s[1], &f, cands(&s[0]));
        assert_eq!(names(pr, &c), vec!["がんせきふうじ"]);
        let mut s = sides(&mut p, &[&format!("アシレーヌ@{N}:ひかえめ:ムーンフォース|アンコール|めいそう|うたかたのアリア:32/0/0/32/0/0:げきりゅう")], &[DUM]);
        let pr: &Pack = &p;
        s[1].party[0].last_used_move = Some(pr.sy.l.のろい);
        s[0].party[0].taunt_count = 2;
        let c = crate::search::prune_futile_moves(pr, &s[0], &s[1], &f, cands(&s[0]));
        assert_eq!(names(pr, &c), vec!["ムーンフォース", "うたかたのアリア"], "ちょうはつ中の変化技");
        s[0].party[0].taunt_count = 0;
        s[0].party[0].throat_chop_count = 2;
        let c = crate::search::prune_futile_moves(pr, &s[0], &s[1], &f, cands(&s[0]));
        assert_eq!(names(pr, &c), vec!["ムーンフォース", "アンコール", "めいそう"], "じごくづき中の音技");
    }

    #[test]
    fn audit40_3_確定KOは命中の高い技で上書き() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("ライチュウ@{N}:ひかえめ:10まんボルト|でんじほう|わるだくみ:0/0/0/32/0/32:ひらいしん")],
                          &[&format!("ギャラドス@{N}:ようき:たきのぼり:0/32/0/0/0/32:いかく")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        s[1].party[0].hp = 30;
        let st = mv_of(pr, &s[0].party[0], "わるだくみ");
        let [mut a, mut b] = s;
        let r = crate::ai::certain_ko_override_opt(pr, st.clone(), &mut a, &mut b, &mut f, &mut Z, true, true, true);
        assert_eq!(pr.intern.resolve(r.mv.unwrap().name), "10まんボルト");
        a.party[0].moves.remove(0);
        a.party[0].pp.remove(0);
        let st = mv_of(pr, &a.party[0], "わるだくみ");
        let r = crate::ai::certain_ko_override_opt(pr, st.clone(), &mut a, &mut b, &mut f, &mut Z, true, true, true);
        assert_eq!(pr.intern.resolve(r.mv.unwrap().name), "わるだくみ", "命中50の技では上書きしない");
    }

    #[test]
    fn audit40_ねむりカウンタの決定化() {
        let mut p = pack();
        let s = sides(&mut p, &[DUM], &[DUM]);
        let pr: &Pack = &p;
        let mut q = s[0].party[0].clone();
        q.status = Some(pr.sy.st.sleep);
        q.sleep_acts = 2;
        q.sleep_count = 1;
        let mut r = crate::cpyrng::CpyRandom::new(5);
        let mut seen = std::collections::BTreeSet::new();
        for _ in 0..60 {
            crate::search::resample_sleep(pr, &mut q, &mut r);
            seen.insert(q.sleep_count);
        }
        assert_eq!(seen.into_iter().collect::<Vec<_>>(), vec![1, 2]);
        q.sleep_rest = true;
        q.sleep_acts = 1;
        crate::search::resample_sleep(pr, &mut q, &mut r);
        assert_eq!(q.sleep_count, 2);
    }

    #[test]
    fn audit40_13_おうごんのからだはいたみわけを防ぐ() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("ウォッシュロトム@{N}:ずぶとい:いたみわけ:32/0/32/0/0/0:ふゆう")],
                          &[&format!("サーフゴー@{N}:ひかえめ:シャドーボール:0/0/0/32/0/32:おうごんのからだ")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        s[0].party[0].hp = 10;
        let a = mv_of(pr, &s[0].party[0], "いたみわけ");
        let mut d = 0;
        execute_move(pr, &mut s, &mut f, 0, &a, None, &mut Z, &mut d);
        assert_eq!(s[0].party[0].hp, 10);
        assert_eq!(s[1].party[0].hp, s[1].party[0].max_hp);
    }
}

/// 監査200（2026-10-04）の修正。test_all.py 40 と同じ局面
#[cfg(test)]
mod fix200_tests {
    use super::*;
    use crate::poke::build_poke;

    fn pack() -> Pack {
        Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"))
    }

    struct Z;
    impl BRng for Z {
        fn random(&mut self) -> f64 { 0.5 }
        fn choice(&mut self, _n: usize) -> usize { 0 }
        fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
        fn choices(&mut self) -> i64 { 2 }
    }

    const N: &str = "メトロノーム";
    const DUM: &str = "カビゴン@メトロノーム:わんぱく:のろい|まもる:32/0/32/0/0/0:あついしぼう";
    const BLK: &str = "ブラッキー@メトロノーム:ずぶとい:ねがいごと|のろい:32/0/32/0/0/0:せいしんりょく";

    fn sides(p: &mut Pack, a: &[&str], b: &[&str]) -> [Side; 2] {
        let pa: Vec<Poke> = a.iter().map(|s| build_poke(p, s, "M-6")).collect();
        let pb: Vec<Poke> = b.iter().map(|s| build_poke(p, s, "M-6")).collect();
        [Side { party: pa, active_idx: 0, field_idx: 0, ..Default::default() },
         Side { party: pb, active_idx: 0, field_idx: 1, ..Default::default() }]
    }

    fn mv_of(p: &Pack, poke: &Poke, n: &str) -> Action {
        let (i, m) = poke.moves.iter().enumerate().find(|(_, m)| p.intern.resolve(m.name) == n).unwrap();
        Action { kind: ActKind::Move, mv: Some(m.clone()), move_idx: i as i64, switch_to: -1, do_mega: false }
    }

    fn run(pr: &Pack, s: &mut [Side; 2], f: &mut Field, who: usize, n: &str) {
        let a = mv_of(pr, &s[who].party[s[who].active_idx], n);
        let mut d = 0;
        execute_move(pr, s, f, who, &a, None, &mut Z, &mut d);
    }

    #[test]
    fn r4mcts_メガ前でもメガソーラーのウェザーボールはほのお() {
        let mut p = pack();
        let me = build_poke(&mut p, "メガニウム@メガニウムナイト:おくびょう:ソーラービーム|ウェザーボール|げんしのちから|くさわけ:2/0/0/32/0/32:しんりょく", "M-6");
        let mv = me.moves.iter().find(|m| p.intern.resolve(m.name) == "ウェザーボール").unwrap().clone();
        let f = Field::default();
        let t = crate::damage::effective_move_type_ab(&p, &me, p.sy.ab.メガソーラー, &mv, &f);
        assert_eq!(t, p.tc.ほのお);
        assert_eq!(crate::damage::effective_move_type_ab(&p, &me, me.ability, &mv, &f), p.tc.ノーマル);
    }

    #[test]
    fn audit200_1_まもるは必中技より先() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("ルカリオ@{N}:おくびょう:はどうだん:0/0/0/32/0/32:せいしんりょく")],
                          &[&format!("ガブリアス@{N}:わんぱく:まもる:32/0/32/0/0/0:さめはだ")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        s[1].party[0].protecting = true;
        run(pr, &mut s, &mut f, 0, "はどうだん");
        assert_eq!(s[1].party[0].hp, s[1].party[0].max_hp);
    }

    #[test]
    fn audit200_3_5_7_ステロの撒き直し_跳ね返し_おいかぜ() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("カバルドン@{N}:わんぱく:ステルスロック|まきびし:32/0/32/0/0/0:すなおこし")],
                          &[&format!("エーフィ@{N}:ずぶとい:おいかぜ:32/0/32/0/0/0:マジックミラー")]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        run(pr, &mut s, &mut f, 0, "ステルスロック");
        run(pr, &mut s, &mut f, 0, "まきびし");
        assert_eq!((f.stealth_rock, f.spikes), ([true, false], [1, 0]));
        s[1].party[0].ability = pr.sy.l.せいしんりょく;
        s[1].stealth_rock_set = true;
        run(pr, &mut s, &mut f, 0, "ステルスロック");
        assert!(s[1].sr_pending);
        run(pr, &mut s, &mut f, 1, "おいかぜ");
        assert_eq!(s[1].tailwind_count, 4);
    }

    #[test]
    fn audit200_4_いたずらごころは自分対象の変化技をあくにも使える() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("エルフーン@{N}:おくびょう:みがわり|でんじは:0/0/0/32/0/32:いたずらごころ")], &[BLK]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        run(pr, &mut s, &mut f, 0, "みがわり");
        run(pr, &mut s, &mut f, 0, "でんじは");
        assert!(s[0].party[0].substitute_hp > 0);
        assert!(s[1].party[0].status.is_none());
    }

    #[test]
    fn audit200_6_8_9_12_23_交代で消える状態としっぽきり() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("ミミズズ@{N}:わんぱく:しっぽきり|でんじふゆう:32/0/32/0/0/0:どしょく"), BLK], &[DUM]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        run(pr, &mut s, &mut f, 0, "でんじふゆう");
        assert_eq!((s[0].party[0].magnet_rise, s[0].party[0].levitate_turns), (true, 5));
        {
            let m = &mut s[0].party[0];
            m.bad_poison_count = 3;
            m.trapped = true;
            m.last_used_move = Some(pr.sy.l.のろい);
        }
        run(pr, &mut s, &mut f, 0, "しっぽきり");
        let sub = s[0].party[0].max_hp / 4;
        s[0].switch_to(pr, 1);
        let m = &s[0].party[0];
        assert_eq!((m.bad_poison_count, m.trapped, m.last_used_move, m.magnet_rise), (0, false, None, false));
        assert_eq!(s[0].party[1].substitute_hp, sub);
    }

    #[test]
    fn audit200_8_ゴーストときれいなぬけがらは交代できる() {
        let mut p = pack();
        let s = sides(&mut p, &[&format!("ゲンガー@{N}:おくびょう:のろい:0/0/0/32/0/32:のろわれボディ"),
                                "カビゴン@きれいなぬけがら:わんぱく:のろい:32/0/32/0/0/0:あついしぼう", DUM], &[DUM]);
        let pr: &Pack = &p;
        let mut ps = s[0].party.clone();
        for q in ps.iter_mut() {
            q.trapped = true;
            q.bound_count = 3;
        }
        let r: Vec<bool> = ps.iter().map(|q| crate::ai::is_trapped(pr, q, None)).collect();
        assert_eq!(r, vec![false, false, true]);
    }

    #[test]
    fn audit200_みがわりは追加効果と接触の反応を防ぐ() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("ドドゲザン@{N}:いじっぱり:はたきおとす:32/32/0/0/0/0:まけんき")],
                          &["ガブリアス@ゴツゴツメット:わんぱく:のろい:32/0/32/0/0/0:さめはだ", BLK]);
        let pr: &Pack = &p;
        let mut f = Field::default();
        s[1].party[0].substitute_hp = 200;
        run(pr, &mut s, &mut f, 0, "はたきおとす");
        assert_eq!(s[1].party[0].item, Some(pr.sy.it.ゴツゴツメット));
        assert_eq!(s[0].party[0].hp, s[0].party[0].max_hp);
        assert!(s[1].party[0].substitute_hp < 200);
    }

    #[test]
    fn audit200_16_うらみつらみは追加効果() {
        let p = pack();
        assert!(p.flags(p.sy.l.うらみつらみ).secondary);
        assert_eq!(def_downs(&p, p.sy.l.うらみつらみ), Some((0, -1, 1.0)));
    }

    #[test]
    fn audit200_2_種名にコロンを含む型() {
        let s = crate::poke::parse_pokemon_spec("ケンタロス:炎@こだわりスカーフ:いじっぱり:レイジングブル|インファイト:0/32/0/0/0/32:いかく");
        assert_eq!(s.name, "ケンタロス:炎");
        assert_eq!(s.item.as_deref(), Some("こだわりスカーフ"));
        assert_eq!(s.evs.map(|e| (e.a, e.s)), Some((32, 32)));
        assert_eq!(s.ability.as_deref(), Some("いかく"));
        assert!(crate::poke::parse_spec_checked("ガブリアス:ようき:じしん:32/x").is_err());
    }

    #[test]
    fn audit200_28_連続のみちづれを候補から外す() {
        let mut p = pack();
        let mut s = sides(&mut p, &[&format!("ジュペッタ@{N}:ゆうかん:みちづれ|かげうち:32/32/0/0/0/0:おみとおし")], &[DUM]);
        let pr: &Pack = &p;
        let f = Field::default();
        s[0].party[0].destiny_bond_last_turn = true;
        let c: Vec<Action> = (0..2).map(|i| mv_of(pr, &s[0].party[0], ["みちづれ", "かげうち"][i])).collect();
        let r = crate::search::prune_futile_moves_opt(pr, &s[0], &s[1], &f, c.clone(), true);
        assert_eq!(r.len(), 1);
        assert_eq!(crate::search::prune_futile_moves_opt(pr, &s[0], &s[1], &f, c, false).len(), 2);
    }
}

#[cfg(test)]
mod hazard_tests {
    use super::*;
    use crate::poke::build_poke;

    fn pack() -> Pack {
        Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"))
    }

    const FOR: &str = "フォレトス@メトロノーム:わんぱく:ステルスロック|まきびし|どくびし|ボディプレス:32/0/32/0/0/0:がんじょう";
    const DEN: &str = "オニシズクモ@メトロノーム:わんぱく:ねばねばネット|アクアブレイク:32/0/32/0/0/0:すいほう";
    const DUM: &str = "カビゴン@メトロノーム:わんぱく:のろい|まもる:32/0/32/0/0/0:あついしぼう";

    fn left(p: &mut Pack, me: &str, f: &Field) -> Vec<String> {
        let s = [Side { party: vec![build_poke(p, me, "M-6")], active_idx: 0, field_idx: 0, ..Default::default() },
                 Side { party: vec![build_poke(p, DUM, "M-6"), build_poke(p, DUM, "M-6")], active_idx: 0, field_idx: 1, ..Default::default() }];
        let pr: &Pack = p;
        let c: Vec<Action> = s[0].party[0].moves.iter().enumerate()
            .map(|(i, m)| Action { kind: ActKind::Move, mv: Some(m.clone()), move_idx: i as i64, switch_to: -1, do_mega: false })
            .collect();
        crate::search::prune_futile_moves(pr, &s[0], &s[1], f, c).iter()
            .map(|a| pr.intern.resolve(a.mv.as_ref().unwrap().name).to_string()).collect()
    }

    #[test]
    fn hazard1004_設置済みのステロと上限の設置技を候補から外す() {
        let mut p = pack();
        let mut f = Field::default();
        assert_eq!(left(&mut p, FOR, &f), ["ステルスロック", "まきびし", "どくびし", "ボディプレス"]);
        f.stealth_rock[0] = true;
        f.spikes[0] = 3;
        f.toxic_spikes[0] = 2;
        assert_eq!(left(&mut p, FOR, &f), ["ステルスロック", "まきびし", "どくびし", "ボディプレス"]);
        f.stealth_rock[1] = true;
        f.spikes[1] = 2;
        f.toxic_spikes[1] = 1;
        assert_eq!(left(&mut p, FOR, &f), ["まきびし", "どくびし", "ボディプレス"]);
        f.spikes[1] = 3;
        f.toxic_spikes[1] = 2;
        assert_eq!(left(&mut p, FOR, &f), ["ボディプレス"]);
        assert_eq!(left(&mut p, DEN, &f), ["ねばねばネット", "アクアブレイク"]);
        f.sticky_web[1] = true;
        assert_eq!(left(&mut p, DEN, &f), ["アクアブレイク"]);
    }

    #[test]
    fn retrain1005_除去されたステロは撒き直しの候補に戻る() {
        let mut p = pack();
        let mut s = [Side { party: vec![build_poke(&mut p, FOR, "M-6")], active_idx: 0, field_idx: 0, ..Default::default() },
                     Side { party: vec![build_poke(&mut p, DUM, "M-6"), build_poke(&mut p, DUM, "M-6")], active_idx: 0, field_idx: 1, ..Default::default() }];
        let pr: &Pack = &p;
        let mut f = Field::default();
        s[1].stealth_rock_set = true;
        let has = |s: &[Side; 2], f: &Field| crate::search::candidate_actions(pr, &s[0], &s[1], f, true).iter()
            .any(|a| a.mv.as_ref().map_or(false, |m| pr.intern.resolve(m.name) == "ステルスロック"));
        assert!(crate::ai::hazard_value(pr, pr.sy.l.ステルスロック, &crate::ai::HazCtx::of(&s[1]), &f) > 0.0);
        assert!(has(&s, &f));
        f.stealth_rock[1] = true;
        assert_eq!(crate::ai::hazard_value(pr, pr.sy.l.ステルスロック, &crate::ai::HazCtx::of(&s[1]), &f), 0.0);
        assert!(!has(&s, &f));
    }
}

/// 選出率の低い4種の監査（audit4_1008）の修正。test_all.py 43 と同じ局面
#[cfg(test)]
mod audit4_tests {
    use super::*;
    use crate::poke::build_poke;
    use crate::cpyrng::CpyRandom;

    fn pack() -> Pack {
        Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"))
    }

    struct Z;
    impl BRng for Z {
        fn random(&mut self) -> f64 { 0.5 }
        fn choice(&mut self, _n: usize) -> usize { 0 }
        fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
        fn choices(&mut self) -> i64 { 2 }
    }

    /// random() の呼び出し回数を数える（値は 0.5＝命中・急所なし・続く）
    struct Cnt(usize);
    impl BRng for Cnt {
        fn random(&mut self) -> f64 {
            self.0 += 1;
            0.5
        }
        fn choice(&mut self, _n: usize) -> usize { 0 }
        fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
        fn choices(&mut self) -> i64 { 2 }
    }

    const N: &str = "メトロノーム";
    const DUM: &str = "カビゴン@メトロノーム:わんぱく:のろい|まもる:32/0/32/0/0/0:あついしぼう";

    fn ju(item: &str, mv: &str) -> String {
        format!("ジュカイン@{item}:ようき:{mv}:0/32/0/0/0/32:かるわざ")
    }

    fn sides(p: &mut Pack, a: &[&str], b: &[&str]) -> [Side; 2] {
        let pa: Vec<Poke> = a.iter().map(|s| build_poke(p, s, "M-6")).collect();
        let pb: Vec<Poke> = b.iter().map(|s| build_poke(p, s, "M-6")).collect();
        [Side { party: pa, active_idx: 0, field_idx: 0, ..Default::default() },
         Side { party: pb, active_idx: 0, field_idx: 1, ..Default::default() }]
    }

    fn act(p: &Pack, poke: &Poke, n: &str) -> Action {
        let (i, m) = poke.moves.iter().enumerate().find(|(_, m)| p.intern.resolve(m.name) == n).unwrap();
        Action { kind: ActKind::Move, mv: Some(m.clone()), move_idx: i as i64, switch_to: -1, do_mega: false }
    }

    fn run(pr: &Pack, s: &mut [Side; 2], who: usize, n: &str, rng: &mut dyn BRng) {
        let a = act(pr, &s[who].party[0], n);
        let mut d = 0;
        let mut f = Field::default();
        execute_move(pr, s, &mut f, who, &a, None, rng, &mut d);
    }

    #[test]
    fn audit4_e1_かるわざは持ち物を失う全経路で発動() {
        let mut p = pack();
        let cases: Vec<(&str, String, String, usize, &str, bool)> = vec![
            ("はたきおとされ", ju("オボンのみ", "つるぎのまい"), format!("ゴリランダー@{N}:わんぱく:はたきおとす:32/0/32/0/0/0:グラスメイカー"), 1, "はたきおとす", false),
            ("ついばむ", ju("オボンのみ", "つるぎのまい"), format!("ムクホーク@{N}:わんぱく:ついばむ:32/0/32/0/0/0:いかく"), 1, "ついばむ", false),
            ("どろぼう", ju("オボンのみ", "つるぎのまい"), format!("ムクホーク@{N}:わんぱく:どろぼう:32/0/32/0/0/0:いかく"), 1, "どろぼう", true),
            ("マジシャン", ju("オボンのみ", "つるぎのまい"), format!("マフォクシー@{N}:ずぶとい:マジカルフレイム:32/0/32/0/0/0:マジシャン"), 1, "マジカルフレイム", true),
            ("わるいてぐせ", ju("オボンのみ", "リーフブレード"), format!("マニューラ@{N}:わんぱく:のろい:32/0/32/0/32/0:わるいてぐせ"), 0, "リーフブレード", true),
            ("トリック", ju("たべのこし", "トリック"), DUM.to_string(), 0, "トリック", true),
            ("なげつける", ju("くろいてっきゅう", "なげつける"), DUM.to_string(), 0, "なげつける", false),
            ("ほおばる", ju("オボンのみ", "ほおばる"), DUM.to_string(), 0, "ほおばる", false),
            ("じゃくてんほけん", "ジュカイン@じゃくてんほけん:ずぶとい:つるぎのまい:32/0/32/0/32/0:かるわざ".to_string(),
             format!("ウインディ@{N}:ずぶとい:かえんほうしゃ:0/0/32/0/0/0:せいぎのこころ"), 1, "かえんほうしゃ", false),
        ];
        for (k, a, b, who, mv, noitem) in cases {
            let mut s = sides(&mut p, &[&a], &[&b]);
            if noitem {
                s[1].party[0].item = None;
            }
            run(&p, &mut s, who, mv, &mut Z);
            let j = &s[0].party[0];
            assert!(j.item.is_none() && j.stage_speed == 2, "{k}: item={:?} S={}", j.item, j.stage_speed);
        }
        let mut q = pack();
        let mut j = build_poke(&mut q, &ju("しろいハーブ", "つるぎのまい"), "M-6");
        j.stage_defense = -1;
        it::try_white_herb(&q, &mut j);
        assert_eq!((j.item, j.stage_speed), (None, 2), "しろいハーブ");
        let mut j = build_poke(&mut q, &ju("メンタルハーブ", "つるぎのまい"), "M-6");
        j.taunt_count = 3;
        it::try_mental_herb(&q, &mut j);
        assert_eq!((j.item, j.stage_speed), (None, 2), "メンタルハーブ");
        let mut j = build_poke(&mut q, &ju("ヒメリのみ", "つるぎのまい"), "M-6");
        j.pp[0] = 0;
        it::try_leppa_berry(&q, &mut j);
        assert_eq!((j.item, j.stage_speed), (None, 2), "ヒメリのみ");
        let mut j = build_poke(&mut q, &ju("ラムのみ", "つるぎのまい"), "M-6");
        j.status = Some(q.sy.st.poison);
        it::try_cure_berry(&q, &mut j);
        assert_eq!((j.item, j.stage_speed), (None, 2), "ラムのみ");
        let mut j = build_poke(&mut q, &ju("サルのみ", "つるぎのまい"), "M-6");
        j.hp = j.max_hp / 4;
        it::apply_hp_berry(&q, &mut j);
        assert_eq!((j.item, j.stage_speed), (None, 2), "サルのみ");
        let mut j = build_poke(&mut q, &ju("オボンのみ", "つるぎのまい"), "M-6");
        it::try_cure_berry(&q, &mut j);
        assert_eq!(j.stage_speed, 0, "持ち物が残れば変わらない");
    }

    #[test]
    fn audit4_e2_トリプルアクセルは1発ごとに命中判定と急所() {
        let mut p = pack();
        let a = build_poke(&mut p, &format!("マスカーニャ@{N}:いじっぱり:トリプルアクセル:32/32/0/0/0/0:しんりょく"), "M-6");
        let sl = build_poke(&mut p, &format!("マスカーニャ@{N}:いじっぱり:トリプルアクセル:32/32/0/0/0/0:スキルリンク"), "M-6");
        let mv = a.moves[0].clone();
        let mut r = CpyRandom::new(43);
        let mut c = [0usize; 4];
        for _ in 0..20000 {
            c[calc_hits(&p, &mv, &a, &mut r) as usize] += 1;
        }
        let fr: Vec<f64> = c.iter().map(|&x| x as f64 / 20000.0).collect();
        assert!((fr[1] - 0.10).abs() < 0.012 && (fr[2] - 0.09).abs() < 0.012 && (fr[3] - 0.81).abs() < 0.015, "{fr:?}");
        assert!((0..200).all(|_| calc_hits(&p, &mv, &sl, &mut r) == 3), "スキルリンク");
        // 3回当たる乱数で random() の回数: トリプルアクセルは急所が3回、ダブルウイングは1回
        let mut n = Vec::new();
        for spec in [format!("マスカーニャ@{N}:いじっぱり:トリプルアクセル:32/32/0/0/0/0:しんりょく"),
                     format!("マスカーニャ@{N}:いじっぱり:ダブルウイング:32/32/0/0/0/0:しんりょく")] {
            let mut s = sides(&mut p, &[&spec], &[DUM]);
            let mut g = Cnt(0);
            let m = p.intern.resolve(s[0].party[0].moves[0].name).to_string();
            run(&p, &mut s, 0, &m, &mut g);
            n.push(g.0);
        }
        assert_eq!(n[0], n[1] + 2 + 2, "トリプルアクセル: 続くかの判定2回＋2・3発目の急所2回 {n:?}");
    }

    #[test]
    fn audit4_e3_ほうしはくさ_ぼうじん_ゴーグルに発動しない() {
        let mut p = pack();
        let rf = build_poke(&mut p, &format!("ラフレシア@{N}:ずぶとい:じこさいせい:32/0/32/0/0/0:ほうし"), "M-6");
        let mut f = Field::default();
        let specs = [
            (format!("ゴリランダー@{N}:いじっぱり:グラススライダー:32/32/0/0/0/0:グラスメイカー"), true),
            (format!("フォレトス@{N}:いじっぱり:ジャイロボール:32/32/0/0/0/0:ぼうじん"), true),
            ("カイリキー@ぼうじんゴーグル:いじっぱり:かみくだく:32/32/0/0/0/0:ノーガード".to_string(), true),
            (format!("カイリキー@{N}:いじっぱり:かみくだく:32/32/0/0/0/0:ノーガード"), false),
        ];
        for (sp, immune) in specs.iter() {
            let base = build_poke(&mut p, sp, "M-6");
            let mv = base.moves[0].clone();
            let mut r = CpyRandom::new(8);
            let mut c = [0usize; 3];
            let nn = 20000;
            for _ in 0..nn {
                let mut at = base.clone();
                let mut df = rf.clone();
                crate::abilities::on_after_hit(&p, &mut at, &mut df, &mv, &mut f, &mut r);
                match at.status {
                    Some(x) if x == p.sy.st.sleep => c[0] += 1,
                    Some(x) if x == p.sy.st.paralysis => c[1] += 1,
                    Some(x) if x == p.sy.st.poison => c[2] += 1,
                    _ => {}
                }
            }
            if *immune {
                assert_eq!(c, [0, 0, 0], "{sp}");
            } else {
                let fr: Vec<f64> = c.iter().map(|&x| x as f64 / nn as f64).collect();
                assert!((fr[0] - 0.11).abs() < 0.008 && (fr[1] - 0.10).abs() < 0.008 && (fr[2] - 0.09).abs() < 0.008, "{fr:?}");
            }
        }
    }
}
