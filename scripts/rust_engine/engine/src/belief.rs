//! simulator/belief.py の移植（決定化サンプリングに必要な部分＋observe_damage）。
//!
//! パリティ規約 #3: `known_moves` は Python では set なので反復順が PYTHONHASHSEED 依存。
//! ここでは sorted（種名のコードポイント順＝UTF-8バイト順）に正規化する。
//! ハーネス側の Python も同じく sorted に monkeypatch する（本番Pythonは無変更）。
use crate::damage::{calc_damage, DMove, EstSnap, Field};
use crate::interner::Sym;
use crate::oppview::OppView;
use crate::pack::{EvEntry, Pack};
use crate::poke::{build_from_template_rand, get_pokemon_template, to_poke, Evs, Poke, Spec, Template};
use crate::pysum::pysum;
use crate::rng::BRng;
use std::collections::HashMap;

const EPS: f64 = 1e-4;
const MAX_EVS: usize = 14;
const MAX_NATS: usize = 7;

fn rolls() -> [f64; 16] {
    let mut r = [0.0f64; 16];
    for (k, x) in r.iter_mut().enumerate() {
        *x = k as f64 / 15.0;
    }
    r
}

#[derive(Clone, Debug)]
pub struct Cand {
    pub ev: EvEntry,
    pub nature: String,
    pub defender: Poke,
}

/// 実機の相手HP表示（整数％、四捨五入）。belief.py の hp_pct と 1:1
pub fn hp_pct(hp: i64, max_hp: i64) -> i64 {
    if max_hp == 0 { 0 } else { (hp * 200 + max_hp).div_euclid(2 * max_hp) }
}

/// 候補で計算したダメージが観測と合うか（belief.py の obs_match と 1:1）。
/// taken: 相手のHPは整数％でしか見えないので±1%の幅で合わせる。dealt: 自分のHPは実数で見えるので整数で比べる
pub fn obs_match(taken: bool, dmg: i64, hp: i64, obs: f64) -> bool {
    if taken {
        hp != 0 && (dmg as f64 * 100.0 / hp as f64 - obs).abs() <= 1.0
    } else {
        dmg as f64 == obs
    }
}

/// 観測時点の相手の個体の写し（belief.py の pub_state と 1:1）。見えている状態をすべて含む
pub type PubState = Poke;

pub fn pub_state(p: &Poke) -> PubState {
    p.clone()
}

/// 自分側の個体の行動前の写し（belief.py の own_state）
pub fn own_state(st: Option<&PubState>, fallback: &Poke) -> Poke {
    st.cloned().unwrap_or_else(|| fallback.clone())
}

/// 観測時点の相手の写しに、候補の型の隠れた部分（性格・努力値・能力値・持ち物・特性）を差し込む
/// （belief.py の with_state と 1:1）
pub fn with_state(pack: &Pack, prof: &Poke, st: Option<&PubState>) -> Poke {
    let st = match st {
        None => return prof.clone(),
        Some(s) => s,
    };
    let mut q = st.clone();
    if st.transformed {
        return q;
    }
    let mut cand = prof.clone();
    if st.mega_evolved && !prof.mega_evolved {
        crate::poke::mega_evolve_poke(pack, &mut cand);
    }
    let frac = if st.max_hp != 0 { st.hp as f64 / st.max_hp as f64 } else { 1.0 };
    q.max_hp = cand.max_hp;
    q.attack = cand.attack;
    q.defense = cand.defense;
    q.sp_attack = cand.sp_attack;
    q.sp_defense = cand.sp_defense;
    q.speed = cand.speed;
    q.nature = cand.nature;
    q.evs = cand.evs;
    if st.item.is_some() {
        q.item = cand.item;
    }
    if !st.mega_evolved {
        q.ability = cand.ability;
    }
    q.hp = if st.hp > 0 {
        std::cmp::max(1, (frac * q.max_hp as f64).round_ties_even() as i64)
    } else {
        0
    };
    q
}

#[derive(Clone, Copy, Debug, PartialEq)]
pub enum ObsKind {
    Taken,
    Dealt,
    Order,
    /// 相手が攻撃技を選んだ（mv=選んだ技、other=こちらの受け手）。belief.py の "choice"
    Choice,
}

/// 技選びの尤度で、明らかに強い技を持つ型に掛ける係数（belief.py の CHOICE_BETA）
pub const CHOICE_BETA: f64 = 0.3;

fn dmove_by_name(pack: &Pack, name: &str) -> Option<DMove> {
    let idx = *pack.move_by_name.get(name)?;
    let md = &pack.moves[idx];
    Some(DMove {
        name: md.name,
        ty: md.ty,
        category: md.category,
        power: md.power,
        accuracy: md.accuracy,
        priority: md.priority,
        pp: md.pp,
    })
}

/// 型プールの重み付けに後から使う観測。Taken=こちらが与えた被ダメージ、Dealt=相手が与えたダメージ、
/// Order=行動順（frac に自分の実効速度、crit に「相手が先」）。other は自分側の個体（行動前の状態）
#[derive(Clone, Debug)]
pub struct DmgObs {
    pub kind: ObsKind,
    pub other: Poke,
    pub mv: DMove,
    pub frac: f64,
    pub field: Field,
    pub crit: bool,
    pub subj: Option<PubState>,
}

