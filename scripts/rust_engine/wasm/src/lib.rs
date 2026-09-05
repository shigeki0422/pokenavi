//! ブラウザ/Node から 1v1 判定を呼ぶための薄い FFI。
//!
//! 本体のルールは `engine::analysis`（＝対戦本体の実走）にあり、ここは
//! 文字列と JSON の受け渡しだけを行う。wasm-bindgen を使わないのは、
//! Astro/Cloudflare のビルドに wasm-pack や npm 依存を持ち込まないため。
//! ABI: `alloc` で確保 → 引数を書き込み → 関数を呼ぶ → `result_ptr/result_len` で読む。
use engine::analysis;
use engine::pack::Pack;
use serde_json::{json, Value};

static mut PACK: Option<Pack> = None;
/// spec に書ける種名への対応表（正式名 → 別名）。
/// DB の正式名にはコロンを含むもの（ケンタロス:炎 等）があり、spec の区切りと衝突して
/// パースできない。データパックの form_aliases は「別名 → 正式名」なので、その逆を持つ。
static mut ALIASES: String = String::new();
static mut RESULT: String = String::new();

fn set_result(v: &Value) {
    unsafe {
        RESULT = v.to_string();
    }
}

#[no_mangle]
pub extern "C" fn alloc(n: usize) -> *mut u8 {
    let mut v = Vec::<u8>::with_capacity(n);
    let p = v.as_mut_ptr();
    std::mem::forget(v);
    p
}

#[no_mangle]
pub extern "C" fn result_ptr() -> *const u8 {
    unsafe { RESULT.as_ptr() }
}

#[no_mangle]
pub extern "C" fn result_len() -> usize {
    unsafe { RESULT.len() }
}

unsafe fn s<'a>(p: *const u8, n: usize) -> &'a str {
    std::str::from_utf8_unchecked(std::slice::from_raw_parts(p, n))
}

/// データパック(JSON)を読み込む。成功なら 0。
#[no_mangle]
pub extern "C" fn init(p: *const u8, n: usize) -> i32 {
    let txt = unsafe { s(p, n) };
    load_impl(txt)
}

pub fn load_impl(txt: &str) -> i32 {
    match serde_json::from_str::<Value>(txt) {
        Ok(v) => {
            // form_aliases は「別名 → 正式名」だが、コロンを含むのは種によってどちらの側か
            // まちまち（ケンタロス:炎 は正式名側、フラエッテ:永遠 は別名側）。
            // spec に書けるのはコロンを含まない方なので、その向きだけを登録する。
            let mut rev = serde_json::Map::new();
            if let Some(fa) = v.get("form_aliases").and_then(|x| x.as_object()) {
                for (alias, canon) in fa {
                    if let Some(c) = canon.as_str() {
                        if c.contains(':') && !alias.contains(':') {
                            rev.insert(c.to_string(), Value::String(alias.clone()));
                        }
                    }
                }
            }
            unsafe {
                ALIASES = Value::Object(rev).to_string();
                PACK = Some(Pack::from_value(&v));
            }
            0
        }
        Err(_) => -1,
    }
}

/// 正式名 → spec に書ける別名 の対応表を返す。
#[no_mangle]
pub extern "C" fn name_aliases() -> i32 {
    unsafe {
        RESULT = ALIASES.clone();
    }
    0
}

/// alloc で確保した領域を返す。呼ばないと呼び出しごとに線形メモリが増え続ける
/// （実測: 20万回で 2.9MB → 89MB）。
#[no_mangle]
pub extern "C" fn dealloc(p: *mut u8, n: usize) {
    unsafe { drop(Vec::from_raw_parts(p, 0, n)) }
}

/// 1v1 の両側について、HP・実効素早さ・各技の与ダメと確定数を返す。
#[no_mangle]
pub extern "C" fn analyze(ap: *const u8, an: usize, bp: *const u8, bn: usize,
                          sp: *const u8, sn: usize) -> i32 {
    let (a, b, season) = unsafe { (s(ap, an), s(bp, bn), s(sp, sn)) };
    analyze_impl(a, b, season)
}

pub fn analyze_impl(a: &str, b: &str, season: &str) -> i32 {
    let pack = match unsafe { PACK.as_mut() } { Some(p) => p, None => return -1 };
    let mut out = json!({});
    for (key, x, y) in [("a", a, b), ("b", b, a)] {
        let (me, _opp) = analysis::side_info(pack, x, y, season);
        let mut moves = Vec::new();
        for (i, (name, is_dmg)) in me.moves.iter().enumerate() {
            if !*is_dmg {
                moves.push(json!({"n": name, "dmg": Value::Null}));
                continue;
            }
            let (hits_lo, dmg_lo) = analysis::run_move(pack, x, y, season, i, 0.0);
            let (hits_hi, dmg_hi) = analysis::run_move(pack, x, y, season, i, 1.0);
            moves.push(json!({
                "n": name, "dmgLo": dmg_lo, "dmgHi": dmg_hi,
                "hitsLo": hits_lo, "hitsHi": hits_hi,
            }));
        }
        out[key] = json!({"hp": me.hp, "speed": me.speed, "moves": moves});
    }
    set_result(&out);
    0
}

/// 乱数n発の確率計算に使う、使用 k 回目ごとの与ダメ分布（16段 × uses）。
#[no_mangle]
pub extern "C" fn dists(ap: *const u8, an: usize, bp: *const u8, bn: usize,
                        sp: *const u8, sn: usize, move_idx: usize, uses: usize) -> i32 {
    let (a, b, season) = unsafe { (s(ap, an), s(bp, bn), s(sp, sn)) };
    let pack = match unsafe { PACK.as_mut() } { Some(p) => p, None => return -1 };
    let rows: Vec<Vec<i64>> = (1..=uses)
        .map(|k| analysis::damage_dist(pack, a, b, season, move_idx, k).to_vec())
        .collect();
    set_result(&json!(rows));
    0
}

/// `hits` 発以内に倒せる確率(0〜1)。内訳ポップアップの「乱数n発(p%)」に使う。
#[no_mangle]
pub extern "C" fn ko_prob(ap: *const u8, an: usize, bp: *const u8, bn: usize,
                          sp: *const u8, sn: usize, move_idx: usize, hits: usize) -> i32 {
    let (a, b, season) = unsafe { (s(ap, an), s(bp, bn), s(sp, sn)) };
    ko_prob_impl(a, b, season, move_idx, hits)
}

pub fn ko_prob_impl(a: &str, b: &str, season: &str, move_idx: usize, hits: usize) -> i32 {
    let pack = match unsafe { PACK.as_mut() } { Some(p) => p, None => return -1 };
    let p = analysis::ko_probability(pack, a, b, season, move_idx, hits);
    set_result(&json!(p));
    0
}
