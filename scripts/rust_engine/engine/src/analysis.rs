//! 1v1 表示のためのルール層 API。Python の正本は `scripts/_mu_engine.py`。
//!
//! ここが担うのは「対戦本体を実走して確定数とダメージを得ること」だけで、
//! 割合(%)・乱数n発の確率・記号(◎○△▲×)の閾値といった表示計算は呼び出し側に置く。
//! ルールを持つ部分だけを一箇所に集めるのが目的で、表示計算を混ぜると
//! 「同じ判定が二重実装される」という当初の問題がここに再発する。
use crate::battle::{calc_hits, entry_effects, hit_damage, is_accuracy_chained, split2, ActKind, Action, Battle, Side};
use crate::damage::Field;
use crate::pack::Pack;
use crate::poke::{build_poke, mega_evolve_poke, Poke};
use crate::rng::BRng;
use std::collections::HashMap;

/// これ以上かかる技は「圏外」。`_mu_engine.CAP` と同値。
pub const CAP: i64 = 12;
pub const OUT_OF_RANGE: i64 = 999;
/// ダメージ乱数の段階数（85%〜100% の16段）。
pub const ROLLS: usize = 16;

/// 1.0 ちょうど未満の最大の f64。`_mu_engine` の `math.nextafter(1.0, 0.0)` と同値。
/// 判定は全て `rng() < prob` なので、prob<1 の追加効果は不発、prob=1 の確定効果
/// （必中急所・りゅうせいぐんの特攻ダウン等）だけが発動する。1.0 を入れると
/// `1.0 < 1.0` が偽になり確定効果まで殺す（Python 側で実際に殺していた）。
const ALMOST_ONE: f64 = f64::from_bits(0x3FEF_FFFF_FFFF_FFFF);

/// 連続技の回数を最大にする乱数。表示するダメージ幅の上端に使う。
/// calc_hits しか使わないので、急所や追加効果には影響しない。
struct MaxHitRng;
impl BRng for MaxHitRng {
    // 急所・追加効果は FixedRng と同じ扱い（prob=1 のものだけ発動）にしたうえで、
    // 連続技の回数だけを最大にする。
    fn random(&mut self) -> f64 { ALMOST_ONE }
    fn hit_continue(&mut self) -> f64 { 0.0 }   // ネズミざんを10回続ける
    fn choice(&mut self, _n: usize) -> usize { 0 }
    fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
    fn choices(&mut self) -> i64 { 5 }
}

struct FixedRng;
impl BRng for FixedRng {
    fn random(&mut self) -> f64 { ALMOST_ONE }
    // 1発ごとの命中判定は必中扱い（always_hit と同じ前提）。外れて止まる技は
    // 常に最大回数まで当たる。ネズミざんが「1発しか当たらない前提」になって
    // 圏外と出るのを避ける。
    fn hit_continue(&mut self) -> f64 { 0.0 }
    fn choice(&mut self, _n: usize) -> usize { 0 }
    fn randint(&mut self, a: i64, _b: i64) -> i64 { a }
    /// 連続技(2〜5発)の回数。確定数は保証値なので最小の2発。
    /// Python の `random.choices([2,3,4,5], ...)` を先頭固定した値と同じ。
    fn choices(&mut self) -> i64 { 2 }
}

/// 正規化ロール（0.0=最低乱数, 1.0=最高乱数）。`calc_damage` は `0.85 + r*0.15` で使う。
#[inline]
pub fn roll_of(step: usize) -> f64 {
    step as f64 / (ROLLS - 1) as f64
}

/// 表示する条件が「実際にその数値へ効いたか」を確かめるために、場や能力変化を打ち消す指定。
#[derive(Clone, Copy, PartialEq)]
pub enum Suppress {
    None,
    Weather,
    Terrain,
    Stages,
}

fn setup_sup(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64, sup: Suppress,
) -> Battle {
    let mut bt = setup(pack, spec_a, spec_b, season, roll);
    match sup {
        Suppress::None => {}
        Suppress::Weather => {
            bt.field.weather = None;
            bt.field.weather_count = 0;
        }
        Suppress::Terrain => {
            bt.field.electric_terrain = false;
            bt.field.grassy_terrain = false;
            bt.field.psychic_terrain = false;
            bt.field.misty_terrain = false;
            bt.field.electric_terrain_count = 0;
            bt.field.grassy_terrain_count = 0;
            bt.field.psychic_terrain_count = 0;
            bt.field.misty_terrain_count = 0;
        }
        Suppress::Stages => {
            for i in 0..2 {
                let p = &mut bt.sides[i].party[0];
                for k in 0..7u8 {
                    p.set_stage(k, 0);
                }
            }
        }
    }
    bt
}

