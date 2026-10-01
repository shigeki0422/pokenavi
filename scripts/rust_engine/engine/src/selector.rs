//! simulator/learned_selection.py の学習選出（温度0）の Rust 版。提案の採点（live_feats）の中で使う。
//! 候補（3体＋先頭・メガ1体ルール）× 相手の仮定（ヒューリスティック選出 温度0＋温度1×2、採点1回）の状態ベクトルを
//! ValMLP（tanh 隠れ層＋sigmoid）で採点し、相手の仮定3つの平均が最大の候補（同点は先）を選ぶ。
//! 乱数: g＝ダメージ計算（Python のグローバル乱数に相当）、s＝相手の仮定の温度つき抽選（Python の rng 引数に相当）。
use crate::battle::Side;
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
        Some(Selector { h, d, w1: flat, w1t, b1: f("b1")?, w2: f("W2")?, b2: v["b2"].as_f64()? })
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
    let osels = {
        let mut gr = GRng(g);
        let mut sr = || s.random();
        crate::ai::select_party_multi(pack, opp, me, nb, &[0.0, 1.0, 1.0], pen, &mut gr, &mut sr)
    };
    let cands = candidates(me, n);
    if cands.is_empty() {
        let mut gr = GRng(g);
        let mut sr = || s.random();
        return crate::ai::select_party_multi(pack, me, opp, n, &[0.0], pen, &mut gr, &mut sr).remove(0);
    }
    let mut memo = DmgMemo::default();
    let mut best = 0usize;
    let mut bv = f64::NEG_INFINITY;
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
        if sc > bv {
            bv = sc;
            best = k;
        }
    }
    cands[best].clone()
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
