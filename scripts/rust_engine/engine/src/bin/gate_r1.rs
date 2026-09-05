//! R1ゲート: ダンプ済み calc_damage ケースを再生し、ダメージ値と副作用をビット比較する。
//! 使い方: gate_r1 <datapack.json> <shard.jsonl> [<shard.jsonl> ...]
use engine::damage::{calc_damage, DMove, Field};
use engine::pack::{Cat, Pack, Ty};
use engine::poke::Poke;
use serde_json::Value;
use std::collections::HashSet;
use std::io::{BufRead, BufReader};

struct Case {
    atk: Poke,
    def: Poke,
    mv: DMove,
    field: Field,
    critical: bool,
    random_roll: Option<f64>,
    roll_override: Option<f64>,
    dmg: i64,
    post_charged: bool,
    post_electro: bool,
    post_def_item: Option<u16>,
    post_def_stage_speed: i32,
    post_weather_negated: bool,
}

fn s_opt(pack: &mut Pack, v: &Value) -> Option<u16> {
    v.as_str().map(|s| pack.intern_new(s))
}
fn ty(pack: &Pack, v: &Value) -> Ty {
    let s = v.as_str().expect("type str");
    pack.types.iter().position(|t| t == s).map(|i| i as Ty).unwrap_or_else(|| panic!("unknown type {}", s))
}
fn ty_opt(pack: &Pack, v: &Value) -> Option<Ty> {
    v.as_str().map(|_| ty(pack, v))
}
fn i(v: &Value) -> i64 {
    v.as_i64().expect("int")
}
fn b(v: &Value) -> bool {
    v.as_bool().expect("bool")
}

fn decode_poke(pack: &mut Pack, a: &[Value]) -> Poke {
    Poke {
        name: pack.intern_new(a[0].as_str().unwrap_or("")),
        name_pika: a[0].as_str().unwrap_or("").contains("ピカチュウ"),
        ability: pack.intern_new(a[1].as_str().unwrap_or("")),
        item: s_opt(pack, &a[2]),
        type1: ty(pack, &a[3]),
        type2: ty_opt(pack, &a[4]),
        status: s_opt(pack, &a[5]),
        hp: i(&a[6]),
        max_hp: i(&a[7]),
        attack: i(&a[8]),
        defense: i(&a[9]),
        sp_attack: i(&a[10]),
        sp_defense: i(&a[11]),
        speed: i(&a[12]),
        stage_attack: i(&a[13]) as i32,
        stage_defense: i(&a[14]) as i32,
        stage_sp_attack: i(&a[15]) as i32,
        stage_sp_defense: i(&a[16]) as i32,
        stage_speed: i(&a[17]) as i32,
        stage_accuracy: i(&a[18]) as i32,
        stage_evasion: i(&a[19]) as i32,
        fainted_allies: i(&a[20]),
        times_hit: i(&a[21]),
        weight_kg: a[22].as_f64().expect("weight"),
        charged: b(&a[23]),
        flash_fire_active: b(&a[24]),
        electromorphosis_charged: b(&a[25]),
        acts_second: b(&a[26]),
        move_failed_last: b(&a[27]),
        took_damage_this_turn: b(&a[28]),
        multi_hit_index: i(&a[29]),
        magnet_rise: b(&a[30]),
        grounded: b(&a[31]),
        last_flung_item: s_opt(pack, &a[32]),
        syrup_count: i(&a[33]),
        charging_move: s_opt(pack, &a[34]),
        minimized: b(&a[35]),
        switched_this_turn: b(&a[36]),
        confused: false,
        protecting: false,
        lock_on: b(&a[37]),
        ..Default::default()
    }
}

