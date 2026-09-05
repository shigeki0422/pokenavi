//! R2ゲート: 行動リプレイ・パリティ。
//! Python がダンプした（初期spec・毎ターンの行動・消費乱数・状態ベクトル）を再生し、
//! 各ターン終了時の正準状態を1要素ずつ比較する。
//! 使い方: gate_r2 <datapack.json> <turn_XX.jsonl> [...]
use engine::battle::{ActKind, Action, Battle, Side};
use engine::damage::{DMove, Field};
use engine::pack::{Cat, Pack, Ty};
use engine::poke::build_poke;
use engine::rng::{BRng, Draw};
use engine::statec::{encode_battle, SV};
use serde_json::Value;
use std::cell::RefCell;
use std::collections::HashSet;
use std::io::{BufRead, BufReader};

struct SegRng {
    segs: Vec<Vec<Draw>>,
    seg: usize,
    pos: usize,
    /// 過剰消費してもターンを完走させ、状態diffで原因を特定できるようにする
    overflow: usize,
    want: Option<Draw>,
}

impl SegRng {
    fn next(&mut self) -> Draw {
        let s = &self.segs[self.seg];
        if self.pos >= s.len() {
            self.overflow += 1;
            self.pos += 1;
            return self.want.unwrap_or(Draw::Random(0.5));
        }
        let d = s[self.pos];
        self.pos += 1;
        d
    }
}

struct Adapter<'a>(&'a RefCell<SegRng>);

impl<'a> BRng for Adapter<'a> {
    fn random(&mut self) -> f64 {
        let mut r = self.0.borrow_mut();
        r.want = Some(Draw::Random(0.5));
        match r.next() {
            Draw::Random(v) => v,
            o => panic!("RNG種別不一致 expected random got {:?} @seg{} pos{}", o, r.seg, r.pos - 1),
        }
    }
    fn choice(&mut self, n: usize) -> usize {
        let mut r = self.0.borrow_mut();
        r.want = Some(Draw::Choice(0));
        match r.next() {
            Draw::Choice(i) => {
                assert!(i < n, "choice index {} >= {}", i, n);
                i
            }
            o => panic!("RNG種別不一致 expected choice got {:?} @seg{} pos{}", o, r.seg, r.pos - 1),
        }
    }
    fn randint(&mut self, a: i64, _b: i64) -> i64 {
        let mut r = self.0.borrow_mut();
        r.want = Some(Draw::Randint(a));
        match r.next() {
            Draw::Randint(v) => v,
            o => panic!("RNG種別不一致 expected randint got {:?} @seg{} pos{}", o, r.seg, r.pos - 1),
        }
    }
    fn choices(&mut self) -> i64 {
        let mut r = self.0.borrow_mut();
        r.want = Some(Draw::Choices(2));
        match r.next() {
            Draw::Choices(v) => v,
            o => panic!("RNG種別不一致 expected choices got {:?} @seg{} pos{}", o, r.seg, r.pos - 1),
        }
    }
}

fn parse_draws(v: &Value) -> Vec<Draw> {
    v.as_array()
        .map(|a| {
            a.iter()
                .map(|d| {
                    let d = d.as_array().unwrap();
                    match d[0].as_str().unwrap() {
                        "r" => Draw::Random(d[1].as_f64().unwrap()),
                        "c" => Draw::Choice(d[1].as_u64().unwrap() as usize),
                        "i" => Draw::Randint(d[1].as_i64().unwrap()),
                        "w" => Draw::Choices(d[1].as_i64().unwrap()),
                        o => panic!("未知の draw kind {}", o),
                    }
                })
                .collect()
        })
        .unwrap_or_default()
}

fn ty_of(pack: &Pack, v: &Value) -> Option<Ty> {
    v.as_str().map(|s| {
        pack.types
            .iter()
            .position(|t| t == s)
            .map(|i| i as Ty)
            .unwrap_or_else(|| panic!("unknown type {}", s))
    })
}

