//! R3-T1 ゲート: CPython MT19937 レプリカのビット一致検証。
//! 使い方: gate_r3_rng cases/rng_00.jsonl [...]
use engine::cpyrng::CpyRandom;
use serde_json::Value;
use std::io::{BufRead, BufReader};

fn fbits(x: f64) -> String {
    let b = x.to_bits().to_le_bytes();
    b.iter().map(|v| format!("{:02x}", v)).collect()
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut draws: u64 = 0;
    let mut checks: u64 = 0;
    let mut bad: u64 = 0;
    let mut seeds = 0u64;
    let mut first: Option<String> = None;
    for path in &args[1..] {
        let f = BufReader::new(std::fs::File::open(path).expect("rng cases"));
        for (ln, line) in f.lines().enumerate() {
            let line = line.unwrap();
            if ln == 0 {
                continue;
            }
            let v: Value = serde_json::from_str(&line).unwrap();
            let seed_s = v["seed"].as_str().unwrap();
            let mut r = CpyRandom::new(0);
            match seed_s.parse::<i128>() {
                Ok(n) => r.seed(n),
                Err(_) => {
                    // i128 に収まらない巨大シード: CPython と同じワード列で初期化
                    let key: Vec<u32> =
                        v["key"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap() as u32).collect();
                    r.seed_words(&key);
                }
            }
            seeds += 1;
            let ops = v["ops"].as_array().unwrap();
            let out = v["out"].as_array().unwrap();
            for (i, op) in ops.iter().enumerate() {
                let o = op.as_array().unwrap();
                let exp = out[i].as_str().unwrap();
                let got: String = match o[0].as_str().unwrap() {
                    "r" => {
                        draws += 1;
                        fbits(r.random())
                    }
                    "g" => {
                        let k = o[1].as_u64().unwrap() as u32;
                        draws += ((k + 31) / 32) as u64;
                        format!("{}", r.getrandbits(k))
                    }
                    "b" => {
                        draws += 1;
                        format!("{}", r.randbelow(o[1].as_u64().unwrap()))
                    }
                    "i" => {
                        draws += 1;
                        format!("{}", r.randint(o[1].as_i64().unwrap(), o[2].as_i64().unwrap()))
                    }
                    "R" => {
                        draws += 1;
                        format!("{}", r.randrange(o[1].as_i64().unwrap(), o[2].as_i64().unwrap()))
                    }
                    "c" => {
                        draws += 1;
                        format!("{}", r.choice(o[1].as_u64().unwrap() as usize))
                    }
                    "w" => {
                        draws += 1;
                        let w: Vec<f64> =
                            o[1].as_array().unwrap().iter().map(|x| x.as_f64().unwrap()).collect();
                        format!("{}", r.choices_one(&w))
                    }
                    "s" => {
                        let n = o[1].as_u64().unwrap() as usize;
                        draws += (n - 1) as u64;
                        let mut x: Vec<usize> = (0..n).collect();
                        r.shuffle(&mut x);
                        x.iter().map(|v| v.to_string()).collect::<Vec<_>>().join(",")
                    }
                    "p" => {
                        let n = o[1].as_u64().unwrap() as usize;
                        let k = o[2].as_u64().unwrap() as usize;
                        draws += k as u64;
                        r.sample(n, k)
                            .iter()
                            .map(|v| v.to_string())
                            .collect::<Vec<_>>()
                            .join(",")
                    }
                    x => panic!("unknown op {}", x),
                };
                checks += 1;
                if got != exp {
                    bad += 1;
                    if first.is_none() {
                        first = Some(format!(
                            "seed={} op#{}={} rust={} py={}",
                            seed_s, i, op, got, exp
                        ));
                    }
                }
            }
        }
    }
    println!("─────────────────────────────────────────");
    println!("R3-T1 RNG GATE: seeds={} ops={} draws>={} mismatches={}", seeds, checks, draws, bad);
    if let Some(f) = first {
        println!("最初の乖離: {}", f);
        std::process::exit(1);
    }
}
