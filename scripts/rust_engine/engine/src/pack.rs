use crate::interner::{Interner, Sym};
use crate::syms::Syms;
use serde_json::Value;
use std::collections::HashMap;

pub type Ty = u8;
pub const NO_TY: Ty = 255;

#[derive(Clone, Copy, PartialEq, Eq, Debug, Default)]
pub enum Cat {
    Physical,
    Special,
    #[default]
    Status,
}

impl Cat {
    pub fn parse(s: &str) -> Cat {
        match s {
            "physical" => Cat::Physical,
            "special" => Cat::Special,
            _ => Cat::Status,
        }
    }
}

#[derive(Clone, Debug)]
pub struct MoveDef {
    pub name: Sym,
    pub name_jp: String,
    pub name_en: String,
    pub ty: Ty,
    pub category: Cat,
    pub power: Option<i64>,
    pub accuracy: Option<i64>,
    pub priority: i64,
    pub pp: Option<i64>,
    pub effect_id: Option<i64>,
}

#[derive(Clone, Debug)]
pub struct BaseStats {
    pub name: String,
    pub dex: i64,
    pub form_index: Option<i64>,
    pub type1: Ty,
    pub type2: Option<Ty>,
    pub hp: i64,
    pub attack: i64,
    pub defense: i64,
    pub sp_attack: i64,
    pub sp_defense: i64,
    pub speed: i64,
    pub weight_kg: Option<f64>,
}

#[derive(Clone, Debug)]
pub struct MegaStats {
    pub mega_name: String,
    pub base_dex: i64,
    pub mega_stone: String,
    pub type1: Ty,
    pub type2: Option<Ty>,
    pub hp: i64,
    pub attack: i64,
    pub defense: i64,
    pub sp_attack: i64,
    pub sp_defense: i64,
    pub speed: i64,
    pub ability: Option<String>,
    pub weight_kg: Option<f64>,
}

#[derive(Clone, Debug, Default)]
pub struct EvEntry {
    pub h: i64,
    pub a: i64,
    pub b: i64,
    pub c: i64,
    pub d: i64,
    pub s: i64,
    pub spread: String,
    pub rate: f64,
}

#[derive(Clone, Debug, Default)]
pub struct Usage {
    pub moves: Vec<(String, f64)>,
    pub items: Vec<(String, f64)>,
    pub abilities: Vec<(String, f64)>,
    pub natures: Vec<(String, f64)>,
    pub evs: Vec<EvEntry>,
}

/// 技名シンボルごとの静的フラグ（Pythonのリテラル集合をビット化）
#[derive(Clone, Copy, Default)]
pub struct MoveFlags {
    pub ball_bomb: bool,
    pub sound: bool,
    pub punch_set: bool,
    pub punch_substr: bool,
    pub non_contact_physical: bool,
    pub special_contact: bool,
    pub slicing: bool,
    pub bypass_damage_calc: bool,
    pub minimize2x: bool,
    pub secondary: bool,
    pub reckless: bool,
    pub strong_jaw: bool,
    pub mega_launcher: bool,
}


/// タイプID定数（ホットパスの文字列検索を避ける）
#[allow(non_snake_case, uncommon_codepoints, mixed_script_confusables)]
#[derive(Clone, Copy)]
pub struct TyC {
    pub ノーマル: Ty, pub かくとう: Ty, pub ひこう: Ty, pub どく: Ty,
    pub じめん: Ty, pub いわ: Ty, pub むし: Ty, pub ゴースト: Ty,
    pub はがね: Ty, pub ほのお: Ty, pub みず: Ty, pub くさ: Ty,
    pub でんき: Ty, pub エスパー: Ty, pub こおり: Ty, pub ドラゴン: Ty,
    pub あく: Ty, pub フェアリー: Ty,
}

#[allow(uncommon_codepoints)]
impl TyC {
    fn build(idx: &HashMap<&str, Ty>) -> TyC {
        TyC {
            ノーマル: idx["ノーマル"], かくとう: idx["かくとう"], ひこう: idx["ひこう"],
            どく: idx["どく"], じめん: idx["じめん"], いわ: idx["いわ"], むし: idx["むし"],
            ゴースト: idx["ゴースト"], はがね: idx["はがね"], ほのお: idx["ほのお"],
            みず: idx["みず"], くさ: idx["くさ"], でんき: idx["でんき"],
            エスパー: idx["エスパー"], こおり: idx["こおり"], ドラゴン: idx["ドラゴン"],
            あく: idx["あく"], フェアリー: idx["フェアリー"],
        }
    }
}

