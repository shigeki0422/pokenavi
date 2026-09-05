//! simulator/pokemon.py の移植（ステータス計算・spec解析・テンプレート構築）
use crate::interner::Sym;
use crate::pack::{Cat, MegaStats, Pack, Ty};
use std::collections::HashMap;

/// STAT_STAGE_MULT（Pythonの式そのままの f64 値）
#[inline]
pub fn stat_stage_mult(stage: i32) -> f64 {
    match stage.clamp(-6, 6) {
        -6 => 2.0 / 8.0,
        -5 => 2.0 / 7.0,
        -4 => 2.0 / 6.0,
        -3 => 2.0 / 5.0,
        -2 => 2.0 / 4.0,
        -1 => 2.0 / 3.0,
        0 => 1.0,
        1 => 3.0 / 2.0,
        2 => 4.0 / 2.0,
        3 => 5.0 / 2.0,
        4 => 6.0 / 2.0,
        5 => 7.0 / 2.0,
        _ => 8.0 / 2.0,
    }
}

#[inline]
pub fn acc_eva_stage(stage: i32) -> f64 {
    match stage.clamp(-6, 6) {
        -6 => 3.0 / 9.0,
        -5 => 3.0 / 8.0,
        -4 => 3.0 / 7.0,
        -3 => 3.0 / 6.0,
        -2 => 3.0 / 5.0,
        -1 => 3.0 / 4.0,
        0 => 1.0,
        1 => 4.0 / 3.0,
        2 => 5.0 / 3.0,
        3 => 6.0 / 3.0,
        4 => 7.0 / 3.0,
        5 => 8.0 / 3.0,
        _ => 9.0 / 3.0,
    }
}

/// calc_stat: math.floor((math.floor((base*2+iv+ev*2)*level/100)+5)*nature_mod)
#[inline]
pub fn calc_stat(base: i64, ev: i64, iv: i64, nature_mod: f64) -> i64 {
    let level = 50i64;
    let inner = (((base * 2 + iv + ev * 2) * level) as f64 / 100.0).floor() as i64;
    (((inner + 5) as f64) * nature_mod).floor() as i64
}

/// calc_hp: math.floor((base*2+iv+ev*2)*level/100)+level+10
#[inline]
pub fn calc_hp(base: i64, ev: i64) -> i64 {
    let level = 50i64;
    let iv = 31i64;
    ((((base * 2 + iv + ev * 2) * level) as f64 / 100.0).floor() as i64) + level + 10
}

#[derive(Clone, Debug, Default, PartialEq)]
pub struct Evs {
    pub h: i64,
    pub a: i64,
    pub b: i64,
    pub c: i64,
    pub d: i64,
    pub s: i64,
}

#[derive(Clone, Debug)]
pub struct MoveInst {
    pub name: Sym,
    pub name_jp: String,
    pub ty: Ty,
    pub category: Cat,
    pub power: Option<i64>,
    pub accuracy: Option<i64>,
    pub priority: i64,
    pub pp: Option<i64>,
}