#[derive(Clone, Debug)]
pub struct PokemonBelief {
    pub name: String,
    pub move_prior: Vec<(String, f64)>,
    pub item_prior: Vec<(String, f64)>,
    pub ability_prior: Vec<(String, f64)>,
    /// set → sorted 正規化（パリティ規約 #3）
    pub known_moves: Vec<String>,
    pub known_item: Option<String>,
    pub item_lost: bool,
    pub item_epoch: u32,
    pub known_ability: Option<String>,
    pub cands: Vec<Cand>,
    pub prior: Vec<f64>,
    pub post: Vec<f64>,
    /// 型プール経路：観測したダメージと、型ごとの事後重み（belief.py と 1:1）
    pub dmg_obs: Vec<DmgObs>,
    pub absent_items: Vec<String>,
    pub pool_w: Vec<f64>,
    pub pool_applied: usize,
    pub pool_prof: Vec<usize>,
    pub profs: Vec<Poke>,
}

fn ev_key(e: &EvEntry) -> (i64, i64, i64, i64, i64, i64) {
    (e.h, e.a, e.b, e.c, e.d, e.s)
}

/// belief.py `_eff_speed_of`: 持ち物倍率を差し替えられる実効速度。
/// 倍率は battle.rs の速度順 / ai::effective_speed に揃える。
fn eff_speed_with(pack: &Pack, p: &Poke, field: &Field, item_mult: f64) -> i64 {
    let l = &pack.sy.l;
    let mut spd = ((p.eff_speed(pack) as f64) * item_mult).floor() as i64;
    let w = field.weather;
    if (w == Some(pack.sy.we.rain) && p.ability == l.すいすい)
        || (w == Some(pack.sy.we.sunny) && p.ability == l.ようりょくそ)
        || (w == Some(pack.sy.we.sandstorm) && p.ability == l.すなかき)
        || (w == Some(pack.sy.we.hail) && p.ability == l.ゆきかき)
    {
        spd *= 2;
    }
    if field.electric_terrain && p.ability == l.サーフテール {
        spd *= 2;
    }
    spd
}

impl PokemonBelief {
    pub fn new(
        pack: &Pack,
        tpl: &Template,
        known_ability: Option<String>,
        known_item: Option<String>,
        extra: Option<&Vec<(EvEntry, String)>>,
    ) -> PokemonBelief {
        let mut natures: Vec<(String, f64)> = tpl.top_natures.clone();
        if natures.is_empty() {
            natures.push(("まじめ".to_string(), 1.0));
        }
        natures.truncate(MAX_NATS);
        let mut evs: Vec<EvEntry> = tpl.top_evs.clone();
        if evs.is_empty() {
            evs.push(EvEntry { spread: "無振り".to_string(), rate: 1.0, ..Default::default() });
        }
        evs.truncate(MAX_EVS);

        let mut cands: Vec<Cand> = Vec::new();
        let mut priors: Vec<f64> = Vec::new();
        for ev in &evs {
            for (nat, nr) in &natures {
                let spec = Spec {
                    name: tpl.name.clone(),
                    item: known_item.clone(),
                    nature: Some(nat.clone()),
                    moves: None,
                    evs: Some(Evs { h: ev.h, a: ev.a, b: ev.b, c: ev.c, d: ev.d, s: ev.s }),
                    ability: known_ability.clone(),
                };
                let b = build_from_template_rand(pack, tpl, &spec, &mut None);
                let d = to_poke(pack, &b);
                cands.push(Cand { ev: ev.clone(), nature: nat.clone(), defender: d });
                priors.push(f64::max(ev.rate, 1e-9) * f64::max(*nr, 1e-9));
            }
        }

        if let Some(ex) = extra {
            let mut keys: Vec<(i64, i64, i64, i64, i64, i64, String)> = cands
                .iter()
                .map(|c| {
                    let k = ev_key(&c.ev);
                    (k.0, k.1, k.2, k.3, k.4, k.5, c.nature.clone())
                })
                .collect();
            let avg = if priors.is_empty() { 1.0 } else { pysum(priors.iter().copied()) / priors.len() as f64 };
            for (ev, nat) in ex {
                let k = ev_key(ev);
                let key = (k.0, k.1, k.2, k.3, k.4, k.5, nat.clone());
                if keys.contains(&key) {
                    continue;
                }
                keys.push(key);
                let spec = Spec {
                    name: tpl.name.clone(),
                    item: known_item.clone(),
                    nature: Some(nat.clone()),
                    moves: None,
                    evs: Some(Evs { h: ev.h, a: ev.a, b: ev.b, c: ev.c, d: ev.d, s: ev.s }),
                    ability: known_ability.clone(),
                };
                let b = build_from_template_rand(pack, tpl, &spec, &mut None);
                let d = to_poke(pack, &b);
                cands.push(Cand { ev: ev.clone(), nature: nat.clone(), defender: d });
                priors.push(avg);
            }
        }

        let s = {
            let t = pysum(priors.iter().copied());
            if t == 0.0 {
                1.0
            } else {
                t
            }
        };
        let prior: Vec<f64> = priors.iter().map(|p| p / s).collect();
        let post = prior.clone();
        PokemonBelief {
            name: tpl.name.clone(),
            move_prior: tpl.top_moves.clone(),
            item_prior: tpl.top_items.clone(),
            ability_prior: tpl.top_abilities.clone(),
            known_moves: Vec::new(),
            known_item,
            item_lost: false,
            item_epoch: 0,
            known_ability,
            cands,
            prior,
            post,
            dmg_obs: Vec::new(),
            absent_items: Vec::new(),
            pool_w: Vec::new(),
            pool_applied: 0,
            pool_prof: Vec::new(),
            profs: Vec::new(),
        }
    }

