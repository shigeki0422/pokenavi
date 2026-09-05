//! simulator/damage.py の忠実移植。
//! Python の式順・floor 位置・分岐順をそのまま写す（f64 でパリティを取る）。
use crate::interner::Sym;
use crate::pack::{Cat, Pack, Ty};
use crate::poke::{acc_eva_stage, Poke};

#[derive(Clone, Debug, Default, PartialEq)]
pub struct DMove {
    pub name: Sym,
    pub ty: Ty,
    pub category: Cat,
    pub power: Option<i64>,
    pub accuracy: Option<i64>,
    pub priority: i64,
    pub pp: Option<i64>,
}

#[derive(Clone, Debug, Default)]
pub struct Field {
    pub weather: Option<Sym>,
    pub electric_terrain: bool,
    pub psychic_terrain: bool,
    pub misty_terrain: bool,
    pub grassy_terrain: bool,
    pub gravity: i64,
    pub weather_negated: bool,
    // ── BattleField の残りフィールド ──
    pub weather_count: i64,
    pub trick_room: bool,
    pub trick_room_count: i64,
    pub stealth_rock: [bool; 2],
    pub spikes: [i64; 2],
    pub toxic_spikes: [i64; 2],
    pub sticky_web: [bool; 2],
    pub misty_terrain_count: i64,
    pub electric_terrain_count: i64,
    pub psychic_terrain_count: i64,
    pub magic_room: i64,
    pub wonder_room: i64,
    pub grassy_terrain_count: i64,
    /// simulator/damage.py の モジュール変数 _ROLL_OVERRIDE（対戦単位で固定）
    pub roll_override: Option<f64>,
    /// 分析専用。確定数は「必中」を前提に数えるため、Python 側は `_mu_engine` が
    /// check_hit を True に差し替える。Rust は命中判定も `rng() < 命中率` なので
    /// 「追加効果は不発・命中は必ず成功」を単一の乱数値では表現できず、専用の旗が要る。
    /// 対戦本体は常に false（Default）で、挙動は一切変わらない。
    pub always_hit: bool,
}

#[inline]
fn fl(x: f64) -> i64 {
    x.floor() as i64
}

/// effective_weather(field, poke)
#[inline]
pub fn effective_weather(pack: &Pack, field: &Field, poke: Option<&Poke>) -> Option<Sym> {
    if let Some(p) = poke {
        if p.ability == pack.sy.ab.メガソーラー {
            return Some(pack.sy.we.sunny);
        }
    }
    if field.weather_negated {
        return None;
    }
    field.weather
}

/// _effective_move_type
pub fn effective_move_type(pack: &Pack, attacker: &Poke, mv: &DMove, field: &Field) -> Ty {
    let t = mv.ty;
    let ab = attacker.ability;
    let normal = pack.tc.ノーマル;
    if t == normal {
        if let Some(&sk) = pack.skin.get(&ab) {
            return sk;
        }
    }
    if ab == pack.sy.ab.うるおいボイス && pack.flags(mv.name).sound {
        return pack.tc.みず;
    }
    if mv.name == pack.sy.mv.ウェザーボール {
        let w = effective_weather(pack, field, Some(attacker));
        return match w {
            Some(x) if x == pack.sy.we.sunny => pack.tc.ほのお,
            Some(x) if x == pack.sy.we.rain => pack.tc.みず,
            Some(x) if x == pack.sy.we.sandstorm => pack.tc.いわ,
            Some(x) if x == pack.sy.we.hail => pack.tc.こおり,
            _ => normal,
        };
    }
    if mv.name == pack.sy.mv.レイジングブル {
        if let Some(t2) = attacker.type2 {
            return t2;
        }
        let fight = pack.tc.かくとう;
        if attacker.type1 == fight {
            return fight;
        }
        return normal;
    }
    if mv.name == pack.sy.mv.だいちのはどう {
        let flying = pack.tc.ひこう;
        let grounded =
            !(attacker.has_type(flying) || ab == pack.sy.ab.ふゆう || attacker.magnet_rise);
        if grounded {
            if field.grassy_terrain {
                return pack.tc.くさ;
            }
            if field.electric_terrain {
                return pack.tc.でんき;
            }
            if field.psychic_terrain {
                return pack.tc.エスパー;
            }
            if field.misty_terrain {
                return pack.tc.フェアリー;
            }
        }
    }
    t
}

// ── abilities.py のダメージ関連ヘルパ ───────────────────────────────

pub fn should_ignore_ability(pack: &Pack, attacker: &Poke) -> bool {
    let a = attacker.ability;
    a == pack.sy.ab.かたやぶり
        || a == pack.sy.ab.ターボブレイズ
        || a == pack.sy.ab.テラボルテージ
        || a == pack.sy.ab.きんぞくおん
}