/// BattlePokemon の全状態（宣言77＋動的45）。simulator/pokemon.py + battle.py の動的属性。
#[derive(Clone, Debug, Default)]
pub struct Poke {
    pub name: Sym,
    pub name_pika: bool,
    pub dex: i64,
    pub ability: Sym,
    pub item: Option<Sym>,
    pub type1: Ty,
    pub type2: Option<Ty>,
    pub status: Option<Sym>,
    pub hp: i64,
    pub max_hp: i64,
    pub attack: i64,
    pub defense: i64,
    pub sp_attack: i64,
    pub sp_defense: i64,
    pub speed: i64,
    pub stage_attack: i32,
    pub stage_defense: i32,
    pub stage_sp_attack: i32,
    pub stage_sp_defense: i32,
    pub stage_speed: i32,
    pub stage_accuracy: i32,
    pub stage_evasion: i32,
    pub fainted_allies: i64,
    pub times_hit: i64,
    pub weight_kg: f64,
    pub charged: bool,
    pub flash_fire_active: bool,
    pub electromorphosis_charged: bool,
    pub acts_second: bool,
    pub move_failed_last: bool,
    pub took_damage_this_turn: bool,
    pub multi_hit_index: i64,
    pub magnet_rise: bool,
    pub grounded: bool,
    pub last_flung_item: Option<Sym>,
    pub syrup_count: i64,
    pub charging_move: Option<Sym>,
    pub minimized: bool,
    pub switched_this_turn: bool,
    pub confused: bool,
    pub protecting: bool,
    pub lock_on: bool,
    // ── 以下 R2 で追加（BattlePokemon の残り） ──
    pub base_type1: Ty,
    pub base_type2: Option<Ty>,
    pub nature: Sym,
    pub evs: [i64; 6],
    pub moves: Vec<crate::damage::DMove>,
    pub pp: Vec<i64>,
    pub bad_poison_count: i64,
    pub sleep_count: i64,
    pub flinched: bool,
    pub is_alive: bool,
    pub mega_evolved: bool,
    pub mega: Option<crate::pack::MegaStats>,
    pub hero_forme: bool,
    pub protect_consecutive: i64,
    pub enduring: bool,
    pub ate_berry: bool,
    pub used_moves: Vec<Sym>,
    pub heal_block_count: i64,
    pub deka_last: bool,
    pub locked_move: Option<Sym>,
    pub choice_locked_move: Option<Sym>,
    pub disabled_move: Option<Sym>,
    pub disabled_turns: i64,
    pub lock_count: i64,
    pub recharge: bool,
    pub seeded: bool,
    pub yawn_count: i64,
    pub encore_count: i64,
    pub taunt_count: i64,
    pub bound_count: i64,
    pub throat_chop_count: i64,
    pub stockpile_count: i64,
    pub infatuation: bool,
    pub torment: bool,
    pub trapped: bool,
    pub ability_suppressed: bool,
    pub rooted: bool,
    pub aqua_ring: bool,
    pub last_used_move: Option<Sym>,
    pub turns_out: i64,
    pub perish_count: i64,
    pub destiny_bond: bool,
    pub cursed: bool,
    pub crit_stage: i64,
    // ── 動的属性 ──
    pub barrier_done: bool,
    pub baton_stages: Option<[i32; 7]>,
    pub beak_primed: bool,
    pub destiny_bond_last_turn: bool,
    pub disguise_broken: bool,
    pub electrified: bool,
    pub force_switch: bool,
    pub gyaku_triggered: bool,
    pub hangry: bool,
    pub honey_used: bool,
    pub illusion_name: Option<Sym>,
    pub in_blade_forme: bool,
    pub info_done: bool,
    pub last_berry: Option<Sym>,
    pub last_consumed_item: Option<Sym>,
    pub last_item: Option<Sym>,
    pub last_move_obj: Option<crate::damage::DMove>,
    pub last_physical_dmg_received: i64,
    pub last_special_dmg_received: i64,
    pub levitate_turns: i64,
    pub move_failed_this_turn: bool,
    pub pierce_quarter: bool,
    pub pivot_out: bool,
    pub protean_used: bool,
    pub protect_move: Option<Sym>,
    pub roost_types: Option<(Ty, Option<Ty>)>,
    pub ruminate_berry: Option<Sym>,
    pub ruminate_count: i64,
    pub salted: bool,
    pub sealed: bool,
    pub shield_atk: i64,
    pub shield_def: i64,
    pub shield_spatk: i64,
    pub shield_spdef: i64,
    pub substitute_hp: i64,
    pub transformed: bool,
    pub transform_backup: Option<Box<TransformBackup>>,
}

#[derive(Clone, Debug, Default)]
pub struct TransformBackup {
    pub attack: i64,
    pub defense: i64,
    pub sp_attack: i64,
    pub sp_defense: i64,
    pub speed: i64,
    pub ability: Sym,
    pub moves: Vec<crate::damage::DMove>,
    pub pp: Vec<i64>,
}