    /// observe_disclosure（known_moves は sorted 正規化して保持）
    pub fn observe_disclosure(&mut self, pack: &Pack, k: &crate::oppview::PokeKnowledge) {
        for mv in &k.known_moves {
            let s = pack.intern.resolve(*mv).to_string();
            if !self.known_moves.contains(&s) {
                self.known_moves.push(s);
            }
        }
        self.known_moves.sort();
        // 持ち物が入れ替わったら、それ以前の持ち物の推論は捨てる（belief.py と同じ）
        if k.item_epoch != self.item_epoch {
            self.item_epoch = k.item_epoch;
            self.absent_items.clear();
            self.item_lost = k.item_lost;
            self.known_item = k.known_item.map(|i| pack.intern.resolve(i).to_string());
        }
        if let Some(i) = k.known_item {
            let s = pack.intern.resolve(i).to_string();
            if !s.is_empty() {
                self.known_item = Some(s);
            }
        }
        if k.item_lost {
            self.item_lost = true;
        }
        // 初登場時にふうせんの表示が無かった（belief.py と 1:1）
        if k.no_balloon {
            self.observe_absent_item(&["ふうせん"]);
        }
        if let Some(a) = k.known_ability {
            let s = pack.intern.resolve(a).to_string();
            if !s.is_empty() {
                self.known_ability = Some(s);
            }
        }
    }

    /// observe_damage: 16ロールで観測割合を再現できた候補の尤度でベイズ更新
    #[allow(clippy::too_many_arguments)]
    pub fn observe_damage(
        &mut self,
        pack: &Pack,
        attacker: &mut Poke,
        mv: &DMove,
        observed_fraction: f64,
        field: &mut Field,
        critical: bool,
        rng: &mut dyn BRng,
        subj: Option<&PubState>,
        other_state: Option<&PubState>,
    ) -> bool {
        // 自分側の個体も行動前の状態に戻す（りゅうせいぐん等で技の後に能力が下がっている）
        let mut att = own_state(other_state, attacker);
        self.dmg_obs.push(DmgObs { kind: ObsKind::Taken, other: att.clone(), mv: mv.clone(),
                                   frac: observed_fraction, field: field.clone(), crit: critical,
                                   subj: subj.cloned() });
        let rs = rolls();
        let mut liks: Vec<f64> = Vec::with_capacity(self.cands.len());
        for c in self.cands.iter() {
            let mut d = with_state(pack, &c.defender, subj);
            let mut hit = 0i64;
            for rr in rs.iter() {
                let mut cb = |kind: u8| match kind {
                    0 => rng.random(),
                    _ => rng.choice(16) as f64,
                };
                let (sa, sd) = (EstSnap::take(&att), EstSnap::take(&d));
                let dmg = calc_damage(
                    pack,
                    &mut att,
                    &mut d,
                    mv,
                    field,
                    critical,
                    Some(*rr),
                    None,
                    &mut cb,
                );
                sa.restore(&mut att);
                sd.restore(&mut d);
                if obs_match(true, dmg, d.max_hp, observed_fraction) {
                    hit += 1;
                }
            }
            liks.push(hit as f64 / 16.0);
        }
        if pysum(liks.iter().copied()) == 0.0 {
            return false;
        }
        let new: Vec<f64> = self
            .post
            .iter()
            .zip(liks.iter())
            .map(|(p, lik)| p * (lik * (1.0 - EPS) + EPS))
            .collect();
        let s = {
            let t = pysum(new.iter().copied());
            if t == 0.0 {
                1.0
            } else {
                t
            }
        };
        self.post = new.iter().map(|x| x / s).collect();
        true
    }

    /// observe_damage_dealt（belief.py と 1:1）
    /// 殴られた側が「自分がどれだけ減ったか」から相手の攻撃側 EV/性格を絞る。
    #[allow(clippy::too_many_arguments)]
    pub fn observe_damage_dealt(
        &mut self,
        pack: &Pack,
        defender: &mut Poke,
        mv: &DMove,
        observed_fraction: f64,
        field: &mut Field,
        critical: bool,
        rng: &mut dyn BRng,
        subj: Option<&PubState>,
        other_state: Option<&PubState>,
    ) -> bool {
        let mut def = own_state(other_state, defender);
        self.dmg_obs.push(DmgObs { kind: ObsKind::Dealt, other: def.clone(), mv: mv.clone(),
                                   frac: observed_fraction, field: field.clone(), crit: critical,
                                   subj: subj.cloned() });
        let rs = rolls();
        let mut liks: Vec<f64> = Vec::with_capacity(self.cands.len());
        for c in self.cands.iter() {
            let mut a = with_state(pack, &c.defender, subj);
            let mut hit = 0i64;
            for rr in rs.iter() {
                let mut cb = |kind: u8| match kind {
                    0 => rng.random(),
                    _ => rng.choice(16) as f64,
                };
                let (sa, sd) = (EstSnap::take(&a), EstSnap::take(&def));
                let dmg = calc_damage(
                    pack,
                    &mut a,
                    &mut def,
                    mv,
                    field,
                    critical,
                    Some(*rr),
                    None,
                    &mut cb,
                );
                sa.restore(&mut a);
                sd.restore(&mut def);
                if obs_match(false, dmg, def.max_hp, observed_fraction) {
                    hit += 1;
                }
            }
            liks.push(hit as f64 / 16.0);
        }
        if pysum(liks.iter().copied()) == 0.0 {
            return false;
        }
        self.apply_liks(&liks);
        true
    }

