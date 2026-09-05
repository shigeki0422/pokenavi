//! simulator/opponent_view.py の移植（ログ文字列は生成しない＝状態更新のみ）。
use crate::interner::Sym;
use crate::pack::Ty;
use crate::poke::Poke;

#[derive(Clone, Debug)]
pub struct DamageObs {
    pub mv: Sym,
    pub attacker: Option<Sym>,
    pub fraction: f64,
}

#[derive(Clone, Debug)]
pub struct PokeKnowledge {
    pub name: Sym,
    pub previewed: bool,
    pub seen: bool,
    pub type1: Option<Ty>,
    pub type2: Option<Ty>,
    pub known_moves: Vec<Sym>,
    pub known_item: Option<Sym>,
    pub known_ability: Option<Sym>,
    pub threat_alert: bool,
    pub hp_fraction: f64,
    pub damage_log: Vec<DamageObs>,
}

impl PokeKnowledge {
    fn new(name: Sym) -> Self {
        PokeKnowledge {
            name,
            previewed: false,
            seen: false,
            type1: None,
            type2: None,
            known_moves: Vec::new(),
            known_item: None,
            known_ability: None,
            threat_alert: false,
            hp_fraction: 1.0,
            damage_log: Vec::new(),
        }
    }
}

#[derive(Clone, Debug, Default)]
pub struct OppView {
    /// Python の dict（挿入順）と同じ順序で保持する
    pub pokemon: Vec<PokeKnowledge>,
}

/// Python の round(x, 3)（正確な10進丸め＝偶数丸め）を再現する
pub fn round3(x: f64) -> f64 {
    format!("{:.3}", x).parse::<f64>().unwrap()
}

impl OppView {
    fn get(&mut self, name: Sym) -> &mut PokeKnowledge {
        if let Some(i) = self.pokemon.iter().position(|k| k.name == name) {
            return &mut self.pokemon[i];
        }
        self.pokemon.push(PokeKnowledge::new(name));
        let n = self.pokemon.len() - 1;
        &mut self.pokemon[n]
    }

    pub fn team_preview(&mut self, party: &[(Sym, Ty, Option<Ty>, Ty, Option<Ty>)]) {
        // 要素: (name, base_type1, base_type2, type1, type2)
        for &(name, bt1, bt2, t1, t2) in party {
            let k = self.get(name);
            k.previewed = true;
            if k.type1.is_none() {
                // Python: base が falsy（None/空）なら現タイプにフォールバック
                k.type1 = Some(if bt1 == crate::pack::NO_TY { t1 } else { bt1 });
                k.type2 = if bt2.is_some() { bt2 } else { t2 };
            }
        }
    }

    pub fn on_anticipation(&mut self, opp_name: Sym) {
        let k = self.get(opp_name);
        if k.threat_alert {
            return;
        }
        k.threat_alert = true;
    }

    pub fn on_enter(&mut self, p: &Poke) {
        let (t1, t2) = (p.type1, p.type2);
        let k = self.get(p.name);
        if k.seen {
            return;
        }
        k.seen = true;
        k.type1 = Some(t1);
        k.type2 = t2;
    }

    pub fn on_move(&mut self, poke_name: Sym, move_name: Sym) {
        let k = self.get(poke_name);
        if k.known_moves.contains(&move_name) {
            return;
        }
        k.known_moves.push(move_name);
    }

    pub fn on_item(&mut self, poke_name: Sym, item: Sym) {
        let k = self.get(poke_name);
        if k.known_item == Some(item) {
            return;
        }
        k.known_item = Some(item);
    }

    pub fn on_ability(&mut self, poke_name: Sym, ability: Sym) {
        let k = self.get(poke_name);
        if k.known_ability == Some(ability) {
            return;
        }
        k.known_ability = Some(ability);
    }

    pub fn on_hp_change(
        &mut self,
        poke_name: Sym,
        cur_hp: i64,
        max_hp: i64,
        damage: i64,
        move_name: Option<Sym>,
        attacker_name: Option<Sym>,
    ) {
        if max_hp <= 0 {
            return;
        }
        let k = self.get(poke_name);
        k.hp_fraction = f64::max(0.0, round3(cur_hp as f64 / max_hp as f64));
        if damage > 0 {
            if let Some(mv) = move_name {
                let frac = round3(damage as f64 / max_hp as f64);
                k.damage_log.push(DamageObs { mv, attacker: attacker_name, fraction: frac });
            }
        }
    }
}
