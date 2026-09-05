//! R0ゲート: spec文字列からビルドした全派生フィールドをJSONで出力する。
//! 使い方: gate_r0 <datapack.json> <input.json> <output.json>
//! input.json = [{"spec": "...", "season": "M-3"}, ...]
use engine::pack::{Cat, Pack, Ty};
use engine::poke::{build_from_template, do_mega_evolve, get_pokemon_template, parse_pokemon_spec, BuiltPokemon};
use serde_json::{json, Value};

fn ty_name(pack: &Pack, t: Ty) -> Value {
    if t == engine::pack::NO_TY {
        Value::Null
    } else {
        json!(pack.types[t as usize])
    }
}
fn ty_opt(pack: &Pack, t: Option<Ty>) -> Value {
    match t {
        Some(x) => ty_name(pack, x),
        None => Value::Null,
    }
}
fn cat_name(c: Cat) -> &'static str {
    match c {
        Cat::Physical => "physical",
        Cat::Special => "special",
        Cat::Status => "status",
    }
}

fn dump(pack: &Pack, p: &BuiltPokemon) -> Value {
    json!({
        "name": p.name,
        "dex": p.dex,
        "type1": ty_name(pack, p.type1),
        "type2": ty_opt(pack, p.type2),
        "max_hp": p.max_hp,
        "hp": p.hp,
        "attack": p.attack,
        "defense": p.defense,
        "sp_attack": p.sp_attack,
        "sp_defense": p.sp_defense,
        "speed": p.speed,
        "ability": p.ability,
        "item": p.item,
        "nature": p.nature,
        "weight_kg": p.weight_kg,
        "evs": {"H": p.evs.h, "A": p.evs.a, "B": p.evs.b, "C": p.evs.c, "D": p.evs.d, "S": p.evs.s},
        "moves": p.moves.iter().map(|m| json!({
            "name_jp": m.name_jp,
            "type": ty_name(pack, m.ty),
            "category": cat_name(m.category),
            "power": m.power,
            "accuracy": m.accuracy,
            "priority": m.priority,
            "pp": m.pp,
        })).collect::<Vec<_>>(),
        "pp": p.pp,
    })
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let pack = Pack::load(&args[1]);
    let input: Value = serde_json::from_str(&std::fs::read_to_string(&args[2]).unwrap()).unwrap();
    let mut out = Vec::new();
    for row in input.as_array().unwrap() {
        let spec_str = row["spec"].as_str().unwrap();
        let season = row["season"].as_str().unwrap();
        let spec = parse_pokemon_spec(spec_str);
        let tpl = get_pokemon_template(&pack, &spec.name, season)
            .unwrap_or_else(|| panic!("template not found: {}", spec.name));
        let mut built = build_from_template(&pack, &tpl, &spec);
        let mut rec = dump(&pack, &built);
        rec["spec"] = json!(spec_str);
        rec["season"] = json!(season);
        rec["parsed"] = json!({
            "name": spec.name, "item": spec.item, "nature": spec.nature,
            "moves": spec.moves, "ability": spec.ability,
            "evs": spec.evs.as_ref().map(|e| json!({"H": e.h, "A": e.a, "B": e.b, "C": e.c, "D": e.d, "S": e.s})),
        });
        rec["mega"] = match &built.mega {
            None => Value::Null,
            Some(m) => json!({
                "mega_name": m.mega_name,
                "mega_stone": m.mega_stone,
                "type1": ty_name(&pack, m.type1),
                "type2": ty_opt(&pack, m.type2),
                "hp": m.hp, "attack": m.attack, "defense": m.defense,
                "sp_attack": m.sp_attack, "sp_defense": m.sp_defense, "speed": m.speed,
                "ability": m.ability, "weight_kg": m.weight_kg,
            }),
        };
        if built.mega.is_some() {
            do_mega_evolve(&pack, &mut built);
            let mut ma = dump(&pack, &built);
            ma.as_object_mut().unwrap().remove("moves");
            ma.as_object_mut().unwrap().remove("pp");
            rec["mega_applied"] = ma;
        } else {
            rec["mega_applied"] = Value::Null;
        }
        out.push(rec);
    }
    std::fs::write(&args[3], serde_json::to_string(&Value::Array(out)).unwrap()).unwrap();
    eprintln!("gate_r0: wrote {}", args[3]);
}