    /// observe_order（belief.py と 1:1）
    /// 行動順から実効速度の上下限を絞る。優先度が同じときだけ呼ぶこと。
    pub fn observe_order(
        &mut self,
        pack: &Pack,
        my_eff_speed: i64,
        opp_first: bool,
        field: &Field,
        subj: Option<&PubState>,
    ) -> bool {
        self.dmg_obs.push(DmgObs { kind: ObsKind::Order, other: Poke::default(), mv: DMove::default(),
                                   frac: my_eff_speed as f64, field: field.clone(), crit: opp_first,
                                   subj: subj.cloned() });
        let scarf = "こだわりスカーフ";
        let scarf_p = self
            .item_prior
            .iter()
            .find(|(n, _)| n == scarf)
            .map_or(0.0, |(_, r)| *r);
        let mut liks: Vec<f64> = Vec::with_capacity(self.cands.len());
        let mut need_scarf = true;
        let scarf_allowed =
            self.known_item.is_none() || self.known_item.as_deref() == Some(scarf);
        for c in self.cands.iter() {
            let d = with_state(pack, &c.defender, subj);
            let base = eff_speed_with(pack, &d, field, 1.0);
            let ok_plain = if opp_first { base >= my_eff_speed } else { base <= my_eff_speed };
            let mut ok_scarf = false;
            if scarf_p > 0.0 && scarf_allowed {
                let sc = eff_speed_with(pack, &d, field, 1.5);
                ok_scarf = if opp_first { sc >= my_eff_speed } else { sc <= my_eff_speed };
            }
            if ok_plain {
                need_scarf = false;
            }
            liks.push(if ok_plain || ok_scarf { 1.0 } else { 0.0 });
        }
        if pysum(liks.iter().copied()) == 0.0 {
            return false;
        }
        self.apply_liks(&liks);
        if need_scarf && scarf_p > 0.0 && self.known_item.is_none() {
            self.known_item = Some(scarf.to_string());
            self.item_prior = vec![(scarf.to_string(), 100.0)];
        }
        true
    }

    /// 相手が攻撃技を選んだ（型プール経路の pool_weights で反映。belief.py の observe_choice）
    pub fn observe_choice(&mut self, mv: &DMove, own_def: Poke, field: &Field, subj: PubState) {
        // 同じ受け手に同じ技を選び続けたのは実質1回の判断（belief.py と同じ）
        if self.dmg_obs.iter().any(|o| o.kind == ObsKind::Choice && o.mv.name == mv.name && o.other.name == own_def.name) {
            return;
        }
        self.dmg_obs.push(DmgObs { kind: ObsKind::Choice, other: own_def, mv: mv.clone(), frac: 0.0,
                                   field: field.clone(), crit: false, subj: Some(subj) });
    }

    /// observe_absent_item（belief.py と 1:1）
    /// 「発動しなかった」ことから持ち物を否定する。開示済みなら何もしない。
    pub fn observe_absent_item(&mut self, items: &[&str]) -> bool {
        if self.known_item.is_some() {
            return false;
        }
        for it in items {
            if !self.absent_items.iter().any(|x| x == it) {
                self.absent_items.push(it.to_string());
            }
        }
        let before = self.item_prior.len();
        self.item_prior.retain(|(n, _)| !items.contains(&n.as_str()));
        if self.item_prior.len() == before {
            return false;
        }
        if self.item_prior.is_empty() {
            self.item_prior = vec![(String::new(), 100.0)];
        }
        true
    }