pub fn check_move_immunity(pack: &Pack, defender: &Poke, move_type: Ty, move_name: Sym) -> bool {
    let ab = defender.ability;
    let g = defender.grounded;
    let s = &pack.sy;
    let ground = pack.tc.じめん;
    if ab == s.ab.ふゆう && move_type == ground && !g {
        return true;
    }
    if ab == s.ab.うなぎのぼり && move_type == ground && !g {
        return true;
    }
    if defender.magnet_rise && move_type == ground && !g {
        return true;
    }
    let electric = pack.tc.でんき;
    if (ab == s.ab.ちくでん || ab == s.ab.ひらいしん || ab == s.ab.でんきエンジン)
        && move_type == electric
    {
        return true;
    }
    let water = pack.tc.みず;
    if ab == s.ab.ちょすい && move_type == water {
        return true;
    }
    let fire = pack.tc.ほのお;
    if ab == s.ab.もらいび && move_type == fire {
        return true;
    }
    if ab == s.ab.こんがりボディ && move_type == fire {
        return true;
    }
    if ab == s.ab.かんそうはだ && move_type == water {
        return true;
    }
    if ab == s.ab.そうしょく && move_type == pack.tc.くさ {
        return true;
    }
    if ab == s.ab.どしょく && move_type == ground {
        return true;
    }
    if ab == s.ab.ふしぎなまもり {
        return pack.eff(move_type, defender.type1, defender.type2) <= 1.0;
    }
    let f = pack.flags(move_name);
    if ab == s.ab.ぼうだん && f.ball_bomb {
        return true;
    }
    if ab == s.ab.ぼうおん && f.sound {
        return true;
    }
    false
}

pub fn scrappy_override(pack: &Pack, attacker: &Poke, move_type: Ty, defender: &Poke) -> bool {
    if attacker.ability == pack.sy.ab.きもったま {
        let normal = pack.tc.ノーマル;
        let fight = pack.tc.かくとう;
        if (move_type == normal || move_type == fight) && defender.has_type(pack.tc.ゴースト) {
            return true;
        }
    }
    false
}

pub fn get_pinch_multiplier(pack: &Pack, attacker: &Poke, move_type: Ty) -> f64 {
    let ab = attacker.ability;
    let s = &pack.sy.ab;
    let req = if ab == s.もうか || ab == s.もうこ {
        Some(pack.tc.ほのお)
    } else if ab == s.げきりゅう {
        Some(pack.tc.みず)
    } else if ab == s.しんりょく {
        Some(pack.tc.くさ)
    } else if ab == s.むしのしらせ {
        Some(pack.tc.むし)
    } else {
        None
    };
    if let Some(rt) = req {
        if move_type == rt && (attacker.hp as f64) <= (attacker.max_hp as f64) * (1.0 / 3.0) {
            return 1.5;
        }
    }
    1.0
}

pub fn get_sharpness_multiplier(pack: &Pack, attacker: &Poke, move_name: Sym) -> f64 {
    if attacker.ability == pack.sy.ab.きれあじ && pack.flags(move_name).slicing {
        1.5
    } else {
        1.0
    }
}

// ── items.py ────────────────────────────────────────────────────────

pub fn get_type_boost(pack: &Pack, item: Option<Sym>, move_type: Ty, attacker_pika: bool) -> f64 {
    let item = match item {
        Some(i) => i,
        None => return 1.0,
    };
    if item == pack.sy.it.でんきだま
        && move_type == pack.tc.でんき && attacker_pika
    {
        return 2.0;
    }
    if let Some(&(t, m)) = pack.type_boost.get(&item) {
        if t == move_type {
            return m;
        }
    }
    1.0
}

pub fn get_crit_stage_bonus(pack: &Pack, item: Option<Sym>) -> i64 {
    match item {
        Some(i) if i == pack.sy.it.ピントレンズ || i == pack.sy.it.するどいツメ => 1,
        Some(i) if i == pack.sy.it.ラッキーパンチ => 2,
        _ => 0,
    }
}

pub fn get_evasion_item_mult(pack: &Pack, item: Option<Sym>) -> f64 {
    match item {
        Some(i) if i == pack.sy.it.ひかりのこな => 0.90,
        _ => 1.0,
    }
}

pub fn get_accuracy_evasion_item(pack: &Pack, item: Option<Sym>) -> f64 {
    match item {
        Some(i) if i == pack.sy.it.こうかくレンズ => 1.1,
        _ => 1.0,
    }
}

/// on_item_consumed（かるわざ）
fn on_item_consumed(pack: &Pack, poke: &mut Poke) {
    if poke.ability == pack.sy.ab.かるわざ && poke.item.is_none() {
        poke.stage_speed = std::cmp::min(6, poke.stage_speed + 2);
    }
}

// ── 威力 ────────────────────────────────────────────────────────────

fn eff_weight(pack: &Pack, p: &Poke) -> f64 {
    let w = p.weight_kg;
    if p.ability == pack.sy.ab.ヘヴィメタル {
        w * 2.0
    } else if p.ability == pack.sy.ab.ライトメタル {
        w * 0.5
    } else {
        w
    }
}

