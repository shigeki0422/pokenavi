//! R3 追加ゲート: ai::select_party のパリティ（選出インデックス列＋副作用後の全状態ハッシュ）。
//! 使い方: gate_r3_sel <datapack.json> <cases/sel_00.jsonl>
use engine::ai::select_party;
use engine::cpyrng::CpyRandom;
use engine::poke::build_poke;
use engine::statec::{poke_fields, sv_hash, Enc};
use serde_json::Value;
use std::io::{BufRead, BufReader};

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut pack = engine::pack::Pack::load(&args[1]);
    let mut cases = 0i64;
    let mut bad_idx = 0i64;
    let mut bad_state = 0i64;
    let mut first: Option<String> = None;

    for path in &args[2..] {
        let f = BufReader::new(std::fs::File::open(path).expect("sel cases"));
        let mut parties: Vec<Vec<String>> = Vec::new();
        let mut seasons: Vec<String> = Vec::new();
        for (ln, line) in f.lines().enumerate() {
            let line = line.unwrap();
            let v: Value = serde_json::from_str(&line).unwrap();
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
            cases += 1;
            let ia = v["ia"].as_u64().unwrap() as usize;
            let ib = v["ib"].as_u64().unwrap() as usize;
            let temp = v["temp"].as_f64().unwrap();
            let mp = v["mp"].as_f64().unwrap();
            let n = v["n"].as_u64().unwrap() as usize;
            let seed = v["seed"].as_i64().unwrap() as i128;
            let sseed = v["sseed"].as_i64().unwrap() as i128;
            let exp_idx: Vec<usize> =
                v["idx"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap() as usize).collect();
            let exp_h = v["H"].as_u64().unwrap();

            let mut grng = CpyRandom::new(seed);
            let mut srng = CpyRandom::new(sseed);
            let mut a: Vec<_> =
                parties[ia].iter().map(|s| build_poke(&mut pack, s, &seasons[ia])).collect();
            let mut b: Vec<_> =
                parties[ib].iter().map(|s| build_poke(&mut pack, s, &seasons[ib])).collect();
            let idx = {
                let mut sf = || srng.random();
                select_party(&pack, &mut a, &mut b, n, temp, mp, &mut grng, &mut sf)
            };
            let mut e = Enc::new(&pack, false);
            for p in a.iter().chain(b.iter()) {
                poke_fields(&mut e, p, "");
            }
            let h = sv_hash(&e.vals);
            if idx != exp_idx {
                bad_idx += 1;
                if first.is_none() {
                    first = Some(format!("case={} 選出 rust={:?} py={:?}", cases - 1, idx, exp_idx));
                }
            } else if h != exp_h {
                bad_state += 1;
                if first.is_none() {
                    first =
                        Some(format!("case={} 副作用後状態 rust={:x} py={:x}", cases - 1, h, exp_h));
                }
            }
        }
    }
    println!("─────────────────────────────────────────");
    println!(
        "R3 select_party GATE: cases={} divergences={} (idx={} state={})",
        cases,
        bad_idx + bad_state,
        bad_idx,
        bad_state
    );
    if let Some(f) = first {
        println!("最初の乖離: {}", f);
        std::process::exit(1);
    }
}
