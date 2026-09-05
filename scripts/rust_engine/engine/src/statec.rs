//! 正準状態シリアライズ（_rust_engine/state_codec.py と 1:1）。
use crate::battle::{Battle, Side};
use crate::damage::Field;
use crate::oppview::OppView;
use crate::pack::{Pack, Ty, NO_TY};
use crate::poke::Poke;

#[derive(Clone, Debug, PartialEq)]
pub enum SV {
    N,
    I(i64),
    F(f64),
    S(String),
    B(bool),
}

pub struct Enc<'a> {
    pub pack: &'a Pack,
    pub vals: Vec<SV>,
    pub names: Option<Vec<String>>,
    pfx: String,
}

impl<'a> Enc<'a> {
    pub fn new(pack: &'a Pack, with_names: bool) -> Self {
        Enc {
            pack,
            vals: Vec::with_capacity(1400),
            names: if with_names { Some(Vec::with_capacity(1400)) } else { None },
            pfx: String::new(),
        }
    }
    #[inline]
    fn a(&mut self, n: &str, v: SV) {
        if let Some(ns) = &mut self.names {
            ns.push(format!("{}{}", self.pfx, n));
        }
        self.vals.push(v);
    }
    #[inline]
    fn i(&mut self, n: &str, v: i64) {
        self.a(n, SV::I(v))
    }
    #[inline]
    fn b(&mut self, n: &str, v: bool) {
        self.a(n, SV::B(v))
    }
    #[inline]
    fn sym(&mut self, n: &str, v: Option<u16>) {
        match v {
            None => self.a(n, SV::N),
            Some(s) => {
                let t = self.pack.intern.resolve(s).to_string();
                self.a(n, SV::S(t))
            }
        }
    }
    #[inline]
    fn ty(&mut self, n: &str, v: Ty) {
        if v == NO_TY {
            self.a(n, SV::N)
        } else {
            let t = self.pack.types[v as usize].clone();
            self.a(n, SV::S(t))
        }
    }
    #[inline]
    fn tyo(&mut self, n: &str, v: Option<Ty>) {
        match v {
            None => self.a(n, SV::N),
            Some(t) => self.ty(n, t),
        }
    }
}

const STAGE_NAMES: [&str; 7] = [
    "stage_attack",
    "stage_defense",
    "stage_sp_attack",
    "stage_sp_defense",
    "stage_speed",
    "stage_accuracy",
    "stage_evasion",
];