fn weight_power(kg: f64) -> i64 {
    if kg <= 10.0 {
        20
    } else if kg <= 25.0 {
        40
    } else if kg <= 50.0 {
        60
    } else if kg <= 100.0 {
        80
    } else if kg <= 200.0 {
        100
    } else {
        120
    }
}

fn hp_ratio_power(ratio: f64) -> i64 {
    if ratio > 0.677 {
        20
    } else if ratio > 0.354 {
        40
    } else if ratio > 0.208 {
        80
    } else if ratio > 0.104 {
        100
    } else if ratio > 0.031 {
        150
    } else {
        200
    }
}

pub fn effective_power(
    pack: &Pack,
    attacker: &Poke,
    defender: &Poke,
    mv: &DMove,
    field: &Field,
    eff_type: Ty,
    rng: &mut dyn FnMut(u8) -> f64,
) -> i64 {
    let s = &pack.sy;
    let mut power: i64 = mv.power.unwrap_or(0);
    let n = mv.name;

    if n == s.mv.おはかまいり {
        power = 50 + 50 * std::cmp::min(5, attacker.fainted_allies);
    } else if n == s.mv.ふんどのこぶし {
        power = 50 + 50 * std::cmp::min(6, attacker.times_hit);
    } else if n == s.mv.からげんき {
        power = if attacker.status.is_none() { 70 } else { 140 };
    } else if n == s.mv.スケイルショット {
        power = 25;
    } else if n == s.mv.ダブルキック || n == s.mv.にどげり {
        power = 30;
    } else if n == s.mv.トリプルアクセル {
        power = 20 * (attacker.multi_hit_index + 1);
    } else if n == s.mv.はたきおとす {
        if let Some(it) = defender.item {
            let name = pack.intern.resolve(it);
            let is_mega = name.ends_with("ナイト")
                || name.ends_with("ナイトＸ")
                || name.ends_with("ナイトＹ")
                || name.ends_with("ナイトX")
                || name.ends_with("ナイトY");
            if !is_mega {
                power = fl(power as f64 * 1.5);
            }
        }
    } else if n == s.mv.たたりめ {
        if defender.status.is_some() {
            power *= 2;
        }
    } else if n == s.mv.ひゃっきやこう {
        if defender.status.is_some() {
            power *= 2;
        }
    } else if n == s.mv.ベノムショック {
        if defender.status == Some(s.st.poison) || defender.status == Some(s.st.badpoison) {
            power *= 2;
        }
    } else if n == s.mv.どくばりセンボン {
        if defender.status == Some(s.st.poison) || defender.status == Some(s.st.badpoison) {
            power *= 2;
        }
    } else if n == s.mv.ライジングボルト {
        if field.electric_terrain
            && !(defender.has_type(pack.tc.ひこう) || defender.ability == s.ab.ふゆう)
        {
            power *= 2;
        }
    } else if n == s.mv.しっぺがえし {
        if attacker.acts_second {
            power *= 2;
        }
    } else if n == s.mv.アクロバット {
        if attacker.item.is_none() {
            power *= 2;
        }
    } else if n == s.mv.きまぐレーザー {
        let r = rng(0);
        if r < 0.30 {
            power *= 2;
        }
    } else if n == s.mv.Gのちから {
        if field.gravity > 0 {
            power = fl(power as f64 * 1.5);
        }
    } else if n == s.mv.ミストバースト {
        let grounded = !(attacker.has_type(pack.tc.ひこう)
            || attacker.ability == s.ab.ふゆう
            || attacker.magnet_rise);
        if field.misty_terrain && grounded {
            power = fl(power as f64 * 1.5);
        }
    } else if n == s.mv.ウェザーボール {
        power = if effective_weather(pack, field, Some(attacker)).is_some() { 100 } else { 50 };
    } else if n == s.mv.くさむすび || n == s.mv.けたぐり {
        power = weight_power(eff_weight(pack, defender));
    } else if n == s.mv.しおふき || n == s.mv.ふんか {
        power = std::cmp::max(
            1,
            fl(150.0 * (attacker.hp as f64) / (attacker.max_hp as f64)),
        );
    } else if n == s.mv.アシストパワー || n == s.mv.つけあがる {
        let rank_sum: i64 = [
            attacker.stage_attack,
            attacker.stage_defense,
            attacker.stage_sp_attack,
            attacker.stage_sp_defense,
            attacker.stage_speed,
        ]
        .iter()
        .map(|&x| std::cmp::max(0, x) as i64)
        .sum();
        power = 20 + 20 * rank_sum;
    } else if n == s.mv.ダメおし {
        if attacker.acts_second {
            power *= 2;
        }
    } else if n == s.mv.きしかいせい {
        let ratio = if attacker.max_hp > 0 {
            (attacker.hp as f64) / (attacker.max_hp as f64)
        } else {
            1.0
        };
        power = hp_ratio_power(ratio);
    } else if n == s.mv.ジャイロボール {
        let atk_spd = std::cmp::max(1, attacker.eff_speed(pack));
        let def_spd = std::cmp::max(1, defender.eff_speed(pack));
        power = std::cmp::min(
            150,
            std::cmp::max(1, fl(25.0 * (def_spd as f64) / (atk_spd as f64))),
        );
    } else if n == s.mv.ヒートスタンプ || n == s.mv.ヘビーボンバー {
        let w_atk = eff_weight(pack, attacker);
        let w_def = eff_weight(pack, defender);
        let ratio_w = w_atk / f64::max(0.1, w_def);
        power = if ratio_w >= 5.0 {
            120
        } else if ratio_w >= 4.0 {
            100
        } else if ratio_w >= 3.0 {
            80
        } else if ratio_w >= 2.0 {
            60
        } else {
            40
        };
    } else if n == s.mv.じたばた {
        let ratio = if attacker.max_hp > 0 {
            (attacker.hp as f64) / (attacker.max_hp as f64)
        } else {
            1.0
        };
        power = hp_ratio_power(ratio);
    } else if n == s.mv.ハードプレス {
        let ratio = if defender.max_hp > 0 {
            (defender.hp as f64) / (defender.max_hp as f64)
        } else {
            1.0
        };
        power = std::cmp::max(1, fl(100.0 * ratio));
    } else if n == s.mv.エレキボール {
        let atk_spd = std::cmp::max(1, attacker.speed);
        let def_spd = std::cmp::max(1, defender.speed);
        let ratio_s = (atk_spd as f64) / (def_spd as f64);
        power = if ratio_s >= 4.0 {
            150
        } else if ratio_s >= 3.0 {
            120
        } else if ratio_s >= 2.0 {
            80
        } else if ratio_s >= 1.0 {
            60
        } else {
            40
        };
    } else if n == s.mv.なげつける {
        let flung = attacker.last_flung_item.or(attacker.item);
        power = match flung {
            Some(f) => pack.fling_power.get(&f).copied().unwrap_or(10),
            None => 0,
        };
    }

    if mv.power.is_none() && power == 0 && !pack.flags(n).bypass_damage_calc {
        panic!("可変威力技 '{}' の威力計算が未実装", pack.intern.resolve(n));
    }

    if n == s.mv.ソーラービーム || n == s.mv.ソーラーブレード {
        if let Some(w) = effective_weather(pack, field, Some(attacker)) {
            if w == s.we.rain || w == s.we.hail || w == s.we.sandstorm {
                power = power.div_euclid(2);
            }
        }
    }

    if eff_type == pack.tc.じめん
        && defender.has_type(pack.tc.ひこう)
        && !defender.grounded
    {
        return 0;
    }

    if effective_weather(pack, field, Some(attacker)) == Some(s.we.sandstorm)
        && attacker.ability == s.ab.すなのちから
    {
        if eff_type == pack.tc.いわ
            || eff_type == pack.tc.じめん
            || eff_type == pack.tc.はがね
        {
            power = fl(power as f64 * 1.3);
        }
    }

    if n == s.mv.だいちのはどう {
        let grounded = !(attacker.has_type(pack.tc.ひこう)
            || attacker.ability == s.ab.ふゆう
            || attacker.magnet_rise);
        if grounded
            && (field.grassy_terrain
                || field.electric_terrain
                || field.psychic_terrain
                || field.misty_terrain)
        {
            power *= 2;
        }
    }

    if (n == s.mv.じだんだ || n == s.mv.やけっぱち) && attacker.move_failed_last {
        power *= 2;
    }

    if (n == s.mv.ゆきなだれ || n == s.mv.リベンジ) && attacker.took_damage_this_turn {
        power *= 2;
    }

    if n == s.mv.うっぷんばらし {
        let any_down = attacker.stage_attack < 0
            || attacker.stage_defense < 0
            || attacker.stage_sp_attack < 0
            || attacker.stage_sp_defense < 0
            || attacker.stage_speed < 0
            || attacker.stage_accuracy < 0
            || attacker.stage_evasion < 0;
        if any_down {
            power *= 2;
        }
    }

    if pack.flags(n).minimize2x && defender.minimized {
        power *= 2;
    }

    if let Some(dc) = defender.charging_move {
        if dc == s.mv.ダイビング && (n == s.mv.なみのり || n == s.mv.うずしお) {
            power *= 2;
        } else if dc == s.mv.あなをほる && (n == s.mv.じしん || n == s.mv.マグニチュード) {
            power *= 2;
        }
    }

    power
}

