//! 表示用のダメージ（analysis::move_damage）が、対戦本体が実際に与えるダメージと
//! 一致するかを機械的に確かめる。
//!
//! move_damage は calc_damage を自前のループで呼ぶため、対戦本体が技を撃つ前に
//! 走らせる処理を取りこぼしうる。実際に multi_hit_index（トリプルアクセルの威力）・
//! 必中急所・へんげんじざいのタイプ変更を順に取りこぼした。いずれも
//! 「確定数は正しいのに表示%だけ違う」形で現れ、Python との照合では
//! （両方が同じ考え違いで書かれていたため）検出できなかった。
//!
//! 対戦本体は「相手が倒れるとヒットループを止める」「きあいのタスキ・がんじょうで
//! ダメージをHP-1に切り詰める」ので、そのままでは表示用の威力と一致しない。
//! 比較するのは「防御側が生き残り、かつ残HPが1でない（切り詰めが起きていない）1発」だけ。
//! そこが食い違えば前処理の取りこぼしを意味する。
//!
//!   cargo run --release -p engine_wasm --bin audit_damage -- <specs.json> [engine.pack.json]
use engine::analysis;
use engine::pack::Pack;

fn main() {
    let sp = std::env::args().nth(1).expect("specs.json のパスを指定する");
    let pack_path = std::env::args().nth(2)
        .unwrap_or_else(|| "public/builder-data/engine.pack.json".to_string());
    let txt = std::fs::read_to_string(&pack_path).unwrap_or_else(|e| panic!("{pack_path}: {e}"));
    let v: serde_json::Value = serde_json::from_str(&txt).unwrap();
    let mut pack = Pack::from_value(&v);
    let specs: Vec<String> =
        serde_json::from_str(&std::fs::read_to_string(&sp).unwrap()).unwrap();

    let (mut checked, mut bad) = (0usize, 0usize);
    for (i, a) in specs.iter().enumerate() {
        let b = &specs[(i * 7 + 3) % specs.len()];
        if a == b { continue; }
        let nmv = a.split(':').nth(2).map(|m| m.split('|').count()).unwrap_or(0);
        for mi in 0..nmv {
            let r = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
                let (exec, alive, hp) = analysis::executed_damage(&mut pack, a, b, "M-3", 0, mi, 0.0);
                let disp = analysis::move_damage(&mut pack, a, b, "M-3", 0, mi, 0.0);
                (exec, alive, hp, disp)
            }));
            let Ok((exec, alive, hp, disp)) = r else { continue };
            // 倒れた／HP-1に切り詰められた回は、対戦本体の値が威力と一致しない
            if !alive || exec == 0 || hp <= 1 { continue; }
            checked += 1;
            if disp != exec {
                bad += 1;
                if bad <= 5 {
                    let mv = a.split(':').nth(2).unwrap().split('|').nth(mi).unwrap();
                    println!("  不一致 {mv}: 表示={disp} 実走={exec}\n     攻={a}\n     防={b}");
                }
            }
        }
    }
    println!("\n=== 表示ダメージ vs 対戦本体の実走 ===");
    println!("  一致 {}/{} ({:.1}%)", checked - bad, checked,
             100.0 * (checked - bad) as f64 / checked.max(1) as f64);
    if bad > 0 { std::process::exit(1); }
}
