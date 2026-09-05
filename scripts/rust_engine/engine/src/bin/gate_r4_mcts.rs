//! R4-G3 ゲート: MCTS フル対戦パリティ（Rust だけで駆動）。
//! Python 側 `_rust_engine/dump_mcts_battles.py`（逐次ネット・sorted belief・HASHSEED=0）と
//! (勝敗・ターン数・毎ターンの正準状態ハッシュ) を厳密比較する。
//! 使い方: gate_r4_mcts <datapack.json> <cases/mc_XX.jsonl> [...]
use engine::sim::mcts_3v3;
use engine::statec::{encode_battle, sv_hash};
use serde_json::Value;
use std::io::{BufRead, BufReader};

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut pack = engine::pack::Pack::load(&args[1]);
    let net = pack.net.clone().expect("datapack に net が無い");
    let bench = std::env::var("R4_BENCH").is_ok();

    let (mut battles, mut turns) = (0i64, 0i64);
    let (mut dr, mut dt, mut dsx) = (0i64, 0i64, 0i64);
    let mut first: Option<String> = None;
    let t0 = std::time::Instant::now();
    let mut eng = 0u128;

    for path in &args[2..] {
        let f = BufReader::new(std::fs::File::open(path).expect("mc cases"));
        let mut parties: Vec<Vec<String>> = Vec::new();
        let mut seasons: Vec<String> = Vec::new();
        for (ln, line) in f.lines().enumerate() {
            let line = line.unwrap();
            let v: Value = serde_json::from_str(&line).expect("json");
            if ln == 0 {
                parties = v["parties"].as_array().unwrap().iter()
                    .map(|p| p.as_array().unwrap().iter().map(|s| s.as_str().unwrap().to_string()).collect())
                    .collect();
                seasons = v["seasons"].as_array().unwrap().iter().map(|s| s.as_str().unwrap().into()).collect();
                continue;
            }
            let bid = v["b"].as_i64().unwrap();
            let ia = v["ia"].as_u64().unwrap() as usize;
            let ib = v["ib"].as_u64().unwrap() as usize;
            let sa: Vec<usize> = v["sa"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap() as usize).collect();
            let sb: Vec<usize> = v["sb"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap() as usize).collect();
            let seed = v["seed"].as_i64().unwrap() as i128;
            let sims = v["sims"].as_u64().unwrap() as usize;
            let exp_h: Vec<u64> = v["H"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap()).collect();
            let exp_res = v["result"].as_i64().unwrap();
            let exp_nturn = v["nturn"].as_i64().unwrap();

            let mut got: Vec<u64> = Vec::with_capacity(exp_h.len());
            let te = std::time::Instant::now();
            let (res, nturn) = mcts_3v3(&mut pack, &net, &parties[ia], &sa, &parties[ib], &sb,
                                        &seasons[ia], &seasons[ib], seed, sims, |pk, bt| {
                if !bench {
                    let e = encode_battle(pk, bt, false);
                    got.push(sv_hash(&e.vals));
                }
            });
            eng += te.elapsed().as_nanos();
            battles += 1;
            turns += got.len().max(exp_h.len()) as i64;
            if bench { continue; }
            let mut bad: Option<String> = None;
            if res != exp_res {
                dr += 1;
                bad = Some(format!("勝敗 rust={} py={}", res, exp_res));
            } else if nturn != exp_nturn || got.len() != exp_h.len() {
                dt += 1;
                bad = Some(format!("ターン数 rust={}({}) py={}({})", nturn, got.len(), exp_nturn, exp_h.len()));
            } else {
                for (i, (a, b)) in got.iter().zip(exp_h.iter()).enumerate() {
                    if a != b {
                        dsx += 1;
                        bad = Some(format!("状態ハッシュ turn={} rust={:x} py={:x}", i + 1, a, b));
                        break;
                    }
                }
            }
            if let Some(m) = bad {
                if first.is_none() {
                    first = Some(format!("{} battle={} seed={} sims={} : {}", path, bid, seed, sims, m));
                }
            }
        }
        println!("[gate_r4_mcts] {} 済: battles={} turns={} div(result/turns/state)={}/{}/{}",
                 path, battles, turns, dr, dt, dsx);
    }
    let secs = t0.elapsed().as_secs_f64();
    println!("─────────────────────────────────────────");
    println!("R4 G3 GATE: battles={} turns={} divergences={} (result={} turns={} state={})",
             battles, turns, dr + dt + dsx, dr, dt, dsx);
    println!("rust: {:.2}s total / {:.2} ms per battle",
             secs, (eng as f64) / 1e6 / (battles.max(1) as f64));
    if let Some(f) = first {
        println!("── 最初の乖離 ──\n{}", f);
        std::process::exit(1);
    }
}