    /// 型プールの型ごとの事後重み（belief.py の pool_weights と 1:1）。
    /// 重み＝型の出現率 × Π(観測したダメージを再現できる尤度)。尤度は持ち物・特性・性格・努力値が
    /// 同じ型で共通なので、その組（プロファイル）ごとに1回だけ計算する。観測は初回参照時にまとめて反映。
    pub fn pool_weights(&mut self, pack: &Pack, tpl: &Template, pool: &[crate::pack::PoolBuild]) -> &[f64] {
        if self.pool_w.len() != pool.len() {
            self.pool_w = pool.iter().map(|b| b.weight).collect();
            self.pool_applied = 0;
            self.pool_prof.clear();
            self.profs.clear();
            let mut idx: HashMap<(String, String, String, (i64, i64, i64, i64, i64, i64)), usize> = HashMap::new();
            for b in pool {
                let key = (b.item.clone(), b.ability.clone(), b.nature.clone(), ev_key(&b.ev));
                let n = self.profs.len();
                let i = *idx.entry(key).or_insert(n);
                if i == n {
                    let spec = Spec {
                        name: tpl.name.clone(),
                        item: if b.item.is_empty() { None } else { Some(b.item.clone()) },
                        nature: Some(b.nature.clone()),
                        moves: None,
                        evs: Some(Evs { h: b.ev.h, a: b.ev.a, b: b.ev.b, c: b.ev.c, d: b.ev.d, s: b.ev.s }),
                        ability: if b.ability.is_empty() { None } else { Some(b.ability.clone()) },
                    };
                    let bb = build_from_template_rand(pack, tpl, &spec, &mut None);
                    self.profs.push(to_poke(pack, &bb));
                }
                self.pool_prof.push(i);
            }
        }
        let rs = rolls();
        // 計測用: POOL_DMG=0 で観測を反映しない（ダメージによる絞り込みの効果の切り分け）
        if std::env::var("POOL_DMG").map(|v| v == "0").unwrap_or(false) {
            self.pool_applied = self.dmg_obs.len();
        }
        while self.pool_applied < self.dmg_obs.len() {
            let mut o = self.dmg_obs[self.pool_applied].clone();
            self.pool_applied += 1;
            if o.kind == ObsKind::Choice {
                if std::env::var("POOL_CHOICE").map(|v| v != "1").unwrap_or(true) {
                    continue;
                }
                // 技選びの尤度（belief.py の _apply_choice と 1:1）
                let rr = 7.0 / 15.0;
                let chosen = pack.intern.resolve(o.mv.name).to_string();
                let mut names: Vec<String> = pool.iter().flat_map(|b| b.moves.iter().cloned()).collect();
                names.sort();
                names.dedup();
                let mvs: Vec<(String, DMove)> = names.into_iter()
                    .filter_map(|n| dmove_by_name(pack, &n).map(|d| (n, d)))
                    .filter(|(_, d)| d.category != crate::pack::Cat::Status)
                    .collect();
                let mut cache: HashMap<usize, HashMap<String, f64>> = HashMap::new();
                let mut lik: Vec<f64> = Vec::with_capacity(pool.len());
                for (b, &pi) in pool.iter().zip(self.pool_prof.iter()) {
                    if !b.moves.iter().any(|m| *m == chosen) {
                        lik.push(1.0);
                        continue;
                    }
                    if !cache.contains_key(&pi) {
                        let mut q = with_state(pack, &self.profs[pi], o.subj.as_ref());
                        let mut dd: HashMap<String, f64> = HashMap::new();
                        for (n, dm) in mvs.iter() {
                            // 持ち物が無いなげつけるは威力0（belief.py と同じ）
                            if dm.name == pack.sy.mv.なげつける && q.last_flung_item.or(q.item).is_none() {
                                dd.insert(n.clone(), 0.0);
                                continue;
                            }
                            let mut cb = |kind: u8| if kind == 0 { 0.99 } else { 0.0 };
                            let mut od = o.other.clone();
                            let sq = EstSnap::take(&q);
                            let d = calc_damage(pack, &mut q, &mut od, dm, &mut o.field, false, Some(rr), None, &mut cb);
                            sq.restore(&mut q);
                            dd.insert(n.clone(), d as f64 * crate::ai::expected_hits(pack, dm, &q));
                        }
                        cache.insert(pi, dd);
                    }
                    let dd = &cache[&pi];
                    let got = dd.get(&chosen).copied().unwrap_or(0.0);
                    let best = b.moves.iter().filter_map(|m| dd.get(m).copied()).fold(0.0f64, f64::max);
                    lik.push(if got >= o.other.hp as f64 || got * 1.5 >= best { 1.0 } else { CHOICE_BETA });
                }
                let mut t = 0.0f64;
                for (w, x) in self.pool_w.iter_mut().zip(lik.iter()) {
                    *w *= *x;
                    t += *w;
                }
                if t > 0.0 {
                    for w in self.pool_w.iter_mut() {
                        *w /= t;
                    }
                }
                continue;
            }
            let mut liks = vec![0.0f64; self.profs.len()];
            let mut any = false;
            for (pi, prof0) in self.profs.iter().enumerate() {
                let mut prof = with_state(pack, prof0, o.subj.as_ref());
                if o.kind == ObsKind::Order {
                    // 行動順：候補自身の持ち物（スカーフ等）込みの実効速度で先後が合うか
                    let m = crate::items::get_speed_item_multiplier(pack, prof.item);
                    let sp = eff_speed_with(pack, &prof, &o.field, m) as f64;
                    let ok = if o.crit { sp >= o.frac } else { sp <= o.frac };
                    liks[pi] = if ok { 1.0 } else { 0.0 };
                    if ok {
                        any = true;
                    }
                    continue;
                }
                let prof = &mut prof;
                let mut hit = 0i64;
                for rr in rs.iter() {
                    // 乱数を使うのはきまぐレーザーの威力判定だけ。観測の再計算で対戦の乱数を消費しない
                    let mut cb = |kind: u8| if kind == 0 { 0.99 } else { 0.0 };
                    let (so, sp) = (EstSnap::take(&o.other), EstSnap::take(prof));
                    let (dmg, hp) = if o.kind == ObsKind::Taken {
                        let d = calc_damage(pack, &mut o.other, prof, &o.mv, &mut o.field,
                                            o.crit, Some(*rr), None, &mut cb);
                        (d, prof.max_hp)
                    } else {
                        let d = calc_damage(pack, prof, &mut o.other, &o.mv, &mut o.field,
                                            o.crit, Some(*rr), None, &mut cb);
                        (d, o.other.max_hp)
                    };
                    so.restore(&mut o.other);
                    sp.restore(prof);
                    if obs_match(o.kind == ObsKind::Taken, dmg, hp, o.frac) {
                        hit += 1;
                    }
                }
                liks[pi] = hit as f64 / 16.0;
                if hit > 0 {
                    any = true;
                }
            }
            if !any {
                continue;   // どの型でも再現できない＝モデル外（更新しない）
            }
            let mut t = 0.0f64;
            for (w, &pi) in self.pool_w.iter_mut().zip(self.pool_prof.iter()) {
                *w *= liks[pi] * (1.0 - EPS) + EPS;
                t += *w;
            }
            if t > 0.0 {
                for w in self.pool_w.iter_mut() {
                    *w /= t;
                }
            }
        }
        &self.pool_w
    }

