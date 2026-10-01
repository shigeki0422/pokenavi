//! simulator/learned_selection.py の学習選出（温度0）の Rust 版。提案の採点（live_feats）の中で使う。
//! 候補（3体＋先頭・メガ1体ルール）× 相手の仮定（ヒューリスティック選出 温度0＋温度1×2、採点1回）の状態ベクトルを
//! ValMLP（tanh 隠れ層＋sigmoid）で採点し、相手の仮定3つの平均が最大の候補（同点は先）を選ぶ。
//! 乱数: g＝ダメージ計算（Python のグローバル乱数に相当）、s＝相手の仮定の温度つき抽選（Python の rng 引数に相当）。
use crate::battle::Side;
use std::sync::atomic::{AtomicU64, Ordering};
use std::collections::HashMap;
use std::sync::{Mutex, OnceLock};
use crate::cpyrng::CpyRandom;
use crate::damage::Field;
use crate::features::{encode_state, DmgMemo, FeatTables};
use crate::pack::Pack;
use crate::poke::Poke;

pub struct Selector {
    pub h: usize,
    pub d: usize,
    pub w1: Vec<f64>,
    w1t: Vec<f64>,
    pub b1: Vec<f64>,
    pub w2: Vec<f64>,
    pub b2: f64,
    /// 高速版の個体ブロックの射影のキャッシュ: (陣営, ブロックのビット列) → 位置 0..3 の W1 射影を並べた 3h
    proj: Mutex<FnvMap<(u8, Vec<u64>), Vec<f64>>>,
}

impl Selector {
    pub fn from_json(path: &str) -> Option<Selector> {
        let v: serde_json::Value = serde_json::from_str(&std::fs::read_to_string(path).ok()?).ok()?;
        let w1 = v["W1"].as_array()?;
        let h = w1.len();
        let d = w1[0].as_array()?.len();
        let mut flat = Vec::with_capacity(h * d);
        for row in w1 {
            for x in row.as_array()? {
                flat.push(x.as_f64()?);
            }
        }
        let f = |k: &str| -> Option<Vec<f64>> { v[k].as_array()?.iter().map(|x| x.as_f64()).collect() };
        let mut w1t = vec![0.0f64; h * d];
        for j in 0..h {
            for k in 0..d {
                w1t[k * h + j] = flat[j * d + k];
            }
        }
        Some(Selector { h, d, w1: flat, w1t, b1: f("b1")?, w2: f("W2")?, b2: v["b2"].as_f64()?, proj: Mutex::new(FnvMap::default()) })
    }

    /// 個体 p のブロック（陣営 side の位置 0..3、先頭の添字 base）の W1 射影を位置ごとに並べた 3h。添字順の逐次和
    fn proj_block(&self, pack: &Pack, ft: &FeatTables, p: &Poke, side: u8, base: usize, pbl: usize) -> Vec<f64> {
        let blk = crate::features::poke_block_vec(pack, ft, p);
        let key = (side, blk.iter().map(|x| x.to_bits()).collect::<Vec<u64>>());
        if let Some(v) = self.proj.lock().unwrap().get(&key) {
            return v.clone();
        }
        let h = self.h;
        let mut out = vec![0.0f64; 3 * h];
        for k in 0..3 {
            let o = &mut out[k * h..(k + 1) * h];
            for (t, &xv) in blk.iter().enumerate() {
                if xv == 0.0 {
                    continue;
                }
                let cl = &self.w1t[(base + k * pbl + t) * h..(base + k * pbl + t + 1) * h];
                for j in 0..h {
                    o[j] += xv * cl[j];
                }
            }
        }
        let mut m = self.proj.lock().unwrap();
        if m.len() >= 20000 {
            m.clear();
        }
        m.insert(key, out.clone());
        out
    }

    /// learned_selection._predict（1行）。tanh(x·W1ᵀ + b1)·W2 + b2 の sigmoid。
    /// 隠れ層の各和は添字順の逐次和（0 の入力は足しても値が変わらないので飛ばす＝predict_dense と同じ値）
    pub fn predict(&self, x: &[f64]) -> f64 {
        let h = self.h;
        let mut s = vec![0.0f64; h];
        for (k, &xk) in x.iter().enumerate().take(self.d) {
            if xk == 0.0 {
                continue;
            }
            let col = &self.w1t[k * h..(k + 1) * h];
            for j in 0..h {
                s[j] += xk * col[j];
            }
        }
        let mut z = 0.0f64;
        for j in 0..h {
            z += (s[j] + self.b1[j]).tanh() * self.w2[j];
        }
        1.0 / (1.0 + (-(z + self.b2)).exp())
    }