// ── 補正ヘルパ ──────────────────────────────────────────────────────

fn apply_attacker_item(pack: &Pack, dmg: i64, attacker: &Poke, mv: &DMove, eff: f64) -> i64 {
    let it = attacker.item;
    let s = &pack.sy.it;
    let d = dmg as f64;
    match it {
        Some(i) if i == s.いのちのたま => fl(d * 1.3),
        Some(i) if i == s.こだわりハチマキ && mv.category == Cat::Physical => fl(d * 1.5),
        Some(i) if i == s.こだわりメガネ && mv.category == Cat::Special => fl(d * 1.5),
        Some(i) if i == s.ちからのハチマキ && mv.category == Cat::Physical => fl(d * 1.1),
        Some(i) if i == s.ものしりメガネ && mv.category == Cat::Special => fl(d * 1.1),
        Some(i) if i == s.たつじんのおび && eff > 1.0 => fl(d * 1.2),
        _ => dmg,
    }
}

fn apply_defender_item(pack: &Pack, dmg: i64, defender: &mut Poke, mv: &DMove, eff: f64) -> i64 {
    let item = match defender.item {
        Some(i) => i,
        None => return dmg,
    };
    let mut dmg = dmg;
    if item == pack.sy.it.ホズのみ && mv.ty == pack.tc.ノーマル && eff > 0.0 {
        dmg = fl(dmg as f64 * 0.5);
        defender.item = None;
        on_item_consumed(pack, defender);
    } else if let Some(&bt) = pack.berry_resist.get(&item) {
        if eff >= 2.0 && mv.ty == bt {
            dmg = fl(dmg as f64 * 0.5);
            defender.item = None;
            on_item_consumed(pack, defender);
        }
    }
    dmg
}