pub fn poke_fields(e: &mut Enc, p: &Poke, pfx: &str) {
    e.pfx = pfx.to_string();
    e.sym("name", Some(p.name));
    e.i("dex", p.dex);
    e.ty("type1", p.type1);
    e.tyo("type2", p.type2);
    e.ty("base_type1", p.base_type1);
    e.tyo("base_type2", p.base_type2);
    e.i("max_hp", p.max_hp);
    e.i("hp", p.hp);
    e.i("attack", p.attack);
    e.i("defense", p.defense);
    e.i("sp_attack", p.sp_attack);
    e.i("sp_defense", p.sp_defense);
    e.i("speed", p.speed);
    e.sym("item", p.item);
    e.sym("ability", Some(p.ability));
    e.sym("nature", Some(p.nature));
    for (k, key) in ["H", "A", "B", "C", "D", "S"].iter().enumerate() {
        e.i(&format!("ev_{}", key), p.evs[k]);
    }
    e.a("weight_kg", SV::F(p.weight_kg));
    for i in 0..4usize {
        match p.moves.get(i) {
            Some(m) => e.sym(&format!("move{}", i), Some(m.name)),
            None => e.a(&format!("move{}", i), SV::N),
        }
        match p.pp.get(i) {
            Some(&v) => e.i(&format!("pp{}", i), v),
            None => e.a(&format!("pp{}", i), SV::N),
        }
    }
    e.i("n_moves", p.moves.len() as i64);
    for (i, nm) in STAGE_NAMES.iter().enumerate() {
        e.i(nm, p.stage(i as u8) as i64);
    }
    e.sym("status", p.status);
    e.i("bad_poison_count", p.bad_poison_count);
    e.i("sleep_count", p.sleep_count);
    e.b("confused", p.confused);
    e.b("flinched", p.flinched);
    e.b("is_alive", p.is_alive);
    e.b("mega_evolved", p.mega_evolved);
    e.b("has_mega_data", p.mega.is_some());
    e.b("hero_forme", p.hero_forme);
    e.b("protecting", p.protecting);
    e.i("protect_consecutive", p.protect_consecutive);
    e.b("enduring", p.enduring);
    e.b("ate_berry", p.ate_berry);
    {
        let mut ms: Vec<&str> = p.used_moves.iter().map(|&s| e.pack.intern.resolve(s)).collect();
        ms.sort_unstable();
        let joined = ms.join("|");
        e.a("used_moves", SV::S(joined));
    }
    e.b("grounded", p.grounded);
    e.i("syrup_count", p.syrup_count);
    e.i("heal_block_count", p.heal_block_count);
    e.b("deka_last", p.deka_last);
    e.sym("locked_move", p.locked_move);
    e.sym("choice_locked_move", p.choice_locked_move);
    e.sym("disabled_move", p.disabled_move);
    e.i("disabled_turns", p.disabled_turns);
    e.i("lock_count", p.lock_count);
    e.b("recharge", p.recharge);
    e.sym("charging_move", p.charging_move);
    e.b("seeded", p.seeded);
    e.i("yawn_count", p.yawn_count);
    e.i("encore_count", p.encore_count);
    e.i("taunt_count", p.taunt_count);
    e.i("bound_count", p.bound_count);
    e.i("throat_chop_count", p.throat_chop_count);
    e.i("stockpile_count", p.stockpile_count);
    e.b("infatuation", p.infatuation);
    e.b("torment", p.torment);
    e.b("trapped", p.trapped);
    e.i("times_hit", p.times_hit);
    e.b("ability_suppressed", p.ability_suppressed);
    e.b("rooted", p.rooted);
    e.b("aqua_ring", p.aqua_ring);
    e.b("magnet_rise", p.magnet_rise);
    e.b("lock_on", p.lock_on);
    e.b("move_failed_last", p.move_failed_last);
    e.b("minimized", p.minimized);
    e.sym("last_used_move", p.last_used_move);
    e.i("turns_out", p.turns_out);
    e.i("fainted_allies", p.fainted_allies);
    e.i("perish_count", p.perish_count);
    e.b("destiny_bond", p.destiny_bond);
    e.b("cursed", p.cursed);
    e.b("charged", p.charged);
    e.i("crit_stage", p.crit_stage);
    // 動的
    e.b("acts_second", p.acts_second);
    e.b("barrier_done", p.barrier_done);
    e.b("has_baton", p.baton_stages.is_some());
    for (i, nm) in STAGE_NAMES.iter().enumerate() {
        let v = p.baton_stages.map(|b| b[i]).unwrap_or(0);
        e.i(&format!("baton_{}", nm), v as i64);
    }
    e.b("beak_primed", p.beak_primed);
    e.b("destiny_bond_last_turn", p.destiny_bond_last_turn);
    e.b("disguise_broken", p.disguise_broken);
    e.b("electrified", p.electrified);
    e.b("electromorphosis_charged", p.electromorphosis_charged);
    e.b("flash_fire_active", p.flash_fire_active);
    e.b("force_switch", p.force_switch);
    e.b("gyaku_triggered", p.gyaku_triggered);
    e.b("hangry", p.hangry);
    e.b("honey_used", p.honey_used);
    e.sym("illusion_name", p.illusion_name);
    e.b("in_blade_forme", p.in_blade_forme);
    e.b("info_done", p.info_done);
    e.sym("last_berry", p.last_berry);
    e.sym("last_consumed_item", p.last_consumed_item);
    e.sym("last_flung_item", p.last_flung_item);
    e.sym("last_item", p.last_item);
    e.sym("last_move_obj", p.last_move_obj.as_ref().map(|m| m.name));
    e.i("last_physical_dmg_received", p.last_physical_dmg_received);
    e.i("last_special_dmg_received", p.last_special_dmg_received);
    e.i("levitate_turns", p.levitate_turns);
    e.b("move_failed_this_turn", p.move_failed_this_turn);
    e.i("multi_hit_index", p.multi_hit_index);
    e.b("pierce_quarter", p.pierce_quarter);
    e.b("pivot_out", p.pivot_out);
    e.b("protean_used", p.protean_used);
    e.sym("protect_move", p.protect_move);
    match p.roost_types {
        None => {
            e.a("roost_t1", SV::N);
            e.a("roost_t2", SV::N);
        }
        Some((t1, t2)) => {
            e.ty("roost_t1", t1);
            e.tyo("roost_t2", t2);
        }
    }
    e.b("has_roost", p.roost_types.is_some());
    e.sym("ruminate_berry", p.ruminate_berry);
    e.i("ruminate_count", p.ruminate_count);
    e.b("salted", p.salted);
    e.b("sealed", p.sealed);
    e.i("shield_atk", p.shield_atk);
    e.i("shield_def", p.shield_def);
    e.i("shield_spatk", p.shield_spatk);
    e.i("shield_spdef", p.shield_spdef);
    e.i("substitute_hp", p.substitute_hp);
    e.b("switched_this_turn", p.switched_this_turn);
    e.b("took_damage_this_turn", p.took_damage_this_turn);
    e.b("transformed", p.transformed);
    e.b("has_transform_backup", p.transform_backup.is_some());
    let tb = p.transform_backup.as_deref();
    e.i("tb_attack", tb.map(|t| t.attack).unwrap_or(0));
    e.i("tb_defense", tb.map(|t| t.defense).unwrap_or(0));
    e.i("tb_sp_attack", tb.map(|t| t.sp_attack).unwrap_or(0));
    e.i("tb_sp_defense", tb.map(|t| t.sp_defense).unwrap_or(0));
    e.i("tb_speed", tb.map(|t| t.speed).unwrap_or(0));
    match tb {
        None => e.a("tb_ability", SV::N),
        Some(t) => e.sym("tb_ability", Some(t.ability)),
    }
    for i in 0..4usize {
        let m = tb.and_then(|t| t.moves.get(i));
        match m {
            Some(mm) => e.sym(&format!("tb_move{}", i), Some(mm.name)),
            None => e.a(&format!("tb_move{}", i), SV::N),
        }
        let pp = tb.and_then(|t| t.pp.get(i));
        match pp {
            Some(&v) => e.i(&format!("tb_pp{}", i), v),
            None => e.a(&format!("tb_pp{}", i), SV::N),
        }
    }
    e.i("tb_n_moves", tb.map(|t| t.moves.len() as i64).unwrap_or(0));
}

