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
    pub w1t: Vec<f64>, // dim x hidden（w1 の転置。forward 用）
    pub b1: Vec<f64>,
    pub w2: Vec<f64>, // hidden2 x hidden
    pub w2t: Vec<f64>, // hidden x hidden2
    pub b2: Vec<f64>,
    pub wv: Vec<f64>, // vbins=0 なら hidden2、vbins>0 なら vbins x hidden2（row-major）
    pub bv: f64,      // vbins=0 のときのスカラーバイアス
    /// 価値ヘッドのビン数。0=従来のスカラー(sigmoid)。>0 で two-hot 分類ヘッド
    /// （スカラー回帰は勝率0.5付近で勾配が潰れるので、分布で持つと接戦の局面も学習できる）。
    pub vbins: usize,
    pub bv_bins: Vec<f64>,
    pub vcent: Vec<f64>,
    pub wp: Vec<f64>, // ACTION_DIM x hidden2
    pub bp: Vec<f64>,
    /// 隠れ層の活性。既定 tanh。JSON の "act":"relu" で ReLU。
    /// 入力正規化は Python 側 fold_norm() で W1/b1 に畳み込まれている前提（ゼロスキップを壊さないため）。
    pub relu: bool,
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

fn transpose(w: &[f64], rows: usize, cols: usize) -> Vec<f64> {
    let mut t = vec![0.0f64; rows * cols];
    for r in 0..rows {
        for c in 0..cols {
            t[c * rows + r] = w[r * cols + c];
        }
    }
    t
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
        let vbins = v.get("vbins").and_then(|x| x.as_u64()).unwrap_or(0) as usize;
        let (wv_flat, bv_scalar, bv_bins, vcent) = if vbins > 0 {
            let (w, rows, cols) = mat(&v["Wv"]);
            assert_eq!(rows, vbins);
            assert_eq!(cols, h2);
            let c: Vec<f64> = (0..vbins).map(|i| (i as f64 + 0.5) / vbins as f64).collect();
            (w, 0.0, vecf(&v["bv"]), c)
        } else {
            (vecf(&v["Wv"]), v["bv"].as_f64().unwrap(), Vec::new(), Vec::new())
        };
        Some(NetW {
            dim: d,
            hidden: h,
            hidden2: h2,
            w1t: transpose(&w1, h, d),
            w1,
            b1: vecf(&v["b1"]),
            w2t: transpose(&w2, h2, h),
            w2,
            b2: vecf(&v["b2"]),
            wv: wv_flat,
            bv: bv_scalar,
            vbins,
            bv_bins,
            vcent,
            wp,
            bp: vecf(&v["bp"]),
            relu: v.get("act").and_then(|a| a.as_str()) == Some("relu"),
        })
    }

    /// 最終隠れ層の活性（各出力は入力の左→右の逐次加算＝丸め順は Python の逐次実装と同じ）。
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
        cols_acc(&self.w1t, self.hidden, nz, &self.b1, h1, self.relu);
        h2.clear();
        h2.resize(self.hidden2, 0.0);
        nz.clear();
        nz.extend(h1.iter().copied().enumerate());
        cols_acc(&self.w2t, self.hidden2, nz, &self.b2, h2, self.relu);
    }

    /// top表現 → 価値。two-hot のときは softmax の期待値（Python の _value_from_top と同じ順序）。
    fn value_of(&self, top: &[f64]) -> f64 {
        if self.vbins == 0 {
            let mut acc = 0.0f64;
            for k in 0..self.hidden2 {
                acc += top[k] * self.wv[k];
            }
            return 1.0 / (1.0 + (-(acc + self.bv)).exp());
        }
        let mut z: Vec<f64> = Vec::with_capacity(self.vbins);
        for b in 0..self.vbins {
            let row = &self.wv[b * self.hidden2..(b + 1) * self.hidden2];
            let mut acc = 0.0f64;
            for k in 0..self.hidden2 {
                acc += top[k] * row[k];
            }
            z.push(acc + self.bv_bins[b]);
        }
        let mx = z.iter().fold(f64::NEG_INFINITY, |a, &b| if b > a { b } else { a });
        let mut sum = 0.0f64;
        for x in z.iter_mut() {
            *x = (*x - mx).exp();
            sum += *x;
        }
        let den = sum + 1e-12;
        let mut v = 0.0f64;
        for b in 0..self.vbins {
            v += (z[b] / den) * self.vcent[b];
        }
        v
    }

    /// PVNetNP.evaluate(x, legal_idx) -> (prior[legal順], value)
    pub fn evaluate(&self, x: &[f64], legal: &[usize], scratch: &mut NetScratch) -> (Vec<f64>, f64) {
        let mut nz = std::mem::take(&mut scratch.nz);
        self.top(x, &mut scratch.h1, &mut scratch.h2, &mut nz);
        scratch.nz = nz;
        let top = &scratch.h2;
        let v = self.value_of(top);
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

#[inline]
fn act1(z: f64, relu: bool) -> f64 {
    if relu {
        if z > 0.0 {
            z
        } else {
            0.0
        }
    } else {
        z.tanh()
    }
}

/// 転置した重みで入力を全出力へ足し込む（out は 0.0 で渡す）。各出力の加算は入力の左→右順のままなので
/// 行ごとの内積とビット完全一致。入力4つずつまとめて足すのは出力の読み書きを1/4にするため（順序は変わらない）
#[inline]
fn cols_acc(wt: &[f64], rows: usize, xs: &[(usize, f64)], b: &[f64], out: &mut [f64], relu: bool) {
    let out = &mut out[..rows];
    let col = |k: usize| &wt[k * rows..(k + 1) * rows];
    let mut q = xs.chunks_exact(4);
    for c in &mut q {
        let (x0, x1, x2, x3) = (c[0].1, c[1].1, c[2].1, c[3].1);
        let (c0, c1, c2, c3) = (col(c[0].0), col(c[1].0), col(c[2].0), col(c[3].0));
        for j in 0..rows {
            let mut o = out[j];
            o += x0 * c0[j];
            o += x1 * c1[j];
            o += x2 * c2[j];
            o += x3 * c3[j];
            out[j] = o;
        }
    }
    for &(k, xv) in q.remainder() {
        for (o, w) in out.iter_mut().zip(col(k)) {
            *o += xv * w;
        }
    }
    for (o, bj) in out.iter_mut().zip(b) {
        *o = act1(*o + bj, relu);
    }
}

#[derive(Default)]
pub struct NetScratch {
    pub h1: Vec<f64>,
    pub h2: Vec<f64>,
    pub nz: Vec<(usize, f64)>,
}