    /// 素朴な実装（照合用）
    pub fn predict_dense(&self, x: &[f64]) -> f64 {
        let mut z = 0.0f64;
        for j in 0..self.h {
            let row = &self.w1[j * self.d..(j + 1) * self.d];
            let mut s = 0.0f64;
            for k in 0..self.d {
                s += x[k] * row[k];
            }
            z += (s + self.b1[j]).tanh() * self.w2[j];
        }
        1.0 / (1.0 + (-(z + self.b2)).exp())
    }
}

/// CpyRandom を BRng として渡す（ダメージ計算の乱数）
pub struct GRng<'a>(pub &'a mut CpyRandom);
impl crate::rng::BRng for GRng<'_> {
    fn random(&mut self) -> f64 {
        self.0.random()
    }
    fn choice(&mut self, n: usize) -> usize {
        self.0.choice(n)
    }
    fn randint(&mut self, a: i64, b: i64) -> i64 {
        self.0.randint(a, b)
    }
    fn choices(&mut self) -> i64 {
        self.0.choices()
    }
}

fn mega_bounds(party: &[Poke]) -> (usize, usize) {
    let t = if party.iter().any(|p| p.mega.is_some()) { 1 } else { 0 };
    let e = |k: &str| std::env::var(k).ok().and_then(|v| v.parse().ok()).unwrap_or(t);
    (e("MIN_MEGA"), e("MAX_MEGA"))
}

/// learned_selection._candidates
pub fn candidates(party: &[Poke], n: usize) -> Vec<Vec<usize>> {
    let (lo, hi) = mega_bounds(party);
    let m = party.len();
    let mut out = Vec::new();
    let mut c = vec![0usize; n];
    fn rec(start: usize, k: usize, m: usize, n: usize, c: &mut Vec<usize>, all: &mut Vec<Vec<usize>>) {
        if k == n {
            all.push(c.clone());
            return;
        }
        for i in start..m {
            c[k] = i;
            rec(i + 1, k + 1, m, n, c, all);
        }
    }
    let mut combos = Vec::new();
    rec(0, 0, m, n, &mut c, &mut combos);
    for cb in combos {
        let nm = cb.iter().filter(|&&i| party[i].mega.is_some()).count();
        if nm < lo || nm > hi {
            continue;
        }
        for li in 0..n {
            let mut o = vec![cb[li]];
            o.extend(cb.iter().enumerate().filter(|(j, _)| *j != li).map(|(_, &i)| i));
            out.push(o);
        }
    }
    out
}

/// 選出（温度0）。sel が None ならヒューリスティック選出（learned_select_party がモデル無しで select_party に落ちるのと同じ）
#[allow(clippy::too_many_arguments)]
pub fn select(
    pack: &Pack,
    ft: &FeatTables,
    sel: Option<&Selector>,
    me: &mut Vec<Poke>,
    opp: &mut Vec<Poke>,
    n: usize,
    g: &mut CpyRandom,
    s: &mut CpyRandom,
) -> Vec<usize> {
    select_cached(pack, ft, sel, me, opp, n, g, s, &mut PairCache::default(), true)
}

/// select と同じ。pc は同じ2パーティの選出（自分→相手・相手→自分）で対面ごとの与ダメ割合を使い回す
/// （me_is_x: 1回目の呼び出しの自分側なら true、自分と相手を入れ替えた2回目なら false）
#[allow(clippy::too_many_arguments)]
pub fn select_cached(
    pack: &Pack,
    ft: &FeatTables,
    sel: Option<&Selector>,
    me: &mut Vec<Poke>,
    opp: &mut Vec<Poke>,
    n: usize,
    g: &mut CpyRandom,
    s: &mut CpyRandom,
    pc: &mut PairCache,
    me_is_x: bool,
) -> Vec<usize> {
    let pen: f64 = std::env::var("MEGA_PENALTY").ok().and_then(|v| v.parse().ok()).unwrap_or(50.0);
    let sel = match sel {
        Some(x) if me.len() > n => x,
        _ => {
            let mut gr = GRng(g);
            let mut sr = || s.random();
            return crate::ai::select_party_multi(pack, me, opp, n, &[0.0], pen, &mut gr, &mut sr).remove(0);
        }
    };
    let nb = n.min(opp.len());
    let simple = fast_on() && me.iter().chain(opp.iter()).all(|p| pristine(pack, ft, p));
    let chk = if simple && fast_check() { Some((g.clone(), s.clone())) } else { None };
    let tab = if simple {
        let mut sr = || s.random();
        heur_tab(pack, opp, me, nb, pen, &mut sr, pc, !me_is_x)
    } else {
        None
    };
    if let (Some(t), Some((mut g2, mut s2))) = (&tab, chk) {
        let want = {
            let mut gr = GRng(&mut g2);
            let mut sr = || s2.random();
            crate::ai::select_party_multi(pack, opp, me, nb, &[0.0, 1.0, 1.0], pen, &mut gr, &mut sr)
        };
        let same = *t == want && g2.random() == g.clone().random() && s2.random() == s.clone().random();
        let mut st = FAST_STATS.get_or_init(|| Mutex::new(FastStats::default())).lock().unwrap();
        st.3 += 1;
        if !same {
            st.4 += 1;
        }
    }
    let osels = match tab {
        Some(x) => x,
        None => {
            let mut gr = GRng(g);
            let mut sr = || s.random();
            crate::ai::select_party_multi(pack, opp, me, nb, &[0.0, 1.0, 1.0], pen, &mut gr, &mut sr)
        }
    };
    let cands = candidates(me, n);
    if cands.is_empty() {
        let mut gr = GRng(g);
        let mut sr = || s.random();
        return crate::ai::select_party_multi(pack, me, opp, n, &[0.0], pen, &mut gr, &mut sr).remove(0);
    }
    if fast_on() && osels.len() == 3 && osels.iter().all(|o| o.len() == 3) && cands.iter().all(|c| c.len() == 3) {
        if let Some((best, vals)) = select_fast(pack, ft, sel, me, opp, &osels, &cands, pc, me_is_x) {
            if !fast_check() {
                return cands[best].clone();
            }
            let old = select_ref(pack, ft, sel, me, opp, &osels, &cands, g);
            let mut st = FAST_STATS.get_or_init(|| Mutex::new(FastStats::default())).lock().unwrap();
            st.0 += 1;
            if old.0 != best {
                st.1 += 1;
            }
            for (a, b) in vals.iter().zip(old.1.iter()) {
                let d = (a - b).abs();
                if d > st.2 {
                    st.2 = d;
                }
            }
            return cands[old.0].clone();
        }
        FAST_FALLBACK.fetch_add(1, Ordering::Relaxed);
    }
    cands[select_ref(pack, ft, sel, me, opp, &osels, &cands, g).0].clone()
}

