//! simulator/belief.py の移植（決定化サンプリングに必要な部分＋observe_damage）。
//!
//! パリティ規約 #3: `known_moves` は Python では set なので反復順が PYTHONHASHSEED 依存。
//! ここでは sorted（種名のコードポイント順＝UTF-8バイト順）に正規化する。
//! ハーネス側の Python も同じく sorted に monkeypatch する（本番Pythonは無変更）。
use crate::damage::{calc_damage, DMove, Field};
use crate::interner::Sym;
use crate::oppview::{round3, OppView};
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

#[derive(Clone, Debug)]
pub struct PokemonBelief {
    pub name: String,
    pub move_prior: Vec<(String, f64)>,
    pub item_prior: Vec<(String, f64)>,
    pub ability_prior: Vec<(String, f64)>,
    /// set → sorted 正規化（パリティ規約 #3）
    pub known_moves: Vec<String>,
    pub known_item: Option<String>,
    pub known_ability: Option<String>,
    pub cands: Vec<Cand>,
    pub prior: Vec<f64>,
    pub post: Vec<f64>,
}

fn ev_key(e: &EvEntry) -> (i64, i64, i64, i64, i64, i64) {
    (e.h, e.a, e.b, e.c, e.d, e.s)
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
            known_ability,
            cands,
            prior,
            post,
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
        if let Some(i) = k.known_item {
            let s = pack.intern.resolve(i).to_string();
            if !s.is_empty() {
                self.known_item = Some(s);
            }
        }
        if let Some(a) = k.known_ability {
            let s = pack.intern.resolve(a).to_string();
            if !s.is_empty() {
                self.known_ability = Some(s);
            }
        }
    }

    /// observe_damage: 16ロールで観測割合を再現できた候補の尤度でベイズ更新
    pub fn observe_damage(
        &mut self,
        pack: &Pack,
        attacker: &mut Poke,
        mv: &DMove,
        observed_fraction: f64,
        field: &mut Field,
        critical: bool,
        rng: &mut dyn BRng,
    ) -> bool {
        let rs = rolls();
        let mut liks: Vec<f64> = Vec::with_capacity(self.cands.len());
        for c in self.cands.iter_mut() {
            let mut hit = 0i64;
            for rr in rs.iter() {
                let mut cb = |kind: u8| match kind {
                    0 => rng.random(),
                    _ => rng.choice(16) as f64,
                };
                let dmg = calc_damage(
                    pack,
                    attacker,
                    &mut c.defender,
                    mv,
                    field,
                    critical,
                    Some(*rr),
                    None,
                    &mut cb,
                );
                if round3(dmg as f64 / c.defender.max_hp as f64) == observed_fraction {
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
        let tpl = get_pokemon_template(pack, name, &self.season)?;
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
    ) -> bool {
        let name = pack.intern.resolve(defender_name).to_string();
        let i = match self.ensure(pack, &name, None, None) {
            None => return false,
            Some(i) => i,
        };
        let mut b = std::mem::replace(&mut self.species[i].1, PokemonBelief::empty());
        let r = b.observe_damage(pack, attacker, mv, observed_fraction, field, critical, rng);
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
            known_ability: None,
            cands: Vec::new(),
            prior: Vec::new(),
            post: Vec::new(),
        }
    }
}

/// SearchAI._tpl_cache 相当
#[derive(Default)]
pub struct TplCache {
    map: HashMap<String, Option<Template>>,
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
}