pub struct Pack {
    pub intern: Interner,
    pub sy: Syms,
    pub types: Vec<String>,
    pub tc: TyC,
    pub chart: [[f64; 18]; 18],
    /// 性格名sym -> (上昇stat, 下降stat)  stat: 0=A 1=B 2=C 3=D 4=S
    pub nature_mods: HashMap<Sym, (u8, u8)>,
    pub form_aliases: HashMap<String, String>,
    pub region_prefixes: Vec<String>,
    pub moves: Vec<MoveDef>,
    pub move_by_name: HashMap<String, usize>,
    pub base_stats: Vec<BaseStats>,
    pub mega_stats: Vec<MegaStats>,
    pub usage: HashMap<String, Usage>,
    pub usage_names_in_moves: std::collections::HashSet<String>,
    pub move_flags: Vec<MoveFlags>,
    /// 道具sym -> (強化タイプ, 倍率)
    pub type_boost: HashMap<Sym, (Ty, f64)>,
    /// 半減きのみ sym -> タイプ
    pub berry_resist: HashMap<Sym, Ty>,
    /// なげつける威力
    pub fling_power: HashMap<Sym, i64>,
    /// スキン特性 sym -> タイプ
    pub skin: HashMap<Sym, Ty>,
    /// R4: 特性 sym -> 効果カテゴリのビット（features.py の ABILITY_CAT_BITS）
    pub abil_cat_bits: HashMap<Sym, u64>,
    pub n_abil_cats: usize,
    /// R4: 登録テンプレートの実スプレッド（belief.registered_spreads_by_species）
    pub registered_spreads: HashMap<String, Vec<(EvEntry, String)>>,
    /// R4: ネット重み
    pub net: Option<crate::net::NetW>,
}

fn j_str(v: &Value) -> Option<String> {
    match v {
        Value::String(s) => Some(s.clone()),
        Value::Null => None,
        _ => None,
    }
}
fn j_i(v: &Value) -> Option<i64> {
    v.as_i64()
}
fn j_f(v: &Value) -> Option<f64> {
    v.as_f64()
}

impl Pack {
    pub fn load(path: &str) -> Pack {
        let txt = std::fs::read_to_string(path).expect("datapack read");
        let v: Value = serde_json::from_str(&txt).expect("datapack parse");
        Pack::from_value(&v)
    }

    pub fn content_hash(v: &Value) -> String {
        v["header"]["content_hash"].as_str().unwrap_or("").to_string()
    }

