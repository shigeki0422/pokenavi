//! simulator/search_ai.py（本番構成 = mcts/regret/fast/qselect/downside-guard）の移植と、
//! simulator/alphazero.py の legal_actions_indexed / train_az2._net_ai の構成を写す。
use crate::ai::{
    self, filter_by_pp, filter_valid_by_lock, forced_charging_action, is_hazard, is_trapped,
    struggle, HazCtx,
};
use crate::battle::{ActKind, Action, Side};
use crate::damage::Field;
use crate::features::{encode_state_into, DmgMemo, FeatTables};
use crate::net::{NetScratch, NetW};
use crate::pack::{Cat, Pack};
use crate::rng::BRng;

pub const ACTION_DIM: usize = 12;

#[inline]
pub fn action_index(a: &Action) -> usize {
    if a.kind == ActKind::Switch {
        return 8 + a.switch_to as usize;
    }
    if a.move_idx >= 0 {
        return a.move_idx as usize + if a.do_mega { 4 } else { 0 };
    }
    11
}

/// alphazero.legal_actions_indexed（方策マスク用の列挙。設置技の除外は無い）
pub fn legal_actions_indexed(pack: &Pack, me_s: &Side, op_s: &Side) -> Vec<usize> {
    let me = me_s.active();
    let can_mega = me.mega.is_some() && !me.mega_evolved && !me_s.mega_used;
    let valid = filter_valid_by_lock(me);
    let pp_valid = filter_by_pp(&valid, me);
    let mut out = Vec::with_capacity(12);
    if pp_valid.is_empty() {
        out.push(11);
    } else {
        for (i, _) in &pp_valid {
            out.push(*i);
            if can_mega {
                out.push(4 + *i);
            }
        }
    }
    if !is_trapped(pack, me, Some(op_s.active())) {
        for (j, p) in me_s.party.iter().enumerate() {
            if j != me_s.active_idx && p.is_alive && j < 3 {
                out.push(8 + j);
            }
        }
    }
    out
}

/// SearchAI._candidate_actions
pub fn candidate_actions(pack: &Pack, me_s: &Side, op_s: &Side, field: &Field, collapse_mega: bool) -> Vec<Action> {
    let me = me_s.active();
    let can_mega = me.mega.is_some() && !me.mega_evolved && !me_s.mega_used;
    let mega_flags: &[bool] = if can_mega {
        if collapse_mega {
            &[true]
        } else {
            &[true, false]
        }
    } else {
        &[false]
    };
    let valid = filter_valid_by_lock(me);
    let pp_valid = filter_by_pp(&valid, me);
    let hz = HazCtx::of(op_s);
    let mut move_cands: Vec<(usize, crate::damage::DMove)> = pp_valid
        .iter()
        .filter(|(_, mv)| {
            !(mv.category == Cat::Status
                && is_hazard(pack, mv.name)
                && ai::hazard_value(pack, mv.name, &hz, field) <= 0.0)
        })
        .cloned()
        .collect();
    if move_cands.is_empty() {
        move_cands = pp_valid.clone();
    }
    let mut out: Vec<Action> = Vec::with_capacity(12);
    if pp_valid.is_empty() {
        for &dm in mega_flags {
            out.push(Action {
                kind: ActKind::Move,
                mv: Some(struggle(pack)),
                move_idx: -1,
                switch_to: -1,
                do_mega: dm,
            });
        }
    } else {
        for (i, mv) in &move_cands {
            for &dm in mega_flags {
                out.push(Action {
                    kind: ActKind::Move,
                    mv: Some(mv.clone()),
                    move_idx: *i as i64,
                    switch_to: -1,
                    do_mega: dm,
                });
            }
        }
    }
    if !is_trapped(pack, me, Some(op_s.active())) {
        for (i, p) in me_s.party.iter().enumerate() {
            if i != me_s.active_idx && p.is_alive {
                out.push(Action {
                    kind: ActKind::Switch,
                    mv: None,
                    move_idx: 0,
                    switch_to: i as i64,
                    do_mega: false,
                });
            }
        }
    }
    out
}

/// search_ai.py `_type_immune_move`。攻撃技が相手にタイプで無効か（execute_move のタイプ無効判定と同じ）。
/// メガ進化と同時の技はメガ後の特性で実効タイプを決める。相手の特性による無効は非公開情報なので見ない。
pub fn type_immune_move(pack: &Pack, me: &crate::poke::Poke, a: &Action, opp: &crate::poke::Poke, field: &Field) -> bool {
    if a.kind != ActKind::Move || a.move_idx < 0 {
        return false;
    }
    let mv = match &a.mv {
        Some(m) => m,
        None => return false,
    };
    if mv.category == Cat::Status {
        return false;
    }
    let mut ab = me.ability;
    if a.do_mega && !me.mega_evolved {
        if let Some(md) = &me.mega {
            if let Some(x) = &md.ability {
                if !x.is_empty() {
                    if let Some(sy) = pack.intern.get(x) {
                        ab = sy;
                    }
                }
            }
        }
    }
    let t = crate::damage::effective_move_type_ab(pack, me, ab, mv, field);
    if pack.eff(t, opp.type1, opp.type2) != 0.0 {
        return false;
    }
    // きもったま（scrappy_override と同じ条件を差し替え後の特性で見る）
    !(ab == pack.sy.ab.きもったま
        && (t == pack.tc.ノーマル || t == pack.tc.かくとう)
        && opp.has_type(pack.tc.ゴースト))
}

/// search_ai.py `_prune_immune_moves`。他に技の候補が無いとき（こだわり固定など）は外さない。
pub fn prune_immune_moves(pack: &Pack, me_s: &Side, op_s: &Side, field: &Field, cands: Vec<Action>) -> Vec<Action> {
    let opp = op_s.active();
    let me = me_s.active();
    if !opp.is_alive {
        return cands;
    }
    let imm: Vec<bool> = cands.iter().map(|a| type_immune_move(pack, me, a, opp, field)).collect();
    if !imm.iter().any(|&x| x) {
        return cands;
    }
    if !cands.iter().zip(imm.iter()).any(|(a, &im)| a.kind == ActKind::Move && !im) {
        return cands;
    }
    cands.into_iter().zip(imm).filter(|(_, im)| !*im).map(|(a, _)| a).collect()
}

/// search_ai.py `_futile_move`: 必ず失敗する手・成功しても効果の無い手か（公開情報だけで判定する）
pub fn futile_move(pack: &Pack, me_s: &Side, op_s: &Side, mv: &crate::damage::DMove, field: &Field) -> bool {
    let me = me_s.active();
    let opp = op_s.active();
    let n = pack.intern.resolve(mv.name);
    let tc = &pack.tc;
    let st = &pack.sy.st;
    if mv.category == Cat::Status && me.taunt_count > 0 {
        return true;
    }
    if me.throat_chop_count > 0 && pack.flags(mv.name).sound {
        return true;
    }
    if (n == "ねこだまし" || n == "であいがしら") && me.turns_out > 0 {
        return true;
    }
    if (n == "ほえる" || n == "ふきとばし")
        && !op_s.party.iter().enumerate().any(|(i, p)| p.is_alive && i != op_s.active_idx)
    {
        return true;
    }
    if n == "でんこうそうげき" && !me.has_type(tc.でんき) {
        return true;
    }
    if n == "もえつきる" && !me.has_type(tc.ほのお) {
        return true;
    }
    if n == "アイアンローラー"
        && !(field.grassy_terrain || field.electric_terrain || field.psychic_terrain || field.misty_terrain)
    {
        return true;
    }
    if n == "ゲップ" && !me.ate_berry {
        return true;
    }
    if (n == "いびき" || n == "ねごと") && me.status != Some(st.sleep) {
        return true;
    }
    if n == "デカハンマー" && me.deka_last {
        return true;
    }
    if n == "とっておき" {
        let others: Vec<_> = me.moves.iter().map(|m| m.name).filter(|&x| pack.intern.resolve(x) != "とっておき").collect();
        if others.is_empty() || !others.iter().all(|x| me.used_moves.contains(x)) {
            return true;
        }
    }
    const HEAL: [&str; 11] = ["じこさいせい", "はねやすめ", "なまける", "タマゴうみ", "ミルクのみ", "つきのひかり", "あさのひざし",
                              "こうごうせい", "すなあつめ", "かいふくしれい", "ねむる"];
    if HEAL.contains(&n) && me.hp >= me.max_hp {
        return true;
    }
    let boost: &[u8] = match n {
        "つるぎのまい" => &[0],
        "わるだくみ" => &[2],
        "りゅうのまい" | "ギアチェンジ" => &[0, 4],
        "めいそう" => &[2, 3],
        "ちょうのまい" => &[2, 3, 4],
        "はいすいのじん" => &[0, 1, 2, 3, 4],
        "コスモパワー" => &[1, 3],
        "てっぺき" | "コットンガード" | "とける" | "たてこもる" => &[1],
        "ビルドアップ" => &[0, 1],
        "こうそくいどう" | "ロックカット" => &[4],
        "ドわすれ" => &[3],
        "とぐろをまく" => &[0, 1, 5],
        "ちいさくなる" | "かげぶんしん" => &[6],
        "せいちょう" => &[0, 2],
        _ => &[],
    };
    if !boost.is_empty() {
        let cap = if me.ability == pack.sy.l.あまのじゃく { -6 } else { 6 };
        if boost.iter().all(|&k| me.stage(k) == cap) {
            return true;
        }
    }
    if (n == "リフレクター" && me_s.reflect) || (n == "ひかりのかべ" && me_s.light_screen) {
        return true;
    }
    if n == "オーロラベール"
        && (me_s.aurora_veil || crate::damage::effective_weather(pack, field, Some(me)) != Some(pack.sy.we.hail))
    {
        return true;
    }
    if n == "おいかぜ" && me_s.tailwind {
        return true;
    }
    if n == "みがわり" && (me.substitute_hp > 0 || me.hp <= me.max_hp / 4) {
        return true;
    }
    if !opp.is_alive {
        return false;
    }
    let stv = match n {
        "でんじは" | "しびれごな" | "へびにらみ" => Some(0),
        "おにび" => Some(1),
        "どくどく" | "どくのこな" => Some(2),
        "ねむりごな" | "さいみんじゅつ" | "うたう" | "キノコのほうし" | "あくび" => Some(3),
        _ => None,
    };
    if let Some(k) = stv {
        if opp.status.is_some() || op_s.safeguard > 0 {
            return true;
        }
        if n == "あくび" && opp.yawn_count != 0 {
            return true;
        }
        if matches!(n, "しびれごな" | "ねむりごな" | "どくのこな" | "キノコのほうし") && opp.has_type(tc.くさ) {
            return true;
        }
        if k == 0 && (opp.has_type(tc.でんき) || (n == "でんじは" && opp.has_type(tc.じめん))) {
            return true;
        }
        if k == 1 && opp.has_type(tc.ほのお) {
            return true;
        }
        if k == 2 && me.ability != pack.sy.l.ふしょく && (opp.has_type(tc.どく) || opp.has_type(tc.はがね)) {
            return true;
        }
    }
    if n == "ちょうはつ" && opp.taunt_count > 0 {
        return true;
    }
    if n == "アンコール" && (opp.encore_count > 0 || opp.last_used_move.is_none()) {
        return true;
    }
    if n == "やどりぎのタネ" && (opp.seeded || opp.has_type(tc.くさ)) {
        return true;
    }
    false
}

