//! simulator/abilities.py の移植（ダメージ計算内の判定は damage.rs 側に既存）。
use crate::damage::{effective_weather, is_contact_move, DMove, Field};
use crate::pack::{Cat, Pack};
use crate::poke::{apply_status, Poke, TransformBackup, ST_ATK, ST_DEF, ST_SPA, ST_SPD, ST_SPE};
use crate::rng::BRng;

/// かたやぶり系
#[inline]
pub fn is_mold(pack: &Pack, p: &Poke) -> bool {
    let l = &pack.sy.l;
    p.ability == l.かたやぶり || p.ability == l.ターボブレイズ || p.ability == l.テラボルテージ
}

/// _apply_forme_type（てんきや/ぎたい）
pub fn apply_forme_type(pack: &Pack, p: &mut Poke, field: &Field) {
    let l = &pack.sy.l;
    let ab = p.ability;
    let new_t = if ab == l.てんきや {
        let w = effective_weather(pack, field, Some(p));
        let we = &pack.sy.we;
        match w {
            Some(x) if x == we.sunny => Some(pack.tc.ほのお),
            Some(x) if x == we.rain => Some(pack.tc.みず),
            Some(x) if x == we.hail => Some(pack.tc.こおり),
            _ => Some(p.base_type1),
        }
    } else if ab == l.ぎたい {
        if field.electric_terrain {
            Some(pack.tc.でんき)
        } else if field.grassy_terrain {
            Some(pack.tc.くさ)
        } else if field.psychic_terrain {
            Some(pack.tc.エスパー)
        } else if field.misty_terrain {
            Some(pack.tc.フェアリー)
        } else {
            Some(p.base_type1)
        }
    } else {
        None
    };
    if let Some(t) = new_t {
        if p.type1 != t || p.type2.is_some() {
            p.type1 = t;
            p.type2 = None;
        }
    }
}

/// entry_ability
pub fn entry_ability(
    pack: &Pack,
    poke: &mut Poke,
    opponent: &mut Poke,
    field: &mut Field,
    weather_duration: i64,
) {
    let l = &pack.sy.l;
    let we = &pack.sy.we;
    let ab = poke.ability;

    let wm = if ab == l.すなおこし {
        Some(we.sandstorm)
    } else if ab == l.ひでり {
        Some(we.sunny)
    } else if ab == l.あめふらし {
        Some(we.rain)
    } else if ab == l.ゆきふらし {
        Some(we.hail)
    } else {
        None
    };
    if let Some(w) = wm {
        if field.weather != Some(w) {
            field.weather = Some(w);
            field.weather_count = weather_duration;
        }
    }

    if ab == l.エレキメイカー && !field.electric_terrain {
        field.electric_terrain = true;
        field.electric_terrain_count = 5;
    }

    if ab == l.いかく {
        let oab = opponent.ability;
        if oab == l.クリアボディ
            || oab == l.しろいけむり
            || oab == l.かがくへんかガス
            || oab == l.マイペース
            || oab == l.どんかん
            || oab == l.きもったま
            || oab == l.せいしんりょく
        {
            // 効かない
        } else if oab == l.あまのじゃく {
            opponent.stage_attack = std::cmp::min(6, opponent.stage_attack + 1);
        } else {
            opponent.stage_attack = std::cmp::max(-6, opponent.stage_attack - 1);
        }
    }

    if ab == l.ダウンロード {
        if opponent.defense <= opponent.sp_defense {
            poke.stage_attack = std::cmp::min(6, poke.stage_attack + 1);
        } else {
            poke.stage_sp_attack = std::cmp::min(6, poke.stage_sp_attack + 1);
        }
    }

    if ab == l.てんきや || ab == l.ぎたい {
        apply_forme_type(pack, poke, field);
    }

    if ab == l.トレース {
        let o = opponent.ability;
        let uncopyable = o == l.トレース
            || o == l.かわりもの
            || o == l.イリュージョン
            || o == l.ばけのかわ
            || o == l.かがくへんかガス;
        // Python: `opponent.ability` が空文字でないこと（未設定は空文字）
        if !pack.intern.resolve(o).is_empty() && !uncopyable {
            poke.ability = o;
        }
    }

    if ab == l.かんろなミツ && !poke.honey_used {
        poke.honey_used = true;
        let oab = opponent.ability;
        if !(oab == l.クリアボディ || oab == l.しろいけむり || oab == l.かいりきバサミ) {
            opponent.stage_evasion = std::cmp::max(-6, opponent.stage_evasion - 1);
        }
    }

    if ab == l.かわりもの && !poke.transformed {
        poke.transform_backup = Some(Box::new(TransformBackup {
            attack: poke.attack,
            defense: poke.defense,
            sp_attack: poke.sp_attack,
            sp_defense: poke.sp_defense,
            speed: poke.speed,
            ability: poke.ability,
            moves: poke.moves.clone(),
            pp: poke.pp.clone(),
        }));
        poke.attack = opponent.attack;
        poke.defense = opponent.defense;
        poke.sp_attack = opponent.sp_attack;
        poke.sp_defense = opponent.sp_defense;
        poke.speed = opponent.speed;
        poke.ability = opponent.ability;
        poke.type1 = opponent.type1;
        poke.type2 = opponent.type2;
        poke.moves = opponent.moves.clone();
        poke.pp = opponent.moves.iter().map(|m| std::cmp::min(5, m.pp.unwrap_or(5))).collect();
        for i in 0..7u8 {
            poke.set_stage(i, opponent.stage(i));
        }
        poke.transformed = true;
    }
}