pub fn view_fields(e: &mut Enc, v: &OppView, pfx: &str) {
    e.pfx = pfx.to_string();
    let mut order: Vec<usize> = (0..v.pokemon.len()).collect();
    order.sort_by(|&a, &b| {
        e.pack.intern.resolve(v.pokemon[a].name).cmp(e.pack.intern.resolve(v.pokemon[b].name))
    });
    e.i("n", order.len() as i64);
    for (i, &ki) in order.iter().enumerate() {
        let k = &v.pokemon[ki];
        e.pfx = format!("{}k{}_", pfx, i);
        e.sym("name", Some(k.name));
        e.b("previewed", k.previewed);
        e.b("seen", k.seen);
        e.tyo("type1", k.type1);
        e.tyo("type2", k.type2);
        {
            let joined: Vec<&str> =
                k.known_moves.iter().map(|&s| e.pack.intern.resolve(s)).collect();
            let j = joined.join("|");
            e.a("moves", SV::S(j));
        }
        e.sym("item", k.known_item);
        e.sym("ability", k.known_ability);
        e.b("threat", k.threat_alert);
        e.a("hpfrac", SV::F(k.hp_fraction));
        e.i("dlog_n", k.damage_log.len() as i64);
        for (j, d) in k.damage_log.iter().enumerate() {
            e.sym(&format!("d{}_mv", j), Some(d.mv));
            e.sym(&format!("d{}_at", j), d.attacker);
            e.a(&format!("d{}_fr", j), SV::F(d.fraction));
        }
    }
    e.pfx = pfx.to_string();
}

pub fn side_fields(e: &mut Enc, s: &Side, pfx: &str) {
    e.pfx = pfx.to_string();
    e.i("active_idx", s.active_idx as i64);
    e.i("n_party", s.party.len() as i64);
    e.b("stealth_rock_set", s.stealth_rock_set);
    e.b("mega_used", s.mega_used);
    e.b("reflect", s.reflect);
    e.i("reflect_count", s.reflect_count);
    e.b("light_screen", s.light_screen);
    e.i("light_screen_count", s.light_screen_count);
    e.b("aurora_veil", s.aurora_veil);
    e.i("aurora_veil_count", s.aurora_veil_count);
    e.b("tailwind", s.tailwind);
    e.i("tailwind_count", s.tailwind_count);
    e.i("wish_hp", s.wish_hp);
    e.i("wish_count", s.wish_count);
    e.b("healing_wish", s.healing_wish);
    e.i("safeguard", s.safeguard);
    e.i("future_sight_count", s.future_sight_count);
    e.i("future_sight_dmg", s.future_sight_dmg);
    match s.future_sight_name {
        None => e.a("future_sight_name", SV::S(String::new())),
        Some(x) => e.sym("future_sight_name", Some(x)),
    }
    e.i("field_idx", s.field_idx as i64);
    e.b("sr_pending", s.sr_pending);
    e.b("entry_pending", s.entry_pending);
    for i in 0..s.party.len() {
        poke_fields(e, &s.party[i], &format!("{}p{}.", pfx, i));
    }
    view_fields(e, &s.opp_view, &format!("{}view.", pfx));
}