/// 元の実装（候補×相手の仮定ごとに状態を符号化して推論）。戻り値: (最良の候補, 各候補の値)
#[allow(clippy::too_many_arguments)]
fn select_ref(
    pack: &Pack,
    ft: &FeatTables,
    sel: &Selector,
    me: &mut Vec<Poke>,
    opp: &mut Vec<Poke>,
    osels: &[Vec<usize>],
    cands: &[Vec<usize>],
    g: &mut CpyRandom,
) -> (usize, Vec<f64>) {
    let mut memo = DmgMemo::default();
    let mut best = 0usize;
    let mut bv = f64::NEG_INFINITY;
    let mut vals = Vec::with_capacity(cands.len());
    for (k, c) in cands.iter().enumerate() {
        let mut v = [0.0f64; 3];
        for (j, os) in osels.iter().enumerate() {
            let mut sides = [
                Side { party: c.iter().map(|&i| me[i].clone()).collect(), active_idx: 0, field_idx: 0, ..Default::default() },
                Side { party: os.iter().map(|&i| opp[i].clone()).collect(), active_idx: 0, field_idx: 1, ..Default::default() },
            ];
            let mut field = Field::default();
            let x = encode_state(pack, ft, &mut sides, 0, &mut field, &mut memo, &mut GRng(g));
            v[j] = sel.predict(&x);
        }
        let sc = (v[0] + v[1] + v[2]) / 3.0;
        vals.push(sc);
        if sc > bv {
            bv = sc;
            best = k;
        }
    }
    (best, vals)
}

// ── 高速版（2026-10-01）: 第1層が線形なので W1·x を寄与の和に分解し、選出1回につき対面ごとに1回だけ前計算する。
// 状態ベクトル（3体×3体・無傷）の内訳:
//   個体ブロック（陣営×位置×個体。個体だけで決まる）／能力ランク・生存数・HP合計・開示・天候・場・設置・壁（無傷なら定数）／
//   期待与ダメ割合 3x3×2 と素早さ上回り 3x3（自分の個体×相手の個体×位置の組）／先頭どうしの素早さ2つ（自分の先頭×相手の先頭）。
//   個体の組に非線形に依存するのは、半減きのみ・ホズのみの消費だけ（符号化の中で前の対面の被弾で消費され、同じ受け手の後の対面と、
//   相手→自分の向きでその持ち主が攻める側の対面の値が変わる）。この分は消費の流れを候補ごとに追って差分を足す。
// 相手の仮定 u（重複は1回）ごとに base[u]＝b1＋定数＋相手のブロック、W[u][p][k]＝自分 p を位置 k に置いたときの
// ブロック・与ダメ・素早さ（k=0 は先頭どうしの素早さも）の寄与を作り、候補の値は base＋W×3＋tanh＋第2層だけ。
// 個体ブロックの射影は Selector 内のキャッシュ（パネル・候補の個体は何度も出る）。対面の与ダメ割合は自分→相手・相手→自分の
// 2回の選出で共有（PairCache）。和の順序だけが元と違う（値の差は丸め誤差のみ）。
// 元の実装に落とす: 無傷でない・能力ランク・じゅうでん等が残っている・乱数を消費する技（きまぐレーザー）・
// 消費される持ち物とかるわざの組（消費で素早さが変わる）・ダメージ計算が乱数を引いた。

