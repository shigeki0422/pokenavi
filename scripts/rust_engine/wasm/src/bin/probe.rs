//! spec の総当たりで panic を探す診断用。wasm は panic=abort で理由が出ないため、
//! 同じコードを native で走らせてメッセージを読む（種名のコロン衝突をこれで特定した）。
//!
//!   cargo run --release -p engine_wasm --bin probe -- <specs.json> [engine.pack.json]
fn main() {
    let s = std::env::args().nth(1).expect("specs.json のパスを指定する");
    let pack_path = std::env::args().nth(2)
        .unwrap_or_else(|| "public/builder-data/engine.pack.json".to_string());
    let pack = std::fs::read_to_string(&pack_path)
        .unwrap_or_else(|e| panic!("{pack_path} が読めない: {e}"));
    engine_wasm::load_impl(&pack);
    let specs: Vec<String> = serde_json::from_str(&std::fs::read_to_string(s).unwrap()).unwrap();
    for (i, a) in specs.iter().enumerate() {
        for b in specs.iter() {
            let r = std::panic::catch_unwind(|| {
                engine_wasm::analyze_impl(a, b, "M-3");
                let n = a.split(':').nth(2).map(|m| m.split('|').count()).unwrap_or(0);
                for mi in 0..n {
                    engine_wasm::ko_prob_impl(a, b, "M-3", 0, mi, 5);
                }
            });
            if r.is_err() {
                println!("PANIC at [{i}]\n  A={a}\n  B={b}");
                return;
            }
        }
    }
    println!("全 {}x{} 組で panic なし", specs.len(), specs.len());
}
