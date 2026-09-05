//! R3-T2/T3 ゲート: フル対戦パリティ（AI＋CPython互換RNG をRustだけで駆動）。
//! Python の (勝敗・ターン数・毎ターンの正準状態ハッシュ) と厳密比較する。
//! 使い方: gate_r3 <datapack.json> <cases/fb_XX.jsonl> [...]
use engine::ai::Ai;
use engine::sim::full_battle;
use engine::statec::{encode_battle, sv_hash};
use serde_json::Value;
use std::io::{BufRead, BufReader};

fn ai_of(c: u8) -> Ai {
    if c == b'g' {
        Ai::Greedy
    } else {
        Ai::heuristic()
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut pack = engine::pack::Pack::load(&args[1]);
    let bench = std::env::var("R3_BENCH").is_ok();
    let only: Option<i64> = std::env::var("R3_ONLY").ok().and_then(|x| x.parse().ok());

    let mut battles = 0i64;
    let mut turns = 0i64;
    let mut div_result = 0i64;
    let mut div_turns = 0i64;
    let mut div_state = 0i64;
    let mut first: Option<String> = None;
    let t0 = std::time::Instant::now();
    let mut engine_nanos = 0u128;

    for path in &args[2..] {
        let f = BufReader::new(std::fs::File::open(path).expect("fb cases"));
        let mut parties: Vec<Vec<String>> = Vec::new();
        let mut seasons: Vec<String> = Vec::new();
        for (ln, line) in f.lines().enumerate() {
            let line = line.unwrap();
            let v: Value = serde_json::from_str(&line).expect("json");
            if ln == 0 {
                parties = v["parties"]
                    .as_array()
                    .unwrap()
                    .iter()
                    .map(|p| {
                        p.as_array().unwrap().iter().map(|s| s.as_str().unwrap().to_string()).collect()
                    })
                    .collect();
                seasons =
                    v["seasons"].as_array().unwrap().iter().map(|s| s.as_str().unwrap().into()).collect();
                continue;
            }
            let bid = v["b"].as_i64().unwrap();
            if let Some(o) = only {
                if bid != o {
                    continue;
                }
            }
            let ia = v["ia"].as_u64().unwrap() as usize;
            let ib = v["ib"].as_u64().unwrap() as usize;
            let sa: Vec<usize> =
                v["sa"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap() as usize).collect();
            let sb: Vec<usize> =
                v["sb"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap() as usize).collect();
            let seed = v["seed"].as_i64().unwrap() as i128;
            let aim = v["ai"].as_str().unwrap().as_bytes();
            let specs_a: Vec<String> = match v.get("specsA") {
                Some(x) if !x.is_null() => {
                    x.as_array().unwrap().iter().map(|s| s.as_str().unwrap().to_string()).collect()
                }
                _ => parties[ia].clone(),
            };
            let specs_b: Vec<String> = match v.get("specsB") {
                Some(x) if !x.is_null() => {
                    x.as_array().unwrap().iter().map(|s| s.as_str().unwrap().to_string()).collect()
                }
                _ => parties[ib].clone(),
            };
            let exp_h: Vec<u64> =
                v["H"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap()).collect();
            let exp_res = v["result"].as_i64().unwrap();
            let exp_nturn = v["nturn"].as_i64().unwrap();

            let mut got_h: Vec<u64> = Vec::with_capacity(exp_h.len());
            let te = std::time::Instant::now();
            let out = {
                let packref = &mut pack;
                full_battle(
                    packref,
                    &specs_a,
                    &sa,
                    &specs_b,
                    &sb,
                    &seasons[ia],
                    &seasons[ib],
                    seed,
                    (ai_of(aim[0]), true),
                    (ai_of(aim[1]), true),
                    true,
                    None,
                    |pk, bt| {
                        if !bench {
                            let e = encode_battle(pk, bt, false);
                            got_h.push(sv_hash(&e.vals));
                        }
                    },
                )
            };
            engine_nanos += te.elapsed().as_nanos();
            battles += 1;
            turns += got_h.len().max(exp_h.len()) as i64;
            if bench {
                continue;
            }
            let mut bad: Option<String> = None;
            if out.result != exp_res {
                div_result += 1;
                bad = Some(format!("勝敗 rust={} py={}", out.result, exp_res));
            } else if out.turns != exp_nturn || got_h.len() != exp_h.len() {
                div_turns += 1;
                bad = Some(format!(
                    "ターン数 rust={}({}) py={}({})",
                    out.turns,
                    got_h.len(),
                    exp_nturn,
                    exp_h.len()
                ));
            } else {
                for (i, (a, b)) in got_h.iter().zip(exp_h.iter()).enumerate() {
                    if a != b {
                        div_state += 1;
                        bad = Some(format!("状態ハッシュ turn={} rust={:x} py={:x}", i + 1, a, b));
                        break;
                    }
                }
            }
            if let Some(m) = bad {
                if first.is_none() {
                    first = Some(format!("{} battle={} seed={} ai={} : {}", path, bid, seed,
                                         std::str::from_utf8(aim).unwrap(), m));
                }
            }
        }
        println!(
            "[gate_r3] {} 済: battles={} turns={} div(result/turns/state)={}/{}/{}",
            path, battles, turns, div_result, div_turns, div_state
        );
    }
    let secs = t0.elapsed().as_secs_f64();
    let esec = (engine_nanos as f64) / 1e9;
    println!("─────────────────────────────────────────");
    println!(
        "R3 GATE: battles={} turns={} divergences={} (result={} turns={} state={})",
        battles,
        turns,
        div_result + div_turns + div_state,
        div_result,
        div_turns,
        div_state
    );
    println!("rust total(JSON込): {:.2}s / battle-only: {:.3}s ({:.2} ms/battle)",
             secs, esec, esec * 1000.0 / (battles.max(1) as f64));
    if let Some(f) = first {
        println!("── 最初の乖離 ──\n{}", f);
        std::process::exit(1);
    }
}
