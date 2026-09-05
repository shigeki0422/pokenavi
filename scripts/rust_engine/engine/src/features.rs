//! simulator/features.py の移植（encode_state = 905次元）。
//! Python の式順・sum の左→右順・min/max の適用順をそのまま写す。
use crate::battle::Side;
use crate::damage::{calc_damage, DMove, Field};
use crate::interner::Sym;
use crate::pack::{Cat, Pack, Ty, NO_TY};
use crate::poke::Poke;
use crate::rng::BRng;
use std::collections::HashMap;

pub const N_TYPES: usize = 18;
pub const N_ITEM_FLAGS: usize = 8;

/// features.py の TYPES 並び（pack.types とは別順序でありうるので明示マップ）
pub const FEAT_TYPES: [&str; N_TYPES] = [
    "ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん",
    "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー",
];

const ITEM_FLAGS: [&[&str]; N_ITEM_FLAGS] = [
    &["きあいのタスキ"],
    &["たべのこし"],
    &["オボンのみ"],
    &["ラムのみ", "カゴのみ"],
    &["シュカのみ", "ハバンのみ", "ソクノのみ", "ヨロギのみ"],
    &[
        "しんぴのしずく", "じしゃく", "とけないこおり", "りゅうのキバ", "やわらかいすな",
        "するどいくちばし", "くろいメガネ", "まがったスプーン", "ようせいのハネ",
        "メタルコート", "のろいのおふだ",
    ],
    &["こだわりスカーフ"],
    &["ひかりのこな"],
];

const M_SETUP: &[&str] = &[
    "つるぎのまい", "りゅうのまい", "ちょうのまい", "めいそう", "わるだくみ", "からをやぶる",
    "てっぺき", "ビルドアップ", "とぐろをまく", "こうそくいどう", "ロックカット", "アシッドボム",
    "はらだいこ", "めざましビンタ", "つめとぎ", "コットンガード", "とける",
];
const M_RECOVER: &[&str] = &[
    "はねやすめ", "じこさいせい", "なまける", "つきのひかり", "あさのひざし", "こうごうせい",
    "タマゴうみ", "ねむる", "じこあんじ", "ミルクのみ", "なかまづくり", "いのちがけ",
];
const M_HAZARD: &[&str] = &["ステルスロック", "まきびし", "どくびし", "ねばねばネット"];
const M_PHAZE: &[&str] = &["ドラゴンテール", "ともえなげ", "ほえる", "ふきとばし"];
const M_PIVOT: &[&str] = &["とんぼがえり", "ボルトチェンジ", "クイックターン"];
const M_PROTECT: &[&str] =
    &["まもる", "みきり", "キングシールド", "トーチカ", "ニードルガード", "スレッドトラップ", "がまん"];
const M_TWOTURN: &[&str] = &[
    "ソーラービーム", "ソーラーブレード", "とびはねる", "あなをほる", "ダイビング", "そらをとぶ",
    "ロケットずつき", "はかいこうせん", "ギガインパクト", "メテオビーム", "ジオコントロール",
];
const M_TRAP: &[&str] = &[
    "バインド", "まきつく", "しめつける", "かなしばり", "くろいまなざし", "ほのおのうず",
    "うずしお", "すなじごく", "マグマストーム", "とおせんぼう", "ありじごく",
];
const M_STATUS: &[&str] = &[
    "でんじは", "おにび", "どくどく", "どくのこな", "しびれごな", "ねむりごな", "キノコのほうし",
    "さいみんじゅつ", "へびにらみ", "あくび", "ちょうおんぱ", "どくガス", "やどりぎのタネ", "あまえる",
];

const MULTI_HIT_2: &[&str] = &[
    "ダブルキック", "にどげり", "ダブルウイング", "ドラゴンアロー", "スパークリングアリア",
    "ダブルパンツァー", "ツインビーム", "ダブルアタック",
];
const MULTI_HIT_25: &[&str] = &[
    "スケイルショット", "みずしゅりけん", "ロックブラスト", "タネマシンガン", "つららばり",
    "ミサイルばり", "ボーンラッシュ", "あわ", "スイープビンタ",
];

