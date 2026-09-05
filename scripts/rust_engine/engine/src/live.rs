//! ライブ提案経路（product3 /suggest・/complete）のスコアリング核。
//!
//! Python 正本:
//!   `_product3.surrogate_score(specs)`  … パネル20面ぶんの encode_state(905) を作り net で評価
//!   `_matchup_surrogate.matchup_feats`  … 6x6 の `_bestdmg` 行列（calc_damage roll=0.85）
//!
//! ここでは **集約（statistics.mean / net forward）は行わない**。Python 側が既存コードで
//! 集約するため、Rust は「その手前の中間量（905次元ベクトル・ダメージ行列）」だけを返す。
//! → 丸め順の差が原理的に入らず、ビット一致が構成的に保証される。
//!
//! パネル個体は Python と同じく **永続・可変**（calc_damage が半減きのみを消費する副作用が
//! 後続候補の採点に持ち越される＝Python の実挙動）。順序も Python と同一に保つ。
use crate::ai::{effective_speed, select_party};
use crate::battle::Side;
use crate::belief::OpponentBelief;
use crate::damage::{calc_damage, Field};
use crate::features::{encode_state, DmgMemo, FeatTables};
use crate::pack::{Cat, Pack};
use crate::poke::{build_poke, mega_evolve_poke, Poke};
use crate::rng::BRng;

/// ライブ経路は乱数を消費しない（Python 側も消費しないことを実測で確認済み）。
/// 消費したら panic → PyO3 経由で Python フォールバックに落ちる。
pub struct NoRng;
impl BRng for NoRng {
    fn random(&mut self) -> f64 {
        panic!("live: 乱数を消費した（Python 経路と挙動が異なる）");
    }
    fn choice(&mut self, _n: usize) -> usize {
        panic!("live: choice を消費した");
    }
    fn randint(&mut self, _a: i64, _b: i64) -> i64 {
        panic!("live: randint を消費した");
    }
    fn choices(&mut self) -> i64 {
        panic!("live: choices を消費した");
    }
}

pub struct Live {
    /// `_product3._W["panel"]`（build_from_spec のみ・メガ進化しない）
    pub panel_net: Vec<Vec<Poke>>,
    /// `_matchup_surrogate.build_party`（メガ石持ちは全員メガ進化済み）
    pub panel_rich: Vec<Vec<Poke>>,
    /// パネル個体の実効素早さ（`_setup_panel` 時点の値を固定保持＝Python の spd dict）
    pub panel_spd: Vec<Vec<i64>>,
    pub panel_hp: Vec<Vec<i64>>,
    /// `EnsembleScorer.field`（永続 BattleField・rich 側のみ共有）
    pub rich_field: Field,
    pub ft: FeatTables,
    pub memo: DmgMemo,
    pub season: String,
}

impl Live {
    pub fn setup(pack: &mut Pack, panel_specs: &[Vec<String>], season: &str) -> Live {
        let mut panel_net = Vec::with_capacity(panel_specs.len());
        let mut panel_rich = Vec::with_capacity(panel_specs.len());
        for sp in panel_specs {
            panel_net.push(sp.iter().map(|s| build_poke(pack, s, season)).collect::<Vec<_>>());
            let mut mons: Vec<Poke> = Vec::with_capacity(sp.len());
            for s in sp {
                let mut p = build_poke(pack, s, season);
                if p.mega.is_some() {
                    mega_evolve_poke(pack, &mut p);
                }
                mons.push(p);
            }
            panel_rich.push(mons);
        }
        let field = Field::default();
        let panel_spd: Vec<Vec<i64>> = panel_rich
            .iter()
            .map(|pm| pm.iter().map(|m| effective_speed(pack, m, &field)).collect())
            .collect();
        let panel_hp: Vec<Vec<i64>> =
            panel_rich.iter().map(|pm| pm.iter().map(|m| m.max_hp).collect()).collect();
        let ft = FeatTables::build(pack);
        Live {
            panel_net,
            panel_rich,
            panel_spd,
            panel_hp,
            rich_field: field,
            ft,
            memo: DmgMemo::default(),
            season: season.to_string(),
        }
    }

