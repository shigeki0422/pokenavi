//! az_np.PVNetNP の forward を「逐次ループ順」で再実装する（パリティ規約 #2）。
//!
//! オラクル＝ハーネス側の逐次Python実装（内積は左→右の f64 加算、tanh/exp は libm）。
//! numpy(BLAS) の丸め順は再現対象外＝その差は R4-G4 の統計等価ゲートで担保する。
use serde_json::Value;

#[derive(Clone, Debug)]
pub struct NetW {
    pub dim: usize,
    pub hidden: usize,
    pub hidden2: usize,
    pub w1: Vec<f64>, // hidden x dim (row-major)
    pub b1: Vec<f64>,
    pub w2: Vec<f64>, // hidden2 x hidden
    pub b2: Vec<f64>,
    pub wv: Vec<f64>, // hidden2
    pub bv: f64,
    pub wp: Vec<f64>, // ACTION_DIM x hidden2
    pub bp: Vec<f64>,
}

pub const ACTION_DIM: usize = 12;

fn mat(v: &Value) -> (Vec<f64>, usize, usize) {
    let rows = v.as_array().unwrap();
    let c = rows[0].as_array().unwrap().len();
    let mut out = Vec::with_capacity(rows.len() * c);
    for r in rows {
        let a = r.as_array().unwrap();
        assert_eq!(a.len(), c);
        for x in a {
            out.push(x.as_f64().unwrap());
        }
    }
    (out, rows.len(), c)
}

fn vecf(v: &Value) -> Vec<f64> {
    v.as_array().unwrap().iter().map(|x| x.as_f64().unwrap()).collect()
}

impl NetW {
    pub fn from_value(v: &Value) -> Option<NetW> {
        if !v.is_object() || v.get("W1").is_none() {
            return None;
        }
        let (w1, h, d) = mat(&v["W1"]);
        let (w2, h2, hh) = mat(&v["W2"]);
        assert_eq!(hh, h);
        let (wp, ad, h2b) = mat(&v["Wp"]);
        assert_eq!(ad, ACTION_DIM);
        assert_eq!(h2b, h2);
        Some(NetW {
            dim: d,
            hidden: h,
            hidden2: h2,
            w1,
            b1: vecf(&v["b1"]),
            w2,
            b2: vecf(&v["b2"]),
            wv: vecf(&v["Wv"]),
            bv: v["bv"].as_f64().unwrap(),
            wp,
            bp: vecf(&v["bp"]),
        })
    }

    /// 最終隠れ層の活性（各行は左→右の逐次加算。行同士は独立なので8行ずつ
    /// インターリーブしてILPを稼ぐ＝丸め順は不変・ビット一致のまま高速化）。
    pub fn top(&self, x: &[f64], h1: &mut Vec<f64>, h2: &mut Vec<f64>, nz: &mut Vec<(usize, f64)>) {
        debug_assert_eq!(x.len(), self.dim);
        h1.clear();
        h1.resize(self.hidden, 0.0);
        // x はワンハット/フラグが多く 6-7割がゼロ。0*w は ±0.0 で、acc は +0.0 始まりのため
        // 決して -0.0 にならない ⇒ ゼロ項のスキップはビット完全等価（丸め順も不変）。
        nz.clear();
        for (k, v) in x.iter().enumerate() {
            if *v != 0.0 {
                nz.push((k, *v));
            }
        }
        rows8_sparse(&self.w1, self.dim, self.hidden, nz, &self.b1, h1);
        h2.clear();
        h2.resize(self.hidden2, 0.0);
        rows8(&self.w2, self.hidden, self.hidden2, h1, &self.b2, h2);
    }

    /// PVNetNP.evaluate(x, legal_idx) -> (prior[legal順], value)
    pub fn evaluate(&self, x: &[f64], legal: &[usize], scratch: &mut NetScratch) -> (Vec<f64>, f64) {
        let mut nz = std::mem::take(&mut scratch.nz);
        self.top(x, &mut scratch.h1, &mut scratch.h2, &mut nz);
        scratch.nz = nz;
        let top = &scratch.h2;
        let mut acc = 0.0f64;
        for k in 0..self.hidden2 {
            acc += top[k] * self.wv[k];
        }
        let v = 1.0 / (1.0 + (-(acc + self.bv)).exp());
        let mut lg: Vec<f64> = Vec::with_capacity(legal.len());
        for &a in legal {
            let row = &self.wp[a * self.hidden2..(a + 1) * self.hidden2];
            let mut s = 0.0f64;
            for k in 0..self.hidden2 {
                s += top[k] * row[k];
            }
            lg.push(s + self.bp[a]);
        }
        // lg = lg - lg.max(); e = exp(lg); p = e / (e.sum() or 1.0)
        let mut mx = f64::NEG_INFINITY;
        for &z in &lg {
            if z > mx {
                mx = z;
            }
        }
        let mut esum = 0.0f64;
        let mut e: Vec<f64> = Vec::with_capacity(lg.len());
        for &z in &lg {
            let q = (z - mx).exp();
            e.push(q);
            esum += q;
        }
        let den = if esum == 0.0 { 1.0 } else { esum };
        for q in e.iter_mut() {
            *q /= den;
        }
        (e, v)
    }
}

/// 非ゼロ入力のみを左→右順にたどる版（rows8 とビット完全一致）
#[inline]
fn rows8_sparse(w: &[f64], dim: usize, rows: usize, nz: &[(usize, f64)], b: &[f64], out: &mut [f64]) {
    const B: usize = 8;
    let mut j = 0usize;
    while j + B <= rows {
        let r0 = &w[j * dim..(j + B) * dim];
        let mut a = [0.0f64; B];
        for &(k, xv) in nz {
            a[0] += xv * r0[k];
            a[1] += xv * r0[dim + k];
            a[2] += xv * r0[2 * dim + k];
            a[3] += xv * r0[3 * dim + k];
            a[4] += xv * r0[4 * dim + k];
            a[5] += xv * r0[5 * dim + k];
            a[6] += xv * r0[6 * dim + k];
            a[7] += xv * r0[7 * dim + k];
        }
        for t in 0..B {
            out[j + t] = (a[t] + b[j + t]).tanh();
        }
        j += B;
    }
    while j < rows {
        let row = &w[j * dim..(j + 1) * dim];
        let mut acc = 0.0f64;
        for &(k, xv) in nz {
            acc += xv * row[k];
        }
        out[j] = (acc + b[j]).tanh();
        j += 1;
    }
}

/// 行ブロック8本の独立な逐次加算（各行内の順序は左→右のまま）
#[inline]
fn rows8(w: &[f64], dim: usize, rows: usize, x: &[f64], b: &[f64], out: &mut [f64]) {
    const B: usize = 8;
    let mut j = 0usize;
    while j + B <= rows {
        let r0 = &w[j * dim..(j + B) * dim];
        let mut a = [0.0f64; B];
        for k in 0..dim {
            let xv = x[k];
            for (t, av) in a.iter_mut().enumerate() {
                *av += xv * r0[t * dim + k];
            }
        }
        for t in 0..B {
            out[j + t] = (a[t] + b[j + t]).tanh();
        }
        j += B;
    }
    while j < rows {
        let row = &w[j * dim..(j + 1) * dim];
        let mut acc = 0.0f64;
        for k in 0..dim {
            acc += x[k] * row[k];
        }
        out[j] = (acc + b[j]).tanh();
        j += 1;
    }
}

#[derive(Default)]
pub struct NetScratch {
    pub h1: Vec<f64>,
    pub h2: Vec<f64>,
    pub nz: Vec<(usize, f64)>,
}