/// 技sym → 能力フラグ（bit0=setup .. bit8=trap, bit9=status）＋連続技フラグ
pub const F_SETUP: u16 = 1;
pub const F_RECOVER: u16 = 1 << 1;
pub const F_HAZARD: u16 = 1 << 2;
pub const F_PHAZE: u16 = 1 << 3;
pub const F_PIVOT: u16 = 1 << 4;
pub const F_PROTECT: u16 = 1 << 5;
pub const F_TWOTURN: u16 = 1 << 6;
pub const F_TRAP: u16 = 1 << 7;
pub const F_STATUS: u16 = 1 << 8;
pub const F_MH2: u16 = 1 << 9;
pub const F_MH3: u16 = 1 << 10;
pub const F_MH25: u16 = 1 << 11;

pub struct FeatTables {
    /// pack の Ty → features.py の TYPES index（無ければ usize::MAX）
    pub ty2fi: [usize; 256],
    /// 道具 sym → 8bit
    pub item_bits: HashMap<Sym, u8>,
    /// 技 sym → フラグ
    pub move_bits: HashMap<Sym, u16>,
    pub kmg: Option<Sym>,
    pub skill_link: Option<Sym>,
    pub bukiyou: Option<Sym>,
    pub scarf: Option<Sym>,
    pub iron_ball: Option<Sym>,
    pub sunakaki: Option<Sym>,
    pub youryokuso: Option<Sym>,
    pub suisui: Option<Sym>,
    pub yukikaki: Option<Sym>,
    pub berry_suffix: Vec<Sym>,
    pub n_cats: usize,
}

fn syms_of(pack: &Pack, list: &[&str]) -> Vec<Sym> {
    list.iter().filter_map(|s| pack.intern.get(s)).collect()
}

impl FeatTables {
    pub fn build(pack: &Pack) -> FeatTables {
        let mut ty2fi = [usize::MAX; 256];
        for (fi, name) in FEAT_TYPES.iter().enumerate() {
            let t = pack.ty_of(name);
            assert!(t != NO_TY, "type {} not in pack", name);
            ty2fi[t as usize] = fi;
        }
        let mut item_bits: HashMap<Sym, u8> = HashMap::new();
        for (bi, grp) in ITEM_FLAGS.iter().enumerate() {
            for s in grp.iter() {
                if let Some(id) = pack.intern.get(s) {
                    *item_bits.entry(id).or_insert(0) |= 1u8 << bi;
                }
            }
        }
        let mut move_bits: HashMap<Sym, u16> = HashMap::new();
        let mut mark = |list: &[&str], f: u16, mb: &mut HashMap<Sym, u16>| {
            for s in list.iter() {
                if let Some(id) = pack.intern.get(s) {
                    *mb.entry(id).or_insert(0) |= f;
                }
            }
        };
        mark(M_SETUP, F_SETUP, &mut move_bits);
        mark(M_RECOVER, F_RECOVER, &mut move_bits);
        mark(M_HAZARD, F_HAZARD, &mut move_bits);
        mark(M_PHAZE, F_PHAZE, &mut move_bits);
        mark(M_PIVOT, F_PIVOT, &mut move_bits);
        mark(M_PROTECT, F_PROTECT, &mut move_bits);
        mark(M_TWOTURN, F_TWOTURN, &mut move_bits);
        mark(M_TRAP, F_TRAP, &mut move_bits);
        mark(M_STATUS, F_STATUS, &mut move_bits);
        mark(MULTI_HIT_2, F_MH2, &mut move_bits);
        mark(&["トリプルアクセル"], F_MH3, &mut move_bits);
        mark(MULTI_HIT_25, F_MH25, &mut move_bits);
        let berry_suffix = (0..pack.intern.len() as u32)
            .filter(|&i| pack.intern.resolve(i as Sym).ends_with("のみ"))
            .map(|i| i as Sym)
            .collect();
        FeatTables {
            ty2fi,
            item_bits,
            move_bits,
            kmg: pack.intern.get("きまぐレーザー"),
            skill_link: pack.intern.get("スキルリンク"),
            bukiyou: pack.intern.get("ぶきよう"),
            scarf: pack.intern.get("こだわりスカーフ"),
            iron_ball: pack.intern.get("くろいてっきゅう"),
            sunakaki: pack.intern.get("すなかき"),
            youryokuso: pack.intern.get("ようりょくそ"),
            suisui: pack.intern.get("すいすい"),
            yukikaki: pack.intern.get("ゆきかき"),
            berry_suffix,
            n_cats: pack.n_abil_cats,
        }
    }
    #[inline]
    fn mb(&self, s: Sym) -> u16 {
        self.move_bits.get(&s).copied().unwrap_or(0)
    }
    #[inline]
    fn is_berry(&self, s: Sym) -> bool {
        self.berry_suffix.binary_search(&s).is_ok()
    }
}