fn setup(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, roll: f64) -> Battle {
    let mut a: Poke = build_poke(pack, spec_a, season);
    let mut b: Poke = build_poke(pack, spec_b, season);
    {
        let p: &Pack = pack;
        mega_evolve_poke(p, &mut a);
        mega_evolve_poke(p, &mut b);
    }
    let mut field = Field { roll_override: Some(roll), always_hit: true, ..Default::default() };
    let mut s1 = Side { party: vec![a], active_idx: 0, ..Default::default() };
    let mut s2 = Side { party: vec![b], active_idx: 0, ..Default::default() };
    {
        let p: &Pack = pack;
        entry_effects(p, &mut s1, 0, &mut field, &mut s2.party[0]);
        entry_effects(p, &mut s2, 1, &mut field, &mut s1.party[0]);
    }
    Battle::new(s1, s2, field)
}

/// `att` 側が同じ技を撃ち続け、もう一方は行動しない。`_mu_engine._run_inner` と同じ手順。
///
/// 攻撃側を常に side0 に置くと、両者が天候特性を持つ対面（キュウコン vs ペリッパー等）で
/// 「後から出た側の天候が勝つ」規則により、評価する向きで場が変わってしまう。
/// 場は対面ごとに1つなので、並び (spec_a, spec_b) は固定したまま攻撃側だけを指定する。
fn drive(bt: &mut Battle, pack: &Pack, att: usize, move_idx: usize, max_turns: i64) -> i64 {
    drive_rng(bt, pack, att, move_idx, max_turns, &mut FixedRng)
}

fn drive_rng(bt: &mut Battle, pack: &Pack, att: usize, move_idx: usize, max_turns: i64,
             rng: &mut dyn BRng) -> i64 {
    let mut turns = 0i64;
    bt.run_loop_lim(pack, rng, max_turns, |b2, _r| {
        turns += 1;
        let mv = b2.sides[att].active().moves.get(move_idx).cloned();
        let act = Action { kind: ActKind::Move, mv, move_idx: move_idx as i64, ..Default::default() };
        if att == 0 { [act, Action::default()] } else { [Action::default(), act] }
    }, |_| {});
    turns
}

/// `spec_a` が `move_idx` の技を撃ち続けて `spec_b` を倒すまでの発数と、初撃の与ダメージ。
/// 倒しきれなければ発数は `OUT_OF_RANGE`。
pub fn run_move(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, roll: f64,
) -> (i64, i64) {
    run_move_sup(pack, spec_a, spec_b, season, att, move_idx, roll, Suppress::None)
}

pub fn run_move_sup(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, roll: f64, sup: Suppress,
) -> (i64, i64) {
    let def = 1 - att;
    let mut bt = setup_sup(pack, spec_a, spec_b, season, roll, sup);
    let hp0 = bt.sides[def].active().max_hp;
    // 初撃ダメージは1ターンだけ進めた時点で測る（2発目以降は自己ランク変化等で変わる）
    let packr: &Pack = pack;
    drive(&mut bt, packr, att, move_idx, 1);
    let first = hp0 - bt.sides[def].active().hp;
    let mut turns = 1i64;
    if bt.sides[def].has_alive() {
        turns += drive(&mut bt, packr, att, move_idx, CAP);
    }
    let hits = if bt.sides[def].has_alive() { OUT_OF_RANGE } else { turns };
    (hits, first.max(0))
}

/// 入場効果まで済ませた時点の、両者の実効素早さと最大HP・技名・能力変化。
pub struct SideInfo {
    pub hp: i64,
    pub speed: i64,
    pub moves: Vec<(String, bool)>, // (技名, ダメージ技か)
    /// 入場時に変化した攻撃/特攻ランク（いかく・ダウンロード等）。0なら変化なし。
    pub atk_stage: i32,
    pub spa_stage: i32,
}

/// 対面開始時に成立している場。ダメージ計算に効くので表示側で明示するために返す。
pub struct FieldInfo {
    pub weather: Option<String>,
    pub terrain: Option<String>,
}

pub fn field_info(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str) -> FieldInfo {
    let bt = setup(pack, spec_a, spec_b, season, 0.0);
    let f = &bt.field;
    let w = f.weather.map(|s| pack.intern.resolve(s).to_string());
    let t = if f.electric_terrain { Some("エレキフィールド") }
        else if f.grassy_terrain { Some("グラスフィールド") }
        else if f.psychic_terrain { Some("サイコフィールド") }
        else if f.misty_terrain { Some("ミストフィールド") }
        else { None };
    FieldInfo { weather: w, terrain: t.map(|x| x.to_string()) }
}