type FastStats = (u64, u64, f64, u64, u64);
static FAST_STATS: OnceLock<Mutex<FastStats>> = OnceLock::new();
static FAST_FALLBACK: AtomicU64 = AtomicU64::new(0);

fn fast_on() -> bool {
    static V: OnceLock<bool> = OnceLock::new();
    *V.get_or_init(|| std::env::var("SEL_FAST").map(|v| v != "0").unwrap_or(true))
}

fn fast_check() -> bool {
    static V: OnceLock<bool> = OnceLock::new();
    *V.get_or_init(|| std::env::var("SEL_FAST_CHECK").map(|v| v == "1").unwrap_or(false))
}

/// 照合用（SEL_FAST_CHECK=1）: (高速版で選んだ回数, 元の実装と選出が違った回数, 候補の値の差の最大, 元の実装に落とした回数,
/// 相手の仮定を表で計算した回数, そのうち元の実装と仮定・乱数の消費が違った回数)。読むとゼロに戻す
pub fn fast_stats_take() -> (u64, u64, f64, u64, u64, u64) {
    let mut st = FAST_STATS.get_or_init(|| Mutex::new(FastStats::default())).lock().unwrap();
    let r = (st.0, st.1, st.2, FAST_FALLBACK.swap(0, Ordering::Relaxed), st.3, st.4);
    *st = FastStats::default();
    r
}

fn consumable(pack: &Pack, p: &Poke) -> bool {
    p.item.map_or(false, |i| i == pack.sy.it.ホズのみ || pack.berry_resist.contains_key(&i))
}

fn pristine(pack: &Pack, ft: &FeatTables, p: &Poke) -> bool {
    p.is_alive
        && p.hp == p.max_hp
        && !p.charged
        && !p.electromorphosis_charged
        && p.stage_attack == 0
        && p.stage_defense == 0
        && p.stage_sp_attack == 0
        && p.stage_sp_defense == 0
        && p.stage_speed == 0
        && p.stage_accuracy == 0
        && p.stage_evasion == 0
        && !(consumable(pack, p) && p.ability == pack.sy.ab.かるわざ)
        && !p.moves.iter().any(|m| Some(m.name) == ft.kmg)
}

/// 攻め手→受け手1組の期待与ダメ割合。v[攻め手の持ち物が消費済み*2＋受け手の持ち物が消費済み]、
/// cons[攻め手の状態]＝受け手が無傷の持ち物でこの組を受けたら消費するか
#[derive(Clone, Copy, Default)]
struct PairT {
    v: [f64; 4],
    cons: [bool; 2],
}

struct Tabs {
    nx: usize,
    ny: usize,
    xy: Vec<PairT>,
    yx: Vec<PairT>,
}

/// 同じ2パーティの選出2回（自分→相手、相手→自分）で共有する対面ごとの与ダメ割合（tabs）と、
/// 相手の仮定（ヒューリスティック選出）の1対面の最大期待ダメージ（hb。キーは heur_key）
#[derive(Default)]
pub struct PairCache {
    tabs: Option<Tabs>,
    hb: FnvMap<u32, (f64, bool)>,
    hbad: bool,
}

/// 乱数を引いたら印を付ける（引かれたら表は使わず元の実装へ）
struct FlagRng(bool);
impl crate::rng::BRng for FlagRng {
    fn random(&mut self) -> f64 {
        self.0 = true;
        0.0
    }
    fn choice(&mut self, _n: usize) -> usize {
        self.0 = true;
        0
    }
    fn randint(&mut self, a: i64, _b: i64) -> i64 {
        self.0 = true;
        a
    }
    fn choices(&mut self) -> i64 {
        self.0 = true;
        2
    }
}