    /// `_product3.surrogate_score` の encode_state までを再現し、パネル数ぶんの905次元を返す。
    /// net forward と statistics.mean は Python 側が行う。
    pub fn panel_states(&mut self, pack: &mut Pack, specs: &[String]) -> Vec<Vec<f64>> {
        let season = self.season.clone();
        let mut a6: Vec<Poke> = specs.iter().map(|s| build_poke(pack, s, &season)).collect();
        let mut out = Vec::with_capacity(self.panel_net.len());
        for pi in 0..self.panel_net.len() {
            let mut b6 = std::mem::take(&mut self.panel_net[pi]);
            let packr: &Pack = pack;
            // sa = select_party(A, B) → sb = select_party(B, A)（この順で両者が変異する）
            let sa = {
                let mut r = NoRng;
                let mut sr = || -> f64 { panic!("live: srng を消費した") };
                select_party(packr, &mut a6, &mut b6, 3, 0.0, 50.0, &mut r, &mut sr)
            };
            let sb = {
                let mut r = NoRng;
                let mut sr = || -> f64 { panic!("live: srng を消費した") };
                select_party(packr, &mut b6, &mut a6, 3, 0.0, 50.0, &mut r, &mut sr)
            };
            let p1: Vec<Poke> = sa.iter().map(|&i| std::mem::take(&mut a6[i])).collect();
            let p2: Vec<Poke> = sb.iter().map(|&i| std::mem::take(&mut b6[i])).collect();
            let mut sides = [
                Side { party: p1, active_idx: 0, ..Default::default() },
                Side { party: p2, active_idx: 0, ..Default::default() },
            ];
            crate::search::set_belief(&mut sides[0], OpponentBelief::new(&season));
            crate::search::set_belief(&mut sides[1], OpponentBelief::new(&season));
            let mut field = Field::default();
            self.memo.begin();
            let x = encode_state(
                packr,
                &self.ft,
                &mut sides,
                0,
                &mut field,
                &mut self.memo,
                &mut NoRng,
            );
            self.memo.end();
            // 変異を元の6体へ書き戻す（Python は同一オブジェクト参照＝副作用が残る）
            for (k, &i) in sa.iter().enumerate() {
                a6[i] = std::mem::take(&mut sides[0].party[k]);
            }
            for (k, &i) in sb.iter().enumerate() {
                b6[i] = std::mem::take(&mut sides[1].party[k]);
            }
            self.panel_net[pi] = b6;
            out.push(x);
        }
        out
    }

    /// `_matchup_surrogate._bestdmg` の 6x6 行列（A→B, B→A）をパネル数ぶん返す。
    /// 併せて A 側の実効素早さ・最大HPを返す（Python 側の集約に使う）。
    #[allow(clippy::type_complexity)]
    pub fn rich_matrices(
        &mut self,
        pack: &mut Pack,
        specs: &[String],
    ) -> (Vec<i64>, Vec<i64>, Vec<(Vec<i64>, Vec<i64>)>) {
        let season = self.season.clone();
        let mut a6: Vec<Poke> = Vec::with_capacity(specs.len());
        for s in specs {
            let mut p = build_poke(pack, s, &season);
            if p.mega.is_some() {
                mega_evolve_poke(pack, &mut p);
            }
            a6.push(p);
        }
        let packr: &Pack = pack;
        let spd_a: Vec<i64> =
            a6.iter().map(|m| effective_speed(packr, m, &self.rich_field)).collect();
        let hp_a: Vec<i64> = a6.iter().map(|m| m.max_hp).collect();
        let mut mats = Vec::with_capacity(self.panel_rich.len());
        for pi in 0..self.panel_rich.len() {
            let mut b6 = std::mem::take(&mut self.panel_rich[pi]);
            let na = a6.len();
            let nb = b6.len();
            let mut dab = vec![0i64; na * nb];
            let mut dba = vec![0i64; nb * na];
            for i in 0..na {
                for j in 0..nb {
                    dab[i * nb + j] = best_dmg(packr, &mut a6[i], &mut b6[j], &mut self.rich_field);
                }
            }
            for j in 0..nb {
                for i in 0..na {
                    dba[j * na + i] = best_dmg(packr, &mut b6[j], &mut a6[i], &mut self.rich_field);
                }
            }
            self.panel_rich[pi] = b6;
            mats.push((dab, dba));
        }
        (spd_a, hp_a, mats)
    }
}

/// `_matchup_surrogate._bestdmg`: 攻撃技のうち最大ダメージ（roll=0.85・急所なし）
///
/// calc_damage は半減きのみ消費で defender.item=None、充電技で attacker.charged=false と
/// 実体を書き換える（対戦本体では正しい）。ここは 6x6 行列を同じ Poke を使い回して埋めるため、
/// 保護しないと 1 回目の計算で相手のきのみが消え 2 回目以降が「きのみ無し」になる。
/// Python 側 `_matchup_surrogate._dmg_safe` と同じ扱いにしてパリティを保つ。
fn best_dmg(pack: &Pack, a: &mut Poke, b: &mut Poke, field: &mut Field) -> i64 {
    let mut best = 0i64;
    let moves = a.moves.clone();
    let (b_item, a_item) = (b.item, a.item);
    let (a_ch, a_em) = (a.charged, a.electromorphosis_charged);
    for mv in &moves {
        if (mv.category == Cat::Physical || mv.category == Cat::Special)
            && mv.power.unwrap_or(0) > 0
        {
            let d =
                calc_damage(pack, a, b, mv, field, false, Some(0.85), None, &mut |_| {
                    panic!("live: calc_damage が乱数を消費した")
                });
            b.item = b_item;
            a.item = a_item;
            a.charged = a_ch;
            a.electromorphosis_charged = a_em;
            if d > best {
                best = d;
            }
        }
    }
    best
}