/// search_ai.py `_known_immune`: 開示済みの ふうせん・特性 で無効な攻撃技か
fn known_immune(pack: &Pack, me: &crate::poke::Poke, a: &Action, opp: &crate::poke::Poke,
                kn: &crate::oppview::PokeKnowledge, field: &Field) -> bool {
    let mv = match &a.mv {
        Some(m) => m,
        None => return false,
    };
    let mut ab = me.ability;
    if a.do_mega && !me.mega_evolved {
        if let Some(md) = &me.mega {
            if let Some(x) = &md.ability {
                if !x.is_empty() {
                    if let Some(sy) = pack.intern.get(x) {
                        ab = sy;
                    }
                }
            }
        }
    }
    let t = crate::damage::effective_move_type_ab(pack, me, ab, mv, field);
    if t == pack.tc.じめん && kn.known_item == Some(pack.sy.it.ふうせん) && !kn.item_lost && !opp.grounded {
        return true;
    }
    if let Some(ka) = kn.known_ability {
        let mut me2 = me.clone();
        me2.ability = ab;
        if !crate::damage::should_ignore_ability(pack, &me2) {
            let mut o2 = opp.clone();
            o2.ability = ka;
            return crate::damage::check_move_immunity(pack, &o2, t, mv.name)
                && !crate::damage::scrappy_override(pack, &me2, t, &o2);
        }
    }
    false
}

/// 監査200 C: 持ち物が無いと判明した相手への ポルターガイスト・連続の みちづれ（search_ai.py `_futile_move` の _FIX200_ON 部分）
pub fn futile_move_200(pack: &Pack, me_s: &Side, op_s: &Side, mv: &crate::damage::DMove) -> bool {
    let me = me_s.active();
    let opp = op_s.active();
    let l = &pack.sy.l;
    if mv.name == l.みちづれ && me.destiny_bond_last_turn {
        return true;
    }
    if mv.name == l.ポルターガイスト && opp.is_alive {
        if let Some(k) = me_s.opp_view.find(opp.name) {
            if k.item_lost {
                return true;
            }
        }
    }
    false
}

/// search_ai.py `_hazard_full`: 相手側に設置済み（上限まで）の ステルスロック・まきびし3層・どくびし2層・ねばねばネット
pub fn hazard_full(pack: &Pack, op_s: &Side, mv: &crate::damage::DMove, field: &Field) -> bool {
    let i = op_s.field_idx;
    match pack.intern.resolve(mv.name) {
        "ステルスロック" => field.stealth_rock[i],
        "まきびし" => field.spikes[i] >= 3,
        "どくびし" => field.toxic_spikes[i] >= 2,
        "ねばねばネット" => field.sticky_web[i],
        _ => false,
    }
}

/// search_ai.py `_prune_futile_moves`。技の候補が残らないときは外さない。
pub fn prune_futile_moves(pack: &Pack, me_s: &Side, op_s: &Side, field: &Field, cands: Vec<Action>) -> Vec<Action> {
    prune_futile_moves_opt(pack, me_s, op_s, field, cands, crate::ai::fix200_env())
}

pub fn prune_futile_moves_opt(pack: &Pack, me_s: &Side, op_s: &Side, field: &Field, cands: Vec<Action>, fix200: bool) -> Vec<Action> {
    prune_futile_moves_opt2(pack, me_s, op_s, field, cands, fix200, crate::ai::fixhz_env())
}

pub fn prune_futile_moves_opt2(pack: &Pack, me_s: &Side, op_s: &Side, field: &Field, cands: Vec<Action>, fix200: bool,
                               fixhz: bool) -> Vec<Action> {
    let me = me_s.active();
    if !me.is_alive {
        return cands;
    }
    let opp = op_s.active();
    let kn = me_s.opp_view.find(opp.name);
    let bad: Vec<bool> = cands
        .iter()
        .map(|a| {
            if a.kind != ActKind::Move || a.move_idx < 0 {
                return false;
            }
            let mv = match &a.mv {
                Some(m) => m,
                None => return false,
            };
            let mut f = futile_move(pack, me_s, op_s, mv, field) || (fix200 && futile_move_200(pack, me_s, op_s, mv))
                || (fixhz && hazard_full(pack, op_s, mv, field));
            if !f && mv.category != Cat::Status && opp.is_alive {
                if let Some(k) = kn {
                    f = known_immune(pack, me, a, opp, k, field);
                }
            }
            f
        })
        .collect();
    if !bad.iter().any(|&x| x) || !cands.iter().zip(bad.iter()).any(|(a, &b)| a.kind == ActKind::Move && !b) {
        return cands;
    }
    cands.into_iter().zip(bad).filter(|(_, b)| !*b).map(|(a, _)| a).collect()
}

/// search_ai.py `_resample_sleep`: 相手のねむりカウンタを、見えている情報（眠ってから行動しようとした回数・ねむる か）と
/// 整合する値から引き直す
pub fn resample_sleep(pack: &Pack, poke: &mut crate::poke::Poke, rng: &mut dyn BRng) {
    let acts = poke.sleep_acts;
    let dec = if poke.ability == pack.sy.l.はやおき { 2 } else { 1 };
    let opts: &[i64] = if poke.sleep_rest { &[3] } else { &[2, 3, 4] };
    let feas: Vec<i64> = opts.iter().copied().filter(|c| c - dec * acts > 0).collect();
    if feas.is_empty() {
        return;
    }
    let c0 = if feas.len() == 1 { feas[0] } else { feas[rng.choice(feas.len())] };
    poke.sleep_count = c0 - dec * acts;
}

/// train_az2._net_ai の nefn: (policy over legal, value=P(A勝))
pub struct NetCtx {
    pub ft: FeatTables,
    pub memo: DmgMemo,
    pub scratch: NetScratch,
    pub x: Vec<f64>,
}

impl NetCtx {
    pub fn new(pack: &Pack) -> NetCtx {
        NetCtx {
            ft: FeatTables::build(pack),
            memo: DmgMemo::default(),
            scratch: NetScratch::default(),
            x: Vec::with_capacity(905),
        }
    }
}