impl Poke {
    #[inline]
    pub fn raw_stat(&self, idx: u8) -> i64 {
        match idx {
            0 => self.attack,
            1 => self.defense,
            2 => self.sp_attack,
            3 => self.sp_defense,
            _ => self.speed,
        }
    }
    /// get_effective_stat: max(1, floor(base * STAT_STAGE_MULT[clamp(stage)]))
    #[inline]
    pub fn eff_stat(&self, idx: u8) -> i64 {
        let base = self.raw_stat(idx);
        let v = ((base as f64) * stat_stage_mult(self.stage(idx))).floor() as i64;
        v.max(1)
    }
    /// get_effective_speed
    #[inline]
    pub fn eff_speed(&self, pack: &Pack) -> i64 {
        let mut spd = self.eff_stat(4);
        if self.status == Some(pack.sy.st.paralysis) && self.ability != pack.sy.ab.はやあし {
            spd = ((spd as f64) * 0.5).floor() as i64;
        }
        if self.syrup_count > 0 {
            spd = ((spd as f64) * 0.5).floor() as i64;
        }
        spd
    }
    #[inline]
    pub fn has_type(&self, t: Ty) -> bool {
        self.type1 == t || self.type2 == Some(t)
    }
}

// ───────────────────────── spec parse / build ─────────────────────────

#[derive(Clone, Debug, Default)]
pub struct Spec {
    pub name: String,
    pub item: Option<String>,
    pub nature: Option<String>,
    pub moves: Option<Vec<String>>,
    pub evs: Option<Evs>,
    pub ability: Option<String>,
}

fn chars(s: &str) -> Vec<char> {
    s.chars().collect()
}
fn substr(v: &[char], a: usize) -> String {
    v[a.min(v.len())..].iter().collect()
}

/// parse_pokemon_spec の忠実移植
pub fn parse_pokemon_spec(spec_str: &str) -> Spec {
    let mut s = spec_str.trim().to_string();
    let mut item: Option<String> = None;
    if let Some(pos) = s.find('@') {
        let head = s[..pos].to_string();
        let item_part = s[pos + '@'.len_utf8()..].to_string();
        let first_seg = item_part.split(':').next().unwrap_or("").trim().to_string();
        let it = if first_seg.is_empty() { None } else { Some(first_seg) };
        let ilen = it.as_deref().unwrap_or("").chars().count();
        let rest = substr(&chars(&item_part), ilen);
        item = it;
        s = head + &rest;
    }
    let parts: Vec<&str> = s.split(':').collect();
    let name = parts.first().unwrap_or(&"").trim().to_string();
    let mut nature = None;
    let mut moves = None;
    let mut evs = None;
    let mut ability = None;
    if parts.len() >= 2 && !parts[1].trim().is_empty() {
        nature = Some(parts[1].trim().to_string());
    }
    if parts.len() >= 3 && !parts[2].trim().is_empty() {
        moves = Some(
            parts[2]
                .trim()
                .split('|')
                .map(|m| m.trim().to_string())
                .filter(|m| !m.is_empty())
                .collect(),
        );
    }
    if parts.len() >= 4 && !parts[3].trim().is_empty() {
        let vals: Vec<i64> =
            parts[3].trim().split('/').map(|x| x.parse::<i64>().expect("ev int")).collect();
        let g = |i: usize| vals.get(i).copied().unwrap_or(0);
        evs = Some(Evs { h: g(0), a: g(1), b: g(2), c: g(3), d: g(4), s: g(5) });
    }
    if parts.len() >= 5 && !parts[4].trim().is_empty() {
        ability = Some(parts[4].trim().to_string());
    }
    Spec { name, item, nature, moves, evs, ability }
}

pub fn normalize_mega_stone(name: &str) -> String {
    name.replace('Ｘ', "X").replace('Ｙ', "Y")
}

#[derive(Clone, Debug)]
pub struct Template {
    pub name: String,
    pub dex: i64,
    pub type1: Ty,
    pub type2: Option<Ty>,
    pub base: [i64; 6], // H A B C D S
    pub weight_kg: f64,
    pub top_moves: Vec<(String, f64)>,
    pub top_items: Vec<(String, f64)>,
    pub top_abilities: Vec<(String, f64)>,
    pub top_natures: Vec<(String, f64)>,
    pub top_evs: Vec<crate::pack::EvEntry>,
    /// 正規化済み石名 -> MegaStats（挿入順を保持）
    pub mega_data: Vec<(String, MegaStats)>,
}