fn decode_action(pack: &mut Pack, v: &Value) -> Action {
    let a = v.as_array().expect("action array");
    let kind = match a[0].as_str().unwrap() {
        "move" => ActKind::Move,
        "switch" => ActKind::Switch,
        "mega" => ActKind::Mega,
        _ => ActKind::Pass,
    };
    let mv = if a[2].is_null() {
        None
    } else {
        let m = a[2].as_array().unwrap();
        let name = pack.intern_new(m[0].as_str().unwrap());
        let ty = {
            let s = m[1].as_str().unwrap();
            pack.types
                .iter()
                .position(|t| t == s)
                .map(|i| i as Ty)
                .unwrap_or_else(|| panic!("unknown move type {}", s))
        };
        Some(DMove {
            name,
            ty,
            category: Cat::parse(m[2].as_str().unwrap()),
            power: m[3].as_i64(),
            accuracy: m[4].as_i64(),
            priority: m[5].as_i64().unwrap_or(0),
            pp: m[6].as_i64(),
        })
    };
    Action {
        kind,
        mv,
        move_idx: a[1].as_i64().unwrap_or(0),
        switch_to: a[3].as_i64().unwrap_or(-1),
        do_mega: a[4].as_bool().unwrap_or(false),
    }
}

fn sv_eq(a: &SV, b: &Value) -> bool {
    match (a, b) {
        (SV::N, Value::Null) => true,
        (SV::B(x), Value::Bool(y)) => x == y,
        (SV::S(x), Value::String(y)) => x == y,
        (SV::I(x), Value::Number(_)) => b.as_f64().map(|f| (*x as f64) == f).unwrap_or(false),
        (SV::F(x), Value::Number(_)) => b.as_f64().map(|f| *x == f).unwrap_or(false),
        _ => false,
    }
}

fn sv_str(a: &SV) -> String {
    match a {
        SV::N => "null".into(),
        SV::B(x) => format!("{}", x),
        SV::S(x) => format!("\"{}\"", x),
        SV::I(x) => format!("{}", x),
        SV::F(x) => format!("{}", x),
    }
}

struct Div {
    battle: i64,
    turn: i64,
    idx: usize,
    name: String,
    rust: String,
    py: String,
}

pub static VERBOSE: std::sync::atomic::AtomicBool = std::sync::atomic::AtomicBool::new(false);