    pub fn from_value(v: &Value) -> Pack {
        let mut intern = Interner::new();

        // ---- types ----
        let types: Vec<String> = v["types"]
            .as_array()
            .unwrap()
            .iter()
            .map(|x| x.as_str().unwrap().to_string())
            .collect();
        assert_eq!(types.len(), 18);
        let tindex: HashMap<&str, Ty> =
            types.iter().enumerate().map(|(i, s)| (s.as_str(), i as Ty)).collect();
        let mut chart = [[1.0f64; 18]; 18];
        for (atk, row) in v["type_chart"].as_object().unwrap() {
            let ai = tindex[atk.as_str()] as usize;
            for (def, m) in row.as_object().unwrap() {
                let di = tindex[def.as_str()] as usize;
                chart[ai][di] = m.as_f64().unwrap();
            }
        }

        // 全語彙をインターン（タイプ→技→特性→道具→性格→種の順）
        for t in &types {
            intern.intern(t);
        }

        // ---- moves ----
        let mut moves = Vec::new();
        let mut move_by_name = HashMap::new();
        for m in v["move_master"].as_array().unwrap() {
            let name_jp = m["name_jp"].as_str().unwrap().to_string();
            let sym = intern.intern(&name_jp);
            let ty = tindex.get(m["type"].as_str().unwrap_or("")).copied().unwrap_or(NO_TY);
            move_by_name.insert(name_jp.clone(), moves.len());
            moves.push(MoveDef {
                name: sym,
                name_jp,
                name_en: j_str(&m["name_en"]).unwrap_or_default(),
                ty,
                category: Cat::parse(m["category"].as_str().unwrap_or("status")),
                power: j_i(&m["power"]),
                accuracy: j_i(&m["accuracy"]),
                priority: j_i(&m["priority"]).unwrap_or(0),
                pp: j_i(&m["pp"]),
                effect_id: j_i(&m["effect_id"]),
            });
        }

        // ---- base stats ----
        let mut base_stats = Vec::new();
        for b in v["pokemon_base_stats"].as_array().unwrap() {
            let name = b["pokemon_name"].as_str().unwrap().to_string();
            intern.intern(&name);
            base_stats.push(BaseStats {
                name,
                dex: j_i(&b["dex_number"]).unwrap_or(0),
                form_index: j_i(&b["form_index"]),
                type1: tindex.get(b["type1"].as_str().unwrap_or("")).copied().unwrap_or(NO_TY),
                type2: b["type2"].as_str().and_then(|s| tindex.get(s).copied()),
                hp: j_i(&b["hp"]).unwrap_or(0),
                attack: j_i(&b["attack"]).unwrap_or(0),
                defense: j_i(&b["defense"]).unwrap_or(0),
                sp_attack: j_i(&b["sp_attack"]).unwrap_or(0),
                sp_defense: j_i(&b["sp_defense"]).unwrap_or(0),
                speed: j_i(&b["speed"]).unwrap_or(0),
                weight_kg: j_f(&b["weight_kg"]),
            });
        }

        // ---- mega stats ----
        let mut mega_stats = Vec::new();
        for m in v["pokemon_mega_stats"].as_array().unwrap() {
            let mn = m["mega_name_jp"].as_str().unwrap_or("").to_string();
            intern.intern(&mn);
            let st = m["mega_stone"].as_str().unwrap_or("").to_string();
            intern.intern(&st);
            if let Some(a) = m["ability"].as_str() {
                intern.intern(a);
            }
            mega_stats.push(MegaStats {
                mega_name: mn,
                base_dex: j_i(&m["base_dex"]).unwrap_or(0),
                mega_stone: st,
                type1: tindex.get(m["type1"].as_str().unwrap_or("")).copied().unwrap_or(NO_TY),
                type2: m["type2"].as_str().and_then(|s| tindex.get(s).copied()),
                hp: j_i(&m["hp"]).unwrap_or(0),
                attack: j_i(&m["attack"]).unwrap_or(0),
                defense: j_i(&m["defense"]).unwrap_or(0),
                sp_attack: j_i(&m["sp_attack"]).unwrap_or(0),
                sp_defense: j_i(&m["sp_defense"]).unwrap_or(0),
                speed: j_i(&m["speed"]).unwrap_or(0),
                ability: m["ability"].as_str().map(|s| s.to_string()),
                weight_kg: j_f(&m["weight_kg"]),
            });
        }

        // ---- natures ----
        let stat_idx = |s: &str| -> u8 {
            match s {
                "attack" => 0,
                "defense" => 1,
                "sp_attack" => 2,
                "sp_defense" => 3,
                "speed" => 4,
                _ => 255,
            }
        };
        let mut nature_mods = HashMap::new();
        for (k, val) in v["nature_mods"].as_object().unwrap() {
            let sym = intern.intern(k);
            let a = val.as_array().unwrap();
            nature_mods.insert(
                sym,
                (stat_idx(a[0].as_str().unwrap()), stat_idx(a[1].as_str().unwrap())),
            );
        }

        // ---- usage ----
        // usage は選出・提案（MCTS 経路）専用で、spec が型を全て明示する 1v1 では読まない。
        // ブラウザ向けデータパックはここを落として 165KB→38KB に縮める。
        let mut usage = HashMap::new();
        let _empty_usage = serde_json::Map::new();
        for (k, u) in v.get("usage").and_then(|x| x.as_object()).unwrap_or(&_empty_usage) {
            let mut e = Usage::default();
            for x in u["moves"].as_array().unwrap() {
                let n = x[0].as_str().unwrap().to_string();
                intern.intern(&n);
                e.moves.push((n, x[1].as_f64().unwrap_or(0.0)));
            }
            for x in u["items"].as_array().unwrap() {
                let n = x[0].as_str().unwrap().to_string();
                intern.intern(&n);
                e.items.push((n, x[1].as_f64().unwrap_or(0.0)));
            }
            for x in u["abilities"].as_array().unwrap() {
                let n = x[0].as_str().unwrap().to_string();
                intern.intern(&n);
                e.abilities.push((n, x[1].as_f64().unwrap_or(0.0)));
            }
            for x in u["natures"].as_array().unwrap() {
                let n = x[0].as_str().unwrap().to_string();
                intern.intern(&n);
                e.natures.push((n, x[1].as_f64().unwrap_or(0.0)));
            }
            for x in u["evs"].as_array().unwrap() {
                e.evs.push(EvEntry {
                    h: j_i(&x["H"]).unwrap_or(0),
                    a: j_i(&x["A"]).unwrap_or(0),
                    b: j_i(&x["B"]).unwrap_or(0),
                    c: j_i(&x["C"]).unwrap_or(0),
                    d: j_i(&x["D"]).unwrap_or(0),
                    s: j_i(&x["S"]).unwrap_or(0),
                    spread: j_str(&x["spread"]).unwrap_or_default(),
                    rate: j_f(&x["rate"]).unwrap_or(0.0),
                });
            }
            usage.insert(k.clone(), e);
        }

        let usage_names_in_moves = v["usage_names_in_moves"]
            .as_array()
            .unwrap()
            .iter()
            .map(|x| x.as_str().unwrap().to_string())
            .collect();

        let form_aliases: HashMap<String, String> = v["form_aliases"]
            .as_object()
            .unwrap()
            .iter()
            .map(|(k, x)| (k.clone(), x.as_str().unwrap().to_string()))
            .collect();
        let region_prefixes: Vec<String> = v["region_prefixes"]
            .as_array()
            .unwrap()
            .iter()
            .map(|x| x.as_str().unwrap().to_string())
            .collect();

        // ---- コード側リテラルをインターン ----
        let sy = Syms::build(&mut intern);

        // ---- 技フラグ ----
        let n = intern.len();
        let mut move_flags = vec![MoveFlags::default(); n];
        {
            let mark = |mf: &mut Vec<MoveFlags>, it: &Interner, list: &[&str], f: fn(&mut MoveFlags)| {
                for s in list {
                    if let Some(id) = it.get(s) {
                        f(&mut mf[id as usize]);
                    }
                }
            };
            mark(&mut move_flags, &intern, crate::syms::BALL_BOMB_MOVES, |m| m.ball_bomb = true);
            mark(&mut move_flags, &intern, crate::syms::SOUND_MOVES, |m| m.sound = true);
            mark(&mut move_flags, &intern, crate::syms::PUNCH_MOVES, |m| m.punch_set = true);
            mark(&mut move_flags, &intern, crate::syms::NON_CONTACT_PHYSICAL, |m| {
                m.non_contact_physical = true
            });
            mark(&mut move_flags, &intern, crate::syms::SPECIAL_CONTACT_MOVES, |m| {
                m.special_contact = true
            });
            mark(&mut move_flags, &intern, crate::syms::SLICING_MOVES, |m| m.slicing = true);
            mark(&mut move_flags, &intern, crate::syms::BYPASS_DAMAGE_CALC, |m| {
                m.bypass_damage_calc = true
            });
            mark(&mut move_flags, &intern, crate::syms::MINIMIZE_2X, |m| m.minimize2x = true);
            mark(&mut move_flags, &intern, crate::syms::RECKLESS_MOVES, |m| m.reckless = true);
            mark(&mut move_flags, &intern, crate::syms::STRONG_JAW_MOVES, |m| m.strong_jaw = true);
            mark(&mut move_flags, &intern, crate::syms::MEGA_LAUNCHER_MOVES, |m| {
                m.mega_launcher = true
            });
            for s in v["secondary_moves"].as_array().unwrap() {
                if let Some(id) = intern.get(s.as_str().unwrap()) {
                    move_flags[id as usize].secondary = true;
                }
            }
            for i in 0..n {
                if intern.resolve(i as Sym).contains("パンチ") {
                    move_flags[i].punch_substr = true;
                }
            }
        }

        let mut type_boost = HashMap::new();
        for (item, ty, mult) in crate::syms::TYPE_BOOST_ITEMS {
            let id = intern.intern(item);
            type_boost.insert(id, (tindex[ty], *mult));
        }
        let mut berry_resist = HashMap::new();
        for (item, ty) in crate::syms::BERRY_RESIST {
            let id = intern.intern(item);
            berry_resist.insert(id, tindex[ty]);
        }
        let mut fling_power = HashMap::new();
        for (item, p) in crate::syms::FLING_POWER {
            let id = intern.intern(item);
            fling_power.insert(id, *p);
        }
        let mut skin = HashMap::new();
        for (ab, ty) in crate::syms::SKIN_ABILITIES {
            let id = intern.intern(ab);
            skin.insert(id, tindex[ty]);
        }
        // ---- R4 ----
        intern.intern("");
        // ---- R4: 特性効果カテゴリ ----
        let mut abil_cat_bits: HashMap<Sym, u64> = HashMap::new();
        let mut n_abil_cats = 0usize;
        if let Some(ac) = v.get("ability_cats") {
            n_abil_cats = ac["names"].as_array().map(|a| a.len()).unwrap_or(0);
            assert!(n_abil_cats <= 64, "ability cats > 64");
            for (k, bits) in ac["bits"].as_object().unwrap() {
                let id = intern.intern(k);
                let mut m = 0u64;
                for (i, b) in bits.as_array().unwrap().iter().enumerate() {
                    if b.as_i64().unwrap_or(0) != 0 {
                        m |= 1u64 << i;
                    }
                }
                abil_cat_bits.insert(id, m);
            }
        }

        // ---- R4: 登録スプレッド ----
        let mut registered_spreads: HashMap<String, Vec<(EvEntry, String)>> = HashMap::new();
        if let Some(rs) = v.get("registered_spreads") {
            for (sp, arr) in rs.as_object().unwrap() {
                let mut out = Vec::new();
                for it in arr.as_array().unwrap() {
                    let ev = &it[0];
                    let nat = it[1].as_str().unwrap_or("").to_string();
                    intern.intern(&nat);
                    out.push((
                        EvEntry {
                            h: j_i(&ev["H"]).unwrap_or(0),
                            a: j_i(&ev["A"]).unwrap_or(0),
                            b: j_i(&ev["B"]).unwrap_or(0),
                            c: j_i(&ev["C"]).unwrap_or(0),
                            d: j_i(&ev["D"]).unwrap_or(0),
                            s: j_i(&ev["S"]).unwrap_or(0),
                            spread: "登録".to_string(),
                            rate: 0.0,
                        },
                        nat,
                    ));
                }
                registered_spreads.insert(sp.clone(), out);
            }
        }

        let net = v.get("net").and_then(crate::net::NetW::from_value);

        // 後追いinternでflags配列が短くならないよう拡張
        move_flags.resize(intern.len(), MoveFlags::default());

        Pack {
            intern,
            sy,
            tc: TyC::build(&tindex),
            types,
            chart,
            nature_mods,
            form_aliases,
            region_prefixes,
            moves,
            move_by_name,
            base_stats,
            mega_stats,
            usage,
            usage_names_in_moves,
            move_flags,
            type_boost,
            berry_resist,
            fling_power,
            skin,
            abil_cat_bits,
            n_abil_cats,
            registered_spreads,
            net,
        }
    }