fn apply_attacker_ability(
    pack: &Pack,
    dmg: i64,
    attacker: &Poke,
    defender: &Poke,
    mv: &DMove,
    field: &Field,
) -> i64 {
    let ab = attacker.ability;
    let s = &pack.sy;
    let f = pack.flags(mv.name);
    let d = dmg as f64;
    if ab == s.ab.ちからずく && mv.category != Cat::Status && f.secondary {
        fl(d * 1.3)
    } else if (ab == s.ab.かたいツメ || ab == s.ab.かたいつめ)
        && mv.category == Cat::Physical
        && !f.non_contact_physical
    {
        fl(d * 1.3)
    } else if ab == s.ab.てつのこぶし && (f.punch_substr || f.punch_set) {
        fl(d * 1.2)
    } else if ab == s.ab.テクニシャン && mv.power.map(|p| p <= 60).unwrap_or(false) {
        fl(d * 1.5)
    } else if ab == s.ab.ねつぼうそう
        && mv.category == Cat::Special
        && attacker.status == Some(s.st.burn)
    {
        fl(d * 1.5)
    } else if ab == s.ab.すてみ && f.reckless {
        fl(d * 1.2)
    } else if ab == s.ab.がんじょうあご && f.strong_jaw {
        fl(d * 1.5)
    } else if ab == s.ab.メガランチャー && f.mega_launcher {
        fl(d * 1.5)
    } else if ab == s.ab.すいほう && mv.ty == pack.tc.みず {
        fl(d * 2.0)
    } else if ab == s.ab.アナライズ && attacker.acts_second {
        fl(d * 1.3)
    } else if ab == s.ab.サンパワー
        && mv.category == Cat::Special
        && effective_weather(pack, field, Some(attacker)) == Some(s.we.sunny)
    {
        fl(d * 1.5)
    } else if ab == s.ab.はりこみ && defender.switched_this_turn {
        fl(d * 2.0)
    } else if ab == s.ab.はがねのせいしん && mv.ty == pack.tc.はがね {
        fl(d * 1.5)
    } else if ab == s.ab.そうだいしょう {
        let boost = 1.0 + 0.1 * (std::cmp::min(5, attacker.fainted_allies) as f64);
        fl(d * boost)
    } else {
        dmg
    }
}

fn apply_defender_ability(pack: &Pack, dmg: i64, defender: &Poke, mv: &DMove) -> i64 {
    let ab = defender.ability;
    let s = &pack.sy.ab;
    let d = dmg as f64;
    let fire = pack.tc.ほのお;
    if ab == s.マルチスケイル && defender.hp == defender.max_hp {
        fl(d * 0.5)
    } else if ab == s.ファーコート && mv.category == Cat::Physical {
        fl(d * 0.5)
    } else if ab == s.あついしぼう && (mv.ty == fire || mv.ty == pack.tc.こおり) {
        fl(d * 0.5)
    } else if ab == s.かんそうはだ && mv.ty == fire {
        fl(d * 1.25)
    } else if (ab == s.たいねつ || ab == s.すいほう) && mv.ty == fire {
        fl(d * 0.5)
    } else if ab == s.きよめのしお && mv.ty == pack.tc.ゴースト {
        fl(d * 0.5)
    } else if ab == s.もふもふ {
        let mut x = dmg;
        if mv.category == Cat::Physical {
            x = fl(x as f64 * 0.5);
        }
        if mv.ty == fire {
            x = fl(x as f64 * 2.0);
        }
        x
    } else if ab == s.フィルター || ab == s.ハードロック || ab == s.プリズムアーマー {
        let e = pack.eff(mv.ty, defender.type1, defender.type2);
        if e > 1.0 {
            fl(d * 0.75)
        } else {
            dmg
        }
    } else {
        dmg
    }
}

// ── 本体 ────────────────────────────────────────────────────────────