impl Template {
    pub fn mega_get(&self, key: &str) -> Option<&MegaStats> {
        self.mega_data.iter().find(|(k, _)| k == key).map(|(_, v)| v)
    }
}

/// DataLoader.get_pokemon_template の忠実移植
pub fn get_pokemon_template(pack: &Pack, raw_name: &str, season: &str) -> Option<Template> {
    let mut pokemon_name = raw_name.replace(" (", "(");
    if let Some(a) = pack.form_aliases.get(&pokemon_name) {
        pokemon_name = a.clone();
    }

    let mut base: Option<&crate::pack::BaseStats> = None;
    for prefix in &pack.region_prefixes {
        let suffix = format!("({})", prefix);
        if pokemon_name.ends_with(&suffix) {
            let cv = chars(&pokemon_name);
            let cut = cv.len() - (prefix.chars().count() + 2);
            let stem: String = cv[..cut].iter().collect();
            let alt = format!("{}{}", prefix, stem);
            base = pack.base_stats.iter().find(|b| b.name == alt);
            break;
        }
    }
    if base.is_none() {
        base = pack.base_stats.iter().find(|b| b.name == pokemon_name);
    }
    if base.is_none() {
        let stem = pokemon_name.split('(').next().unwrap_or("").to_string();
        base = pack.base_stats.iter().find(|b| b.name.contains(&stem));
    }
    let base = base?;

    // 使用率DBの名前解決
    let mut usage_name = pokemon_name.clone();
    for prefix in &pack.region_prefixes {
        let suffix = format!("({})", prefix);
        if pokemon_name.ends_with(&suffix) {
            let cv = chars(&pokemon_name);
            let cut = cv.len() - (prefix.chars().count() + 2);
            let base_part: String = cv[..cut].iter().collect();
            let spaced = format!("{} ({})", base_part, prefix);
            if pack.usage_names_in_moves.contains(&spaced) {
                usage_name = spaced;
            } else {
                let prefixed = format!("{}{}", prefix, base_part);
                if pack.usage_names_in_moves.contains(&prefixed) {
                    usage_name = prefixed;
                }
            }
            break;
        }
    }

    let empty = crate::pack::Usage::default();
    let u = pack.usage.get(&format!("{}\t{}", season, usage_name)).unwrap_or(&empty);

    // メガデータ解決
    let mut mega_data: Vec<(String, MegaStats)> = Vec::new();
    for (item, _) in &u.items {
        if !item.contains("ナイト") {
            continue;
        }
        let stone = normalize_mega_stone(item);
        if mega_data.iter().any(|(k, _)| *k == stone) {
            continue;
        }
        if let Some(m) =
            pack.mega_stats.iter().find(|m| m.mega_stone == stone || m.mega_stone == *item)
        {
            mega_data.push((stone, m.clone()));
        }
    }
    for m in pack.mega_stats.iter().filter(|m| m.base_dex == base.dex) {
        let st = normalize_mega_stone(&m.mega_stone);
        if mega_data.iter().any(|(k, _)| *k == st) {
            continue;
        }
        mega_data.push((st, m.clone()));
    }

    Some(Template {
        name: pokemon_name,
        dex: base.dex,
        type1: base.type1,
        type2: base.type2,
        base: [
            base.hp,
            base.attack,
            base.defense,
            base.sp_attack,
            base.sp_defense,
            base.speed,
        ],
        weight_kg: match base.weight_kg {
            Some(w) if w != 0.0 => w,
            _ => 50.0,
        },
        top_moves: u.moves.clone(),
        top_items: u.items.clone(),
        top_abilities: u.abilities.clone(),
        top_natures: u.natures.clone(),
        top_evs: u.evs.clone(),
        mega_data,
    })
}

