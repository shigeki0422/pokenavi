//! CPython 3.12 の `sum()` は float 入力に対して Neumaier 補償総和を使う
//! （Python/bltinmodule.c builtin_sum_impl）。1-ulp の差が探索の分岐を変えうるため、
//! Python の `sum(floats)` を写す箇所は必ずこれを使う。
#[derive(Clone, Copy, Default)]
pub struct Neumaier {
    pub f: f64,
    pub c: f64,
}

impl Neumaier {
    #[inline]
    pub fn new() -> Neumaier {
        Neumaier { f: 0.0, c: 0.0 }
    }
    #[inline]
    pub fn add(&mut self, x: f64) {
        let t = self.f + x;
        if self.f.abs() >= x.abs() {
            self.c += (self.f - t) + x;
        } else {
            self.c += (x - t) + self.f;
        }
        self.f = t;
    }
    #[inline]
    pub fn value(&self) -> f64 {
        self.f + self.c
    }
}

/// `sum(iterable_of_float)` 相当
#[inline]
pub fn pysum<I: IntoIterator<Item = f64>>(it: I) -> f64 {
    let mut n = Neumaier::new();
    for x in it {
        n.add(x);
    }
    n.value()
}

#[inline]
pub fn pysum_slice(v: &[f64]) -> f64 {
    pysum(v.iter().copied())
}