pub fn calc_damage(
    pack: &Pack,
    attacker: &mut Poke,
    defender: &mut Poke,
    mv: &DMove,
    field: &mut Field,
    critical: bool,
    random_roll: Option<f64>,
    roll_override: Option<f64>,
    rng: &mut dyn FnMut(u8) -> f64,
) -> i64 {
    let s = &pack.sy;
    if mv.category == Cat::Status {
        return 0;
    }
    field.weather_negated =
        attacker.ability == s.ab.ノーてんき || defender.ability == s.ab.ノーてんき;

    let level = 50i64;
    let eff_type = effective_move_type(pack, attacker, mv, field);
    let power = effective_power(pack, attacker, defender, mv, field, eff_type, rng);
    if power == 0 {
        return 0;
    }

    let ignore_ab = should_ignore_ability(pack, attacker);
    if !ignore_ab && check_move_immunity(pack, defender, eff_type, mv.name) {
        if !scrappy_override(pack, attacker, eff_type, defender) {
            return 0;
        }
    }

    let atk_ignores_def_stage = !ignore_ab && attacker.ability == s.ab.てんねん;
    let def_ignores_atk_stage = !ignore_ab && defender.ability == s.ab.てんねん;

    let mut cat = mv.category;
    if mv.name == s.mv.シェルアームズ {
        let phys = (attacker.eff_stat(0) as f64) / (std::cmp::max(1, defender.eff_stat(1)) as f64);
        let spec = (attacker.eff_stat(2) as f64) / (std::cmp::max(1, defender.eff_stat(3)) as f64);
        cat = if phys > spec { Cat::Physical } else { Cat::Special };
    }

    let mut atk: i64;
    let mut dfs: i64;
    if cat == Cat::Physical {
        atk = if def_ignores_atk_stage {
            attacker.attack
        } else if critical {
            std::cmp::max(attacker.eff_stat(0), attacker.attack)
        } else {
            attacker.eff_stat(0)
        };
        dfs = if atk_ignores_def_stage {
            defender.defense
        } else if critical {
            std::cmp::min(defender.eff_stat(1), defender.defense)
        } else {
            defender.eff_stat(1)
        };
    } else {
        atk = if def_ignores_atk_stage {
            attacker.sp_attack
        } else if critical {
            std::cmp::max(attacker.eff_stat(2), attacker.sp_attack)
        } else {
            attacker.eff_stat(2)
        };
        dfs = if atk_ignores_def_stage {
            defender.sp_defense
        } else if critical {
            std::cmp::min(defender.eff_stat(3), defender.sp_defense)
        } else {
            defender.eff_stat(3)
        };
    }

    if mv.name == s.mv.ボディプレス {
        atk = if !critical {
            attacker.eff_stat(1)
        } else {
            std::cmp::max(attacker.eff_stat(1), attacker.defense)
        };
    }
    if mv.name == s.mv.イカサマ {
        atk = if !critical {
            defender.eff_stat(0)
        } else {
            std::cmp::max(defender.eff_stat(0), defender.attack)
        };
    }
    let psy_b = mv.name == s.mv.サイコショック
        || mv.name == s.mv.サイコブレイク
        || mv.name == s.mv.シークレットソード;
    if psy_b {
        dfs = if !critical {
            defender.eff_stat(1)
        } else {
            std::cmp::min(defender.eff_stat(1), defender.defense)
        };
    }
    let sacred = mv.name == s.mv.せいなるつるぎ || mv.name == s.mv.DDラリアット;
    if sacred {
        dfs = if !critical {
            defender.defense
        } else {
            std::cmp::min(defender.eff_stat(1), defender.defense)
        };
    }

    let uses_defense = cat == Cat::Physical || psy_b || sacred;
    let def_weather = effective_weather(pack, field, Some(defender));
    if uses_defense
        && def_weather == Some(s.we.hail)
        && defender.has_type(pack.tc.こおり)
    {
        dfs = fl(dfs as f64 * 1.5);
    }
    if !uses_defense
        && def_weather == Some(s.we.sandstorm)
        && defender.has_type(pack.tc.いわ)
    {
        dfs = fl(dfs as f64 * 1.5);
    }

    if defender.ability == s.ab.ふしぎなうろこ && defender.status.is_some() && uses_defense {
        dfs = fl(dfs as f64 * 1.5);
    }

    if mv.category == Cat::Physical
        && (attacker.ability == s.ab.ちからもち || attacker.ability == s.ab.ヨガパワー)
    {
        atk *= 2;
    }
    if mv.category == Cat::Physical
        && attacker.ability == s.ab.こんじょう
        && attacker.status.is_some()
    {
        atk = fl(atk as f64 * 1.5);
    }
    if attacker.status == Some(s.st.burn) && mv.category == Cat::Physical {
        if attacker.ability != s.ab.こんじょう && mv.name != s.mv.からげんき {
            atk = fl(atk as f64 * 0.5);
        }
    }

    let a0 = ((2 * level) as f64 / 5.0 + 2.0).floor() as i64;
    let inner = ((a0 * power * atk) as f64 / dfs as f64).floor();
    let mut dmg = (inner / 50.0).floor() as i64 + 2;

    if critical {
        dmg = fl(dmg as f64 * if attacker.ability == s.ab.スナイパー { 2.25 } else { 1.5 });
    }

    let eff_weather = effective_weather(pack, field, Some(attacker));
    if eff_weather == Some(s.we.sunny) {
        if eff_type == pack.tc.ほのお {
            dmg = fl(dmg as f64 * 1.5);
        } else if eff_type == pack.tc.みず {
            dmg = fl(dmg as f64 * 0.5);
        }
    } else if eff_weather == Some(s.we.rain) {
        if eff_type == pack.tc.みず {
            dmg = fl(dmg as f64 * 1.5);
        } else if eff_type == pack.tc.ほのお {
            dmg = fl(dmg as f64 * 0.5);
        }
    }

    if attacker.charged && eff_type == pack.tc.でんき {
        dmg = fl(dmg as f64 * 2.0);
        attacker.charged = false;
    }

    let grounded =
        !(attacker.has_type(pack.tc.ひこう) || attacker.ability == s.ab.ふゆう);
    if grounded {
        if field.electric_terrain && eff_type == pack.tc.でんき {
            dmg = fl(dmg as f64 * 1.3);
        } else if field.psychic_terrain && eff_type == pack.tc.エスパー {
            dmg = fl(dmg as f64 * 1.3);
        } else if field.misty_terrain && eff_type == pack.tc.ドラゴン {
            dmg = fl(dmg as f64 * 0.5);
        } else if field.grassy_terrain && eff_type == pack.tc.くさ {
            dmg = fl(dmg as f64 * 1.3);
        }
    }
    if field.grassy_terrain
        && (mv.name == s.mv.じしん || mv.name == s.mv.じならし || mv.name == s.mv.マグニチュード)
    {
        dmg = fl(dmg as f64 * 0.5);
    }

    let rr = random_roll.or(roll_override);
    let roll = match rr {
        None => (85.0 + rng(1)) / 100.0,
        Some(r) => 0.85 + r * 0.15,
    };
    dmg = fl(dmg as f64 * roll);

    let stab_type = eff_type;
    if attacker.has_type(stab_type) {
        if attacker.ability == s.ab.てきおうりょく {
            dmg = fl(dmg as f64 * 2.0);
        } else {
            dmg = fl(dmg as f64 * 1.5);
        }
    }
    if mv.ty == pack.tc.ノーマル && pack.skin.contains_key(&attacker.ability) {
        dmg = fl(dmg as f64 * 1.2);
    }
    if eff_type == pack.tc.フェアリー
        && (attacker.ability == s.ab.フェアリーオーラ || defender.ability == s.ab.フェアリーオーラ)
    {
        dmg = fl(dmg as f64 * 1.33);
    }

    let mut effectiveness = pack.eff(eff_type, defender.type1, defender.type2);
    if mv.name == s.mv.フライングプレス && effectiveness != 0.0 {
        effectiveness *= pack.eff(pack.tc.ひこう, defender.type1, defender.type2);
    }
    if eff_type == pack.tc.じめん
        && defender.grounded
        && defender.has_type(pack.tc.ひこう)
    {
        effectiveness = 1.0;
        let flying = pack.tc.ひこう;
        for t in [Some(defender.type1), defender.type2] {
            if let Some(t) = t {
                if t != flying {
                    effectiveness *= pack.eff(eff_type, t, None);
                }
            }
        }
    }
    if effectiveness == 0.0 && scrappy_override(pack, attacker, eff_type, defender) {
        effectiveness = 1.0;
    }
    if mv.name == s.mv.フリーズドライ && defender.has_type(pack.tc.みず) {
        effectiveness = f64::max(effectiveness, 2.0);
    }
    dmg = fl(dmg as f64 * effectiveness);
    if dmg == 0 {
        return 0;
    }

    if attacker.ability != s.ab.ぶきよう {
        dmg = apply_attacker_item(pack, dmg, attacker, mv, effectiveness);
    }
    if defender.ability != s.ab.ぶきよう {
        dmg = apply_defender_item(pack, dmg, defender, mv, effectiveness);
    }
    dmg = apply_attacker_ability(pack, dmg, attacker, defender, mv, field);
    if !ignore_ab {
        dmg = apply_defender_ability(pack, dmg, defender, mv);
    }

    let pinch = get_pinch_multiplier(pack, attacker, mv.ty);
    if pinch > 1.0 {
        dmg = fl(dmg as f64 * pinch);
    }
    let sharp = get_sharpness_multiplier(pack, attacker, mv.name);
    if sharp > 1.0 {
        dmg = fl(dmg as f64 * sharp);
    }
    let type_boost = if attacker.ability != s.ab.ぶきよう {
        get_type_boost(pack, attacker.item, mv.ty, attacker.name_pika)
    } else {
        1.0
    };
    if type_boost > 1.0 {
        dmg = fl(dmg as f64 * type_boost);
    }
    if eff_type == pack.tc.ほのお && attacker.flash_fire_active {
        dmg = fl(dmg as f64 * 1.5);
    }
    if eff_type == pack.tc.ほのお && attacker.ability == s.ab.ほのおのたてがみ {
        dmg = fl(dmg as f64 * 1.5);
    }
    if eff_type == pack.tc.でんき && attacker.electromorphosis_charged {
        dmg = fl(dmg as f64 * 1.5);
        attacker.electromorphosis_charged = false;
    }

    if effectiveness > 0.0 {
        std::cmp::max(1, dmg)
    } else {
        0
    }
}

