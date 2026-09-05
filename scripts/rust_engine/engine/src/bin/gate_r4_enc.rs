//! R4-G1/G2 ゲート: encode_state(905) と 逐次ネットforward のビット一致。
//! Python 側 `_rust_engine/dump_encode_cases.py` の記録を再生して比較する。
//! 使い方: gate_r4_enc <datapack.json> <cases/enc_XX.jsonl> [...]
use engine::ai::Ai;
use engine::rng::BRng;
use engine::search::{net_eval_x, NetCtx};
use engine::sim::full_battle;
use engine::statec::{encode_battle, f64_hash, sv_hash};
use serde_json::Value;
use std::io::{BufRead, BufReader};

/// encode 中に乱数を引いたら即検出する（コーパスに きまぐレーザー は無い前提）
struct NoRng;
impl BRng for NoRng {
    fn random(&mut self) -> f64 {
        panic!("encode_state が乱数を消費した（きまぐレーザー？）");
    }
    fn choice(&mut self, _n: usize) -> usize {
        panic!("encode_state が choice を消費した");
    }
    fn randint(&mut self, _a: i64, _b: i64) -> i64 {
        panic!("encode_state が randint を消費した");
    }
    fn choices(&mut self) -> i64 {
        panic!("encode_state が choices を消費した");
    }
}