/// features.py の _DMG_MEMO（リーフ展開スコープ）。key は (side, party_idx) で id() を代替。
#[derive(Default)]
pub struct DmgMemo {
    pub on: bool,
    dmg: HashMap<(u8, u8, u8), f64>,
    spd: HashMap<(u8, u8, u8), f64>,
    kmg: HashMap<(u8, u8), bool>,
}

impl DmgMemo {
    pub fn begin(&mut self) {
        self.on = true;
        self.dmg.clear();
        self.spd.clear();
        self.kmg.clear();
    }
    pub fn end(&mut self) {
        self.on = false;
    }
}

/// 参照を (side_index, party_index) で表す軽量ハンドル
pub type Ref = (u8, u8);

fn ordered_party(side: &Side) -> Vec<Option<usize>> {
    let mut bench: Vec<usize> = (0..side.party.len()).filter(|&i| i != side.active_idx).collect();
    // key = (-(alive), -(hp/max_hp))  安定ソート
    bench.sort_by(|&a, &b| {
        let ka = key_of(&side.party[a]);
        let kb = key_of(&side.party[b]);
        ka.partial_cmp(&kb).unwrap()
    });
    let mut ordered: Vec<Option<usize>> = vec![Some(side.active_idx)];
    for i in bench {
        ordered.push(Some(i));
    }
    ordered.truncate(3);
    while ordered.len() < 3 {
        ordered.push(None);
    }
    ordered
}

fn key_of(p: &Poke) -> (f64, f64) {
    let a = if p.is_alive { -1.0 } else { 0.0 };
    let h = if p.max_hp != 0 { p.hp as f64 / p.max_hp as f64 } else { 0.0 };
    (a, -h)
}

#[inline]
fn abil_cats(pack: &Pack, out: &mut Vec<f64>, ability: Sym, n: usize) {
    let m = pack.abil_cat_bits.get(&ability).copied().unwrap_or(0);
    for i in 0..n {
        out.push(if (m >> i) & 1 == 1 { 1.0 } else { 0.0 });
    }
}