// ── check_hit（RNGは呼び出し側から注入。R3でCPython MTに接続）───────

pub fn check_hit(
    pack: &Pack,
    attacker: &Poke,
    defender: &Poke,
    mv: &DMove,
    field: &mut Field,
    rng: &mut dyn FnMut() -> f64,
) -> bool {
    let s = &pack.sy;
    field.weather_negated =
        attacker.ability == s.ab.ノーてんき || defender.ability == s.ab.ノーてんき;
    // `_mu_engine._enter_fixed` の `check_hit = lambda *a, **k: True` と同じ位置づけ。
    // weather_negated の副作用だけは対戦本体と揃える必要があるため、その後に返す。
    if field.always_hit {
        return true;
    }
    let acc = match mv.accuracy {
        None => return true,
        Some(a) => a,
    };
    if attacker.lock_on {
        return true;
    }
    if attacker.ability == s.ab.ノーガード || defender.ability == s.ab.ノーガード {
        return true;
    }
    if mv.name == s.mv.どくどく && attacker.has_type(pack.tc.どく) {
        return true;
    }
    if mv.name == s.mv.なみだめ {
        return true;
    }
    const POWDER: [&str; 6] =
        ["しびれごな", "ねむりごな", "どくのこな", "キノコのほうし", "わたほうし", "ちょうのこな"];
    let nm = pack.intern.resolve(mv.name);
    if POWDER.contains(&nm) && defender.has_type(pack.tc.くさ) {
        return false;
    }
    if mv.name == s.mv.ぜったいれいど {
        let a = if attacker.has_type(pack.tc.こおり) { 0.30 } else { 0.20 };
        return rng() < a;
    }
    let w_atk = effective_weather(pack, field, Some(attacker));
    if w_atk == Some(s.we.rain) && (mv.name == s.mv.かみなり || mv.name == s.mv.ぼうふう) {
        return true;
    }
    if w_atk == Some(s.we.sunny) && (mv.name == s.mv.かみなり || mv.name == s.mv.ぼうふう) {
        return rng() < 0.5;
    }
    if w_atk == Some(s.we.hail) && mv.name == s.mv.ふぶき {
        return true;
    }
    let w_def = effective_weather(pack, field, Some(defender));
    if w_def == Some(s.we.sandstorm) && defender.ability == s.ab.すながくれ {
        let mut hit_rate = (acc as f64) / 100.0 * 0.8;
        let acc_stage = attacker.stage_accuracy - defender.stage_evasion;
        hit_rate *= acc_eva_stage(acc_stage);
        hit_rate *= get_evasion_item_mult(pack, defender.item);
        if defender.protecting
            && mv.name != s.mv.フェイント
            && mv.name != s.mv.ゴーストダイブ
        {
            return false;
        }
        return rng() < hit_rate;
    }
    let eva = if attacker.ability == s.ab.するどいめ || attacker.ability == s.ab.はっこう {
        0
    } else {
        defender.stage_evasion
    };
    let acc_stage = attacker.stage_accuracy - eva;
    let mut hit_rate = (acc as f64) * acc_eva_stage(acc_stage) / 100.0;
    if attacker.ability == s.ab.ふくがん {
        hit_rate *= 1.3;
    }
    if w_def == Some(s.we.hail) && defender.ability == s.ab.ゆきがくれ {
        hit_rate *= 0.8;
    }
    if defender.confused && defender.ability == s.ab.ちどりあし {
        hit_rate *= 0.5;
    }
    if attacker.ability == s.ab.はりきり && mv.category == Cat::Physical {
        hit_rate *= 0.8;
    }
    hit_rate *= get_evasion_item_mult(pack, defender.item);
    hit_rate *= get_accuracy_evasion_item(pack, attacker.item);
    if defender.protecting && mv.name != s.mv.フェイント && mv.name != s.mv.ゴーストダイブ {
        return false;
    }
    rng() < hit_rate
}

/// is_contact_move（simulator/damage.py:450）
#[inline]
pub fn is_contact_move(pack: &Pack, mv: &DMove) -> bool {
    let f = pack.flags(mv.name);
    if f.special_contact {
        return true;
    }
    if mv.category != Cat::Physical {
        return false;
    }
    !f.non_contact_physical
}