/// nefn(A,B,f): L=legal_actions_indexed(A,B,f) → net.evaluate(encode_state(A,B,f), L or [0])
pub fn net_eval(
    pack: &Pack,
    net: &NetW,
    ctx: &mut NetCtx,
    sides: &mut [Side; 2],
    first: usize,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> (Vec<(usize, f64)>, f64) {
    let legal = legal_actions_indexed(pack, &sides[first], &sides[1 - first]);
    let mut x = std::mem::take(&mut ctx.x);
    encode_state_into(pack, &ctx.ft, sides, first, field, &mut ctx.memo, rng, &mut x);
    let l: Vec<usize> = if legal.is_empty() { vec![0] } else { legal.clone() };
    let (p, v) = net.evaluate(&x, &l, &mut ctx.scratch);
    crate::sim::eval_log_push(crate::statec::f64_hash(&x), v);
    crate::sim::eval_x_push(&x);
    ctx.x = x;
    let pol: Vec<(usize, f64)> = if legal.is_empty() {
        Vec::new()
    } else {
        l.iter().copied().zip(p.iter().copied()).collect()
    };
    (pol, v)
}

/// G1/G2 ゲート用: x（905次元）も返す net_eval
pub fn net_eval_x(
    pack: &Pack,
    net: &NetW,
    ctx: &mut NetCtx,
    sides: &mut [Side; 2],
    first: usize,
    field: &mut Field,
    rng: &mut dyn BRng,
) -> (Vec<f64>, Vec<(usize, f64)>, f64) {
    let legal = legal_actions_indexed(pack, &sides[first], &sides[1 - first]);
    let mut x = Vec::with_capacity(905);
    encode_state_into(pack, &ctx.ft, sides, first, field, &mut ctx.memo, rng, &mut x);
    let l: Vec<usize> = if legal.is_empty() { vec![0] } else { legal.clone() };
    let (p, v) = net.evaluate(&x, &l, &mut ctx.scratch);
    let pol: Vec<(usize, f64)> = if legal.is_empty() {
        Vec::new()
    } else {
        l.iter().copied().zip(p.iter().copied()).collect()
    };
    (x, pol, v)
}


// ══════════════════════════════════════════════════════════════════════════
//  SearchAI（本番構成: mcts=True / mcts_select="regret" / mcts_fast=True /
//            qselect / downside_guard / collapse_mega / HIDDEN_SELECTION=on）
// ══════════════════════════════════════════════════════════════════════════
use crate::battle::{Battle, BeliefSlot};
use crate::belief::{OpponentBelief, TplCache};
use crate::cpyrng::CpyRandom;
use crate::pysum::pysum;
use std::collections::HashMap;

#[derive(Default, Clone)]
struct Node {
    n: [HashMap<usize, i64>; 2],
    w: [HashMap<usize, f64>; 2],
    p: [HashMap<usize, f64>; 2],
    r: [HashMap<usize, f64>; 2],
    children: HashMap<(usize, usize), usize>,
    total: i64,
    expanded: bool,
    v: Option<f64>,
}

/// _sample_opp_config の1体分
#[derive(Clone, Debug)]
pub struct SampledCfg {
    pub ev: crate::pack::EvEntry,
    pub nature: String,
    pub item: Option<String>,
    pub ability: String,
    pub moves: Vec<String>,
}

pub struct SearchAI {
    pub season: String,
    pub rng: CpyRandom,
    pub mcts_sims: usize,
    pub mcts_fpu: f64,
    pub mcts_p_floor: f64,
    pub mcts_max_depth: usize,
    pub rm_prior_mix: f64,
    pub collapse_mega: bool,
    pub qselect: bool,
    pub qselect_frac: f64,
    pub qselect_min: i64,
    pub downside_guard: bool,
    pub downside_k: usize,
    pub downside_margin: f64,
    pub tree_roll: f64,
    pub hidden: bool,
    /// 完全情報AI: 相手の型を決定化せず真値のまま読む（Python の SearchAI.oracle と同じ）。
    /// 型推定のノイズを外してネット品質だけを測る/学ぶためのもの。
    pub oracle: bool,
    /// 決定化で型プールから型まるごと引く（既定ON。env JOINT_BUILD=0 で無効）。
    pub joint_build: bool,
    /// 消費・はたき落としで無くなった既知の持ち物を決定化で戻さない（ITEM_GONE=0 で旧挙動＝A/B用）
    pub item_gone: bool,
    /// 確定KO安全弁を姿変化・連続技込みで判定する（AI_KO_PRECISE=0 で旧判定＝A/B用。本番は常に true）
    pub ko_precise: bool,
    /// 確定KO安全弁で成功条件のある技（2ターン目以降のであいがしら等）を除く（AI_KO_COND=0 で旧判定＝A/B用）
    pub ko_cond: bool,
    /// 相手の場のポケモンにタイプで無効な攻撃技を根の候補から外す（AI_PRUNE_IMMUNE=0 で旧挙動＝A/B用）
    pub prune_immune: bool,
    /// 監査40の AI 修正（必ず失敗・効果の無い手を根から外す／確定KOの命中・タイプ条件／ねむりカウンタの決定化）。
    /// 既定ON。AI_FIX40=0 で旧挙動（A/B用。AI_FIX40_2 で側2だけ）
    pub fix40: bool,
    /// 既定ON。AI_FIX200=0 で旧挙動（監査200 C。AI_FIX200_2 で側2だけ）
    pub fix200: bool,
    /// 既定ON。AI_FIXHZ=0 で旧挙動（設置済みの設置技を外す。AI_FIXHZ_2 で側2だけ）
    pub fixhz: bool,
    /// 計測用: この確率で相手の真の型をそのまま使う（型予測の精度を人為的に上げ、精度と勝率の関係を測る）
    pub oracle_mix: f64,
    /// 計測用: 相手の真の型のうち一部だけを使う（1=持ち物 2=特性 4=技 8=性格・努力値 のビット和）。
    /// どの項目の予測精度が勝率に効くかを切り分ける（search_ai.py の oracle_reveal に相当）
    pub oracle_reveal: u32,
    /// 終盤（残り体数が SOLVE_MAX_ALIVE 以下）で、MCTS の代わりに厳密ソルバの最善手を指す。
    /// ソルバで指したら実際に何%勝てるか＝探索の質の伸び代を勝率で測るためのもの。
    pub solve_play: bool,
    pub ctx: NetCtx,
    tpl: TplCache,
    nodes: Vec<Node>,
    /// NODE_TRACE>0 のとき、展開したノードの (node_id, 特徴ベクトル) を溜める。
    /// 探索終了後に逆伝播済みの値と組にして教師として吐く。
    pending_nodes: Vec<(usize, Vec<f64>)>,
}

impl SearchAI {
    pub fn new(pack: &Pack, season: &str, seed: i128, sims: usize) -> SearchAI {
        SearchAI {
            season: season.to_string(),
            rng: CpyRandom::new(seed),
            mcts_sims: sims,
            mcts_fpu: std::env::var("MCTS_FPU").ok().and_then(|v| v.parse().ok()).unwrap_or(0.5),
            mcts_p_floor: std::env::var("MCTS_P_FLOOR").ok().and_then(|v| v.parse().ok()).unwrap_or(1e-3),
            mcts_max_depth: std::env::var("MCTS_MAX_DEPTH").ok().and_then(|v| v.parse().ok()).unwrap_or(60),
            rm_prior_mix: std::env::var("RM_PRIOR_MIX").ok().and_then(|v| v.parse().ok()).unwrap_or(0.25),
            collapse_mega: true,
            qselect: true,
            qselect_frac: std::env::var("QSELECT_FRAC").ok().and_then(|v| v.parse().ok()).unwrap_or(0.1),
            qselect_min: 10,
            downside_guard: true,
            downside_k: 8,
            downside_margin: 0.20,
            tree_roll: 0.85,
            hidden: true,
            oracle: std::env::var("ORACLE").map(|v| v == "1").unwrap_or(false),
            // 既定ON（belief.py と同じ）。JOINT_BUILD=0 で旧挙動（要素ごとの決定化）
            joint_build: std::env::var("JOINT_BUILD").map(|v| v != "0").unwrap_or(true),
            item_gone: std::env::var("ITEM_GONE").map(|v| v != "0").unwrap_or(true),
            ko_precise: std::env::var("AI_KO_PRECISE").map(|v| v != "0").unwrap_or(true),
            ko_cond: crate::ai::ko_cond_env(),
            prune_immune: std::env::var("AI_PRUNE_IMMUNE").map(|v| v != "0").unwrap_or(true),
            fix40: crate::ai::fix40_env(),
            fix200: crate::ai::fix200_env(),
            fixhz: crate::ai::fixhz_env(),
            oracle_mix: std::env::var("ORACLE_MIX").ok().and_then(|v| v.parse().ok()).unwrap_or(0.0),
            oracle_reveal: std::env::var("ORACLE_REVEAL").ok().and_then(|v| v.parse().ok()).unwrap_or(0),
            solve_play: std::env::var("SOLVE_PLAY").ok().and_then(|v| v.parse::<f64>().ok()).unwrap_or(0.0) > 0.5,
            ctx: NetCtx::new(pack),
            tpl: TplCache::default(),
            nodes: Vec::new(),
            pending_nodes: Vec::new(),
        }
    }

    fn new_node(&mut self) -> usize {
        self.nodes.push(Node::default());
        self.nodes.len() - 1
    }

    /// SearchAI.__call__（mcts 経路）
    #[allow(clippy::too_many_arguments)]
    pub fn choose(
        &mut self,
        pack: &Pack,
        net: &NetW,
        sides: &mut [Side; 2],
        me_idx: usize,
        field: &mut Field,
        belief: &mut OpponentBelief,
        grng: &mut dyn BRng,
    ) -> Action {
        let op_idx = 1 - me_idx;
        if !sides[me_idx].active().is_alive {
            return Action { kind: ActKind::Pass, ..Default::default() };
        }
        if let Some(a) = forced_charging_action(sides[me_idx].active_mut()) {
            return a;
        }
        let mut cands =
            candidate_actions(pack, &sides[me_idx], &sides[op_idx], field, self.collapse_mega);
        if self.prune_immune {
            cands = prune_immune_moves(pack, &sides[me_idx], &sides[op_idx], field, cands);
        }
        if self.fix40 {
            cands = prune_futile_moves_opt2(pack, &sides[me_idx], &sides[op_idx], field, cands, self.fix200, self.fixhz);
        }
        if cands.len() <= 1 {
            if let Some(a) = cands.into_iter().next() {
                return a;
            }
            // _fallback = HeuristicAI()（実運用では到達しない）
            let (me, op) = crate::battle::split2(sides, me_idx);
            return ai::decide(pack, ai::Ai::heuristic(), me, op, field, false, grng);
        }
        self.mcts_choose(pack, net, sides, me_idx, field, belief, &cands, grng)
    }

    #[allow(clippy::too_many_arguments)]
    fn mcts_choose(
        &mut self,
        pack: &Pack,
        net: &NetW,
        sides: &mut [Side; 2],
        me_idx: usize,
        field: &mut Field,
        belief: &mut OpponentBelief,
        cands: &[Action],
        grng: &mut dyn BRng,
    ) -> Action {
        let root = self.build_mcts_root(pack, net, sides, me_idx, field, belief, cands, grng);
        let my_is_s1 = me_idx == 0;
        // stats = [(a, n, q)]
        let mut stats: Vec<(usize, i64, f64)> = Vec::with_capacity(cands.len());
        for (ai_, a) in cands.iter().enumerate() {
            let ix = action_index(a);
            let n = self.nodes[root].n[0].get(&ix).copied().unwrap_or(0);
            let q = if n != 0 {
                self.nodes[root].w[0].get(&ix).copied().unwrap_or(0.0) / n as f64
            } else {
                -1.0
            };
            stats.push((ai_, n, q));
        }
        let chosen_i = if self.qselect {
            let mut maxn = 0i64;
            for (_, n, _) in &stats {
                if *n > maxn {
                    maxn = *n;
                }
            }
            let maxn = if maxn == 0 { 1 } else { maxn };
            let thr = std::cmp::max(self.qselect_min, (self.qselect_frac * maxn as f64) as i64);
            let elig: Vec<&(usize, i64, f64)> =
                stats.iter().filter(|x| x.1 >= thr).collect::<Vec<_>>();
            let src: Vec<&(usize, i64, f64)> =
                if elig.is_empty() { stats.iter().collect() } else { elig };
            let mut best = src[0];
            for x in src.iter().skip(1) {
                if x.2 > best.2 {
                    best = x;
                }
            }
            best.0
        } else {
            let mut best = &stats[0];
            for x in stats.iter().skip(1) {
                if x.1 > best.1 {
                    best = x;
                }
            }
            best.0
        };
        // 探索木の内部ノードを教師として吐く。値は逆伝播済みの平均（探索側視点）。
        // 訪問が少ないノードは値が不安定なので捨てる。
        if !self.pending_nodes.is_empty() {
            let pend = std::mem::take(&mut self.pending_nodes);
            let minv = crate::sim::node_min_visits();
            for (nid, x) in pend {
                let nd = &self.nodes[nid];
                if nd.total < minv {
                    continue;
                }
                let s: f64 = nd.w[0].values().sum();
                let n: i64 = nd.n[0].values().sum();
                if n <= 0 {
                    continue;
                }
                // 合法手は prior のキー（legal_actions_indexed 由来）。訪問0の手も 0 として出す
                let mut pi: Vec<(usize, i64)> =
                    nd.p[0].keys().map(|&ix| (ix, nd.n[0].get(&ix).copied().unwrap_or(0))).collect();
                pi.sort_unstable();
                if pi.len() > 1 {
                    crate::sim::node_trace_push((x, s / n as f64, pi));
                }
            }
        }
        // 終盤の厳密ソルバで、選んだ手が最善からどれだけ損しているかを採点する
        let sd = crate::sim::solve_depth();
        let mut solver_decided = false;
        let mut chosen_i = chosen_i;
        if sd > 0 {
            let alive: usize = sides.iter().map(|s| s.party.iter().filter(|p| p.is_alive).count()).sum();
            let record = crate::sim::solve_record();
            if alive <= crate::sim::solve_max_alive() && (record || self.solve_play) {
                let mut sv = crate::solver::Solver::new(pack, net);
                sv.collapse_mega = self.collapse_mega;
                let (v, per) = sv.root(sides, field, me_idx, sd);
                if record {
                    crate::sim::solve_trace_push((me_idx, v, per.clone(), action_index(&cands[chosen_i]), alive,
                                                  sv.nodes, sv.cells, sv.cells_full));
                }
                if self.solve_play {
                    if let Some(&(best_ix, _)) = per.iter().max_by(|a, b| a.1.partial_cmp(&b.1).unwrap()) {
                        if let Some(k) = cands.iter().position(|a| action_index(a) == best_ix) {
                            chosen_i = k;
                            solver_decided = true;
                        }
                    }
                }
            }
        }
        if let Some(cfg) = crate::sim::explore_cfg() {
            let best_i = chosen_i;
            let win = crate::sim::explore_window();
            if win {
                let maxn = stats.iter().map(|x| x.1).max().unwrap_or(0);
                let thr = std::cmp::max(1, (cfg.min_frac * maxn as f64).ceil() as i64);
                let ws: Vec<f64> = stats
                    .iter()
                    .map(|(_, n, _)| if *n >= thr { (*n as f64).powf(1.0 / cfg.temp.max(1e-3)) } else { 0.0 })
                    .collect();
                let tot: f64 = ws.iter().sum();
                if tot > 0.0 {
                    let r = crate::sim::explore_rand() * tot;
                    let mut acc = 0.0;
                    for (k, w) in ws.iter().enumerate() {
                        acc += w;
                        if r <= acc && *w > 0.0 {
                            chosen_i = k;
                            break;
                        }
                    }
                }
            }
            let ntot: i64 = stats.iter().map(|(_, n, _)| *n).sum();
            crate::sim::explore_log_push((
                crate::sim::explore_turn(), me_idx, win, chosen_i != best_i,
                stats[chosen_i].1, stats[best_i].1, stats[chosen_i].2, stats[best_i].2, ntot,
            ));
        }
        // パリティ調査用: ルート直下の (行動, 訪問数, Q) を記録する（ROOT_LOG が Some のときだけ）。
        crate::sim::root_log_push(pack, cands, &stats, chosen_i);
        // 学習用: 盤面と根の訪問分布を記録する（PI_TRACE が Some のときだけ）。
        if crate::sim::pi_trace_enabled() {
            let mut x: Vec<f64> = Vec::new();
            crate::features::encode_state_into(
                pack, &self.ctx.ft, sides, me_idx, field, &mut self.ctx.memo, grng, &mut x,
            );
            let pi: Vec<(usize, i64)> =
                stats.iter().map(|(ai_, n, _)| (action_index(&cands[*ai_]), *n)).collect();
            // 価値ターゲットの取り方。既定は訪問数で重み付けした平均＝「探索の混合戦略どおりに
            // 指したときの期待値」。VALUE_Q=max にすると根の最善手の値になり、
            // 自分の方策の弱さが価値に混入しにくくなる（V^π を V* 寄りにする）。
            let ntot: i64 = stats.iter().map(|(_, n, _)| *n).sum();
            let rq = if ntot <= 0 {
                0.5
            } else if crate::sim::value_q_max() {
                let thr = std::cmp::max(1, ntot / 50);
                stats
                    .iter()
                    .filter(|(_, n, _)| *n >= thr)
                    .map(|(_, _, q)| *q)
                    .fold(f64::NEG_INFINITY, f64::max)
            } else {
                stats.iter().filter(|(_, n, _)| *n > 0).map(|(_, n, q)| *n as f64 * q).sum::<f64>()
                    / ntot as f64
            };
            let rq = if rq.is_finite() { rq } else { 0.5 };
            crate::sim::pi_trace_push((me_idx, x, pi, rq));
        }
        let mut chosen = cands[chosen_i].clone();
        let keep_guard = std::env::var("SOLVE_GUARD").map(|v| v != "0").unwrap_or(true);
        if self.downside_guard && (keep_guard || !solver_decided) {
            chosen = self.apply_downside_guard(
                pack, net, sides, me_idx, field, belief, cands, chosen, my_is_s1, grng,
            );
        }
        chosen
    }

    #[allow(clippy::too_many_arguments)]
    fn build_mcts_root(
        &mut self,
        pack: &Pack,
        net: &NetW,
        sides: &mut [Side; 2],
        me_idx: usize,
        field: &mut Field,
        belief: &mut OpponentBelief,
        cands: &[Action],
        grng: &mut dyn BRng,
    ) -> usize {
        belief.observe_disclosure(pack, &sides[me_idx].opp_view);
        let my_is_s1 = me_idx == 0;
        self.nodes.clear();
        let root = self.new_node();
        if cands.len() <= 1 {
            return root;
        }
        for _t in 0..self.mcts_sims {
            let mut cs: [Side; 2] = [sides[0].clone(), sides[1].clone()];
            let mut cfield = field.clone();
            let dopp = 1 - me_idx;
            if self.hidden && !self.oracle {
                self.resample_hidden_bench(pack, &mut cs, dopp, &sides[me_idx].opp_view, grng);
            }
            let cfg = self.sample_opp_config(pack, &cs[dopp], belief);
            for (i, c) in cfg.iter().enumerate() {
                if let Some(c) = c {
                    self.determinize(pack, &mut cs[dopp].party[i], c);
                }
            }
            self.mcts_simulate(pack, net, root, &mut cs, &mut cfield, my_is_s1, grng);
        }
        root
    }

    /// SearchAI._resample_hidden_bench
    fn resample_hidden_bench(
        &mut self,
        pack: &Pack,
        cs: &mut [Side; 2],
        di: usize,
        opp_view: &crate::oppview::OppView,
        grng: &mut dyn BRng,
    ) {
        if cs[di].source6_names.len() <= cs[di].party.len() {
            return;
        }
        let mut seen: Vec<crate::interner::Sym> =
            opp_view.pokemon.iter().filter(|k| k.seen).map(|k| k.name).collect();
        let an = cs[di].active().name;
        if !seen.contains(&an) {
            seen.push(an);
        }
        let mut pool: Vec<crate::interner::Sym> =
            cs[di].source6_names.iter().copied().filter(|n| !seen.contains(n)).collect();
        // random.Random.shuffle（Fisher-Yates 下降・_randbelow）
        self.rng.shuffle(&mut pool);
        let mut pi = 0usize;
        for i in 0..cs[di].party.len() {
            if i == cs[di].active_idx {
                continue;
            }
            if seen.contains(&cs[di].party[i].name) || !cs[di].party[i].is_alive {
                continue;
            }
            if pi >= pool.len() {
                continue;
            }
            let name_sym = pool[pi];
            pi += 1;
            let name = pack.intern.resolve(name_sym).to_string();
            let tpl = match self.tpl.get_playable(pack, &name, &self.season) {
                None => continue,
                Some(t) => t,
            };
            let spec = crate::poke::Spec {
                name: name.clone(),
                item: None,
                nature: None,
                moves: None,
                evs: None,
                ability: None,
            };
            let mut r: Option<&mut dyn BRng> = Some(grng);
            let b = crate::poke::build_from_template_rand(pack, &tpl, &spec, &mut r);
            let nb = crate::poke::to_poke(pack, &b);
            if nb.moves.is_empty() {
                continue;
            }
            cs[di].party[i] = nb;
        }
    }

    /// SearchAI._sample_opp_config
    /// 決定化で引いた型を相手の真の型と突き合わせて記録する（計測用・既定でも走る）。
    #[allow(clippy::too_many_arguments)]
    fn det_score(pack: &Pack, truth: &crate::poke::Poke, known: usize, item: Option<&str>,
                 ability: &str, moves: &[String], nature: &str, ev: &crate::pack::EvEntry) {
        let t_item = truth.item.map(|s| pack.intern.resolve(s).to_string());
        let t_abil = pack.intern.resolve(truth.ability).to_string();
        let t_moves: Vec<String> =
            truth.moves.iter().map(|m| pack.intern.resolve(m.name).to_string()).collect();
        let hit = moves.iter().filter(|m| t_moves.contains(m)).count() as u64;
        let ok_item = item.map(String::from) == t_item;
        let ok_abil = ability == t_abil;
        let ok_moves = hit as usize == t_moves.len() && moves.len() == t_moves.len();
        let ok_nat = pack.intern.resolve(truth.nature) == nature;
        let ok_ev = truth.evs == [ev.h, ev.a, ev.b, ev.c, ev.d, ev.s];
        crate::sim::det_hit_add(known, ok_item, ok_abil, hit, ok_moves,
                                ok_item && ok_abil && ok_moves, ok_nat, ok_ev);
    }

/// 相手の真の技を採用率の高い順（定番→自由枠）に並べる
fn truth_moves_by_prior(pack: &Pack, truth: &crate::poke::Poke, prior: &[(String, f64)]) -> Vec<String> {
    let mut t: Vec<(String, f64)> = truth.moves.iter().map(|m| {
        let n = pack.intern.resolve(m.name).to_string();
        let r = prior.iter().find(|(x, _)| *x == n).map_or(0.0, |x| x.1);
        (n, r)
    }).collect();
    t.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap_or(std::cmp::Ordering::Equal).then(a.0.cmp(&b.0)));
    t.into_iter().map(|x| x.0).collect()
}

/// 枠ごとの当たり率（計測用）: 真の技を採用率順に並べ、未判明の枠を引いた型が当てているか
fn det_slot(pack: &Pack, truth: &crate::poke::Poke, known: &[String], prior: &[(String, f64)], moves: &[String]) {
    let order = Self::truth_moves_by_prior(pack, truth, prior);
    for (rank, m) in order.iter().enumerate().take(4) {
        if known.contains(m) {
            continue;
        }
        crate::sim::det_slot_add(known.len(), rank, moves.contains(m));
    }
}

/// 型プールから既知情報と矛盾しない型を1つ引く。候補が無ければ None（従来の周辺分布に落ちる）。
fn pick_pool_build<'a>(
    pack: &'a Pack,
    name: &str,
    pb: &mut crate::belief::PokemonBelief,
    tpl: Option<&crate::poke::Template>,
    rng: &mut CpyRandom,
) -> Option<&'a crate::pack::PoolBuild> {
    let arr = pack.build_pool.get(name)?;
    // 観測したダメージで絞った型ごとの重み（テンプレが無ければ元の出現率）
    let wts: Vec<f64> = match tpl {
        Some(t) => pb.pool_weights(pack, t, arr).to_vec(),
        None => arr.iter().map(|b| b.weight).collect(),
    };
    let mut tot = 0.0;
    let mut ok: Vec<(&crate::pack::PoolBuild, f64)> = Vec::with_capacity(arr.len());
    for (b, &bw) in arr.iter().zip(wts.iter()) {
        if let Some(it) = pb.known_item.as_deref() {
            if b.item != it {
                continue;
            }
        }
        // メガ進化で分かる特性はメガ後のもの。判明したメガ石の型は特性で弾かない（belief.py と同じ）
        let mega_seen = pb.known_item.as_deref() == Some(b.item.as_str())
            && crate::battle::is_megastone(pack, pack.intern.get(&b.item));
        if let Some(ab) = pb.known_ability.as_deref() {
            if !b.ability.is_empty() && b.ability != ab && !mega_seen {
                continue;
            }
        }
        if !pb.known_moves.iter().all(|m| b.moves.iter().any(|x| x == m)) {
            continue;
        }
        if pb.known_item.is_none() && pb.absent_items.iter().any(|x| *x == b.item) {
            continue;   // 発動しなかった持ち物（たべのこし等）
        }
        tot += bw;
        ok.push((b, bw));
    }
    if ok.is_empty() || tot <= 0.0 {
        return None;
    }
    let mut r = rng.random() * tot;
    for (b, bw) in &ok {
        r -= bw;
        if r <= 0.0 {
            return Some(b);
        }
    }
    ok.last().map(|x| x.0)
}

    fn sample_opp_config(
        &mut self,
        pack: &Pack,
        opp_side: &Side,
        belief: &mut OpponentBelief,
    ) -> Vec<Option<SampledCfg>> {
        if self.oracle {
            // 決定化しない＝真の型のまま。呼び出し側は None を「上書きしない」と解釈する
            return vec![None; opp_side.party.len()];
        }
        let mut out = Vec::with_capacity(opp_side.party.len());
        for p in &opp_side.party {
            let name = pack.intern.resolve(p.name).to_string();
            let bi = belief.ensure(pack, &name, None, None);
            let bi = match bi {
                None => {
                    out.push(None);
                    continue;
                }
                Some(i) => i,
            };
            if self.oracle_mix > 0.0 && self.rng.random() < self.oracle_mix {
                let km = belief.species[bi].1.known_moves.len();
                crate::sim::det_hit_add(km, true, true, p.moves.len() as u64, true, true, true, true);
                out.push(None);
                continue;
            }
            let tpl_j = if self.joint_build { self.tpl.get(pack, &name, &self.season) } else { None };
            let pb = &mut belief.species[bi].1;
            // 型プールから型まるごと引く。技・持ち物・性格・努力値を独立に引くと
            // 実在しない組み合わせになる（型丸ごと一致は事前で7%しかなかった）。
            if self.joint_build {
                if let Some(b) = Self::pick_pool_build(pack, &name, pb, tpl_j.as_ref(), &mut self.rng) {
                    crate::sim::cfg_log_push(pack, &name, &b.ev, &b.nature,
                                             Some(b.item.as_str()), &b.ability, &b.moves);
                    Self::det_score(pack, p, pb.known_moves.len(),
                                    Some(b.item.as_str()), &b.ability, &b.moves, &b.nature, &b.ev);
                    Self::det_slot(pack, p, &pb.known_moves, &pb.move_prior, &b.moves);
                    out.push(Some(SampledCfg {
                        ev: b.ev.clone(),
                        nature: b.nature.clone(),
                        item: if b.item.is_empty() { None } else { Some(b.item.clone()) },
                        // 判明した特性を優先（search_ai.py と同じ。メガ後の特性をメガ前で上書きしない）
                        ability: pb.known_ability.clone().unwrap_or_else(|| b.ability.clone()),
                        moves: b.moves.clone(),
                    }));
                    continue;
                }
            }
            let (ev, nature) = pb.sample_spread(&mut self.rng);
            let item = pb.sample_item(&mut self.rng);
            let ability = pb.sample_ability(&mut self.rng);
            let moves = pb.sample_moves(&mut self.rng, 4);
            crate::sim::cfg_log_push(pack, &name, &ev, &nature, item.as_deref(), &ability, &moves);
            Self::det_score(pack, p, pb.known_moves.len(), item.as_deref(), &ability, &moves,
                            &nature, &ev);
            Self::det_slot(pack, p, &pb.known_moves, &pb.move_prior, &moves);
            out.push(Some(SampledCfg { ev, nature, item, ability, moves }));
        }
        // 持ち物が消費・はたき落としで無くなったことは公開情報（opp_view.item_lost・search_ai.py と同じ）
        for (c, p) in out.iter_mut().zip(opp_side.party.iter()) {
            if let Some(c) = c {
                if self.item_gone {
                    let name = pack.intern.resolve(p.name).to_string();
                    if let Some(bi) = belief.ensure(pack, &name, None, None) {
                        if belief.species[bi].1.item_lost {
                            c.item = None;
                        }
                    }
                }
            }
        }
        if self.oracle_reveal != 0 {
            for (c, p) in out.iter_mut().zip(opp_side.party.iter()) {
                let c = match c { Some(c) => c, None => continue };
                if self.oracle_reveal & 1 != 0 {
                    c.item = p.item.map(|x| pack.intern.resolve(x).to_string());
                }
                if self.oracle_reveal & 2 != 0 {
                    c.ability = pack.intern.resolve(p.ability).to_string();
                }
                if self.oracle_reveal & 4 != 0 {
                    c.moves = p.moves.iter().map(|m| pack.intern.resolve(m.name).to_string()).collect();
                }
                if self.oracle_reveal & (16 | 32) != 0 {
                    // 16=自由枠（未判明の真の技のうち採用率が最も低い1つ）だけ、32=定番3技だけを教える
                    let name = pack.intern.resolve(p.name).to_string();
                    if let Some(bi) = belief.ensure(pack, &name, None, None) {
                        let pb = &belief.species[bi].1;
                        let order = Self::truth_moves_by_prior(pack, p, &pb.move_prior);
                        let mut give: Vec<String> = pb.known_moves.clone();
                        if self.oracle_reveal & 32 != 0 {
                            for m in order.iter().take(3) {
                                if !give.contains(m) {
                                    give.push(m.clone());
                                }
                            }
                        }
                        if self.oracle_reveal & 16 != 0 {
                            if let Some(m) = order.iter().rev().find(|m| !pb.known_moves.contains(m)) {
                                if !give.contains(m) {
                                    give.push(m.clone());
                                }
                            }
                        }
                        for m in c.moves.iter() {
                            if give.len() >= 4 {
                                break;
                            }
                            if !give.contains(m) {
                                give.push(m.clone());
                            }
                        }
                        c.moves = give;
                    }
                }
                if self.oracle_reveal & 8 != 0 {
                    let e = p.evs;
                    c.ev = crate::pack::EvEntry { h: e[0], a: e[1], b: e[2], c: e[3], d: e[4], s: e[5],
                                                  ..Default::default() };
                    c.nature = pack.intern.resolve(p.nature).to_string();
                }
            }
        }
                // 整合チェック（計測用・既定でも走る）: 引いた型と相手の真の型が、判明情報と矛盾していないか
        for (c, p) in out.iter().zip(opp_side.party.iter()) {
            let c = match c { Some(c) => c, None => continue };
            let name = pack.intern.resolve(p.name).to_string();
            let bi = match belief.ensure(pack, &name, None, None) { Some(i) => i, None => continue };
            let pb = &belief.species[bi].1;
            if pb.known_moves.is_empty() && pb.known_item.is_none() && pb.known_ability.is_none() {
                continue;
            }
            let mut bad = [false; 8];
            bad[0] = !pb.known_moves.iter().all(|m| c.moves.contains(m));
            bad[1] = if pb.item_lost && self.item_gone {
                c.item.is_some()
            } else {
                pb.known_item.is_some() && c.item != pb.known_item
            };
            bad[2] = pb.known_ability.as_ref().is_some_and(|a| *a != c.ability);
            bad[3] = pb.known_item.is_none()
                && c.item.as_ref().is_some_and(|it| pb.absent_items.contains(it));
            let t_moves: Vec<String> =
                p.moves.iter().map(|m| pack.intern.resolve(m.name).to_string()).collect();
            let t_item = p.item.map(|x| pack.intern.resolve(x).to_string());
            let t_abil = pack.intern.resolve(p.ability).to_string();
            bad[4] = !pb.known_moves.iter().all(|m| t_moves.contains(m));
            bad[5] = if pb.item_lost { t_item.is_some() } else { pb.known_item.is_some() && t_item != pb.known_item };
            bad[6] = pb.known_ability.as_ref().is_some_and(|a| *a != t_abil);
            bad[7] = pb.known_item.is_none() && t_item.as_ref().is_some_and(|it| pb.absent_items.contains(it));
            crate::sim::det_consist_add(&bad);
        }
        out
    }

    /// SearchAI._determinize
    fn determinize(&mut self, pack: &Pack, poke: &mut crate::poke::Poke, c: &SampledCfg) {
        let name = pack.intern.resolve(poke.name).to_string();
        let tpl = match self.tpl.get(pack, &name, &self.season) {
            None => return,
            Some(t) => t,
        };
        if !poke.mega_evolved && !poke.transformed {
            let nat_sym = pack.intern.get(&c.nature);
            let nm = |k: u8| -> f64 {
                match nat_sym.and_then(|s| pack.nature_mods.get(&s)) {
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
            let frac = if poke.max_hp != 0 { poke.hp as f64 / poke.max_hp as f64 } else { 1.0 };
            let e = &c.ev;
            poke.max_hp = crate::poke::calc_hp(tpl.base[0], e.h);
            poke.attack = crate::poke::calc_stat(tpl.base[1], e.a, 31, nm(0));
            poke.defense = crate::poke::calc_stat(tpl.base[2], e.b, 31, nm(1));
            poke.sp_attack = crate::poke::calc_stat(tpl.base[3], e.c, 31, nm(2));
            poke.sp_defense = crate::poke::calc_stat(tpl.base[4], e.d, 31, nm(3));
            poke.speed = crate::poke::calc_stat(tpl.base[5], e.s, 31, nm(4));
            poke.nature = nat_sym.unwrap_or(poke.nature);
            poke.evs = [e.h, e.a, e.b, e.c, e.d, e.s];
            poke.hp = if poke.is_alive {
                std::cmp::max(1, (frac * poke.max_hp as f64).round_ties_even() as i64)
            } else {
                0
            };
        }
        crate::sim::det_log_push(
            pack.intern.resolve(poke.name),
            poke.max_hp, poke.hp, poke.attack, poke.defense,
            poke.sp_attack, poke.sp_defense, poke.speed,
        );
        if let Some(it) = &c.item {
            poke.item = pack.intern.get(it);
        }
        if !c.ability.is_empty() {
            if let Some(a) = pack.intern.get(&c.ability) {
                poke.ability = a;
            }
        }
        if self.fix40 && poke.status == Some(pack.sy.st.sleep) {
            resample_sleep(pack, poke, &mut self.rng);
        }
        let mut mvs: Vec<crate::damage::DMove> = Vec::new();
        for m in &c.moves {
            if let Some(&idx) = pack.move_by_name.get(m) {
                let md = &pack.moves[idx];
                mvs.push(crate::damage::DMove {
                    name: md.name,
                    ty: md.ty,
                    category: md.category,
                    power: md.power,
                    accuracy: md.accuracy,
                    priority: md.priority,
                    pp: md.pp,
                });
            }
        }
        if !mvs.is_empty() {
            let names: Vec<crate::interner::Sym> = mvs.iter().map(|m| m.name).collect();
            poke.pp = mvs.iter().map(|m| m.pp.unwrap_or(5)).collect();
            poke.moves = mvs;
            for slot in [
                &mut poke.last_used_move,
                &mut poke.choice_locked_move,
                &mut poke.locked_move,
                &mut poke.disabled_move,
                &mut poke.charging_move,
            ] {
                if let Some(x) = *slot {
                    if !names.contains(&x) {
                        *slot = None;
                    }
                }
            }
        }
    }

    /// SearchAI._advance_turn（固定ロール tree_roll で1ターン解決）
    fn advance_turn(
        &mut self,
        pack: &Pack,
        cs: &mut [Side; 2],
        cfield: &mut Field,
        a_me: &Action,
        a_op: &Action,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) -> i64 {
        let (a1, a2) = if my_is_s1 { (a_me, a_op) } else { (a_op, a_me) };
        let mut b = Battle {
            sides: [std::mem::take(&mut cs[0]), std::mem::take(&mut cs[1])],
            field: std::mem::take(cfield),
            turn: 0,
            item_snap: Vec::new(),
        };
        b.sides[0].field_idx = 0;
        b.sides[1].field_idx = 1;
        let prev = b.field.roll_override;
        b.field.roll_override = Some(self.tree_roll);
        let acts = [a1.clone(), a2.clone()];
        let mut used = false;
        let w = b.run_loop_lim(
            pack,
            grng,
            1,
            |_bt, _rng| {
                assert!(!used, "resume(max_turns=1) は1回だけ行動を要求するはず");
                used = true;
                [acts[0].clone(), acts[1].clone()]
            },
            |_| {},
        );
        b.field.roll_override = prev;
        cs[0] = std::mem::take(&mut b.sides[0]);
        cs[1] = std::mem::take(&mut b.sides[1]);
        *cfield = b.field;
        w
    }

    /// SearchAI._mcts_leaf_value（net_eval あり）
    fn leaf_value(
        &mut self,
        pack: &Pack,
        net: &NetW,
        cs: &mut [Side; 2],
        cfield: &mut Field,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) -> f64 {
        let (_, v1) = net_eval(pack, net, &mut self.ctx, cs, 0, cfield, grng);
        if my_is_s1 {
            v1
        } else {
            1.0 - v1
        }
    }

    /// SearchAI._expand_with_value（葉のencode+forwardを2回に統合・memo有効）
    #[allow(clippy::too_many_arguments)]
    fn expand_with_value(
        &mut self,
        pack: &Pack,
        net: &NetW,
        node: usize,
        cs: &mut [Side; 2],
        cfield: &mut Field,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) -> f64 {
        // Python: ev(me,op) → ev(op,me) → ev(cs1,cs2)（3つ目はメモヒット）
        let (fa, fb) = if my_is_s1 { (0usize, 1usize) } else { (1usize, 0usize) };
        self.ctx.memo.begin();
        crate::sim::eval_tag_set(true);
        let (pol_a, val_a) = net_eval(pack, net, &mut self.ctx, cs, fa, cfield, grng);
        // 教師として残すのは探索側（fa）視点の特徴ベクトル。逆伝播される値と視点を揃える。
        // 抽出は node_id のハッシュで決める（共有RNGを消費すると探索自体が変わりパリティが崩れる）。
        let rate = crate::sim::node_trace_rate();
        if rate > 0.0
            && crate::sim::pi_trace_enabled()
            && ((node as u64).wrapping_mul(2654435761) >> 8) % 1000 < (rate * 1000.0) as u64
        {
            self.pending_nodes.push((node, self.ctx.x.clone()));
        }
        let (pol_b, val_b) = net_eval(pack, net, &mut self.ctx, cs, fb, cfield, grng);
        crate::sim::eval_tag_set(false);
        self.ctx.memo.end();
        let nd = &mut self.nodes[node];
        nd.p[0] = pol_a.iter().copied().collect();
        nd.p[1] = pol_b.iter().copied().collect();
        nd.expanded = true;
        let v1 = if my_is_s1 { val_a } else { val_b };
        if my_is_s1 {
            v1
        } else {
            1.0 - v1
        }
    }

    /// SearchAI._select（mcts_select="regret"）
    fn select(&mut self, node: usize, side: usize, cands: &[Action]) -> (usize, usize, f64) {
        let mut items: Vec<(usize, usize, f64, f64)> = Vec::with_capacity(cands.len());
        {
            let nd = &self.nodes[node];
            for (k, a) in cands.iter().enumerate() {
                let ix = action_index(a);
                let n = nd.n[side].get(&ix).copied().unwrap_or(0);
                let q = if n != 0 {
                    nd.w[side].get(&ix).copied().unwrap_or(0.0) / n as f64
                } else {
                    self.mcts_fpu
                };
                let p = f64::max(
                    nd.p[side].get(&ix).copied().unwrap_or(self.mcts_p_floor),
                    self.mcts_p_floor,
                );
                items.push((ix, k, q, p));
            }
        }
        let psum = {
            let t = pysum(items.iter().map(|x| x.3));
            if t == 0.0 {
                1.0
            } else {
                t
            }
        };
        // regret-matching
        let mut sig: Vec<f64> = Vec::with_capacity(items.len());
        {
            let nd = &self.nodes[node];
            let pos: Vec<f64> =
                items.iter().map(|x| f64::max(0.0, nd.r[side].get(&x.0).copied().unwrap_or(0.0))).collect();
            let z = pysum(pos.iter().copied());
            if z > 0.0 {
                for v in &pos {
                    sig.push(v / z);
                }
            } else {
                for _ in 0..items.len() {
                    sig.push(1.0 / items.len() as f64);
                }
            }
        }
        let lam = self.rm_prior_mix;
        for (i, it) in items.iter().enumerate() {
            sig[i] = (1.0 - lam) * sig[i] + lam * (it.3 / psum);
        }
        let v = pysum(items.iter().enumerate().map(|(i, it)| sig[i] * it.2));
        {
            let nd = &mut self.nodes[node];
            for it in items.iter() {
                let e = nd.r[side].entry(it.0).or_insert(0.0);
                *e += it.2 - v;
            }
        }
        // _sample
        let r = self.rng.random();
        let mut acc = 0.0f64;
        for (i, it) in items.iter().enumerate() {
            acc += sig[i];
            if r <= acc {
                return (it.0, it.1, sig[i]);
            }
        }
        let last = items.len() - 1;
        (items[last].0, items[last].1, sig[last])
    }

    #[allow(clippy::too_many_arguments)]
    fn mcts_simulate(
        &mut self,
        pack: &Pack,
        net: &NetW,
        root: usize,
        cs: &mut [Side; 2],
        cfield: &mut Field,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) {
        if !self.nodes[root].expanded {
            self.expand_with_value(pack, net, root, cs, cfield, my_is_s1, grng);
            if crate::sim::explore_window() {
                if let Some(cfg) = crate::sim::explore_cfg() {
                    if cfg.eps > 0.0 {
                        let nd = &mut self.nodes[root];
                        let mut keys: Vec<usize> = nd.p[0].keys().copied().collect();
                        keys.sort_unstable();
                        let g: Vec<f64> = keys.iter().map(|_| crate::sim::explore_gamma(cfg.alpha)).collect();
                        let gs: f64 = g.iter().sum();
                        if gs > 0.0 {
                            for (k, gv) in keys.iter().zip(g.iter()) {
                                let e = nd.p[0].get_mut(k).unwrap();
                                *e = (1.0 - cfg.eps) * *e + cfg.eps * gv / gs;
                            }
                        }
                    }
                }
            }
        }
        let mut node = root;
        let mut path: Vec<(usize, usize, usize)> = Vec::new();
        let mut depth = 0usize;
        let v: f64;
        let me_i = if my_is_s1 { 0usize } else { 1 };
        let op_i = 1 - me_i;
        loop {
            let my_cands =
                candidate_actions(pack, &cs[me_i], &cs[op_i], cfield, self.collapse_mega);
            let opp_cands =
                candidate_actions(pack, &cs[op_i], &cs[me_i], cfield, self.collapse_mega);
            if my_cands.is_empty() || opp_cands.is_empty() {
                v = self.leaf_value(pack, net, cs, cfield, my_is_s1, grng);
                break;
            }
            let (ix_me, k_me, _sg_me) = self.select(node, 0, &my_cands);
            let (ix_op, k_op, _sg_op) = self.select(node, 1, &opp_cands);
            path.push((node, ix_me, ix_op));
            let winner = self.advance_turn(
                pack,
                cs,
                cfield,
                &my_cands[k_me],
                &opp_cands[k_op],
                my_is_s1,
                grng,
            );
            depth += 1;
            if winner != 0 {
                v = if (winner == 1) == my_is_s1 { 1.0 } else { 0.0 };
                break;
            }
            let key = (ix_me, ix_op);
            match self.nodes[node].children.get(&key).copied() {
                None => {
                    let child = self.new_node();
                    self.nodes[node].children.insert(key, child);
                    let vv = self.expand_with_value(pack, net, child, cs, cfield, my_is_s1, grng);
                    self.nodes[child].v = Some(vv);
                    v = vv;
                    break;
                }
                Some(child) => {
                    node = child;
                    if depth >= self.mcts_max_depth {
                        v = self.leaf_value(pack, net, cs, cfield, my_is_s1, grng);
                        break;
                    }
                }
            }
        }
        depth_stat(depth);
        // backup（nextturn_lambda=0 なので v_root == v）
        for (nd_i, im, io) in path {
            let nd = &mut self.nodes[nd_i];
            nd.total += 1;
            *nd.n[0].entry(im).or_insert(0) += 1;
            *nd.w[0].entry(im).or_insert(0.0) += v;
            *nd.n[1].entry(io).or_insert(0) += 1;
            *nd.w[1].entry(io).or_insert(0.0) += 1.0 - v;
        }
    }

    /// SearchAI._downside_value
    #[allow(clippy::too_many_arguments)]
    fn downside_value(
        &mut self,
        pack: &Pack,
        net: &NetW,
        sides: &[Side; 2],
        me_idx: usize,
        field: &Field,
        belief: &mut OpponentBelief,
        a: &Action,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) -> f64 {
        belief.observe_disclosure(pack, &sides[me_idx].opp_view);
        let di = 1 - me_idx;
        let mut worst = 1.0f64;
        for _k in 0..self.downside_k {
            let mut b: [Side; 2] = [sides[0].clone(), sides[1].clone()];
            let mut bf = field.clone();
            if self.hidden && !self.oracle {
                self.resample_hidden_bench(pack, &mut b, di, &sides[me_idx].opp_view, grng);
            }
            let cfg = self.sample_opp_config(pack, &b[di], belief);
            for (i, c) in cfg.iter().enumerate() {
                if let Some(c) = c {
                    self.determinize(pack, &mut b[di].party[i], c);
                }
            }
            let all = candidate_actions(pack, &b[di], &b[me_idx], &bf, self.collapse_mega);
            let moves: Vec<Action> =
                all.iter().filter(|x| x.kind == ActKind::Move).cloned().collect();
            let opp_cands = if moves.is_empty() { all } else { moves };
            let mut v_type = 1.0f64;
            for oa in &opp_cands {
                let mut c: [Side; 2] = [b[0].clone(), b[1].clone()];
                let mut cf = bf.clone();
                let winner = self.advance_turn(pack, &mut c, &mut cf, a, oa, my_is_s1, grng);
                let v = if winner != 0 {
                    if (winner == 1) == my_is_s1 {
                        1.0
                    } else {
                        0.0
                    }
                } else {
                    self.leaf_value(pack, net, &mut c, &mut cf, my_is_s1, grng)
                };
                if v < v_type {
                    v_type = v;
                }
            }
            if v_type < worst {
                worst = v_type;
            }
            let _ = &mut bf;
        }
        worst
    }

    /// SearchAI._apply_downside_guard
    #[allow(clippy::too_many_arguments)]
    fn apply_downside_guard(
        &mut self,
        pack: &Pack,
        net: &NetW,
        sides: &[Side; 2],
        me_idx: usize,
        field: &Field,
        belief: &mut OpponentBelief,
        root_my: &[Action],
        chosen: Action,
        my_is_s1: bool,
        grng: &mut dyn BRng,
    ) -> Action {
        let switches: Vec<Action> =
            root_my.iter().filter(|a| a.kind == ActKind::Switch).cloned().collect();
        if switches.is_empty() {
            return chosen;
        }
        let chosen_is_switch = chosen.kind == ActKind::Switch;
        let mut cand: Vec<Action> = Vec::new();
        if !chosen_is_switch {
            cand.push(chosen.clone());
        }
        cand.extend(switches.iter().cloned());
        let mut ds: Vec<f64> = Vec::with_capacity(cand.len());
        for a in &cand {
            let v =
                self.downside_value(pack, net, sides, me_idx, field, belief, a, my_is_s1, grng);
            ds.push(v);
        }
        let off = if chosen_is_switch { 0 } else { 1 };
        let mut bi = 0usize;
        for j in 1..switches.len() {
            if ds[off + j] > ds[off + bi] {
                bi = j;
            }
        }
        let base = if chosen_is_switch {
            // chosen は switches のどれか（値一致）＝ Python は id(chosen) で引く
            let mut k = 0usize;
            for (j, s) in switches.iter().enumerate() {
                if s.switch_to == chosen.switch_to {
                    k = j;
                    break;
                }
            }
            ds[k]
        } else {
            ds[0]
        };
        if ds[off + bi] - base >= self.downside_margin {
            return switches[bi].clone();
        }
        chosen
    }
}

/// Side に belief を設定する補助
pub fn set_belief(side: &mut Side, b: OpponentBelief) {
    side.belief = BeliefSlot(Some(Box::new(b)));
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::poke::build_poke;

    fn pack() -> Pack {
        Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"))
    }
    const HIP: &str = "カバルドン@オボンのみ:わんぱく:じしん|あくび|ふきとばし|なまける:32/0/32/0/0/0:すなおこし";
    const SAL: &str = "ボーマンダ@ボーマンダナイト:ようき:すてみタックル|じしん|りゅうのまい|はねやすめ:0/32/0/0/0/32:いかく";
    const MIM: &str = "ミミッキュ@いのちのたま:ようき:じゃれつく|シャドークロー|かげうち|つるぎのまい:0/32/0/0/0/32:ばけのかわ";
    const GAR: &str = "ガブリアス@こだわりスカーフ:ようき:じしん|ドラゴンクロー|どくづき|つるぎのまい:0/32/0/0/0/32:さめはだ";
    const SKA: &str = "エアームド@ゴツゴツメット:わんぱく:ボディプレス|はねやすめ|てっぺき|ステルスロック:32/0/32/0/0/0:がんじょう";
    const TAU: &str = "ケンタロス@こだわりハチマキ:いじっぱり:すてみタックル|インファイト|じしん|アイアンヘッド:0/32/0/0/0/32:きもったま";

    /// test_all.py 26f と同じ局面で、根の候補から外れる技が Python と一致する。
    fn names(p: &mut Pack, me: &str, opp: &str, bench: &[&str], lock: Option<&str>) -> Vec<String> {
        let mut party = vec![build_poke(p, me, "M-6")];
        for b in bench {
            party.push(build_poke(p, b, "M-6"));
        }
        if let Some(l) = lock {
            party[0].choice_locked_move = Some(p.intern.get(l).unwrap());
        }
        let s1 = Side { party, active_idx: 0, ..Default::default() };
        let s2 = Side { party: vec![build_poke(p, opp, "M-6")], active_idx: 0, ..Default::default() };
        let f = Field::default();
        let pr: &Pack = p;
        let c = prune_immune_moves(pr, &s1, &s2, &f, candidate_actions(pr, &s1, &s2, &f, false));
        c.iter()
            .map(|a| match a.kind {
                ActKind::Move => {
                    format!("{}{}", if a.do_mega { "メガ+" } else { "" }, pr.intern.resolve(a.mv.as_ref().unwrap().name))
                }
                _ => "交代".to_string(),
            })
            .collect()
    }

    #[test]
    fn 無効技を根の候補から外す() {
        let mut p = pack();
        let n = names(&mut p, HIP, SAL, &[], None);
        assert!(!n.contains(&"じしん".to_string()) && n.contains(&"あくび".to_string()), "{n:?}");
        let n = names(&mut p, GAR, SKA, &[], None);
        assert!(!n.contains(&"どくづき".to_string()) && !n.contains(&"じしん".to_string())
            && n.contains(&"ドラゴンクロー".to_string()), "{n:?}");
        let n = names(&mut p, SAL, MIM, &[], None);
        assert!(n.contains(&"メガ+すてみタックル".to_string()) && !n.contains(&"すてみタックル".to_string()), "{n:?}");
        let n = names(&mut p, GAR, SKA, &[HIP], Some("どくづき"));
        assert!(n.contains(&"どくづき".to_string()) && n.contains(&"交代".to_string()), "こだわり固定は外さない {n:?}");
        let n = names(&mut p, TAU, MIM, &[], None);
        assert!(n.contains(&"すてみタックル".to_string()) && n.contains(&"インファイト".to_string()), "きもったま {n:?}");
    }
}

static DEPTH_ON: std::sync::OnceLock<bool> = std::sync::OnceLock::new();
static DEPTH_HIST: std::sync::Mutex<[u64; 16]> = std::sync::Mutex::new([0; 16]);

/// 計測用（env MCTS_DEPTH_STATS=1）: 1 シミュレーションで木の中を何ターン進んだか（葉の評価までの手番数）の分布
fn depth_stat(d: usize) {
    if !*DEPTH_ON.get_or_init(|| std::env::var("MCTS_DEPTH_STATS").map(|v| v == "1").unwrap_or(false)) {
        return;
    }
    DEPTH_HIST.lock().unwrap_or_else(|e| e.into_inner())[d.min(15)] += 1;
}

pub fn depth_stats_take() -> Vec<u64> {
    let mut h = DEPTH_HIST.lock().unwrap_or_else(|e| e.into_inner());
    let out = h.to_vec();
    *h = [0; 16];
    out
}
