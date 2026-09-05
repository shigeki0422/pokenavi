//! CPython の `random` モジュール（Mersenne Twister 19937）の厳密レプリカ。
//! 正本: CPython 3.12 `Modules/_randommodule.c` + `Lib/random.py`
//!
//! 再現対象:
//!   random.seed(int)                 -> random_seed(): abs(n) を 32bit ワード列(LE)にして init_by_array
//!   random.random()                  -> genrand_res53
//!   random.getrandbits(k)
//!   Random._randbelow_with_getrandbits(n)  (棄却サンプリング)
//!   randrange / randint / choice / choices(weights=) / shuffle / sample
//!
//! グローバル `random` もインスタンス `random.Random(seed)` も同一アルゴリズム。
//! 本構造体を用途ごとに別インスタンスとして持てば独立ストリームになる。

const N: usize = 624;
const M: usize = 397;
const MATRIX_A: u32 = 0x9908b0df;
const UPPER_MASK: u32 = 0x80000000;
const LOWER_MASK: u32 = 0x7fffffff;

#[derive(Clone)]
pub struct CpyRandom {
    mt: [u32; N],
    idx: usize,
}

impl Default for CpyRandom {
    fn default() -> Self {
        CpyRandom::new(0)
    }
}

impl CpyRandom {
    pub fn new(seed: i128) -> Self {
        let mut r = CpyRandom { mt: [0u32; N], idx: N + 1 };
        r.seed(seed);
        r
    }

    /// init_genrand
    fn init_genrand(&mut self, s: u32) {
        self.mt[0] = s;
        for i in 1..N {
            self.mt[i] = 1812433253u32
                .wrapping_mul(self.mt[i - 1] ^ (self.mt[i - 1] >> 30))
                .wrapping_add(i as u32);
        }
        self.idx = N;
    }

    /// init_by_array
    fn init_by_array(&mut self, key: &[u32]) {
        self.init_genrand(19650218);
        let mut i: usize = 1;
        let mut j: usize = 0;
        let mut k: usize = std::cmp::max(N, key.len());
        while k > 0 {
            let prev = self.mt[i - 1];
            self.mt[i] = (self.mt[i] ^ (prev ^ (prev >> 30)).wrapping_mul(1664525))
                .wrapping_add(key[j])
                .wrapping_add(j as u32);
            i += 1;
            j += 1;
            if i >= N {
                self.mt[0] = self.mt[N - 1];
                i = 1;
            }
            if j >= key.len() {
                j = 0;
            }
            k -= 1;
        }
        let mut k: usize = N - 1;
        while k > 0 {
            let prev = self.mt[i - 1];
            self.mt[i] = (self.mt[i] ^ (prev ^ (prev >> 30)).wrapping_mul(1566083941))
                .wrapping_sub(i as u32);
            i += 1;
            if i >= N {
                self.mt[0] = self.mt[N - 1];
                i = 1;
            }
            k -= 1;
        }
        self.mt[0] = 0x80000000;
        self.idx = N;
    }

    /// `random.seed(n)` (n は int)。CPython は abs(n) を 32bit ワード列（リトルエンディアン）
    /// に分解し init_by_array に渡す。ワード数は `bits==0 ? 1 : (bits-1)/32+1`。
    pub fn seed(&mut self, n: i128) {
        let a: u128 = n.unsigned_abs();
        let bits = 128 - a.leading_zeros() as usize;
        let keyused = if bits == 0 { 1 } else { (bits - 1) / 32 + 1 };
        let mut key = Vec::with_capacity(keyused);
        for i in 0..keyused {
            key.push(((a >> (32 * i)) & 0xffff_ffff) as u32);
        }
        self.init_by_array(&key);
    }

    /// 任意精度シード（32bit ワード列 LE を直接指定）。128bit を超えるシードの検証用。
    pub fn seed_words(&mut self, words: &[u32]) {
        let mut w = words.to_vec();
        while w.len() > 1 && *w.last().unwrap() == 0 {
            w.pop();
        }
        self.init_by_array(&w);
    }

    #[inline]
    pub fn genrand_uint32(&mut self) -> u32 {
        if self.idx >= N {
            for kk in 0..(N - M) {
                let y = (self.mt[kk] & UPPER_MASK) | (self.mt[kk + 1] & LOWER_MASK);
                self.mt[kk] = self.mt[kk + M] ^ (y >> 1) ^ if y & 1 != 0 { MATRIX_A } else { 0 };
            }
            for kk in (N - M)..(N - 1) {
                let y = (self.mt[kk] & UPPER_MASK) | (self.mt[kk + 1] & LOWER_MASK);
                self.mt[kk] =
                    self.mt[kk + M - N] ^ (y >> 1) ^ if y & 1 != 0 { MATRIX_A } else { 0 };
            }
            let y = (self.mt[N - 1] & UPPER_MASK) | (self.mt[0] & LOWER_MASK);
            self.mt[N - 1] = self.mt[M - 1] ^ (y >> 1) ^ if y & 1 != 0 { MATRIX_A } else { 0 };
            self.idx = 0;
        }
        let mut y = self.mt[self.idx];
        self.idx += 1;
        y ^= y >> 11;
        y ^= (y << 7) & 0x9d2c5680;
        y ^= (y << 15) & 0xefc60000;
        y ^= y >> 18;
        y
    }