pub fn field_fields(e: &mut Enc, f: &Field) {
    e.pfx = "F.".to_string();
    e.sym("weather", f.weather);
    e.i("weather_count", f.weather_count);
    e.b("trick_room", f.trick_room);
    e.i("trick_room_count", f.trick_room_count);
    e.b("stealth_rock0", f.stealth_rock[0]);
    e.b("stealth_rock1", f.stealth_rock[1]);
    e.i("spikes0", f.spikes[0]);
    e.i("spikes1", f.spikes[1]);
    e.i("toxic_spikes0", f.toxic_spikes[0]);
    e.i("toxic_spikes1", f.toxic_spikes[1]);
    e.b("sticky_web0", f.sticky_web[0]);
    e.b("sticky_web1", f.sticky_web[1]);
    e.b("misty_terrain", f.misty_terrain);
    e.i("misty_terrain_count", f.misty_terrain_count);
    e.b("electric_terrain", f.electric_terrain);
    e.i("electric_terrain_count", f.electric_terrain_count);
    e.b("psychic_terrain", f.psychic_terrain);
    e.i("psychic_terrain_count", f.psychic_terrain_count);
    e.i("gravity", f.gravity);
    e.i("magic_room", f.magic_room);
    e.i("wonder_room", f.wonder_room);
    e.b("grassy_terrain", f.grassy_terrain);
    e.i("grassy_terrain_count", f.grassy_terrain_count);
    e.b("weather_negated", f.weather_negated);
}

pub fn encode_battle<'a>(pack: &'a Pack, b: &Battle, with_names: bool) -> Enc<'a> {
    let mut e = Enc::new(pack, with_names);
    e.pfx = String::new();
    e.i("turn", b.turn);
    field_fields(&mut e, &b.field);
    side_fields(&mut e, &b.sides[0], "S1.");
    side_fields(&mut e, &b.sides[1], "S2.");
    e
}

// ───────────── 正準ハッシュ（_rust_engine/canon_hash.py と 1:1） ─────────────

const CRC_POLY: u32 = 0xEDB88320;

fn crc32(buf: &[u8]) -> u32 {
    let mut table = [0u32; 256];
    for (i, t) in table.iter_mut().enumerate() {
        let mut c = i as u32;
        for _ in 0..8 {
            c = if c & 1 != 0 { CRC_POLY ^ (c >> 1) } else { c >> 1 };
        }
        *t = c;
    }
    let mut c = 0xFFFF_FFFFu32;
    for &b in buf {
        c = table[((c ^ b as u32) & 0xff) as usize] ^ (c >> 8);
    }
    c ^ 0xFFFF_FFFF
}

fn adler32(buf: &[u8]) -> u32 {
    let (mut a, mut b) = (1u32, 0u32);
    for &x in buf {
        a = (a + x as u32) % 65521;
        b = (b + a) % 65521;
    }
    (b << 16) | a
}

pub fn canon_bytes(vals: &[SV]) -> Vec<u8> {
    let mut out: Vec<u8> = Vec::with_capacity(vals.len() * 9);
    for v in vals {
        match v {
            SV::N => out.push(0),
            SV::B(x) => {
                out.push(1);
                out.push(if *x { 1 } else { 0 });
            }
            SV::I(x) => {
                out.push(2);
                out.extend_from_slice(&(*x as f64).to_le_bytes());
            }
            SV::F(x) => {
                out.push(2);
                out.extend_from_slice(&x.to_le_bytes());
            }
            SV::S(s) => {
                out.push(3);
                out.extend_from_slice(s.as_bytes());
                out.push(0);
            }
        }
    }
    out
}

pub fn sv_hash(vals: &[SV]) -> u64 {
    let b = canon_bytes(vals);
    ((crc32(&b) as u64) << 32) | (adler32(&b) as u64)
}

/// R4: f64 ベクトルの 64bit ハッシュ（_rust_engine/canon_hash.py::f_hash と 1:1）
pub fn f64_hash(v: &[f64]) -> u64 {
    let mut buf: Vec<u8> = Vec::with_capacity(v.len() * 9);
    for x in v {
        buf.push(2);
        buf.extend_from_slice(&x.to_le_bytes());
    }
    ((crc32(&buf) as u64) << 32) | (adler32(&buf) as u64)
}