fn compare(pack: &Pack, b: &Battle, exp: &[Value], bid: i64, turn: i64) -> Option<Div> {
    let enc = encode_battle(pack, b, false);
    let n = std::cmp::min(enc.vals.len(), exp.len());
    for i in 0..n {
        if !sv_eq(&enc.vals[i], &exp[i]) {
            let named = encode_battle(pack, b, true);
            let nm = named.names.as_ref().unwrap()[i].clone();
            if VERBOSE.load(std::sync::atomic::Ordering::Relaxed) {
                let ns = named.names.as_ref().unwrap();
                let mut shown = 0;
                for j in 0..n {
                    if !sv_eq(&enc.vals[j], &exp[j]) {
                        println!("   diff {:<40} rust={:<16} py={}", ns[j], sv_str(&enc.vals[j]), exp[j]);
                        shown += 1;
                        if shown >= 20 {
                            break;
                        }
                    }
                }
            }
            return Some(Div {
                battle: bid,
                turn,
                idx: i,
                name: nm,
                rust: sv_str(&enc.vals[i]),
                py: exp[i].to_string(),
            });
        }
    }
    if enc.vals.len() != exp.len() {
        return Some(Div {
            battle: bid,
            turn,
            idx: n,
            name: format!("<長さ不一致 rust={} py={}>", enc.vals.len(), exp.len()),
            rust: format!("{}", enc.vals.len()),
            py: format!("{}", exp.len()),
        });
    }
    None
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if std::env::var("R2_VERBOSE").is_ok() {
        VERBOSE.store(true, std::sync::atomic::Ordering::Relaxed);
    }
    let only: Option<i64> = std::env::var("R2_ONLY").ok().and_then(|x| x.parse().ok());
    let bench = std::env::var("R2_BENCH").is_ok();
    let mut pack = Pack::load(&args[1]);

    let mut battles = 0i64;
    let mut turns = 0i64;
    let mut divergences = 0i64;
    let mut first: Option<Div> = None;
    let mut errors: Vec<String> = Vec::new();
    let mut moves_seen: HashSet<u16> = HashSet::new();
    let mut abils_seen: HashSet<u16> = HashSet::new();
    let mut items_seen: HashSet<u16> = HashSet::new();
    let mut moves_used: HashSet<u16> = HashSet::new();
    let mut abils_active: HashSet<u16> = HashSet::new();
    let mut items_active: HashSet<u16> = HashSet::new();
    let t0 = std::time::Instant::now();
    let mut engine_nanos = 0u128;

    for path in &args[2..] {
        let f = BufReader::new(std::fs::File::open(path).expect("trace"));
        for (ln, line) in f.lines().enumerate() {
            let line = line.unwrap();
            if ln == 0 {
                continue;
            }
            let v: Value = serde_json::from_str(&line).expect("trace json");
            let bid = v["b"].as_i64().unwrap_or(0);
            if let Some(o) = only {
                if bid != o {
                    continue;
                }
            }

            // パーティ構築
            let sa: Vec<String> =
                v["specsA"].as_array().unwrap().iter().map(|x| x.as_str().unwrap().into()).collect();
            let sb: Vec<String> =
                v["specsB"].as_array().unwrap().iter().map(|x| x.as_str().unwrap().into()).collect();
            let season_a = v["seasonA"].as_str().unwrap();
            let season_b = v["seasonB"].as_str().unwrap();
            let mut pa = Vec::new();
            for s in &sa {
                pa.push(build_poke(&mut pack, s, season_a));
            }
            let mut pb = Vec::new();
            for s in &sb {
                pb.push(build_poke(&mut pack, s, season_b));
            }
            for p in pa.iter().chain(pb.iter()) {
                abils_seen.insert(p.ability);
                if let Some(i) = p.item {
                    items_seen.insert(i);
                }
                for m in &p.moves {
                    moves_seen.insert(m.name);
                }
            }

            let mut s1 = Side { party: pa, ..Default::default() };
            let mut s2 = Side { party: pb, ..Default::default() };
            s1.active_idx = 0;
            s2.active_idx = 0;
            let field = Field {
                roll_override: v["roll_override"].as_f64(),
                ..Default::default()
            };
            let mut b = Battle::new(s1, s2, field);

            let pv = |pack: &mut Pack, key: &str| -> Vec<(u16, Ty, Option<Ty>, Ty, Option<Ty>)> {
                v[key]
                    .as_array()
                    .unwrap()
                    .iter()
                    .map(|e| {
                        let e = e.as_array().unwrap();
                        let name = pack.intern_new(e[0].as_str().unwrap());
                        let bt1 = ty_of(pack, &e[1]).unwrap_or(engine::pack::NO_TY);
                        let bt2 = ty_of(pack, &e[2]);
                        let t1 = ty_of(pack, &e[3]).unwrap_or(engine::pack::NO_TY);
                        let t2 = ty_of(pack, &e[4]);
                        (name, bt1, bt2, t1, t2)
                    })
                    .collect()
            };
            let pv1 = pv(&mut pack, "pv1");
            let pv2 = pv(&mut pack, "pv2");

            b.start(&pack, &pv1, &pv2);

            // S0 比較
            let s0 = v["S0"].as_array().unwrap();
            if let Some(d) = (if bench { None } else { compare(&pack, &b, s0, bid, 0) }) {
                divergences += 1;
                if first.is_none() {
                    first = Some(d);
                }
                battles += 1;
                continue;
            }

            let tv = v["turns"].as_array().unwrap();
            let mut acts: Vec<[Action; 2]> = Vec::with_capacity(tv.len());
            let mut segs: Vec<Vec<Draw>> = Vec::with_capacity(tv.len() + 1);
            for t in tv {
                let a = t["acts"].as_array().unwrap();
                let pair = [decode_action(&mut pack, &a[0]), decode_action(&mut pack, &a[1])];
                for x in pair.iter() {
                    if let Some(m) = &x.mv {
                        moves_used.insert(m.name);
                    }
                }
                acts.push(pair);
                segs.push(parse_draws(&t["rng"]));
            }
            segs.push(Vec::new()); // 番兵

            let rc = RefCell::new(SegRng { segs, seg: 0, pos: 0, overflow: 0, want: None });
            let expected: Vec<&Vec<Value>> =
                tv.iter().map(|t| t["S"].as_array().unwrap()).collect();
            let mut local_div: Option<Div> = None;
            let mut nturn_done = 0i64;
            {
                let mut ad = Adapter(&rc);
                let packr = &pack;
                let te = std::time::Instant::now();
                let res = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
                    b.run_replay(packr, &acts, &mut ad, |bt| {
                        let ti = (bt.turn - 1) as usize;
                        let mut rngdiv: Option<Div> = None;
                        {
                            let mut r = rc.borrow_mut();
                            let seg = r.seg;
                            let mismatch = r.pos != r.segs[seg].len();
                            let (p, ln) = (r.pos, r.segs[seg].len());
                            r.seg += 1;
                            r.pos = 0;
                            r.overflow = 0;
                            drop(r);
                            if mismatch {
                                rngdiv = Some(Div {
                                    battle: bid,
                                    turn: bt.turn,
                                    idx: usize::MAX,
                                    name: "<RNG消費数不一致>".into(),
                                    rust: format!("{}", p),
                                    py: format!("{}", ln),
                                });
                            }
                        }
                        if local_div.is_none() && !bench {
                            local_div = compare(packr, bt, expected[ti], bid, bt.turn);
                        }
                        if local_div.is_none() {
                            local_div = rngdiv;
                        }
                        if !bench {
                            for sx in 0..2usize {
                                let p = bt.sides[sx].active();
                                abils_active.insert(p.ability);
                                if let Some(i) = p.item {
                                    items_active.insert(i);
                                }
                            }
                        }
                        nturn_done += 1;
                    })
                }));
                engine_nanos += te.elapsed().as_nanos();
                if let Err(e) = res {
                    let msg = e
                        .downcast_ref::<String>()
                        .cloned()
                        .or_else(|| e.downcast_ref::<&str>().map(|s| s.to_string()))
                        .unwrap_or_else(|| "panic".into());
                    errors.push(format!("battle {}: panic: {}", bid, msg));
                    divergences += 1;
                    if first.is_none() {
                        first = Some(Div {
                            battle: bid,
                            turn: -1,
                            idx: usize::MAX,
                            name: "<panic>".into(),
                            rust: msg,
                            py: String::new(),
                        });
                    }
                    battles += 1;
                    continue;
                }
                let res = res.unwrap();
                let exp_res = v["result"].as_i64().unwrap_or(-1);
                if local_div.is_none() && res != exp_res {
                    local_div = Some(Div {
                        battle: bid,
                        turn: b.turn,
                        idx: usize::MAX,
                        name: "<勝敗不一致>".into(),
                        rust: format!("{}", res),
                        py: format!("{}", exp_res),
                    });
                }
            }
            turns += nturn_done;
            if let Some(d) = local_div {
                divergences += 1;
                if first.is_none() {
                    first = Some(d);
                }
            }
            battles += 1;
        }
        println!(
            "[gate_r2] {} 済: battles={} turns={} divergences={}",
            path, battles, turns, divergences
        );
    }

    let secs = t0.elapsed().as_secs_f64();
    println!("─────────────────────────────────────────");
    println!("R2 GATE: battles={} turns={} divergences={}", battles, turns, divergences);
    println!(
        "rust replay(JSON込): {:.2}s ({:.0} turns/s)",
        secs,
        (turns as f64) / secs.max(1e-9)
    );
    let esec = (engine_nanos as f64) / 1e9;
    println!(
        "rust engine only: {:.3}s ({:.0} turns/s, {:.1} us/turn)",
        esec,
        (turns as f64) / esec.max(1e-9),
        esec * 1e6 / (turns.max(1) as f64)
    );
    println!(
        "coverage(所持): moves={} abilities={} items={}",
        moves_seen.len(),
        abils_seen.len(),
        items_seen.len()
    );
    println!(
        "coverage(実行/場に出た): moves_used={} abilities_active={} items_active={}",
        moves_used.len(),
        abils_active.len(),
        items_active.len()
    );
    if let Ok(path) = std::env::var("R2_COVERAGE_OUT") {
        let names = |h: &HashSet<u16>| -> Vec<String> {
            let mut v: Vec<String> = h.iter().map(|&s| pack.intern.resolve(s).to_string()).collect();
            v.sort();
            v
        };
        let j = serde_json::json!({
            "battles": battles,
            "turns": turns,
            "divergences": divergences,
            "moves_in_party": names(&moves_seen),
            "moves_used": names(&moves_used),
            "abilities_in_party": names(&abils_seen),
            "abilities_active": names(&abils_active),
            "items_in_party": names(&items_seen),
            "items_active": names(&items_active),
        });
        std::fs::write(&path, serde_json::to_string_pretty(&j).unwrap()).unwrap();
        println!("coverage -> {}", path);
    }
    if let Some(d) = &first {
        println!("── 最初の乖離 ──");
        println!(
            "battle={} turn={} idx={} field={}\n  rust={}\n  py  ={}",
            d.battle, d.turn, d.idx, d.name, d.rust, d.py
        );
    }
    for e in errors.iter().take(5) {
        println!("  {}", e);
    }
    if divergences > 0 {
        std::process::exit(1);
    }
}