    fn apply_liks(&mut self, liks: &[f64]) {
        let new: Vec<f64> = self
            .post
            .iter()
            .zip(liks.iter())
            .map(|(p, lik)| p * (lik * (1.0 - EPS) + EPS))
            .collect();
        let t = pysum(new.iter().copied());
        let s = if t == 0.0 { 1.0 } else { t };
        self.post = new.iter().map(|x| x / s).collect();
    }

    /// `_weighted(rng, items)`: 重み>0 のみ、total は Neumaier 和
    fn weighted<'b, T: Clone>(rng: &mut dyn BRng, items: &'b [(T, f64)]) -> Option<T> {
        let f: Vec<&(T, f64)> = items.iter().filter(|x| x.1 > 0.0).collect();
        if f.is_empty() {
            return None;
        }
        let total = pysum(f.iter().map(|x| x.1));
        let mut r = rng.random() * total;
        for (v, w) in f.iter() {
            r -= *w;
            if r <= 0.0 {
                return Some(v.clone());
            }
        }
        Some(f[f.len() - 1].0.clone())
    }

    pub fn sample_spread(&self, rng: &mut dyn BRng) -> (EvEntry, String) {
        let items: Vec<(usize, f64)> =
            (0..self.cands.len()).map(|i| (i, self.post[i])).collect();
        let i = Self::weighted(rng, &items).unwrap_or(0);
        (self.cands[i].ev.clone(), self.cands[i].nature.clone())
    }

    pub fn sample_item(&self, rng: &mut dyn BRng) -> Option<String> {
        if let Some(i) = &self.known_item {
            return Some(i.clone());
        }
        Self::weighted(rng, &self.item_prior)
    }

    pub fn sample_ability(&self, rng: &mut dyn BRng) -> String {
        if let Some(a) = &self.known_ability {
            return a.clone();
        }
        Self::weighted(rng, &self.ability_prior).unwrap_or_default()
    }

    pub fn sample_moves(&self, rng: &mut dyn BRng, n: usize) -> Vec<String> {
        let mut chosen: Vec<String> = self.known_moves.iter().take(n).cloned().collect();
        let mut pool: Vec<(String, f64)> = self
            .move_prior
            .iter()
            .filter(|(m, _)| !chosen.contains(m))
            .cloned()
            .collect();
        while chosen.len() < n && !pool.is_empty() {
            let m = match Self::weighted(rng, &pool) {
                None => break,
                Some(m) => m,
            };
            chosen.push(m.clone());
            pool.retain(|(x, _)| *x != m);
        }
        chosen
    }
}

#[derive(Clone, Debug, Default)]
pub struct OpponentBelief {
    pub season: String,
    /// 種名 → belief（Python dict の挿入順を保持）
    pub species: Vec<(String, PokemonBelief)>,
    pub use_registered: bool,
}

impl OpponentBelief {
    pub fn new(season: &str) -> OpponentBelief {
        OpponentBelief { season: season.to_string(), species: Vec::new(), use_registered: true }
    }

    fn idx(&self, name: &str) -> Option<usize> {
        self.species.iter().position(|(n, _)| n == name)
    }

    pub fn ensure(
        &mut self,
        pack: &Pack,
        name: &str,
        known_ability: Option<String>,
        known_item: Option<String>,
    ) -> Option<usize> {
        if let Some(i) = self.idx(name) {
            return Some(i);
        }
        // 使用率行のあるシーズンへフォールバックする（正本: simulator/belief.py _tpl_with_prior）。
        // 事前分布が空だと determinize が falsy を上書きせず、相手の真の型が探索に残る＝型リーク。
        let tpl = {
            let t = get_pokemon_template(pack, name, &self.season);
            let has_prior = |t: &Option<Template>| {
                t.as_ref().map_or(false, |x| {
                    !x.top_moves.is_empty() || !x.top_items.is_empty() || !x.top_abilities.is_empty()
                })
            };
            if has_prior(&t) {
                t
            } else {
                let mut alt = None;
                for s in ["M-6", "M-5", "M-4", "M-3", "M-2"] {
                    if s == self.season {
                        continue;
                    }
                    let c = get_pokemon_template(pack, name, s);
                    if has_prior(&c) {
                        alt = c;
                        break;
                    }
                }
                alt.or(t)
            }
        }?;
        let extra = if self.use_registered {
            pack.registered_spreads.get(name).cloned()
        } else {
            None
        };
        let b = PokemonBelief::new(pack, &tpl, known_ability, known_item, extra.as_ref());
        self.species.push((name.to_string(), b));
        Some(self.species.len() - 1)
    }