fn move_features(pack: &Pack, ft: &FeatTables, p: &Poke, out: &mut Vec<f64>) {
    let mut cover = [0.0f64; N_TYPES];
    let (mut pri, mut setup, mut recover, mut hazard, mut phaze, mut pivot, mut protect, mut twoturn, mut trap, mut status) =
        (0.0f64, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
    for mv in &p.moves {
        let pw = mv.power.unwrap_or(0);
        if pw != 0 && mv.category != Cat::Status {
            let fi = ft.ty2fi[mv.ty as usize];
            if fi != usize::MAX {
                let v = (pw as f64 / 120.0).min(1.5);
                if v > cover[fi] {
                    cover[fi] = v;
                }
                if mv.priority > 0 {
                    pri = 1.0;
                }
            }
        }
        let b = ft.mb(mv.name);
        if b & F_SETUP != 0 { setup = 1.0; }
        if b & F_RECOVER != 0 { recover = 1.0; }
        if b & F_HAZARD != 0 { hazard = 1.0; }
        if b & F_PHAZE != 0 { phaze = 1.0; }
        if b & F_PIVOT != 0 { pivot = 1.0; }
        if b & F_PROTECT != 0 { protect = 1.0; }
        if b & F_TWOTURN != 0 { twoturn = 1.0; }
        if b & F_TRAP != 0 { trap = 1.0; }
        if b & F_STATUS != 0 { status = 1.0; }
    }
    out.extend_from_slice(&cover);
    out.extend_from_slice(&[pri, setup, recover, status, hazard, phaze, pivot, protect, twoturn, trap]);
}

fn volatile_block(p: Option<&Poke>, out: &mut Vec<f64>) {
    match p {
        None => out.extend_from_slice(&[0.0; 12]),
        Some(p) => {
            out.push((p.bad_poison_count as f64 / 15.0).min(1.0));
            out.push(if p.seeded { 1.0 } else { 0.0 });
            out.push(if p.yawn_count != 0 { 1.0 } else { 0.0 });
            out.push(if p.perish_count != 0 { 1.0 - p.perish_count as f64 / 3.0 } else { 0.0 });
            out.push(if p.taunt_count != 0 { 1.0 } else { 0.0 });
            out.push(if p.encore_count != 0 { 1.0 } else { 0.0 });
            out.push(if p.disabled_turns != 0 { 1.0 } else { 0.0 });
            out.push(if p.torment { 1.0 } else { 0.0 });
            out.push(if p.trapped { 1.0 } else { 0.0 });
            out.push(if p.charging_move.is_some() { 1.0 } else { 0.0 });
            out.push((p.protect_consecutive as f64 / 3.0).min(1.0));
            out.push(if p.choice_locked_move.is_some() { 1.0 } else { 0.0 });
        }
    }
}

pub fn poke_block_len(pack: &Pack) -> usize {
    2 + N_TYPES + 5 + 6 + N_ITEM_FLAGS + pack.n_abil_cats + 1 + N_TYPES + 10 + 12
}

fn poke_block(pack: &Pack, ft: &FeatTables, p: Option<&Poke>, mega_used: bool, out: &mut Vec<f64>) {
    let p = match p {
        None => {
            for _ in 0..poke_block_len(pack) {
                out.push(0.0);
            }
            return;
        }
        Some(p) => p,
    };
    out.push(if p.is_alive { 1.0 } else { 0.0 });
    out.push(if p.is_alive && p.max_hp != 0 { p.hp as f64 / p.max_hp as f64 } else { 0.0 });
    let mut tvec = [0.0f64; N_TYPES];
    for t in [Some(p.type1), p.type2].into_iter().flatten() {
        if t != NO_TY {
            let fi = ft.ty2fi[t as usize];
            if fi != usize::MAX {
                tvec[fi] = 1.0;
            }
        }
    }
    out.extend_from_slice(&tvec);
    let mut st = [0.0f64; 5];
    if let Some(s) = p.status {
        let sy = &pack.sy.st;
        let idx = if s == sy.paralysis {
            Some(0)
        } else if s == sy.sleep {
            Some(1)
        } else if s == sy.freeze {
            Some(2)
        } else if s == sy.burn {
            Some(3)
        } else if s == sy.poison || s == sy.badpoison {
            Some(4)
        } else {
            None
        };
        if let Some(i) = idx {
            st[i] = 1.0;
        }
    }
    out.extend_from_slice(&st);
    out.push(p.max_hp as f64 / 250.0);
    out.push(p.attack as f64 / 300.0);
    out.push(p.defense as f64 / 300.0);
    out.push(p.sp_attack as f64 / 300.0);
    out.push(p.sp_defense as f64 / 300.0);
    out.push(p.speed as f64 / 300.0);
    let ib = p.item.and_then(|i| ft.item_bits.get(&i).copied()).unwrap_or(0);
    for b in 0..N_ITEM_FLAGS {
        out.push(if (ib >> b) & 1 == 1 { 1.0 } else { 0.0 });
    }
    abil_cats(pack, out, p.ability, ft.n_cats);
    out.push(if p.mega.is_some() && !p.mega_evolved && !mega_used { 1.0 } else { 0.0 });
    move_features(pack, ft, p, out);
    volatile_block(Some(p), out);
}

const STAGE_IDX: [u8; 7] = [0, 1, 2, 3, 4, 5, 6];

fn side_features(pack: &Pack, ft: &FeatTables, side: &Side, out: &mut Vec<f64>) {
    let ord = ordered_party(side);
    for o in &ord {
        poke_block(pack, ft, o.map(|i| &side.party[i]), side.mega_used, out);
    }
    let act = side.active();
    for s in STAGE_IDX {
        let v = stage_val(act, s) as f64 / 6.0;
        out.push(v.min(1.0).max(-1.0));
    }
    let alive: Vec<&Poke> = side.party.iter().filter(|p| p.is_alive).collect();
    out.push(alive.len() as f64 / 3.0);
    // Python の sum(float) は Neumaier 補償総和（CPython 3.12）
    let s = crate::pysum::pysum(
        alive.iter().filter(|p| p.max_hp != 0).map(|p| p.hp as f64 / p.max_hp as f64),
    );
    out.push(s / 3.0);
}

#[inline]
fn stage_val(p: &Poke, i: u8) -> i32 {
    match i {
        0 => p.stage_attack,
        1 => p.stage_defense,
        2 => p.stage_sp_attack,
        3 => p.stage_sp_defense,
        4 => p.stage_speed,
        5 => p.stage_accuracy,
        _ => p.stage_evasion,
    }
}

fn disclosure(pack: &Pack, view: &crate::oppview::OppView, ord: &[Option<usize>], party: &[Poke], out: &mut Vec<f64>) {
    for o in ord {
        let p = match o {
            None => {
                out.extend_from_slice(&[0.0, 0.0, 0.0]);
                continue;
            }
            Some(i) => &party[*i],
        };
        match view.pokemon.iter().find(|k| k.name == p.name) {
            None => out.extend_from_slice(&[0.0, 0.0, 0.0]),
            Some(k) => {
                out.push((k.known_moves.len() as f64 / 4.0).min(1.0));
                out.push(if truthy(pack, k.known_item) { 1.0 } else { 0.0 });
                out.push(if truthy(pack, k.known_ability) { 1.0 } else { 0.0 });
            }
        }
    }
}

#[inline]
fn truthy(pack: &Pack, s: Option<Sym>) -> bool {
    match s {
        None => false,
        Some(x) => !pack.intern.resolve(x).is_empty(),
    }
}

// ── 期待与ダメージ / 実効速度 ─────────────────────────────────────────

fn real_speed_calc(pack: &Pack, ft: &FeatTables, p: &Poke, tailwind: bool, field: &Field) -> f64 {
    let mut spd = p.eff_speed(pack) as f64;
    if Some(p.ability) != ft.bukiyou {
        let m = if p.item.is_some() && p.item == ft.scarf {
            1.5
        } else if p.item.is_some() && p.item == ft.iron_ball {
            0.5
        } else {
            1.0
        };
        spd *= m;
    }
    if tailwind {
        spd *= 2.0;
    }
    let w = field.weather;
    let we = &pack.sy.we;
    let boost = (Some(p.ability) == ft.sunakaki && w == Some(we.sandstorm))
        || (Some(p.ability) == ft.youryokuso && w == Some(we.sunny))
        || (Some(p.ability) == ft.suisui && w == Some(we.rain))
        || (Some(p.ability) == ft.yukikaki && w == Some(we.hail));
    if boost {
        spd *= 2.0;
    }
    spd
}

fn real_speed(
    pack: &Pack,
    ft: &FeatTables,
    memo: &mut DmgMemo,
    p: Option<&Poke>,
    pref: Ref,
    sref: u8,
    tailwind: bool,
    field: &Field,
) -> f64 {
    let p = match p {
        None => return -1.0,
        Some(p) if !p.is_alive => return -1.0,
        Some(p) => p,
    };
    if memo.on {
        let k = (pref.0, pref.1, sref);
        if let Some(&v) = memo.spd.get(&k) {
            return v;
        }
        let v = real_speed_calc(pack, ft, p, tailwind, field);
        memo.spd.insert(k, v);
        return v;
    }
    real_speed_calc(pack, ft, p, tailwind, field)
}

/// `_expected_frac(att, deff, field, def_side, multi_hit=False)` の移植。
/// att/deff は calc_damage が変異させるため、呼び出し側で分離した可変参照を渡す。
#[allow(clippy::too_many_arguments)]
fn expected_frac_calc(
    pack: &Pack,
    att: &mut Poke,
    deff: &mut Poke,
    field: &mut Field,
    screens: Option<(bool, bool, bool)>, // (reflect, light_screen, aurora_veil)
    rng: &mut dyn FnMut(u8) -> f64,
) -> f64 {
    let mut best = 0.0f64;
    let moves: Vec<DMove> = att.moves.clone();
    for mv in &moves {
        if mv.power.unwrap_or(0) != 0 && mv.category != Cat::Status {
            let mut d = calc_damage(pack, att, deff, mv, field, false, Some(0.925), None, rng) as f64;
            if let Some((refl, ls, av)) = screens {
                if mv.category == Cat::Physical && (refl || av) {
                    d *= 0.5;
                } else if mv.category == Cat::Special && (ls || av) {
                    d *= 0.5;
                }
            }
            let f = d / (deff.max_hp.max(1)) as f64;
            if f > best {
                best = f;
            }
        }
    }
    best.min(1.5)
}

/// 副作用の有無で memo の可否を判定（features._expected_frac / _att_memo_safe）
fn memo_usable(ft: &FeatTables, memo: &mut DmgMemo, att: &Poke, aref: Ref, deff: &Poke) -> bool {
    if !memo.on {
        return false;
    }
    if let Some(i) = deff.item {
        if ft.is_berry(i) {
            return false;
        }
    }
    if att.charged || att.electromorphosis_charged {
        return false;
    }
    let k = (aref.0, aref.1);
    if let Some(&c) = memo.kmg.get(&k) {
        return c;
    }
    let c = !att.moves.iter().any(|m| Some(m.name) == ft.kmg);
    memo.kmg.insert(k, c);
    c
}

/// encode_state 本体。sides[first] が side1。
pub fn encode_state(
    pack: &Pack,
    ft: &FeatTables,
    sides: &mut [Side; 2],
    first: usize,
    field: &mut Field,
    memo: &mut DmgMemo,
    rng: &mut dyn BRng,
) -> Vec<f64> {
    let mut out = Vec::with_capacity(905);
    encode_state_into(pack, ft, sides, first, field, memo, rng, &mut out);
    out
}

#[allow(clippy::too_many_arguments)]
pub fn encode_state_into(
    pack: &Pack,
    ft: &FeatTables,
    sides: &mut [Side; 2],
    first: usize,
    field: &mut Field,
    memo: &mut DmgMemo,
    rng: &mut dyn BRng,
    out: &mut Vec<f64>,
) {
    let second = 1 - first;
    out.clear();
    let f: &mut Vec<f64> = out;
    side_features(pack, ft, &sides[first], f);
    side_features(pack, ft, &sides[second], f);

    let o1 = ordered_party(&sides[first]);
    let o2 = ordered_party(&sides[second]);
    let scr1 = (sides[first].reflect, sides[first].light_screen, sides[first].aurora_veil);
    let scr2 = (sides[second].reflect, sides[second].light_screen, sides[second].aurora_veil);

    // 自分の各体 → 相手の各体（def_side = side2）、次に逆向き（def_side = side1）
    for (dir, (oa, ob)) in [(0u8, (&o1, &o2)), (1u8, (&o2, &o1))] {
        let (asi, dsi) = if dir == 0 { (first, second) } else { (second, first) };
        let scr = if dir == 0 { scr2 } else { scr1 };
        for a in oa.iter() {
            for d in ob.iter() {
                f.push(expected_frac(
                    pack, ft, sides, asi, *a, dsi, *d, field, Some(scr), memo, rng,
                ));
            }
        }
    }

    // すばやさ上回り 3x3
    let tr = field.trick_room;
    let tw1 = sides[first].tailwind;
    let tw2 = sides[second].tailwind;
    let mut s1s = [0.0f64; 3];
    let mut s2s = [0.0f64; 3];
    for i in 0..3 {
        s1s[i] = real_speed(
            pack, ft, memo,
            o1[i].map(|x| &sides[first].party[x]),
            (first as u8, o1[i].unwrap_or(255) as u8),
            first as u8, tw1, field,
        );
        s2s[i] = real_speed(
            pack, ft, memo,
            o2[i].map(|x| &sides[second].party[x]),
            (second as u8, o2[i].unwrap_or(255) as u8),
            second as u8, tw2, field,
        );
    }
    for i in 0..3 {
        for j in 0..3 {
            if s1s[i] < 0.0 || s2s[j] < 0.0 {
                f.push(0.0);
            } else {
                let faster = if tr { s1s[i] <= s2s[j] } else { s1s[i] >= s2s[j] };
                f.push(if faster { 1.0 } else { 0.0 });
            }
        }
    }

    // 開示情報
    {
        let (a, b) = (first, second);
        let mut tmp = Vec::new();
        disclosure(pack, &sides[a].opp_view, &o2, &sides[b].party, &mut tmp);
        f.extend_from_slice(&tmp);
        tmp.clear();
        disclosure(pack, &sides[b].opp_view, &o1, &sides[a].party, &mut tmp);
        f.extend_from_slice(&tmp);
    }

    // 天候
    let we = &pack.sy.we;
    let widx = match field.weather {
        None => 0,
        Some(w) if w == we.rain => 1,
        Some(w) if w == we.sunny => 2,
        Some(w) if w == we.sandstorm => 3,
        Some(w) if w == we.hail => 4,
        _ => 0,
    };
    for i in 0..5 {
        f.push(if i == widx { 1.0 } else { 0.0 });
    }
    f.push((field.weather_count as f64 / 5.0).min(1.0));
    f.push(if field.misty_terrain { 1.0 } else { 0.0 });
    f.push(if field.electric_terrain { 1.0 } else { 0.0 });
    f.push(if field.psychic_terrain { 1.0 } else { 0.0 });
    f.push(if field.grassy_terrain { 1.0 } else { 0.0 });
    let tcount = field
        .misty_terrain_count
        .max(field.electric_terrain_count)
        .max(field.psychic_terrain_count)
        .max(field.grassy_terrain_count);
    f.push((tcount as f64 / 5.0).min(1.0));
    f.push(if field.trick_room { 1.0 } else { 0.0 });
    f.push((field.trick_room_count as f64 / 5.0).min(1.0));
    f.push((field.gravity as f64 / 5.0).min(1.0));
    for s in [first, second] {
        f.push((sides[s].wish_count as f64 / 2.0).min(1.0));
        f.push((sides[s].future_sight_count as f64 / 3.0).min(1.0));
    }
    for s in [first, second] {
        let idx = sides[s].field_idx;
        f.push(if field.stealth_rock[idx] { 1.0 } else { 0.0 });
        f.push(field.spikes[idx] as f64 / 3.0);
        f.push(field.toxic_spikes[idx] as f64 / 2.0);
        f.push(if field.sticky_web[idx] { 1.0 } else { 0.0 });
    }
    for s in [first, second] {
        f.push(if sides[s].reflect { 1.0 } else { 0.0 });
        f.push(if sides[s].light_screen { 1.0 } else { 0.0 });
        f.push(if sides[s].aurora_veil { 1.0 } else { 0.0 });
        f.push(if sides[s].tailwind { 1.0 } else { 0.0 });
        f.push((sides[s].safeguard as f64 / 5.0).min(1.0));
    }
    let a1s = sides[first].active().eff_speed(pack);
    let a2s = sides[second].active().eff_speed(pack);
    f.push(if a1s >= a2s { 1.0 } else { 0.0 });
    let d = (a1s - a2s) as f64 / 200.0;
    f.push(d.min(1.0).max(-1.0));
}

#[allow(clippy::too_many_arguments)]
fn expected_frac(
    pack: &Pack,
    ft: &FeatTables,
    sides: &mut [Side; 2],
    asi: usize,
    ai: Option<usize>,
    dsi: usize,
    di: Option<usize>,
    field: &mut Field,
    screens: Option<(bool, bool, bool)>,
    memo: &mut DmgMemo,
    rng: &mut dyn BRng,
) -> f64 {
    let (ai, di) = match (ai, di) {
        (Some(a), Some(d)) => (a, d),
        _ => return 0.0,
    };
    if !sides[asi].party[ai].is_alive || !sides[dsi].party[di].is_alive {
        return 0.0;
    }
    let aref = (asi as u8, ai as u8);
    let dref = (dsi as u8, di as u8);
    let use_memo = memo_usable(ft, memo, &sides[asi].party[ai], aref, &sides[dsi].party[di]);
    if use_memo {
        // memo key: (id(att), id(deff), id(def_side)) → def_side は dsi 固定なので (att, deff)
        let k = (aref.0 * 8 + aref.1, dref.0 * 8 + dref.1, dsi as u8);
        if let Some(&v) = memo.dmg.get(&k) {
            return v;
        }
    }
    let v = {
        assert!(asi != dsi, "encode: att/deff は別サイド前提");
        let hi = asi.max(dsi);
        let (lo_s, hi_s) = sides.split_at_mut(hi);
        let (att, deff) = if asi < dsi {
            (&mut lo_s[asi].party[ai], &mut hi_s[0].party[di])
        } else {
            (&mut hi_s[0].party[ai], &mut lo_s[dsi].party[di])
        };
        let mut cb = |kind: u8| match kind {
            0 => rng.random(),
            _ => rng.choice(16) as f64,
        };
        expected_frac_calc(pack, att, deff, field, screens, &mut cb)
    };
    if use_memo {
        let k = (aref.0 * 8 + aref.1, dref.0 * 8 + dref.1, dsi as u8);
        memo.dmg.insert(k, v);
    }
    v
}

pub fn feature_dim(pack: &Pack) -> usize {
    let per_side = 3 * poke_block_len(pack) + 7 + 2;
    2 * per_side + 18 + 9 + 18 + 38
}