fn bits(x: f64) -> u64 {
    x.to_bits()
}

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
    let net = pack.net.clone().expect("datapack に net が無い");
    let mut ctx = NetCtx::new(&pack);
    let bench = std::env::var("R4_BENCH").is_ok();

    let mut battles = 0i64;
    let mut states = 0i64;
    let (mut div_x, mut div_v, mut div_p, mut div_state) = (0i64, 0i64, 0i64, 0i64);
    let mut first_msg: Option<String> = None;
    let t0 = std::time::Instant::now();
    let mut enc_nanos = 0u128;

    for path in &args[2..] {
        let f = BufReader::new(std::fs::File::open(path).expect("enc cases"));
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
                    .map(|p| p.as_array().unwrap().iter().map(|s| s.as_str().unwrap().to_string()).collect())
                    .collect();
                seasons =
                    v["seasons"].as_array().unwrap().iter().map(|s| s.as_str().unwrap().into()).collect();
                continue;
            }
            let bid = v["b"].as_i64().unwrap();
            let ia = v["ia"].as_u64().unwrap() as usize;
            let ib = v["ib"].as_u64().unwrap() as usize;
            let sa: Vec<usize> =
                v["sa"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap() as usize).collect();
            let sb: Vec<usize> =
                v["sb"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap() as usize).collect();
            let seed = v["seed"].as_i64().unwrap() as i128;
            let aim = v["ai"].as_str().unwrap().as_bytes();
            let exp_h: Vec<u64> = v["H"].as_array().unwrap().iter().map(|x| x.as_u64().unwrap()).collect();
            let exp_e = v["E"].as_array().unwrap();
            let mut ti = 0usize;
            let mut local_bad: Option<String> = None;
            let (mut dx, mut dv, mut dp, mut ds) = (0i64, 0i64, 0i64, 0i64);
            let mut nst = 0i64;
            let te = std::time::Instant::now();
            let _out = {
                let packref = &mut pack;
                full_battle(
                    packref,
                    &parties[ia],
                    &sa,
                    &parties[ib],
                    &sb,
                    &seasons[ia],
                    &seasons[ib],
                    seed,
                    (ai_of(aim[0]), true),
                    (ai_of(aim[1]), true),
                    true,
                    None,
                    |pk, bt| {
                        if bench {
                            let mut c = bt.clone();
                            ctx.memo.begin();
                            for first in 0..2usize {
                                let _ = net_eval_x(pk, &net, &mut ctx, &mut c.sides, first, &mut c.field, &mut NoRng);
                            }
                            ctx.memo.end();
                            nst += 2;
                            ti += 1;
                            return;
                        }
                        let e = encode_battle(pk, bt, false);
                        let h = sv_hash(&e.vals);
                        if ti < exp_h.len() && h != exp_h[ti] {
                            ds += 1;
                            if local_bad.is_none() {
                                local_bad = Some(format!("状態ハッシュ turn={}", ti + 1));
                            }
                        }
                        let mut c = bt.clone();
                        ctx.memo.begin();
                        for first in 0..2usize {
                            let (x, pol, val) =
                                net_eval_x(pk, &net, &mut ctx, &mut c.sides, first, &mut c.field, &mut NoRng);
                            nst += 1;
                            if ti >= exp_e.len() {
                                continue;
                            }
                            let ex = &exp_e[ti][first];
                            let xh = f64_hash(&x);
                            if xh != ex[0].as_u64().unwrap() {
                                dx += 1;
                                if local_bad.is_none() {
                                    let mut det = String::new();
                                    if let Some(fx) = ex.get(3).and_then(|z| z.as_array()) {
                                        for (i, z) in fx.iter().enumerate() {
                                            let pb = z.as_u64().unwrap();
                                            if i >= x.len() || x[i].to_bits() != pb {
                                                det = format!(
                                                    " idx={} rust={:?} py={:?}",
                                                    i,
                                                    x.get(i).copied().unwrap_or(f64::NAN),
                                                    f64::from_bits(pb)
                                                );
                                                break;
                                            }
                                        }
                                        if det.is_empty() && fx.len() != x.len() {
                                            det = format!(" len rust={} py={}", x.len(), fx.len());
                                        }
                                    }
                                    local_bad =
                                        Some(format!("encode turn={} first={} h={:x} py={:x}{}", ti + 1, first, xh, ex[0].as_u64().unwrap(), det));
                                }
                                continue;
                            }
                            if bits(val) != ex[1].as_u64().unwrap() {
                                dv += 1;
                                if local_bad.is_none() {
                                    local_bad = Some(format!(
                                        "value turn={} first={} rust={:?} py_bits={:x}",
                                        ti + 1, first, val, ex[1].as_u64().unwrap()
                                    ));
                                }
                                continue;
                            }
                            let epol = ex[2].as_array().unwrap();
                            let mut ok = epol.len() == pol.len();
                            if ok {
                                for (k, (a, p)) in pol.iter().enumerate() {
                                    let ea = epol[k][0].as_u64().unwrap() as usize;
                                    let eb = epol[k][1].as_u64().unwrap();
                                    if ea != *a || bits(*p) != eb {
                                        ok = false;
                                        break;
                                    }
                                }
                            }
                            if !ok {
                                dp += 1;
                                if local_bad.is_none() {
                                    local_bad = Some(format!("policy turn={} first={}", ti + 1, first));
                                }
                            }
                        }
                        ctx.memo.end();
                        ti += 1;
                    },
                )
            };
            enc_nanos += te.elapsed().as_nanos();
            battles += 1;
            states += nst;
            div_x += dx;
            div_v += dv;
            div_p += dp;
            div_state += ds;
            if let Some(m) = local_bad {
                if first_msg.is_none() {
                    first_msg = Some(format!("{} battle={} seed={} : {}", path, bid, seed, m));
                }
            }
        }
        println!(
            "[gate_r4_enc] {} 済: battles={} states={} div(x/v/p/state)={}/{}/{}/{}",
            path, battles, states, div_x, div_v, div_p, div_state
        );
    }
    let secs = t0.elapsed().as_secs_f64();
    println!("─────────────────────────────────────────");
    println!(
        "R4 G1/G2 GATE: battles={} states={} divergences={} (encode={} value={} policy={} state={})",
        battles,
        states,
        div_x + div_v + div_p + div_state,
        div_x,
        div_v,
        div_p,
        div_state
    );
    println!(
        "rust: {:.2}s total / {:.4} ms per state (encode+forward込み)",
        secs,
        (enc_nanos as f64) / 1e6 / (states.max(1) as f64)
    );
    if let Some(f) = first_msg {
        println!("── 最初の乖離 ──\n{}", f);
        std::process::exit(1);
    }
}