pub struct BuiltPokemon {
    pub name: String,
    pub dex: i64,
    pub type1: Ty,
    pub type2: Option<Ty>,
    pub max_hp: i64,
    pub hp: i64,
    pub attack: i64,
    pub defense: i64,
    pub sp_attack: i64,
    pub sp_defense: i64,
    pub speed: i64,
    pub moves: Vec<MoveInst>,
    pub pp: Vec<i64>,
    pub item: Option<String>,
    pub ability: String,
    pub nature: String,
    pub evs: Evs,
    pub weight_kg: f64,
    pub mega: Option<MegaStats>,
}

fn nat_mod(pack: &Pack, nature: &str, stat: u8) -> f64 {
    let sym = match pack.intern.get(nature) {
        Some(s) => s,
        None => return 1.0,
    };
    match pack.nature_mods.get(&sym) {
        Some(&(up, dn)) => {
            if up == stat {
                1.1
            } else if dn == stat {
                0.9
            } else {
                1.0
            }
        }
        None => 1.0,
    }
}

/// build_from_template（全override指定・randomize非依存の経路）
/// pokemon.py `weighted_choice`。rng=None は randomize=False（使用率1位）。
/// 返り値は items のインデックス。
fn weighted_choice(rates: &[f64], rng: &mut Option<&mut dyn crate::rng::BRng>) -> Option<usize> {
    if rates.is_empty() {
        return None;
    }
    let r = match rng {
        None => return Some(0),
        Some(r) => r,
    };
    let total: f64 = crate::pysum::pysum(rates.iter().copied());
    if total == 0.0 {
        return Some(0);
    }
    let mut x = r.random() * total;
    for (i, rate) in rates.iter().enumerate() {
        x -= *rate;
        if x <= 0.0 {
            return Some(i);
        }
    }
    Some(rates.len() - 1)
}

pub fn build_from_template(pack: &Pack, tpl: &Template, spec: &Spec) -> BuiltPokemon {
    build_from_template_rand(pack, tpl, spec, &mut None)
}

