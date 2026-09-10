//! simulator/items.py の移植（ダメージ計算内の補正は damage.rs 側）。
use crate::interner::Sym;
use crate::pack::Pack;
use crate::damage::Field;
use crate::poke::Poke;
use crate::rng::BRng;

pub fn get_speed_item_multiplier(pack: &Pack, item: Option<Sym>) -> f64 {
    let s = &pack.sy.l;
    match item {
        Some(i) if i == s.こだわりスカーフ => 1.5,
        Some(i) if i == s.くろいてっきゅう => 0.5,
        _ => 1.0,
    }
}

pub fn is_choice_item(pack: &Pack, item: Option<Sym>) -> bool {
    let s = &pack.sy.l;
    matches!(item, Some(i) if i == s.こだわりスカーフ || i == s.こだわりハチマキ || i == s.こだわりメガネ)
}

pub fn has_quick_claw_trigger(pack: &Pack, item: Option<Sym>, rng: &mut dyn BRng) -> bool {
    if item == Some(pack.sy.l.せんせいのツメ) {
        return rng.random() < 0.20;
    }
    false
}

/// apply_hp_berry: ターン終了時の能力上昇きのみ
pub fn apply_hp_berry(pack: &Pack, p: &mut Poke) {
    let l = &pack.sy.l;
    if p.item == Some(l.たべのこし) {
        return;
    }
    // QUARTER_BERRIES: きのみ -> stage index
    let it = match p.item {
        Some(i) => i,
        None => return,
    };
    let stat = if it == l.カムラのみ {
        4
    } else if it == l.サルのみ {
        2
    } else if it == l.リュガのみ {
        1
    } else if it == l.タラプのみ {
        3
    } else {
        return;
    };
    let div = if p.ability == l.くいしんぼう { 2 } else { 4 };
    let thr = p.max_hp / div;
    if p.hp > thr {
        return;
    }
    let amt = if p.ability == l.じゅくせい { 2 } else { 1 };
    p.set_stage(stat, std::cmp::min(6, p.stage(stat) + amt));
    p.last_berry = p.item;
    if p.ability == l.はんすう && p.ruminate_berry.is_none() {
        p.ruminate_berry = p.item;
        p.ruminate_count = 1;
    }
    p.item = None;
    if p.ability == l.ほおぶくろ {
        let h = std::cmp::max(1, p.max_hp / 3);
        p.hp = std::cmp::min(p.max_hp, p.hp + h);
    }
}

pub fn try_cure_berry(pack: &Pack, p: &mut Poke) {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    let it = match p.item {
        Some(i) => i,
        None => return,
    };
    if it == l.ラムのみ && (p.status.is_some() || p.confused) {
        p.status = None;
        p.bad_poison_count = 0;
        p.sleep_count = 0;
        p.confused = false;
        p.item = None;
    } else if it == l.カゴのみ && p.status == Some(st.sleep) {
        p.status = None;
        p.sleep_count = 0;
        p.item = None;
    } else if it == l.モモンのみ
        && (p.status == Some(st.poison) || p.status == Some(st.badpoison))
    {
        p.status = None;
        p.bad_poison_count = 0;
        p.item = None;
    } else if it == l.チーゴのみ && p.status == Some(st.burn) {
        p.status = None;
        p.item = None;
    } else if it == l.クラボのみ && p.status == Some(st.paralysis) {
        p.status = None;
        p.item = None;
    } else if it == l.キーのみ && p.status == Some(st.freeze) {
        p.status = None;
        p.item = None;
    } else if it == l.ナナシのみ && p.confused {
        p.confused = false;
        p.item = None;
    }
}

pub fn try_white_herb(pack: &Pack, p: &mut Poke) {
    if p.item != Some(pack.sy.l.しろいハーブ) {
        return;
    }
    if (0..5).any(|i| p.stage(i) < 0) {
        for i in 0..5 {
            if p.stage(i) < 0 {
                p.set_stage(i, 0);
            }
        }
        p.item = None;
    }
}

pub fn try_mental_herb(pack: &Pack, p: &mut Poke) {
    if p.item != Some(pack.sy.l.メンタルハーブ) {
        return;
    }
    let afflicted = p.infatuation
        || p.taunt_count > 0
        || p.encore_count > 0
        || p.heal_block_count > 0
        || p.disabled_turns > 0;
    if !afflicted {
        return;
    }
    p.infatuation = false;
    p.taunt_count = 0;
    p.encore_count = 0;
    p.locked_move = None;
    p.heal_block_count = 0;
    p.disabled_move = None;
    p.disabled_turns = 0;
    p.item = None;
}

pub fn try_leppa_berry(pack: &Pack, p: &mut Poke) {
    if p.item != Some(pack.sy.l.ヒメリのみ) {
        return;
    }
    for i in 0..p.moves.len() {
        if i < p.pp.len() && p.pp[i] == 0 {
            let cap = p.moves[i].pp.unwrap_or(0);
            p.pp[i] = std::cmp::min(cap, p.pp[i] + 10);
            p.item = None;
            return;
        }
    }
}

/// フィールドの継続ターン数。グランドコートで5→8（天候の あついいわ 等と同じ考え方）。
pub fn terrain_turns(pack: &Pack, setter_item: Option<crate::interner::Sym>) -> i64 {
    if setter_item == Some(pack.sy.it.グランドコート) {
        8
    } else {
        5
    }
}

/// フィールド発動アイテム（シード）。該当フィールドが張られていれば能力+1して消費する。
/// フィールド設置時と、継続中フィールドへの登場時の両方から呼ぶ（Python: items.try_terrain_seed）。
pub fn try_terrain_seed(pack: &Pack, poke: &mut Poke, field: &Field) -> bool {
    if !poke.is_alive {
        return false;
    }
    let it = &pack.sy.it;
    // (道具, フィールドが張られているか, 上げる能力: 1=防御 3=特防)
    let ent = if poke.item == Some(it.エレキシード) {
        (field.electric_terrain, 1u8)
    } else if poke.item == Some(it.グラスシード) {
        (field.grassy_terrain, 1u8)
    } else if poke.item == Some(it.ミストシード) {
        (field.misty_terrain, 3u8)
    } else if poke.item == Some(it.サイコシード) {
        (field.psychic_terrain, 3u8)
    } else {
        return false;
    };
    if !ent.0 {
        return false;
    }
    let cur = if ent.1 == 1 { poke.stage_defense } else { poke.stage_sp_defense };
    if cur >= 6 {
        return false;
    }
    if ent.1 == 1 {
        poke.stage_defense = std::cmp::min(6, poke.stage_defense + 1);
    } else {
        poke.stage_sp_defense = std::cmp::min(6, poke.stage_sp_defense + 1);
    }
    poke.item = None;
    on_item_consumed(pack, poke);
    true
}

pub fn on_item_consumed(pack: &Pack, p: &mut Poke) {
    if p.ability == pack.sy.l.かるわざ && p.item.is_none() {
        p.stage_speed = std::cmp::min(6, p.stage_speed + 2);
    }
}