/// on_after_hit
pub fn on_after_hit(
    pack: &Pack,
    attacker: &mut Poke,
    defender: &mut Poke,
    mv: &DMove,
    rng: &mut dyn BRng,
) {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    let ab = defender.ability;

    if ab == l.くだけるよろい && mv.category == Cat::Physical {
        defender.stage_defense = std::cmp::max(-6, defender.stage_defense - 1);
        defender.stage_speed = std::cmp::min(6, defender.stage_speed + 2);
    }

    if ab == l.せいでんき && is_contact_move(pack, mv) && attacker.ability != l.えんかく {
        if rng.random() < 0.30 {
            apply_status(pack, attacker, st.paralysis, false);
        }
    }

    if ab == l.ほうし && is_contact_move(pack, mv) && attacker.ability != l.えんかく {
        if rng.random() < 0.30 {
            let idx = rng.choice(3);
            let s = [st.poison, st.paralysis, st.sleep][idx];
            let ok = apply_status(pack, attacker, s, false);
            if ok && s == st.sleep {
                attacker.sleep_count = rng.randint(1, 3);
            }
        }
    }

    if ab == l.ひらいしん && mv.ty == pack.tc.でんき {
        defender.stage_sp_attack = std::cmp::min(6, defender.stage_sp_attack + 1);
    }

    // ちくでん/ちょすい/かんそうはだ/どしょく
    let absorb = if ab == l.ちくでん {
        Some(pack.tc.でんき)
    } else if ab == l.ちょすい || ab == l.かんそうはだ {
        Some(pack.tc.みず)
    } else if ab == l.どしょく {
        Some(pack.tc.じめん)
    } else {
        None
    };
    if let Some(t) = absorb {
        if mv.ty == t && defender.hp < defender.max_hp {
            let heal = std::cmp::max(1, defender.max_hp / 4);
            defender.hp = std::cmp::min(defender.max_hp, defender.hp + heal);
        }
    }

    if ab == l.もらいび && mv.ty == pack.tc.ほのお && !defender.flash_fire_active {
        defender.flash_fire_active = true;
    }

    if ab == l.でんきエンジン && mv.ty == pack.tc.でんき {
        defender.stage_speed = std::cmp::min(6, defender.stage_speed + 1);
    }

    if ab == l.そうしょく && mv.ty == pack.tc.くさ {
        defender.stage_attack = std::cmp::min(6, defender.stage_attack + 1);
    }

    if ab == l.でんきにかえる {
        defender.electromorphosis_charged = true;
    }

    let n = mv.name;
    let is_wind = n == l.こごえるかぜ || n == l.ぼうふう || n == l.ふぶき || n == l.ねっぷう
        || n == l.ふきとばし || n == l.おいかぜ || n == l.すなあらし || n == l.はなふぶき
        || n == l.エアカッター;
    if ab == l.ふうりょく && is_wind {
        defender.charged = true;
    }

    if ab == l.シンクロ && defender.is_alive {
        if let Some(s) = defender.status {
            if (s == st.poison || s == st.badpoison || s == st.paralysis || s == st.burn)
                && attacker.is_alive
            {
                apply_status(pack, attacker, s, false);
            }
        }
    }

    if ab == l.ぎゃくじょう && defender.is_alive {
        let was_above_half = !defender.gyaku_triggered;
        if was_above_half && defender.hp <= defender.max_hp / 2 {
            defender.stage_sp_attack = std::cmp::min(6, defender.stage_sp_attack + 1);
            defender.gyaku_triggered = true;
        }
    }

    if (ab == l.ねばりかわ || ab == l.ながいしっぽ)
        && is_contact_move(pack, mv)
        && attacker.ability != l.えんかく
        && !is_mold(pack, attacker)
    {
        attacker.stage_speed = std::cmp::max(-6, attacker.stage_speed - 1);
    }

    if ab == l.じきゅうりょく && !is_mold(pack, attacker) {
        defender.stage_defense = std::cmp::min(6, defender.stage_defense + 1);
    }

    let mold = is_mold(pack, attacker);
    let contact = is_contact_move(pack, mv) && attacker.ability != l.えんかく;

    if ab == l.せいぎのこころ && mv.ty == pack.tc.あく {
        defender.stage_attack = std::cmp::min(6, defender.stage_attack + 1);
    }

    if contact && !mold && attacker.is_alive {
        if ab == l.ほのおのからだ && rng.random() < 0.30 {
            apply_status(pack, attacker, st.burn, false);
        }
        if ab == l.どくのトゲ && rng.random() < 0.30 {
            apply_status(pack, attacker, st.poison, false);
        }
        if ab == l.ぬめぬめ {
            attacker.stage_speed = std::cmp::max(-6, attacker.stage_speed - 1);
        }
        if ab == l.ミイラ && attacker.ability != l.ミイラ && attacker.ability != l.かがくへんかガス {
            attacker.ability = l.ミイラ;
        } else if ab == l.さまようたましい && attacker.ability != l.かがくへんかガス {
            std::mem::swap(&mut attacker.ability, &mut defender.ability);
        }
    }

    if attacker.ability == l.どくしゅ && contact && defender.is_alive && rng.random() < 0.30 {
        apply_status(pack, defender, st.poison, false);
    }

    if attacker.ability == l.あくしゅう
        && defender.is_alive
        && mv.category != Cat::Status
        && rng.random() < 0.10
    {
        defender.flinched = true;
    }

    if attacker.item == Some(l.おうじゃのしるし)
        && defender.is_alive
        && mv.category != Cat::Status
        && defender.ability != l.せいしんりょく
        && defender.ability != l.どんかん
        && rng.random() < 0.10
    {
        defender.flinched = true;
    }
}

