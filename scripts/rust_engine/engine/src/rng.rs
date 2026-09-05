//! エンジンが消費する乱数の抽象。R2 では記録済みストリームの再生（種別・件数を厳格照合）、
//! R3 で CPython 互換 MT19937 実装に差し替える。
//!
//! Python 側の消費点（simulator/*）:
//!   random()            -> `random`
//!   random.choice(seq)  -> `choice(len)` … 返り値はインデックス
//!   random.randint(a,b) -> `randint`
//!   random.choices(...) -> `choices` … 値そのもの（連続技のヒット数のみ）
pub trait BRng {
    fn random(&mut self) -> f64;
    fn choice(&mut self, n: usize) -> usize;
    fn randint(&mut self, a: i64, b: i64) -> i64;
    fn choices(&mut self) -> i64;
}

/// calc_damage 用アダプタ（kind 0=random / 1=ダメージロールの choice インデックス）
pub struct DmgRng<'a>(pub &'a mut dyn BRng);

impl<'a> DmgRng<'a> {
    pub fn call(&mut self, kind: u8) -> f64 {
        match kind {
            0 => self.0.random(),
            _ => self.0.choice(16) as f64,
        }
    }
}

#[derive(Clone, Copy, Debug, PartialEq)]
pub enum Draw {
    Random(f64),
    Choice(usize),
    Randint(i64),
    Choices(i64),
}

/// 記録済みストリームの再生。種別・件数が食い違えば即 panic（消費漏れ/過剰の検出）。
pub struct ReplayRng {
    pub log: Vec<Draw>,
    pub pos: usize,
    pub ctx: String,
}

impl ReplayRng {
    pub fn new(log: Vec<Draw>) -> Self {
        ReplayRng { log, pos: 0, ctx: String::new() }
    }
    pub fn exhausted(&self) -> bool {
        self.pos == self.log.len()
    }
    fn next(&mut self) -> Draw {
        if self.pos >= self.log.len() {
            panic!("RNG過剰消費: pos={} len={} ctx={}", self.pos, self.log.len(), self.ctx);
        }
        let d = self.log[self.pos];
        self.pos += 1;
        d
    }
}

impl BRng for ReplayRng {
    fn random(&mut self) -> f64 {
        match self.next() {
            Draw::Random(v) => v,
            o => panic!("RNG種別不一致: expected random, got {:?} @{}", o, self.pos - 1),
        }
    }
    fn choice(&mut self, n: usize) -> usize {
        match self.next() {
            Draw::Choice(i) => {
                if i >= n {
                    panic!("choice インデックス範囲外: {} >= {} @{}", i, n, self.pos - 1);
                }
                i
            }
            o => panic!("RNG種別不一致: expected choice, got {:?} @{}", o, self.pos - 1),
        }
    }
    fn randint(&mut self, _a: i64, _b: i64) -> i64 {
        match self.next() {
            Draw::Randint(v) => v,
            o => panic!("RNG種別不一致: expected randint, got {:?} @{}", o, self.pos - 1),
        }
    }
    fn choices(&mut self) -> i64 {
        match self.next() {
            Draw::Choices(v) => v,
            o => panic!("RNG種別不一致: expected choices, got {:?} @{}", o, self.pos - 1),
        }
    }
}