/// randomize=True 相当（rng=Some）。消費順は Python と同じ: 性格→道具→特性→努力値→技。
pub fn build_from_template_rand(
    pack: &Pack,
    tpl: &Template,
    spec: &Spec,
    rng: &mut Option<&mut dyn crate::rng::BRng>,
) -> BuiltPokemon {
    let nature = spec.nature.clone().unwrap_or_else(|| {
        let rates: Vec<f64> = tpl.top_natures.iter().map(|x| x.1).collect();
        match weighted_choice(&rates, rng) {
            Some(i) if !tpl.top_natures[i].0.is_empty() => tpl.top_natures[i].0.clone(),
            _ => "まじめ".to_string(),
        }
    });
    let item = match &spec.item {
        Some(i) => Some(i.clone()),
        None => {
            let rates: Vec<f64> = tpl.top_items.iter().map(|x| x.1).collect();
            weighted_choice(&rates, rng).map(|i| tpl.top_items[i].0.clone())
        }
    };
    let ability = match &spec.ability {
        Some(a) => a.clone(),
        None => {
            let rates: Vec<f64> = tpl.top_abilities.iter().map(|x| x.1).collect();
            weighted_choice(&rates, rng)
                .map(|i| tpl.top_abilities[i].0.clone())
                .unwrap_or_default()
        }
    };
    let evs = match &spec.evs {
        Some(e) => e.clone(),
        None => {
            let rates: Vec<f64> = tpl.top_evs.iter().map(|x| x.rate).collect();
            match weighted_choice(&rates, rng) {
                Some(i) => {
                    let e = &tpl.top_evs[i];
                    Evs { h: e.h, a: e.a, b: e.b, c: e.c, d: e.d, s: e.s }
                }
                None => Evs::default(),
            }
        }
    };

    let max_hp = calc_hp(tpl.base[0], evs.h);
    let mut attack = calc_stat(tpl.base[1], evs.a, 31, nat_mod(pack, &nature, 0));
    let defense = calc_stat(tpl.base[2], evs.b, 31, nat_mod(pack, &nature, 1));
    let sp_attack = calc_stat(tpl.base[3], evs.c, 31, nat_mod(pack, &nature, 2));
    let sp_defense = calc_stat(tpl.base[4], evs.d, 31, nat_mod(pack, &nature, 3));
    let speed = calc_stat(tpl.base[5], evs.s, 31, nat_mod(pack, &nature, 4));

    let mut moves = Vec::new();
    if let Some(ms) = &spec.moves {
        for m in ms {
            if let Some(&idx) = pack.move_by_name.get(m) {
                let md = &pack.moves[idx];
                moves.push(MoveInst {
                    name: md.name,
                    name_jp: md.name_jp.clone(),
                    ty: md.ty,
                    category: md.category,
                    power: md.power,
                    accuracy: md.accuracy,
                    priority: md.priority,
                    pp: md.pp,
                });
            }
        }
    } else {
        let mut pool: Vec<(String, f64)> = tpl.top_moves.clone();
        for _ in 0..std::cmp::min(4, tpl.top_moves.len()) {
            let total: f64 = crate::pysum::pysum(pool.iter().map(|x| x.1));
            if total == 0.0 || pool.is_empty() {
                break;
            }
            let chosen = match rng {
                None => pool[0].0.clone(),
                Some(r) => {
                    let mut x = r.random() * total;
                    let mut c = pool[pool.len() - 1].0.clone();
                    for (name, rate) in pool.iter() {
                        x -= *rate;
                        if x <= 0.0 {
                            c = name.clone();
                            break;
                        }
                    }
                    c
                }
            };
            pool.retain(|(n, _)| *n != chosen);
            if let Some(&idx) = pack.move_by_name.get(&chosen) {
                let md = &pack.moves[idx];
                moves.push(MoveInst {
                    name: md.name,
                    name_jp: md.name_jp.clone(),
                    ty: md.ty,
                    category: md.category,
                    power: md.power,
                    accuracy: md.accuracy,
                    priority: md.priority,
                    pp: md.pp,
                });
            }
        }
    }
    let pp: Vec<i64> = moves.iter().map(|m| m.pp.unwrap_or(5)).collect();

    let mega = item.as_ref().and_then(|it| {
        tpl.mega_get(&normalize_mega_stone(it)).or_else(|| tpl.mega_get(it)).cloned()
    });

    if ability == "はりきり" {
        attack = ((attack as f64) * 1.5).floor() as i64;
    }

    BuiltPokemon {
        name: tpl.name.clone(),
        dex: tpl.dex,
        type1: tpl.type1,
        type2: tpl.type2,
        max_hp,
        hp: max_hp,
        attack,
        defense,
        sp_attack,
        sp_defense,
        speed,
        moves,
        pp,
        item,
        ability,
        nature,
        evs,
        weight_kg: tpl.weight_kg,
        mega,
    }
}

/// do_mega_evolve の忠実移植（HP満タン前提ではなく hp/max_hp 比を保持）
pub fn do_mega_evolve(pack: &Pack, p: &mut BuiltPokemon) {
    let md = match &p.mega {
        Some(m) => m.clone(),
        None => return,
    };
    let hp_ratio = (p.hp as f64) / (p.max_hp as f64);
    p.max_hp = calc_hp(md.hp, p.evs.h);
    p.hp = std::cmp::max(1, ((p.max_hp as f64) * hp_ratio).floor() as i64);
    p.attack = calc_stat(md.attack, p.evs.a, 31, nat_mod(pack, &p.nature, 0));
    p.defense = calc_stat(md.defense, p.evs.b, 31, nat_mod(pack, &p.nature, 1));
    p.sp_attack = calc_stat(md.sp_attack, p.evs.c, 31, nat_mod(pack, &p.nature, 2));
    p.sp_defense = calc_stat(md.sp_defense, p.evs.d, 31, nat_mod(pack, &p.nature, 3));
    p.speed = calc_stat(md.speed, p.evs.s, 31, nat_mod(pack, &p.nature, 4));
    p.type1 = md.type1;
    p.type2 = md.type2;
    if let Some(a) = &md.ability {
        if !a.is_empty() {
            p.ability = a.clone();
        }
    }
    if let Some(w) = md.weight_kg {
        if w != 0.0 {
            p.weight_kg = w;
        }
    }
}