/// ai::select_party_multi(party, opp, 温度 0,1,1) を表で。party_is_x: party が PairCache の x 側か
#[allow(clippy::too_many_arguments)]
fn heur_tab(
    pack: &Pack,
    party: &[Poke],
    opp: &[Poke],
    n: usize,
    pen: f64,
    srng: &mut dyn FnMut() -> f64,
    pc: &mut PairCache,
    party_is_x: bool,
) -> Option<Vec<Vec<usize>>> {
    if pc.hbad || party.len() > 15 || opp.len() > 15 {
        return None;
    }
    let hb = &mut pc.hb;
    let mut bad = false;
    let mut bed = |pa: bool, ai: usize, am: bool, ac: bool, di: usize, dm: bool, dc: bool| -> Option<(f64, bool)> {
        let ax = pa == party_is_x;
        let key = (ax as u32) | (ai as u32) << 1 | (am as u32) << 5 | (ac as u32) << 6 | (di as u32) << 7 | (dm as u32) << 11 | (dc as u32) << 12;
        if let Some(&r) = hb.get(&key) {
            return Some(r);
        }
        let (att, def) = if pa { (&party[ai], &opp[di]) } else { (&opp[ai], &party[di]) };
        let mut a = att.clone();
        let mut d = def.clone();
        if am {
            crate::poke::mega_evolve_poke(pack, &mut a);
        }
        if ac {
            a.item = None;
        }
        if dm {
            crate::poke::mega_evolve_poke(pack, &mut d);
        }
        if dc {
            d.item = None;
        }
        let it = d.item;
        let mut f = Field::default();
        let mut r = FlagRng(false);
        let v = crate::ai::best_expected_damage(pack, &mut a, &mut d, &mut f, &mut r);
        if r.0 {
            bad = true;
            return None;
        }
        let out = (v, d.item != it);
        hb.insert(key, out);
        Some(out)
    };
    let out = crate::ai::select_party_multi_tab(pack, party, opp, n, &[0.0, 1.0, 1.0], pen, srng, &mut bed);
    if bad {
        pc.hbad = true;
    }
    out
}

/// att/deff は作業用の複製（持ち物は呼ぶ前の状態に戻す）
fn pair_table(pack: &Pack, att: &mut Poke, deff: &mut Poke, rng_used: &mut bool) -> PairT {
    let ac = consumable(pack, att);
    let dc = consumable(pack, deff);
    let (ai, di) = (att.item, deff.item);
    let mut run = |a_cons: bool, d_cons: bool| -> (f64, bool) {
        att.item = if a_cons { None } else { ai };
        deff.item = if d_cons { None } else { di };
        let it = deff.item;
        let v = crate::features::pair_frac(pack, att, deff, rng_used);
        let c = deff.item != it;
        att.item = ai;
        deff.item = di;
        (v, c)
    };
    let mut t = PairT::default();
    (t.v[0], t.cons[0]) = run(false, false);
    if ac {
        (t.v[2], t.cons[1]) = run(true, false);
    } else {
        t.v[2] = t.v[0];
        t.cons[1] = t.cons[0];
    }
    if dc {
        t.v[1] = run(false, true).0;
        t.v[3] = if ac { run(true, true).0 } else { t.v[1] };
    } else {
        t.v[1] = t.v[0];
        t.v[3] = t.v[2];
    }
    t
}

impl Tabs {
    fn build(pack: &Pack, xs: &[Poke], ys: &[Poke]) -> Option<Tabs> {
        let (nx, ny) = (xs.len(), ys.len());
        let mut used = false;
        let mut xw = xs.to_vec();
        let mut yw = ys.to_vec();
        let mut xy = Vec::with_capacity(nx * ny);
        for x in xw.iter_mut() {
            for y in yw.iter_mut() {
                xy.push(pair_table(pack, x, y, &mut used));
            }
        }
        let mut yx = Vec::with_capacity(nx * ny);
        for y in yw.iter_mut() {
            for x in xw.iter_mut() {
                yx.push(pair_table(pack, y, x, &mut used));
            }
        }
        if used {
            return None;
        }
        Some(Tabs { nx, ny, xy, yx })
    }
}

/// 定数部分の符号化（技なし＝ダメージ計算なし）用。乱数は引かれない
struct NoRng;
impl crate::rng::BRng for NoRng {
    fn random(&mut self) -> f64 {
        0.0
    }
    fn choice(&mut self, _n: usize) -> usize {
        0
    }
    fn randint(&mut self, a: i64, _b: i64) -> i64 {
        a
    }
    fn choices(&mut self) -> i64 {
        2
    }
}

/// 射影キャッシュのキー用（8バイトずつの FNV 風。既定の SipHash は 150 語のキーで遅い）
#[derive(Default, Clone, Copy)]
struct Fnv(u64);
impl std::hash::Hasher for Fnv {
    fn finish(&self) -> u64 {
        self.0
    }
    fn write(&mut self, b: &[u8]) {
        let mut it = b.chunks_exact(8);
        for c in &mut it {
            self.write_u64(u64::from_le_bytes(c.try_into().unwrap()));
        }
        for &x in it.remainder() {
            self.write_u64(x as u64);
        }
    }
    fn write_u64(&mut self, x: u64) {
        let h = if self.0 == 0 { 0xcbf29ce484222325 } else { self.0 };
        self.0 = (h ^ x).wrapping_mul(0x100000001b3).rotate_left(29);
    }
}
type FnvMap<K, V> = HashMap<K, V, std::hash::BuildHasherDefault<Fnv>>;