    /// genrand_res53: (a*67108864.0+b)*(1.0/9007199254740992.0)
    #[inline]
    pub fn random(&mut self) -> f64 {
        let a = (self.genrand_uint32() >> 5) as f64;
        let b = (self.genrand_uint32() >> 6) as f64;
        (a * 67108864.0 + b) * (1.0 / 9007199254740992.0)
    }

    /// getrandbits(k)（k <= 64）
    #[inline]
    pub fn getrandbits(&mut self, k: u32) -> u64 {
        if k == 0 {
            return 0;
        }
        if k <= 32 {
            return (self.genrand_uint32() >> (32 - k)) as u64;
        }
        // words = (k-1)/32+1、下位ワードから埋め、最上位ワードだけシフトで落とす
        let words = ((k - 1) / 32 + 1) as usize;
        let mut out: u64 = 0;
        let mut kk = k;
        for i in 0..words {
            let mut r = self.genrand_uint32();
            if kk < 32 {
                r >>= 32 - kk;
            }
            out |= (r as u64) << (32 * i);
            kk = kk.saturating_sub(32);
        }
        out
    }

    /// Random._randbelow_with_getrandbits: 0 <= r < n
    #[inline]
    pub fn randbelow(&mut self, n: u64) -> u64 {
        if n == 0 {
            return 0;
        }
        let k = 64 - n.leading_zeros(); // n.bit_length()
        loop {
            let r = self.getrandbits(k);
            if r < n {
                return r;
            }
        }
    }

    /// randrange(a, b) step=1
    #[inline]
    pub fn randrange(&mut self, a: i64, b: i64) -> i64 {
        a + self.randbelow((b - a) as u64) as i64
    }

    /// randint(a, b)
    #[inline]
    pub fn randint(&mut self, a: i64, b: i64) -> i64 {
        self.randrange(a, b + 1)
    }

    /// choice(seq) の選択インデックス
    #[inline]
    pub fn choice(&mut self, len: usize) -> usize {
        self.randbelow(len as u64) as usize
    }

    /// choices(population, weights=w, k=1) の選択インデックス。
    /// cum = itertools.accumulate(w)（前から順に加算）、total = cum[-1]+0.0、
    /// bisect_right(cum, random()*total, 0, len-1)
    pub fn choices_one(&mut self, weights: &[f64]) -> usize {
        let n = weights.len();
        let mut cum = Vec::with_capacity(n);
        let mut acc = 0.0f64;
        for (i, w) in weights.iter().enumerate() {
            acc = if i == 0 { *w } else { acc + *w };
            cum.push(acc);
        }
        let total = cum[n - 1];
        let x = self.random() * total;
        bisect_right(&cum, x, 0, n - 1)
    }

    /// shuffle(x)（Fisher-Yates 下向き）。呼び出し側の配列をそのまま並べ替える。
    pub fn shuffle<T>(&mut self, x: &mut [T]) {
        for i in (1..x.len()).rev() {
            let j = self.randbelow((i + 1) as u64) as usize;
            x.swap(i, j);
        }
    }

    /// sample(range(n), k) 相当。返り値は選ばれたインデックス列（選択順）。
    pub fn sample(&mut self, n: usize, k: usize) -> Vec<usize> {
        let mut result = vec![0usize; k];
        let mut setsize = 21usize;
        if k > 5 {
            setsize += 4usize.pow(((k as f64 * 3.0).ln() / 4f64.ln()).ceil() as u32);
        }
        if n <= setsize {
            let mut pool: Vec<usize> = (0..n).collect();
            for i in 0..k {
                let j = self.randbelow((n - i) as u64) as usize;
                result[i] = pool[j];
                pool[j] = pool[n - i - 1];
            }
        } else {
            let mut selected = std::collections::HashSet::new();
            for i in 0..k {
                let mut j = self.randbelow(n as u64) as usize;
                while selected.contains(&j) {
                    j = self.randbelow(n as u64) as usize;
                }
                selected.insert(j);
                result[i] = j;
            }
        }
        result
    }
}

/// bisect.bisect_right(a, x, lo, hi)
pub fn bisect_right(a: &[f64], x: f64, lo: usize, hi: usize) -> usize {
    let (mut lo, mut hi) = (lo, hi);
    while lo < hi {
        let mid = (lo + hi) / 2;
        if x < a[mid] {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    lo
}

/// エンジンが使うグローバル `random` 相当のアダプタ（rng::BRng 実装）
impl crate::rng::BRng for CpyRandom {
    fn random(&mut self) -> f64 {
        CpyRandom::random(self)
    }
    fn choice(&mut self, n: usize) -> usize {
        CpyRandom::choice(self, n)
    }
    fn randint(&mut self, a: i64, b: i64) -> i64 {
        CpyRandom::randint(self, a, b)
    }
    /// battle.py:2519 `random.choices([2,3,4,5], weights=[3,3,1,1])[0]`
    fn choices(&mut self) -> i64 {
        let i = self.choices_one(&[3.0, 3.0, 1.0, 1.0]);
        [2i64, 3, 4, 5][i]
    }
}