fn decode(pack: &mut Pack, v: &Value) -> Case {
    let c = v.as_array().expect("case array");
    let atk = decode_poke(pack, c[0].as_array().unwrap());
    let def = decode_poke(pack, c[1].as_array().unwrap());
    let m = c[2].as_array().unwrap();
    let mv = DMove {
        name: pack.intern_new(m[0].as_str().unwrap()),
        ty: ty(pack, &m[1]),
        category: Cat::parse(m[2].as_str().unwrap()),
        power: m[3].as_i64(),
        accuracy: None,
        ..Default::default()
    };
    let f = c[3].as_array().unwrap();
    let field = Field {
        weather: s_opt(pack, &f[0]),
        electric_terrain: b(&f[1]),
        psychic_terrain: b(&f[2]),
        misty_terrain: b(&f[3]),
        grassy_terrain: b(&f[4]),
        gravity: i(&f[5]),
        weather_negated: false,
        ..Default::default()
    };
    let p = c[8].as_array().unwrap();
    Case {
        atk,
        def,
        mv,
        field,
        critical: b(&c[4]),
        random_roll: c[5].as_f64(),
        roll_override: c[6].as_f64(),
        dmg: i(&c[7]),
        post_charged: b(&p[0]),
        post_electro: b(&p[1]),
        post_def_item: s_opt(pack, &p[2]),
        post_def_stage_speed: i(&p[3]) as i32,
        post_weather_negated: b(&p[4]),
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut pack = Pack::load(&args[1]);

    let mut total = 0usize;
    let mut ok = 0usize;
    let mut fails = 0usize;
    let mut calc_nanos = 0u128;
    let mut moves_seen: HashSet<u16> = HashSet::new();
    let mut abils_seen: HashSet<u16> = HashSet::new();
    let mut items_seen: HashSet<u16> = HashSet::new();
    let mut first_fail: Option<String> = None;

    for path in &args[2..] {
        let f = BufReader::new(std::fs::File::open(path).expect("shard"));
        let mut cases: Vec<Case> = Vec::new();
        let mut idx0 = total;
        for (ln, line) in f.lines().enumerate() {
            let line = line.unwrap();
            if ln == 0 {
                continue; // schema header
            }
            let v: Value = serde_json::from_str(&line).expect("case json");
            let c = decode(&mut pack, &v);
            moves_seen.insert(c.mv.name);
            abils_seen.insert(c.atk.ability);
            abils_seen.insert(c.def.ability);
            if let Some(x) = c.atk.item {
                items_seen.insert(x);
            }
            if let Some(x) = c.def.item {
                items_seen.insert(x);
            }
            cases.push(c);
        }
        let t0 = std::time::Instant::now();
        let mut results: Vec<i64> = Vec::with_capacity(cases.len());
        for c in cases.iter_mut() {
            let d = calc_damage(
                &pack,
                &mut c.atk,
                &mut c.def,
                &c.mv,
                &mut c.field,
                c.critical,
                c.random_roll,
                c.roll_override,
                &mut |_| panic!("R1ケースは live RNG を消費しない"),
            );
            results.push(d);
        }
        calc_nanos += t0.elapsed().as_nanos();
        for (k, c) in cases.iter().enumerate() {
            total += 1;
            let d = results[k];
            let mut bad: Vec<String> = Vec::new();
            if d != c.dmg {
                bad.push(format!("dmg {} != {}", d, c.dmg));
            }
            if c.atk.charged != c.post_charged {
                bad.push(format!("charged {} != {}", c.atk.charged, c.post_charged));
            }
            if c.atk.electromorphosis_charged != c.post_electro {
                bad.push(format!(
                    "electromorphosis {} != {}",
                    c.atk.electromorphosis_charged, c.post_electro
                ));
            }
            if c.def.item != c.post_def_item {
                bad.push(format!("def.item {:?} != {:?}", c.def.item, c.post_def_item));
            }
            if c.def.stage_speed != c.post_def_stage_speed {
                bad.push(format!(
                    "def.stage_speed {} != {}",
                    c.def.stage_speed, c.post_def_stage_speed
                ));
            }
            if c.field.weather_negated != c.post_weather_negated {
                bad.push(format!(
                    "weather_negated {} != {}",
                    c.field.weather_negated, c.post_weather_negated
                ));
            }
            if bad.is_empty() {
                ok += 1;
            } else {
                fails += 1;
                if first_fail.is_none() {
                    first_fail = Some(format!(
                        "case#{} ({}:{}) move={} atk={}({}) def={}({}) -> {}",
                        idx0 + k,
                        path,
                        k + 2,
                        pack.intern.resolve(c.mv.name),
                        c.atk.name,
                        pack.intern.resolve(c.atk.ability),
                        c.def.name,
                        pack.intern.resolve(c.def.ability),
                        bad.join("; ")
                    ));
                }
            }
        }
        idx0 = total;
        let _ = idx0;
        eprintln!("[gate_r1] {} done: total={} ok={} fail={}", path, total, ok, fails);
    }

    println!("R1 GATE: {}/{} match ({} mismatches)", ok, total, fails);
    println!(
        "calc_damage rust: {:.3}s for {} cases = {:.0} ns/case",
        calc_nanos as f64 / 1e9,
        total,
        calc_nanos as f64 / total as f64
    );
    println!(
        "coverage: moves={} abilities={} items={}",
        moves_seen.len(),
        abils_seen.len(),
        items_seen.len()
    );
    let mut mv: Vec<&str> = moves_seen.iter().map(|&s| pack.intern.resolve(s)).collect();
    mv.sort();
    std::fs::write(
        "coverage_r1.json",
        serde_json::to_string_pretty(&serde_json::json!({
            "moves": mv,
            "abilities": abils_seen.iter().map(|&s| pack.intern.resolve(s)).collect::<Vec<_>>(),
            "items": items_seen.iter().map(|&s| pack.intern.resolve(s)).collect::<Vec<_>>(),
        }))
        .unwrap(),
    )
    .ok();
    if let Some(f) = first_fail {
        println!("FIRST DIVERGENCE: {}", f);
        std::process::exit(1);
    }
}