/// _rough_skin_recoil
pub fn rough_skin_recoil(pack: &Pack, attacker: &mut Poke, defender: &mut Poke, mv: &DMove) {
    let l = &pack.sy.l;
    let st = &pack.sy.st;
    let ab = defender.ability;
    let enkaku = attacker.ability == l.えんかく;
    if (ab == l.さめはだ || ab == l.てつのとげ) && is_contact_move(pack, mv) && !enkaku {
        if !is_mold(pack, attacker) {
            let recoil = std::cmp::max(1, attacker.max_hp / 8);
            attacker.take_damage(recoil);
        }
    }
    if ab == l.ゆうばく
        && is_contact_move(pack, mv)
        && !enkaku
        && !defender.is_alive
        && attacker.is_alive
        && !is_mold(pack, attacker)
    {
        let recoil = std::cmp::max(1, attacker.max_hp / 4);
        attacker.take_damage(recoil);
    }
    if ab == l.とびだすハバネロ && mv.category != Cat::Status && !is_mold(pack, attacker) {
        apply_status(pack, attacker, st.burn, false);
    }
}

pub fn on_defender_ko(pack: &Pack, attacker: &mut Poke, defender: &Poke, damage: i64) {
    if defender.ability == pack.sy.l.とびだすなかみ && damage > 0 && attacker.is_alive {
        attacker.take_damage(damage);
    }
}

pub fn on_ko(pack: &Pack, attacker: &mut Poke) {
    let l = &pack.sy.l;
    let ab = attacker.ability;
    if ab == l.じしんかじょう {
        attacker.stage_attack = std::cmp::min(6, attacker.stage_attack + 1);
    }
    if ab == l.うなぎのぼり {
        // Python: dict の挿入順で max（同値なら先勝ち）＝ A,B,C,D,S の順
        let cand = [
            (ST_ATK, attacker.attack),
            (ST_DEF, attacker.defense),
            (ST_SPA, attacker.sp_attack),
            (ST_SPD, attacker.sp_defense),
            (ST_SPE, attacker.speed),
        ];
        let mut best = cand[0];
        for c in cand.iter().skip(1) {
            if c.1 > best.1 {
                best = *c;
            }
        }
        attacker.set_stage(best.0, std::cmp::min(6, attacker.stage(best.0) + 1));
    }
}