    pub fn observe_disclosure(&mut self, pack: &Pack, view: &OppView) {
        for k in view.pokemon.clone() {
            let name = pack.intern.resolve(k.name).to_string();
            let ka = k.known_ability.map(|a| pack.intern.resolve(a).to_string());
            let ki = k.known_item.map(|i| pack.intern.resolve(i).to_string());
            if let Some(i) = self.ensure(pack, &name, ka, ki) {
                self.species[i].1.observe_disclosure(pack, &k);
            }
        }
        // 同じ持ち物はパーティに1つ。判明した味方の持ち物は他の個体の候補から外す（belief.py と 1:1）
        let team: Vec<(String, String)> = view.pokemon.iter()
            .filter(|k| k.item_epoch == 0)
            .filter_map(|k| k.known_item.map(|i| (pack.intern.resolve(k.name).to_string(),
                                                  pack.intern.resolve(i).to_string())))
            .filter(|(_, i)| !i.is_empty())
            .collect();
        for k in view.pokemon.iter() {
            let name = pack.intern.resolve(k.name).to_string();
            if let Some(e) = self.species.iter_mut().find(|e| e.0 == name) {
                for (other, it) in &team {
                    if *other != name {
                        e.1.observe_absent_item(&[it.as_str()]);   // 持ち物の事前分布からも外す
                    }
                }
            }
        }
    }

    pub fn observe_damage(
        &mut self,
        pack: &Pack,
        defender_name: Sym,
        attacker: &mut Poke,
        mv: &DMove,
        observed_fraction: f64,
        field: &mut Field,
        critical: bool,
        rng: &mut dyn BRng,
        subj: Option<&PubState>,
        other_state: Option<&PubState>,
    ) -> bool {
        let name = pack.intern.resolve(defender_name).to_string();
        let i = match self.ensure(pack, &name, None, None) {
            None => return false,
            Some(i) => i,
        };
        let mut b = std::mem::replace(&mut self.species[i].1, PokemonBelief::empty());
        let r = b.observe_damage(pack, attacker, mv, observed_fraction, field, critical, rng,
                                 subj, other_state);
        self.species[i].1 = b;
        r
    }

    #[allow(clippy::too_many_arguments)]
    pub fn observe_damage_dealt(
        &mut self,
        pack: &Pack,
        attacker_name: Sym,
        defender: &mut Poke,
        mv: &DMove,
        observed_fraction: f64,
        field: &mut Field,
        critical: bool,
        rng: &mut dyn BRng,
        subj: Option<&PubState>,
        other_state: Option<&PubState>,
    ) -> bool {
        let name = pack.intern.resolve(attacker_name).to_string();
        let i = match self.ensure(pack, &name, None, None) {
            None => return false,
            Some(i) => i,
        };
        let mut b = std::mem::replace(&mut self.species[i].1, PokemonBelief::empty());
        let r = b.observe_damage_dealt(pack, defender, mv, observed_fraction, field, critical, rng,
                                       subj, other_state);
        self.species[i].1 = b;
        r
    }

    pub fn observe_order(
        &mut self,
        pack: &Pack,
        opp_name: Sym,
        my_eff_speed: i64,
        opp_first: bool,
        field: &Field,
        subj: Option<&PubState>,
    ) -> bool {
        let name = pack.intern.resolve(opp_name).to_string();
        let i = match self.ensure(pack, &name, None, None) {
            None => return false,
            Some(i) => i,
        };
        let mut b = std::mem::replace(&mut self.species[i].1, PokemonBelief::empty());
        let r = b.observe_order(pack, my_eff_speed, opp_first, field, subj);
        self.species[i].1 = b;
        r
    }

    pub fn observe_choice(&mut self, pack: &Pack, opp_name: Sym, mv: &DMove, own_def: Poke, field: &Field,
                          subj: PubState) {
        let name = pack.intern.resolve(opp_name).to_string();
        if let Some(i) = self.ensure(pack, &name, None, None) {
            self.species[i].1.observe_choice(mv, own_def, field, subj);
        }
    }

    pub fn observe_absent_item(&mut self, pack: &Pack, opp_name: Sym, items: &[&str]) -> bool {
        let name = pack.intern.resolve(opp_name).to_string();
        let i = match self.ensure(pack, &name, None, None) {
            None => return false,
            Some(i) => i,
        };
        let mut b = std::mem::replace(&mut self.species[i].1, PokemonBelief::empty());
        let r = b.observe_absent_item(items);
        self.species[i].1 = b;
        r
    }
}