pub fn side_info(pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str) -> (SideInfo, SideInfo) {
    let bt = setup(pack, spec_a, spec_b, season, 0.0);
    let packr: &Pack = pack;
    let one = |p: &Poke| SideInfo {
        atk_stage: p.stage(0),
        spa_stage: p.stage(2),
        hp: p.max_hp,
        speed: crate::ai::effective_speed(packr, p, &bt.field),
        moves: p
            .moves
            .iter()
            .map(|m| {
                (
                    packr.intern.resolve(m.name).to_string(),
                    m.category != crate::pack::Cat::Status && m.power.unwrap_or(0) > 0,
                )
            })
            .collect(),
    };
    (one(bt.sides[0].active()), one(bt.sides[1].active()))
}


/// `hits` 発以内に防御側を倒せる確率（0.0〜1.0）。各発のダメージ乱数は16段から
/// 独立に選ばれる前提で、局面を分岐させて厳密に数える。
///
/// ターン終了時の増減（たべのこし・オボンのみ・すなあらし・自分の反動）は
/// 対戦本体がそのまま処理するので、ここで再実装しない。以前 TypeScript 側が
/// この部分を独自に持っていたことが、確定数と表示の食い違いの発生源だった。
///
/// 枝は「防御側の残HPと持ち物」で畳む。攻撃側は同じ技を撃ち続けるため、
/// 同じターン数・同じ残HP・同じ持ち物に至った枝はその後の展開も等しい。
pub fn ko_probability(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, hits: usize,
) -> f64 {
    let def = 1 - att;
    let base = setup(pack, spec_a, spec_b, season, 0.0);
    let packr: &Pack = pack;
    let mut states: Vec<(Battle, f64)> = vec![(base, 1.0)];
    let mut ko = 0.0f64;
    for _ in 0..hits {
        let mut next: HashMap<(i64, Option<u16>), (Battle, f64)> = HashMap::new();
        for (bt, w) in states.into_iter() {
            let p = w / ROLLS as f64;
            for step in 0..ROLLS {
                let mut c = bt.clone();
                c.field.roll_override = Some(roll_of(step));
                let lim = c.turn + 1;
                drive(&mut c, packr, att, move_idx, lim);
                if !c.sides[def].has_alive() {
                    ko += p;
                    continue;
                }
                let key = { let d = c.sides[def].active(); (d.hp, d.item) };
                next.entry(key).and_modify(|e| e.1 += p).or_insert((c, p));
            }
        }
        states = next.into_values().collect();
        if states.is_empty() {
            break;
        }
    }
    ko
}


/// 技1回ぶんの与ダメージ（連続技は全ヒットの合計）。表示用。
///
/// 「1ターンで防御側の HP がいくら減ったか」ではなく「その技が与えるダメージ」を返す。
/// 前者を表示に使うと、ばけのかわで直撃が無効化された分・すなあらしの削り・
/// たべのこしの回復まで技のダメージとして出てしまう
/// （カバルドンのじしん→ミミッキュが「18〜18%」と表示された。内訳は身代わり16＋砂8）。
/// 発数の方は run_move（実走）で数えるので、耐え効果や回復はそちらに反映される。
pub fn move_damage(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, roll: f64,
) -> i64 {
    move_damage_sup(pack, spec_a, spec_b, season, att, move_idx, roll, Suppress::None, false)
}

/// `hits_max` は連続技の回数を最大にするかどうか。表示するダメージ幅は
/// 「最小回数×最低乱数 〜 最大回数×最高乱数」で出す（最小回数だけだと過小評価になる）。
pub fn move_damage_sup(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str,
    att: usize, move_idx: usize, roll: f64, sup: Suppress, hits_max: bool,
) -> i64 {
    let mut bt = setup_sup(pack, spec_a, spec_b, season, roll, sup);
    let packr: &Pack = pack;
    let mv = match bt.sides[att].active().moves.get(move_idx).cloned() {
        Some(m) => m,
        None => return 0,
    };
    let n = if hits_max {
        calc_hits(packr, &mv, bt.sides[att].active(), &mut MaxHitRng)
    } else {
        calc_hits(packr, &mv, bt.sides[att].active(), &mut FixedRng)
    };
    let mut total = 0i64;
    for hit_i in 0..n.max(1) {
        let Battle { sides, field, .. } = &mut bt;
        let (sa, sd) = split2(sides, att);
        let att = &mut sa.party[0];
        let def = &mut sd.party[0];
        // 1発ぶんの計算は対戦本体と同じ関数を使う（何発目かの反映を含む）。
        // ここで自前に組み直すと、対戦本体の変更が分析側に伝わらなくなる。
        let mut r = FixedRng;
        let d = hit_damage(packr, att, def, &mv, field, hit_i, false, Some(roll), &mut r);
        total += d;
        // マルチスケイル等「満タンのときだけ」の効果を2発目以降に持ち越さないよう、
        // 連続技の各ヒットは HP を減らしながら計算する。
        def.hp = (def.hp - d).max(1);
    }
    total
}