    #[inline]
    pub fn ty_of(&self, name: &str) -> Ty {
        self.types.iter().position(|t| t == name).map(|i| i as Ty).unwrap_or(NO_TY)
    }

    #[inline]
    pub fn eff(&self, atk: Ty, d1: Ty, d2: Option<Ty>) -> f64 {
        let e1 = if atk == NO_TY || d1 == NO_TY { 1.0 } else { self.chart[atk as usize][d1 as usize] };
        let e2 = match d2 {
            Some(d) if atk != NO_TY && d != NO_TY => self.chart[atk as usize][d as usize],
            _ => 1.0,
        };
        e1 * e2
    }

    /// ケース再生で未知文字列が来た場合の遅延インターン。
    /// リテラル集合は Pack 構築時に全て登録済みなので、新規文字列のフラグは
    /// パンチ部分一致以外すべて false が正しい。
    pub fn intern_new(&mut self, s: &str) -> Sym {
        let id = self.intern.intern(s);
        if self.move_flags.len() <= id as usize {
            self.move_flags.resize(id as usize + 1, MoveFlags::default());
            self.move_flags[id as usize].punch_substr = s.contains("パンチ");
        }
        id
    }

    #[inline]
    pub fn flags(&self, s: Sym) -> MoveFlags {
        self.move_flags.get(s as usize).copied().unwrap_or_default()
    }
}
