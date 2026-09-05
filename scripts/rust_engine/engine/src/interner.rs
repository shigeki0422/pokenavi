use std::collections::HashMap;

/// 文字列インターン。全語彙（技/特性/道具/タイプ/性格/種）をu16へ。
pub type Sym = u16;
pub const NO_SYM: Sym = u16::MAX;

#[derive(Default)]
pub struct Interner {
    map: HashMap<String, Sym>,
    vec: Vec<String>,
}

impl Interner {
    pub fn new() -> Self {
        Interner { map: HashMap::new(), vec: Vec::new() }
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
