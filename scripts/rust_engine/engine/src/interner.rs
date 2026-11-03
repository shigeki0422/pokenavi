use std::collections::HashMap;
use std::hash::{BuildHasherDefault, Hasher};

/// 引くだけの表（走査しない）用の速いハッシュ。探索中の名前引きで SipHash が数%を食っていた
#[derive(Default, Clone, Copy)]
pub struct FxHasher(u64);

impl Hasher for FxHasher {
    #[inline]
    fn write(&mut self, bytes: &[u8]) {
        let mut h = self.0;
        let mut c = bytes.chunks_exact(8);
        for w in &mut c {
            h = (h.rotate_left(5) ^ u64::from_le_bytes(w.try_into().unwrap())).wrapping_mul(0x51_7c_c1_b7_27_22_0a_95);
        }
        for &b in c.remainder() {
            h = (h.rotate_left(5) ^ b as u64).wrapping_mul(0x51_7c_c1_b7_27_22_0a_95);
        }
        self.0 = h;
    }
    #[inline]
    fn write_u8(&mut self, i: u8) {
        self.0 = (self.0.rotate_left(5) ^ i as u64).wrapping_mul(0x51_7c_c1_b7_27_22_0a_95);
    }
    #[inline]
    fn finish(&self) -> u64 {
        self.0
    }
}

pub type FxMap<K, V> = HashMap<K, V, BuildHasherDefault<FxHasher>>;

/// 文字列インターン。全語彙（技/特性/道具/タイプ/性格/種）をu16へ。
pub type Sym = u16;
pub const NO_SYM: Sym = u16::MAX;

#[derive(Default)]
pub struct Interner {
    map: FxMap<String, Sym>,
    vec: Vec<String>,
}

impl Interner {
    pub fn new() -> Self {
        Interner { map: FxMap::default(), vec: Vec::new() }
    }
    pub fn intern(&mut self, s: &str) -> Sym {
        if let Some(&id) = self.map.get(s) {
            return id;
        }
        let id = self.vec.len() as Sym;
        assert!(id != NO_SYM, "interner overflow");
        self.vec.push(s.to_string());
        self.map.insert(s.to_string(), id);
        id
    }
    /// 未登録なら None（読み取り専用参照）
    pub fn get(&self, s: &str) -> Option<Sym> {
        self.map.get(s).copied()
    }
    pub fn resolve(&self, id: Sym) -> &str {
        &self.vec[id as usize]
    }
    pub fn len(&self) -> usize {
        self.vec.len()
    }
    pub fn is_empty(&self) -> bool {
        self.vec.is_empty()
    }
}

/// Japanese-identifier シンボル束を生成するマクロ。
#[macro_export]
macro_rules! sym_struct {
    ($S:ident { $($f:ident => $lit:literal),* $(,)? }) => {
        #[allow(non_snake_case, non_camel_case_types, uncommon_codepoints, mixed_script_confusables)]
        pub struct $S { $(pub $f: $crate::interner::Sym),* }
        #[allow(uncommon_codepoints)]
        impl $S {
            pub fn build(i: &mut $crate::interner::Interner) -> Self {
                Self { $($f: i.intern($lit)),* }
            }
        }
    };
}
