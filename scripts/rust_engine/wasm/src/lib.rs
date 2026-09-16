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

/// 以降の判定を「この状況なら」に切り替える。すべて0で既定（特性由来の天候のまま・積みなし）。
/// weather: 0=指定なし 1=晴れ 2=雨 3=すなあらし 4=あられ
/// terrain: 0=指定なし 1=エレキ 2=グラス 3=サイコ 4=ミスト
/// boost:   側0(spec_a)が技欄の先頭にある積み技を使った回数
#[no_mangle]
pub extern "C" fn set_scenario(weather: i32, terrain: i32, boost: i32) -> i32 {
    let pack = match unsafe { PACK.as_mut() } { Some(p) => p, None => return -1 };
    pack.scenario = engine::pack::Scenario {
        weather: weather.clamp(0, 4) as u8,
        terrain: terrain.clamp(0, 4) as u8,
        boost: boost.clamp(0, 6),
    };
    0
}

/// 積み技（自分の能力を上げる変化技）の名前一覧。
/// 「積み回数」の指定を出すかどうかを表示側が決めるために使う。
/// 判定に使う表と同じものを返すので、表示と計算がずれない。
#[no_mangle]
pub extern "C" fn setup_move_names() -> i32 {
    let pack = match unsafe { PACK.as_ref() } { Some(p) => p, None => return -1 };
    let names: Vec<String> = pack.moves.iter()
        .filter(|m| engine::battle::self_boosts(pack, m.name)
            .is_some_and(|v| v.iter().any(|(_, d)| *d > 0)))
        .map(|m| m.name_jp.clone())
        .collect();
    set_result(&json!(names));
    0
}

/// 型だけでは無効(0倍)を判定できない技と特性。
///
/// 表示側は「相性0倍と分かる技はエンジンに渡さない」事前除外をしている。
/// 状況でタイプが変わる技(だいちのはどう等)や、技のタイプを書き換える・無効を貫く特性を
/// 手で並べると取りこぼす(実際に だいちのはどう・レイジングブル・うるおいボイス が
/// 抜けていた)ので、判定に使う条件そのものを返す。
#[no_mangle]
pub extern "C" fn type_dynamic() -> i32 {
    let pack = match unsafe { PACK.as_ref() } { Some(p) => p, None => return -1 };
    let sy = &pack.sy;
    let moves: Vec<String> = [sy.mv.ウェザーボール, sy.mv.レイジングブル, sy.mv.だいちのはどう]
        .iter().map(|m| pack.intern.resolve(*m).to_string()).collect();
    let mut abilities: Vec<String> = pack.skin.keys()
        .map(|a| pack.intern.resolve(*a).to_string()).collect();
    abilities.push(pack.intern.resolve(sy.ab.うるおいボイス).to_string());
    abilities.push(pack.intern.resolve(sy.ab.きもったま).to_string());
    abilities.sort();
    set_result(&json!({"moves": moves, "abilities": abilities}));
    0
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
    // 組み立ても判定も engine 側（analysis::analyze_json）にある。
    // ここに持つと提案API(PyO3)経路と食い違うため、受け渡しだけを行う。
    set_result(&analysis::analyze_json(pack, a, b, season));
    0
}

/// `hits` 発以内に倒せる確率(0〜1)。内訳ポップアップの「乱数n発(p%)」に使う。
#[no_mangle]
pub extern "C" fn ko_prob(ap: *const u8, an: usize, bp: *const u8, bn: usize,
                          sp: *const u8, sn: usize, att: usize, move_idx: usize, hits: usize) -> i32 {
    let (a, b, season) = unsafe { (s(ap, an), s(bp, bn), s(sp, sn)) };
    ko_prob_impl(a, b, season, att, move_idx, hits)
}

pub fn ko_prob_impl(a: &str, b: &str, season: &str, att: usize, move_idx: usize, hits: usize) -> i32 {
    let pack = match unsafe { PACK.as_mut() } { Some(p) => p, None => return -1 };
    let p = analysis::ko_probability(pack, a, b, season, att, move_idx, hits);
    set_result(&json!(p));
    0
}