/// 戻り値: (最良の候補, 各候補の値)。None なら元の実装で
#[allow(clippy::too_many_arguments)]
fn select_fast(
    pack: &Pack,
    ft: &FeatTables,
    sel: &Selector,
    me: &[Poke],
    opp: &[Poke],
    osels: &[Vec<usize>],
    cands: &[Vec<usize>],
    pc: &mut PairCache,
    me_is_x: bool,
) -> Option<(usize, Vec<f64>)> {
    if me.len() < 3 || opp.len() < 3 || !me.iter().chain(opp.iter()).all(|p| pristine(pack, ft, p)) {
        return None;
    }
    let (h, d) = (sel.h, sel.d);
    let pbl = crate::features::poke_block_len(pack);
    let per = 3 * pbl + 7 + 2;
    let (m1, m2, sp) = (2 * per, 2 * per + 9, 2 * per + 18);
    if d != crate::features::feature_dim(pack) {
        return None;
    }
    if pc.tabs.is_none() {
        let (xs, ys) = if me_is_x { (me, opp) } else { (opp, me) };
        pc.tabs = Some(Tabs::build(pack, xs, ys)?);
    }
    let tb = pc.tabs.as_ref().unwrap();
    let (nm, no) = (me.len(), opp.len());
    if (if me_is_x { (tb.nx, tb.ny) } else { (tb.ny, tb.nx) }) != (nm, no) {
        return None;
    }
    // 自分 p → 相手 q / 相手 q → 自分 p
    let d0 = |p: usize, q: usize| -> &PairT { if me_is_x { &tb.xy[p * tb.ny + q] } else { &tb.yx[p * tb.nx + q] } };
    let d1 = |q: usize, p: usize| -> &PairT { if me_is_x { &tb.yx[q * tb.nx + p] } else { &tb.xy[q * tb.ny + p] } };

    // 定数部分: 技を外した複製で符号化（ダメージ計算なし）し、個体ブロック・与ダメ・素早さを 0 にした残り
    let cst = {
        let strip = |p: &Poke| {
            let mut q = p.clone();
            q.moves.clear();
            q
        };
        let mut sides = [
            Side { party: me[..3].iter().map(strip).collect(), active_idx: 0, field_idx: 0, ..Default::default() },
            Side { party: opp[..3].iter().map(strip).collect(), active_idx: 0, field_idx: 1, ..Default::default() },
        ];
        let mut field = Field::default();
        let mut memo = DmgMemo::default();
        let mut c = encode_state(pack, ft, &mut sides, 0, &mut field, &mut memo, &mut NoRng);
        if c.len() != d {
            return None;
        }
        for v in c[0..3 * pbl].iter_mut() {
            *v = 0.0;
        }
        for v in c[per..per + 3 * pbl].iter_mut() {
            *v = 0.0;
        }
        for v in c[m1..sp + 9].iter_mut() {
            *v = 0.0;
        }
        c[d - 2] = 0.0;
        c[d - 1] = 0.0;
        c
    };
    let col = |k: usize| &sel.w1t[k * h..(k + 1) * h];
    let axpy = |o: &mut [f64], a: f64, k: usize| {
        if a != 0.0 {
            let cl = col(k);
            for j in 0..h {
                o[j] += a * cl[j];
            }
        }
    };
    let mut c0 = sel.b1.clone();
    for (k, &v) in cst.iter().enumerate() {
        axpy(&mut c0, v, k);
    }
    // 個体ブロックの射影（位置 0..3 を並べた 3h）
    let u1: Vec<Vec<f64>> = me.iter().map(|p| sel.proj_block(pack, ft, p, 0, 0, pbl)).collect();
    let u2: Vec<Vec<f64>> = opp.iter().map(|p| sel.proj_block(pack, ft, p, 1, per, pbl)).collect();
    let spm: Vec<f64> = me.iter().map(|p| crate::features::plain_speed(pack, ft, p)).collect();
    let spo: Vec<f64> = opp.iter().map(|p| crate::features::plain_speed(pack, ft, p)).collect();
    let esm: Vec<i64> = me.iter().map(|p| p.eff_speed(pack)).collect();
    let eso: Vec<i64> = opp.iter().map(|p| p.eff_speed(pack)).collect();
    let consm: Vec<bool> = me.iter().map(|p| consumable(pack, p)).collect();
    let conso: Vec<bool> = opp.iter().map(|p| consumable(pack, p)).collect();

    // 相手の仮定の重複を除く
    let mut uniq: Vec<&Vec<usize>> = Vec::new();
    let mut umap = [0usize; 3];
    for (j, os) in osels.iter().enumerate() {
        umap[j] = match uniq.iter().position(|u| *u == os) {
            Some(i) => i,
            None => {
                uniq.push(os);
                uniq.len() - 1
            }
        };
    }
    let mut base: Vec<Vec<f64>> = Vec::with_capacity(uniq.len());
    let mut wt: Vec<Vec<f64>> = Vec::with_capacity(uniq.len()); // [(p*3+k)*h + j]
    for os in &uniq {
        let mut b = c0.clone();
        for k in 0..3 {
            let u = &u2[os[k]][k * h..(k + 1) * h];
            for j in 0..h {
                b[j] += u[j];
            }
        }
        base.push(b);
        let mut w = vec![0.0f64; nm * 3 * h];
        for p in 0..nm {
            for k in 0..3 {
                let o = &mut w[(p * 3 + k) * h..(p * 3 + k + 1) * h];
                o.copy_from_slice(&u1[p][k * h..(k + 1) * h]);
                for j in 0..3 {
                    let q = os[j];
                    axpy(o, d0(p, q).v[0], m1 + k * 3 + j);
                    axpy(o, d1(q, p).v[0], m2 + j * 3 + k);
                    let fast = if spm[p] < 0.0 || spo[q] < 0.0 { 0.0 } else if spm[p] >= spo[q] { 1.0 } else { 0.0 };
                    axpy(o, fast, sp + k * 3 + j);
                }
                if k == 0 {
                    let (a1, a2) = (esm[p], eso[os[0]]);
                    axpy(o, if a1 >= a2 { 1.0 } else { 0.0 }, d - 2);
                    axpy(o, ((a1 - a2) as f64 / 200.0).min(1.0).max(-1.0), d - 1);
                }
            }
        }
        wt.push(w);
    }

    let mut s = vec![0.0f64; h];
    let mut value = |c: &[usize], u: usize| -> f64 {
        s.copy_from_slice(&base[u]);
        let w = &wt[u];
        for k in 0..3 {
            let o = &w[(c[k] * 3 + k) * h..(c[k] * 3 + k + 1) * h];
            for j in 0..h {
                s[j] += o[j];
            }
        }
        let os = uniq[u];
        if c.iter().any(|&p| consm[p]) || os.iter().any(|&q| conso[q]) {
            // 符号化の順（自分→相手: 自分の位置 i × 相手の位置 j、次に相手→自分）に持ち物の消費を追う
            let mut dc = [false; 3];
            for i in 0..3 {
                for j in 0..3 {
                    let t = d0(c[i], os[j]);
                    if dc[j] {
                        axpy(&mut s, t.v[1] - t.v[0], m1 + i * 3 + j);
                    } else if t.cons[0] {
                        dc[j] = true;
                    }
                }
            }
            let mut mc = [false; 3];
            for i in 0..3 {
                let a = dc[i] as usize;
                for j in 0..3 {
                    let t = d1(os[i], c[j]);
                    let idx = a * 2 + mc[j] as usize;
                    if idx != 0 {
                        axpy(&mut s, t.v[idx] - t.v[0], m2 + i * 3 + j);
                    }
                    if !mc[j] && t.cons[a] {
                        mc[j] = true;
                    }
                }
            }
        }
        let mut z = 0.0f64;
        for j in 0..h {
            z += s[j].tanh() * sel.w2[j];
        }
        1.0 / (1.0 + (-(z + sel.b2)).exp())
    };
    let mut best = 0usize;
    let mut bv = f64::NEG_INFINITY;
    let mut vals = Vec::with_capacity(cands.len());
    let mut uv = vec![0.0f64; uniq.len()];
    for (k, c) in cands.iter().enumerate() {
        for (u, x) in uv.iter_mut().enumerate() {
            *x = value(c, u);
        }
        let sc = (uv[umap[0]] + uv[umap[1]] + uv[umap[2]]) / 3.0;
        vals.push(sc);
        if sc > bv {
            bv = sc;
            best = k;
        }
    }
    Some((best, vals))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sparse_predict_equals_dense() {
        let p = concat!(env!("CARGO_MANIFEST_DIR"), "/../../simulator/selector_m6b.json");
        let s = match Selector::from_json(p) {
            Some(s) => s,
            None => return,
        };
        let mut seed = 12345u64;
        for t in 0..50 {
            let x: Vec<f64> = (0..s.d)
                .map(|_| {
                    seed = seed.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
                    let u = (seed >> 11) as f64 / (1u64 << 53) as f64;
                    if u < 0.7 { 0.0 } else if t % 2 == 0 { -0.0 + (u - 0.85) * 4.0 } else { 1.0 }
                })
                .collect();
            assert_eq!(s.predict(&x).to_bits(), s.predict_dense(&x).to_bits());
        }
    }

    /// 高速版（分解した第1層・表で引く相手の仮定）が元の実装と同じ選出・値の差は丸め誤差だけ（半減きのみ・ホズのみの消費を含む）
    #[test]
    fn fast_equals_ref() {
        let p = concat!(env!("CARGO_MANIFEST_DIR"), "/../../simulator/selector_m6b.json");
        let sel = match Selector::from_json(p) {
            Some(s) => s,
            None => return,
        };
        let mut pack = Pack::load(concat!(env!("CARGO_MANIFEST_DIR"), "/../../_rust_engine/datapack.json"));
        let a = [
            "ボーマンダ@ボーマンダナイト:いじっぱり:げきりん|じしん|すてみタックル|りゅうのまい:0/32/0/0/0/32:いかく",
            "ギルガルド@いのちのたま:れいせい:かげうち|アイアンヘッド|キングシールド|シャドーボール:32/0/0/32/0/0:バトルスイッチ",
            "アシレーヌ@リンドのみ:ずぶとい:なみのり|ねむる|めいそう|ムーンフォース:32/0/32/0/0/0:げきりゅう",
            "カバルドン@イトケのみ:わんぱく:じしん|あくび|ふきとばし|なまける:32/0/32/0/0/0:すなおこし",
            "ミミッキュ@いのちのたま:ようき:じゃれつく|シャドークロー|かげうち|つるぎのまい:0/32/0/0/0/32:ばけのかわ",
            "サーフゴー@たべのこし:ひかえめ:シャドーボール|ゴールドラッシュ|わるだくみ|じこさいせい:32/0/0/32/0/0:おうごんのからだ",
        ];
        let b = [
            "ガブリアス@ヤチェのみ:ようき:じしん|ドラゴンクロー|スケイルショット|つるぎのまい:0/32/0/0/0/32:さめはだ",
            "イダイトウ(オス)@こだわりハチマキ:いじっぱり:ウェーブタックル|おはかまいり|アクアジェット|クイックターン:0/32/0/0/0/32:てきおうりょく",
            "エアームド@オッカのみ:わんぱく:ボディプレス|はねやすめ|てっぺき|ステルスロック:32/0/32/0/0/0:がんじょう",
            "リザードン@リザードナイトＹ:おくびょう:かえんほうしゃ|ソーラービーム|エアスラッシュ|ねっぷう:0/0/0/32/0/32:もうか",
            "ニンフィア@ホズのみ:ひかえめ:ハイパーボイス|でんこうせっか|めいそう|まもる:32/0/0/32/0/0:フェアリースキン",
            "ドドゲザン@ヨプのみ:いじっぱり:ドゲザン|アイアンヘッド|ふいうち|つるぎのまい:0/32/0/0/0/32:そうだいしょう",
        ];
        let a6: Vec<Poke> = a.iter().map(|s| crate::poke::build_poke(&mut pack, s, "M-6")).collect();
        let b6: Vec<Poke> = b.iter().map(|s| crate::poke::build_poke(&mut pack, s, "M-6")).collect();
        let pack = pack;
        let ft = FeatTables::build(&pack);
        let mut pc = PairCache::default();
        for (k, (me, opp)) in [(&a6, &b6), (&b6, &a6)].into_iter().enumerate() {
            let me_is_x = k == 0;
            for seed in 0..4i128 {
                let mut s1 = CpyRandom::new(100 + seed);
                let mut s2 = s1.clone();
                let tab = heur_tab(&pack, opp, me, 3, 50.0, &mut || s1.random(), &mut pc, !me_is_x).unwrap();
                let (mut o2, mut m2) = (opp.clone(), me.clone());
                let mut g = CpyRandom::new(7);
                let want = crate::ai::select_party_multi(&pack, &mut o2, &mut m2, 3, &[0.0, 1.0, 1.0], 50.0, &mut GRng(&mut g), &mut || s2.random());
                assert_eq!(tab, want);
                assert_eq!(s1.random(), s2.random(), "相手の仮定の抽選の乱数の消費");
                let cands = candidates(me, 3);
                let (fb, fv) = select_fast(&pack, &ft, &sel, me, opp, &tab, &cands, &mut pc, me_is_x).unwrap();
                let (mut m3, mut o3) = (me.clone(), opp.clone());
                let (rb, rv) = select_ref(&pack, &ft, &sel, &mut m3, &mut o3, &tab, &cands, &mut g);
                assert_eq!(fb, rb);
                for (x, y) in fv.iter().zip(rv.iter()) {
                    assert!((x - y).abs() < 1e-12, "{x} {y}");
                }
            }
        }
        assert!(pc.tabs.as_ref().unwrap().xy.iter().any(|t| t.cons[0]), "半減きのみの消費が起きる組を含む");
    }

    #[test]
    fn candidates_order() {
        let ps: Vec<Poke> = (0..6).map(|_| Poke::default()).collect();
        let c = candidates(&ps, 3);
        assert_eq!(c.len(), 20 * 3);
        assert_eq!(c[0], vec![0, 1, 2]);
        assert_eq!(c[1], vec![1, 0, 2]);
        assert_eq!(c[2], vec![2, 0, 1]);
    }
}