/// end_of_turn_ability
pub fn end_of_turn_ability(pack: &Pack, p: &mut Poke, field: &Field, rng: &mut dyn BRng) {
    let l = &pack.sy.l;
    let we = &pack.sy.we;
    let ab = p.ability;

    if ab == l.かそく {
        p.stage_speed = std::cmp::min(6, p.stage_speed + 1);
    }
    if ab == l.アイスボディ && effective_weather(pack, field, Some(p)) == Some(we.hail) {
        let heal = std::cmp::max(1, p.max_hp / 16);
        p.hp = std::cmp::min(p.max_hp, p.hp + heal);
    }
    if ab == l.あめうけざら && effective_weather(pack, field, Some(p)) == Some(we.rain) {
        let heal = std::cmp::max(1, p.max_hp / 16);
        p.hp = std::cmp::min(p.max_hp, p.hp + heal);
    }
    if ab == l.うるおいボディ
        && effective_weather(pack, field, Some(p)) == Some(we.rain)
        && p.status.is_some()
    {
        p.status = None;
        p.bad_poison_count = 0;
    }
    if ab == l.だっぴ && p.status.is_some() && rng.random() < 0.30 {
        p.status = None;
        p.bad_poison_count = 0;
    }
    if ab == l.てんきや || ab == l.ぎたい {
        apply_forme_type(pack, p, field);
    }
    if ab == l.はらぺこスイッチ {
        p.hangry = !p.hangry;
    }
    if ab == l.しゅうかく && p.item.is_none() && p.last_berry.is_some() {
        if effective_weather(pack, field, Some(p)) == Some(we.sunny) || rng.random() < 0.50 {
            p.item = p.last_berry;
        }
    }
    if p.ruminate_count > 0 {
        p.ruminate_count -= 1;
        if p.ruminate_count == 0 {
            let berry = p.ruminate_berry;
            p.ruminate_berry = None;
            if berry == Some(l.オボンのみ) {
                let h = std::cmp::max(1, p.max_hp / 4);
                p.hp = std::cmp::min(p.max_hp, p.hp + h);
            } else if let Some(b) = berry {
                let stat = if b == l.カムラのみ {
                    Some(ST_SPE)
                } else if b == l.サルのみ {
                    Some(ST_SPA)
                } else if b == l.リュガのみ {
                    Some(ST_DEF)
                } else if b == l.タラプのみ {
                    Some(ST_SPD)
                } else {
                    None
                };
                if let Some(sx) = stat {
                    p.set_stage(sx, std::cmp::min(6, p.stage(sx) + 1));
                }
            }
        }
    }
    if ab == l.サンパワー && effective_weather(pack, field, Some(p)) == Some(we.sunny) {
        let dmg = std::cmp::max(1, p.max_hp / 8);
        p.take_damage(dmg);
    }
    if ab == l.かんそうはだ {
        let w = effective_weather(pack, field, Some(p));
        if w == Some(we.sunny) {
            let d = std::cmp::max(1, p.max_hp / 8);
            p.take_damage(d);
        } else if w == Some(we.rain) {
            let heal = std::cmp::max(1, p.max_hp / 8);
            p.hp = std::cmp::min(p.max_hp, p.hp + heal);
        }
    }
    if ab == l.ムラっけ {
        let up = rng.choice(7) as u8;
        p.set_stage(up, std::cmp::min(6, p.stage(up) + 2));
        // Python: [s for s in STATS if s != up_stat] の6要素から choice
        let idx = rng.choice(6);
        let mut rest: Vec<u8> = Vec::with_capacity(6);
        for i in 0..7u8 {
            if i != up {
                rest.push(i);
            }
        }
        let down = rest[idx];
        p.set_stage(down, std::cmp::max(-6, p.stage(down) - 1));
    }
}

/// on_switch_out
pub fn on_switch_out(pack: &Pack, p: &mut Poke) {
    let l = &pack.sy.l;
    let ab = p.ability;
    if ab == l.マイティチェンジ && !p.hero_forme {
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
        use crate::poke::calc_stat;
        p.attack = calc_stat(160, p.evs[1], 31, nat(0));
        p.defense = calc_stat(97, p.evs[2], 31, nat(1));
        p.sp_attack = calc_stat(106, p.evs[3], 31, nat(2));
        p.sp_defense = calc_stat(87, p.evs[4], 31, nat(3));
        p.speed = calc_stat(100, p.evs[5], 31, nat(4));
        p.hero_forme = true;
    }
    if ab == l.さいせいりょく {
        let heal = p.max_hp / 3;
        p.hp = std::cmp::min(p.max_hp, p.hp + heal);
    }
    if ab == l.しぜんかいふく && p.status.is_some() {
        p.status = None;
        p.bad_poison_count = 0;
    }
}

pub fn on_stat_lowered(pack: &Pack, p: &mut Poke) {
    let l = &pack.sy.l;
    if p.ability == l.かちき {
        p.stage_sp_attack = std::cmp::min(6, p.stage_sp_attack + 2);
    }
    if p.ability == l.まけんき {
        p.stage_attack = std::cmp::min(6, p.stage_attack + 2);
    }
}