pub type NatureTable = HashMap<Sym, (u8, u8)>;

// ───────────────── R2: BattlePokemon のメソッド群 ─────────────────

/// ランク indices: 0=attack 1=defense 2=sp_attack 3=sp_defense 4=speed 5=accuracy 6=evasion
pub const ST_ATK: u8 = 0;
pub const ST_DEF: u8 = 1;
pub const ST_SPA: u8 = 2;
pub const ST_SPD: u8 = 3;
pub const ST_SPE: u8 = 4;
pub const ST_ACC: u8 = 5;
pub const ST_EVA: u8 = 6;

impl Poke {
    #[inline]
    pub fn stage(&self, i: u8) -> i32 {
        match i {
            0 => self.stage_attack,
            1 => self.stage_defense,
            2 => self.stage_sp_attack,
            3 => self.stage_sp_defense,
            4 => self.stage_speed,
            5 => self.stage_accuracy,
            _ => self.stage_evasion,
        }
    }
    #[inline]
    pub fn set_stage(&mut self, i: u8, v: i32) {
        match i {
            0 => self.stage_attack = v,
            1 => self.stage_defense = v,
            2 => self.stage_sp_attack = v,
            3 => self.stage_sp_defense = v,
            4 => self.stage_speed = v,
            5 => self.stage_accuracy = v,
            _ => self.stage_evasion = v,
        }
    }
    /// 実数値（attack..speed）へのアクセス（0..4）
    #[inline]
    pub fn set_raw_stat(&mut self, i: u8, v: i64) {
        match i {
            0 => self.attack = v,
            1 => self.defense = v,
            2 => self.sp_attack = v,
            3 => self.sp_defense = v,
            _ => self.speed = v,
        }
    }
    /// BattlePokemon.take_damage
    #[inline]
    pub fn take_damage(&mut self, dmg: i64) {
        if self.enduring && dmg >= self.hp && self.hp > 0 {
            self.hp = 1;
            return;
        }
        self.hp = std::cmp::max(0, self.hp - dmg);
        if self.hp == 0 {
            self.is_alive = false;
        }
    }
    pub fn has_type_opt(&self, t: Option<Ty>) -> bool {
        match t {
            Some(t) => self.has_type(t),
            None => false,
        }
    }
}

/// BattlePokemon.apply_status
pub fn apply_status(pack: &Pack, p: &mut Poke, status: Sym, corrosion: bool) -> bool {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    if p.status.is_some() {
        return false;
    }
    let ab = p.ability;
    if ab == l.きよめのしお {
        return false;
    }
    if ab == l.じゅうなん && status == st.paralysis {
        return false;
    }
    if ab == l.めんえき && (status == st.poison || status == st.badpoison) {
        return false;
    }
    if ab == l.マグマのよろい && status == st.freeze {
        return false;
    }
    if ab == l.すいほう && status == st.burn {
        return false;
    }
    if (ab == l.ふみん || ab == l.やるき || ab == l.スイートベール) && status == st.sleep {
        return false;
    }
    if status == st.burn && p.has_type(pack.tc.ほのお) {
        return false;
    }
    if (status == st.poison || status == st.badpoison)
        && !corrosion
        && (p.has_type(pack.tc.どく) || p.has_type(pack.tc.はがね))
    {
        return false;
    }
    if status == st.paralysis && p.has_type(pack.tc.でんき) {
        return false;
    }
    if status == st.freeze && p.has_type(pack.tc.こおり) {
        return false;
    }
    p.status = Some(status);
    true
}

