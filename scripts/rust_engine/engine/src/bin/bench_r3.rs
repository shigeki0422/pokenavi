//! R3 速度実測（Rust 側）: bench_r3.py が書いた同一ジョブで greedy_3v3 を単一スレッド計測。
use engine::sim::greedy_3v3;
use serde_json::Value;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut pack = engine::pack::Pack::load(&args[1]);
    let v: Value = serde_json::from_str(&std::fs::read_to_string(&args[2]).unwrap()).unwrap();
    let season = v["season"].as_str().unwrap().to_string();
    let jobs = v["jobs"].as_array().unwrap();
    let exp: Vec<i64> = v["results"].as_array().unwrap().iter().map(|x| x.as_i64().unwrap()).collect();

    let parsed: Vec<(Vec<String>, Vec<usize>, Vec<String>, Vec<usize>, i128)> = jobs
        .iter()
        .map(|j| {
            let g = |k: &str| -> Vec<String> {
                j[k].as_array().unwrap().iter().map(|s| s.as_str().unwrap().to_string()).collect()
            };
            let gi = |k: &str| -> Vec<usize> {
                j[k].as_array().unwrap().iter().map(|s| s.as_u64().unwrap() as usize).collect()
            };
            (g("pa"), gi("sa"), g("pb"), gi("sb"), j["seed"].as_i64().unwrap() as i128)
        })
        .collect();

    // ウォームアップ（テンプレート解決のキャッシュ有無を Python と揃えるための空回し）
    for j in parsed.iter().take(20) {
        greedy_3v3(&mut pack, &j.0, &j.1, &j.2, &j.3, &season, j.4);
    }

    let t = std::time::Instant::now();
    let mut out = Vec::with_capacity(parsed.len());
    for j in &parsed {
        out.push(greedy_3v3(&mut pack, &j.0, &j.1, &j.2, &j.3, &season, j.4));
    }
    let secs = t.elapsed().as_secs_f64();
    let n = parsed.len();
    let mismatch = out.iter().zip(exp.iter()).filter(|(a, b)| a != b).count();
    println!("n={} rust greedy_3v3: {:.4} ms/battle (合計 {:.2}s)", n, secs / n as f64 * 1000.0, secs);
    println!("Python 結果との不一致: {}", mismatch);
    println!("python_ms(belief込)={:.3} python_ms(belief無効)={:.3}",
             v["python_ms_per_battle"].as_f64().unwrap_or(0.0),
             v["python_nobelief_ms_per_battle"].as_f64().unwrap_or(0.0));
    println!("speedup vs 実 _greedy_3v3: {:.1}x / vs belief無効版: {:.1}x",
             v["python_ms_per_battle"].as_f64().unwrap_or(0.0) / (secs / n as f64 * 1000.0),
             v["python_nobelief_ms_per_battle"].as_f64().unwrap_or(0.0) / (secs / n as f64 * 1000.0));
    if mismatch > 0 {
        std::process::exit(1);
    }
}