impl PokemonBelief {
    fn empty() -> PokemonBelief {
        PokemonBelief {
            name: String::new(),
            move_prior: Vec::new(),
            item_prior: Vec::new(),
            ability_prior: Vec::new(),
            known_moves: Vec::new(),
            known_item: None,
            item_lost: false,
            item_epoch: 0,
            known_ability: None,
            cands: Vec::new(),
            prior: Vec::new(),
            post: Vec::new(),
            dmg_obs: Vec::new(),
            absent_items: Vec::new(),
            pool_w: Vec::new(),
            pool_applied: 0,
            pool_prof: Vec::new(),
            profs: Vec::new(),
        }
    }
}

/// SearchAI._tpl_cache 相当
#[derive(Default)]
pub struct TplCache {
    map: HashMap<String, Option<Template>>,
    playable: HashMap<String, Option<Template>>,
}

impl TplCache {
    pub fn get(&mut self, pack: &Pack, name: &str, season: &str) -> Option<Template> {
        if let Some(t) = self.map.get(name) {
            return t.clone();
        }
        let t = get_pokemon_template(pack, name, season);
        self.map.insert(name.to_string(), t.clone());
        t
    }

    /// SearchAI._tpl_playable: season に使用率行（技）が無い種は、行のある新しいシーズンのテンプレを使う
    pub fn get_playable(&mut self, pack: &Pack, name: &str, season: &str) -> Option<Template> {
        if let Some(t) = self.playable.get(name) {
            return t.clone();
        }
        let t = self.get(pack, name, season);
        let r = match &t {
            Some(x) if x.top_moves.is_empty() => {
                let mut alt = None;
                for s in ["M-6", "M-5", "M-4", "M-3", "M-2"] {
                    if s == season {
                        continue;
                    }
                    if let Some(c) = get_pokemon_template(pack, name, s) {
                        if !c.top_moves.is_empty() {
                            alt = Some(c);
                            break;
                        }
                    }
                }
                alt.or(t)
            }
            _ => t,
        };
        self.playable.insert(name.to_string(), r.clone());
        r
    }
}

#[cfg(test)]
mod fix200_belief_tests {
    use super::*;
    use crate::pack::PoolBuild;
    use crate::poke::build_poke;

    struct Z;
    impl BRng for Z {
        fn random(&mut self) -> f64 { 0.5 }
        fn choice(&mut self, _n: usize) -> usize { 0 }
        fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
        fn choices(&mut self) -> i64 { 2 }
    }

    fn pb_(w: f64, nature: &str, ev: [i64; 6]) -> PoolBuild {
        PoolBuild {
            weight: w,
            item: "たべのこし".into(),
            nature: nature.into(),
            ability: "せいしんりょく".into(),
            ev: EvEntry { h: ev[0], a: ev[1], b: ev[2], c: ev[3], d: ev[4], s: ev[5], ..Default::default() },
            moves: vec!["あくび".into(), "イカサマ".into(), "つきのひかり".into(), "まもる".into()],
            side: String::new(),
        }
    }

    #[test]
    fn r4mcts_観測の再計算で充電を消費しない() {
        let mut p = Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"));
        let mut att = build_poke(&mut p, "ハラバリー@たべのこし:ひかえめ:10まんボルト|みずびたし|どくどく|なまける:32/0/0/32/0/0:でんきにかえる", "M-6");
        let mut dfn = build_poke(&mut p, "ブラッキー@たべのこし:おだやか:イカサマ|あくび|まもる|つきのひかり:32/0/0/0/32/0:せいしんりょく", "M-6");
        let p = p;
        let mut ob = OpponentBelief::new("M-6");
        let i = ob.ensure(&p, "ブラッキー", None, None).unwrap();
        let sub = dfn.clone();
        let mv = att.moves.iter().find(|m| p.intern.resolve(m.name) == "10まんボルト").unwrap().clone();
        let mut f = Field::default();
        att.electromorphosis_charged = true;
        let mut cb = |k: u8| if k == 0 { 0.99 } else { 0.0 };
        let d = calc_damage(&p, &mut att, &mut dfn, &mv, &mut f, false, Some(0.5), None, &mut cb);
        let frac = (d as f64 * 100.0 / dfn.max_hp as f64).round();
        att.electromorphosis_charged = true;
        let pb = &mut ob.species[i].1;
        pb.observe_damage(&p, &mut att, &mv, frac, &mut f, false, &mut Z, Some(&sub), None);
        let tpl = get_pokemon_template(&p, "ブラッキー", "M-6").unwrap();
        let pool = vec![pb_(0.5, "いじっぱり", [0, 32, 0, 0, 2, 32]), pb_(0.5, "おだやか", [32, 0, 0, 0, 32, 0])];
        let w = pb.pool_weights(&p, &tpl, &pool).to_vec();
        assert!(pb.dmg_obs.last().unwrap().other.electromorphosis_charged);
        assert!(w[1] > 0.9, "{:?}", w);
    }

    #[test]
    fn r4mcts_控えの再サンプルは技のあるシーズンのテンプレ() {
        let p = Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"));
        let mut c = TplCache::default();
        assert!(c.get(&p, "ケンタロス:水", "M-6").map_or(false, |t| t.top_moves.is_empty()));
        assert!(c.get_playable(&p, "ケンタロス:水", "M-6").map_or(false, |t| !t.top_moves.is_empty()));
        assert!(c.get_playable(&p, "ガブリアス", "M-6").map_or(false, |t| !t.top_moves.is_empty()));
    }
}