/// BattlePokemon.do_mega_evolve（実インスタンス版）
pub fn mega_evolve_poke(pack: &Pack, p: &mut Poke) {
    if p.mega_evolved || p.mega.is_none() {
        return;
    }
    let md = p.mega.clone().unwrap();
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
    let hp_ratio = (p.hp as f64) / (p.max_hp as f64);
    p.max_hp = calc_hp(md.hp, p.evs[0]);
    p.hp = std::cmp::max(1, ((p.max_hp as f64) * hp_ratio).floor() as i64);
    p.attack = calc_stat(md.attack, p.evs[1], 31, nat(0));
    p.defense = calc_stat(md.defense, p.evs[2], 31, nat(1));
    p.sp_attack = calc_stat(md.sp_attack, p.evs[3], 31, nat(2));
    p.sp_defense = calc_stat(md.sp_defense, p.evs[4], 31, nat(3));
    p.speed = calc_stat(md.speed, p.evs[5], 31, nat(4));
    p.type1 = md.type1;
    p.type2 = md.type2;
    p.base_type1 = md.type1;
    p.base_type2 = md.type2;
    if let Some(a) = &md.ability {
        if !a.is_empty() {
            p.ability = pack.intern.get(a).expect("mega ability interned");
        }
    }
    if let Some(w) = md.weight_kg {
        if w != 0.0 {
            p.weight_kg = w;
        }
    }
    p.mega_evolved = true;
}

/// build_from_spec 相当: spec 文字列から実戦用 Poke を作る（randomize=False 経路）
pub fn build_poke(pack: &mut Pack, spec_str: &str, season: &str) -> Poke {
    build_poke_rand(pack, spec_str, season, &mut None)
}

/// build_from_spec(randomize=True) 相当（rng=Some）
pub fn build_poke_rand(
    pack: &mut Pack,
    spec_str: &str,
    season: &str,
    rng: &mut Option<&mut dyn crate::rng::BRng>,
) -> Poke {
    let spec = parse_pokemon_spec(spec_str);
    let tpl = get_pokemon_template(pack, &spec.name, season)
        .unwrap_or_else(|| panic!("ポケモン '{}' が見つかりません (season={})", spec.name, season));
    let b = build_from_template_rand(pack, &tpl, &spec, rng);
    to_poke_mut(pack, &b)
}

/// 未登録語彙を登録してから Poke 化する（spec 由来の新語彙に対応）
pub fn to_poke_mut(pack: &mut Pack, b: &BuiltPokemon) -> Poke {
    pack.intern_new(&b.name);
    pack.intern_new(&b.ability);
    if let Some(i) = &b.item {
        pack.intern_new(i);
    }
    pack.intern_new(&b.nature);
    to_poke(pack, b)
}

/// BuiltPokemon -> Poke（語彙は登録済み前提＝&Pack のみ）
pub fn to_poke(pack: &Pack, b: &BuiltPokemon) -> Poke {
    let g = |s: &str| pack.intern.get(s).unwrap_or_else(|| panic!("未インターン語彙: {:?}", s));
    let name_sym = g(&b.name);
    let ability_sym = g(&b.ability);
    let item_sym = b.item.as_ref().map(|x| g(x));
    let nature_sym = g(&b.nature);
    let moves: Vec<crate::damage::DMove> = b
        .moves
        .iter()
        .map(|m| crate::damage::DMove {
            name: m.name,
            ty: m.ty,
            category: m.category,
            power: m.power,
            accuracy: m.accuracy,
            priority: m.priority,
            pp: m.pp,
        })
        .collect();
    Poke {
        name: name_sym,
        name_pika: b.name.contains("ピカチュウ"),
        dex: b.dex,
        ability: ability_sym,
        item: item_sym,
        type1: b.type1,
        type2: b.type2,
        base_type1: b.type1,
        base_type2: b.type2,
        status: None,
        hp: b.hp,
        max_hp: b.max_hp,
        attack: b.attack,
        defense: b.defense,
        sp_attack: b.sp_attack,
        sp_defense: b.sp_defense,
        speed: b.speed,
        weight_kg: b.weight_kg,
        nature: nature_sym,
        evs: [b.evs.h, b.evs.a, b.evs.b, b.evs.c, b.evs.d, b.evs.s],
        pp: b.pp.clone(),
        moves,
        is_alive: true,
        mega: b.mega.clone(),
        ..Default::default()
    }
}