/// この技の表示値（与ダメ・確定数）に実際に効いた条件だけを返す。
///
/// 場に出ているものをそのまま並べると、無関係な計算にまで注記が付く。
/// （ミミッキュのウッドハンマー→カバルドンに「すなあらし で計算」と出た。
///   カバルドンは じめん で砂のダメージを受けず、砂は草技の威力にも効かない。）
/// 判定は実測で行う——その条件を打ち消して計算し直し、与ダメか確定数が
/// 変わったときだけ「効いた」とみなす。
pub fn relevant_conds(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize, move_idx: usize,
) -> Vec<String> {
    let base_bt = setup(pack, spec_a, spec_b, season, 0.0);
    let has_weather = base_bt.field.weather.is_some();
    let f = &base_bt.field;
    let has_terrain = f.electric_terrain || f.grassy_terrain || f.psychic_terrain || f.misty_terrain;
    let has_stage = (0..2).any(|i| (0..7u8).any(|k| base_bt.sides[i].party[0].stage(k) != 0));
    let weather_name = base_bt.field.weather.map(|w| pack.intern.resolve(w).to_string());
    let terrain_name = if f.electric_terrain { Some("エレキフィールド") }
        else if f.grassy_terrain { Some("グラスフィールド") }
        else if f.psychic_terrain { Some("サイコフィールド") }
        else if f.misty_terrain { Some("ミストフィールド") }
        else { None }.map(|x| x.to_string());
    let stage_label = {
        let p = &base_bt.sides[att].party[0];
        let a = p.stage(0);
        let c = p.stage(2);
        let mut v = Vec::new();
        if a != 0 { v.push(format!("攻撃{}{}", if a > 0 { "+" } else { "" }, a)); }
        if c != 0 { v.push(format!("特攻{}{}", if c > 0 { "+" } else { "" }, c)); }
        v.join("・")
    };
    drop(base_bt);

    let base_dmg = move_damage(pack, spec_a, spec_b, season, att, move_idx, 0.0);
    let (base_hits, _) = run_move(pack, spec_a, spec_b, season, att, move_idx, 0.0);
    let mut out = Vec::new();
    let mut check = |pack: &mut Pack, sup: Suppress, label: Option<String>| {
        let Some(label) = label else { return };
        if label.is_empty() { return; }
        // 与ダメが変われば確定数も見るまでもない。安い方から確かめる。
        let d = move_damage_sup(pack, spec_a, spec_b, season, att, move_idx, 0.0, sup, false);
        if d != base_dmg {
            out.push(label);
            return;
        }
        let (h, _) = run_move_sup(pack, spec_a, spec_b, season, att, move_idx, 0.0, sup);
        if h != base_hits {
            out.push(label);
        }
    };
    if has_weather { check(pack, Suppress::Weather, weather_name); }
    if has_terrain { check(pack, Suppress::Terrain, terrain_name); }
    if has_stage { check(pack, Suppress::Stages, Some(stage_label)); }
    // 1発ごとに命中判定がある技は、必中を仮定している以上「全部当たった場合」の値になる。
    // 妥当ではあるが読み手を誤解させるので明示する。
    {
        let bt = setup(pack, spec_a, spec_b, season, 0.0);
        if let Some(mv) = bt.sides[att].active().moves.get(move_idx) {
            if is_accuracy_chained(pack, mv) {
                out.push("最大ヒット時".to_string());
            }
        }
    }
    out
}


/// この技の連続回数の下限・上限。乱数で変わる技（2〜5回のもの、ネズミざん）は
/// 下限と上限が食い違う。表示するダメージ幅の両端に使う。
pub fn hit_range(
    pack: &mut Pack, spec_a: &str, spec_b: &str, season: &str, att: usize, move_idx: usize,
) -> (i64, i64) {
    let bt = setup(pack, spec_a, spec_b, season, 0.0);
    let packr: &Pack = pack;
    let Some(mv) = bt.sides[att].active().moves.get(move_idx).cloned() else { return (1, 1) };
    let p = bt.sides[att].active();
    (
        calc_hits(packr, &mv, p, &mut FixedRng).max(1),
        calc_hits(packr, &mv, p, &mut MaxHitRng).max(1),
    )
}
