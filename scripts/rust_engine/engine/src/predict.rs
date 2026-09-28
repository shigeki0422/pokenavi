//! simulator/predict.py の移植。AI の「相手の型の読み」のスナップショット（記録・再生・精度集計用）。
//! 信念は書き換えない（写しの上で型プールの事後を計算する）。出力の形は Python と同じ JSON。
use crate::battle::Side;
use crate::belief::{OpponentBelief, PokemonBelief};
use crate::pack::Pack;
use serde_json::{json, Value};

fn ev_str(e: &crate::pack::EvEntry) -> String {
    format!("{}/{}/{}/{}/{}/{}", e.h, e.a, e.b, e.c, e.d, e.s)
}

fn r4(x: f64) -> f64 {
    format!("{:.4}", x).parse::<f64>().unwrap()
}

/// Python の dict（挿入順）を模した (key, value) 列への加算
fn add(v: &mut Vec<(String, f64)>, k: &str, x: f64) {
    if let Some(e) = v.iter_mut().find(|e| e.0 == k) {
        e.1 += x;
    } else {
        v.push((k.to_string(), x));
    }
}

fn norm(d: &[(String, f64)]) -> Vec<(String, f64)> {
    let mut t = 0.0;
    for (_, v) in d {
        if *v > 0.0 {
            t += v;
        }
    }
    if t <= 0.0 {
        return Vec::new();
    }
    d.iter().filter(|(_, v)| *v > 0.0).map(|(k, v)| (k.clone(), v / t)).collect()
}

/// predict.py `_top`: 確率降順・同率は名前順で上位 n 件
fn top(d: &[(String, f64)], n: usize) -> Value {
    let mut v: Vec<&(String, f64)> = d.iter().collect();
    v.sort_by(|a, b| r4(b.1).partial_cmp(&r4(a.1)).unwrap().then_with(|| a.0.cmp(&b.0)));
    Value::Array(v.into_iter().take(n).map(|(k, x)| json!([k, r4(*x)])).collect())
}

/// 1体ぶん。pb は信念の写し（known 等は呼び出し側で opp_view と合わせ済み）
fn entry(pack: &Pack, name: &str, pb: &mut PokemonBelief, season: &str, appeared: bool, joint: bool,
         topn: usize) -> Value {
    let known = json!({"moves": pb.known_moves, "item": pb.known_item, "ability": pb.known_ability,
                       "item_lost": pb.item_lost});
    // ── 周辺分布（JOINT_BUILD=0 の決定化） ──
    let mut mv: Vec<(String, f64)> = pb.move_prior.iter().map(|(m, r)| (m.clone(), (r / 100.0).min(1.0))).collect();
    for m in &pb.known_moves {
        if let Some(e) = mv.iter_mut().find(|e| &e.0 == m) {
            e.1 = 1.0;
        } else {
            mv.push((m.clone(), 1.0));
        }
    }
    let it: Vec<(String, f64)> = match &pb.known_item {
        Some(k) => vec![(k.clone(), 1.0)],
        None => norm(&pb.item_prior.iter().filter(|(i, _)| !pb.absent_items.contains(i)).cloned()
            .collect::<Vec<_>>()),
    };
    let ab: Vec<(String, f64)> = match &pb.known_ability {
        Some(k) if !k.is_empty() => vec![(k.clone(), 1.0)],
        _ => norm(&pb.ability_prior),
    };
    let mut sp: Vec<(usize, f64)> = pb.post.iter().cloned().enumerate().collect();
    sp.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
    let spread: Vec<Value> = sp.iter().take(3)
        .map(|(i, p)| json!({"ev": ev_str(&pb.cands[*i].ev), "nature": pb.cands[*i].nature, "p": r4(*p)}))
        .collect();
    let marginal = json!({"moves": top(&mv, 12), "item": top(&it, topn), "ability": top(&ab, 3),
                          "spread": spread});
    // ── 型プールの事後（JOINT_BUILD=1 の決定化） ──
    let mut pool = Value::Null;
    if let (Some(arr), Some(tpl)) = (pack.build_pool.get(name).filter(|a| !a.is_empty()),
                                     crate::poke::get_pokemon_template(pack, name, season)) {
        // search.rs pick_pool_build / belief.py consistent_builds と同じ条件
        let ok: Vec<usize> = (0..arr.len()).filter(|&i| {
            let b = &arr[i];
            if let Some(k) = pb.known_item.as_deref() {
                if b.item != k {
                    return false;
                }
            }
            if pb.known_item.is_none() && pb.absent_items.iter().any(|x| *x == b.item) {
                return false;
            }
            let mega_seen = pb.known_item.as_deref() == Some(b.item.as_str())
                && crate::battle::is_megastone(pack, pack.intern.get(&b.item));
            if let Some(a) = pb.known_ability.as_deref() {
                if !b.ability.is_empty() && b.ability != a && !mega_seen {
                    return false;
                }
            }
            pb.known_moves.iter().all(|m| b.moves.iter().any(|x| x == m))
        }).collect();
        if !ok.is_empty() {
            let pw = pb.pool_weights(pack, &tpl, arr).to_vec();
            let mut ws: Vec<(usize, f64)> = ok.iter().map(|&i| (i, pw[i])).collect();
            let tot: f64 = ws.iter().map(|x| x.1).sum();
            if tot > 0.0 {
                ws.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
                let (mut pm, mut pi, mut pn) = (Vec::new(), Vec::new(), Vec::new());
                for (i, x) in &ws {
                    let b = &arr[*i];
                    let p = x / tot;
                    for m in &b.moves {
                        add(&mut pm, m, p);
                    }
                    add(&mut pi, &b.item, p);
                    add(&mut pn, &format!("{} {}", ev_str(&b.ev), b.nature), p);
                }
                let tops: Vec<Value> = ws.iter().take(topn).map(|(i, x)| {
                    let b = &arr[*i];
                    json!({"side": b.side, "p": r4(x / tot), "item": b.item, "nature": b.nature,
                           "ev": ev_str(&b.ev), "ability": b.ability, "moves": b.moves})
                }).collect();
                pool = json!({"n_consistent": ok.len(), "top": tops, "moves": top(&pm, 12),
                              "item": top(&pi, topn), "spread": top(&pn, 3)});
            }
        }
    }
    let used = if joint && !pool.is_null() { "pool" } else { "marginal" };
    json!({"appeared": appeared, "known": known, "marginal": marginal, "pool": pool, "used": used})
}

/// predict.py `Predictor.snapshot`。side（読む側）が相手の各ポケモンをどう読んでいるか。
/// appeared は場に出たことのある相手の名前（呼び出し側で蓄積）。joint は決定化が型プールを使うか。
pub fn snapshot(pack: &Pack, side: &Side, appeared: &[String], joint: bool) -> Value {
    let bel: Option<&OpponentBelief> = side.belief.0.as_deref();
    let season = bel.map(|b| b.season.clone()).unwrap_or_else(|| crate::sim::belief_season().to_string());
    let mut out = serde_json::Map::new();
    let mut fresh = OpponentBelief::new(&season);
    for k in &side.opp_view.pokemon {
        let name = pack.intern.resolve(k.name).to_string();
        let mut pb = match bel.and_then(|b| b.species.iter().find(|(n, _)| *n == name)) {
            Some((_, pb)) => pb.clone(),
            None => match fresh.ensure(pack, &name, None, None) {
                Some(i) => fresh.species[i].1.clone(),
                None => continue,
            },
        };
        // 記録時点で判明している分は写しに足して読む（信念そのものは書き換えない）
        for m in &k.known_moves {
            let m = pack.intern.resolve(*m).to_string();
            if !pb.known_moves.contains(&m) {
                pb.known_moves.push(m);
            }
        }
        pb.known_moves.sort();
        if pb.known_item.is_none() {
            pb.known_item = k.known_item.map(|x| pack.intern.resolve(x).to_string());
        }
        if pb.known_ability.is_none() {
            pb.known_ability = k.known_ability.map(|x| pack.intern.resolve(x).to_string());
        }
        pb.item_lost = pb.item_lost || k.item_lost;
        let app = k.seen || appeared.iter().any(|x| *x == name);
        out.insert(name.clone(), entry(pack, &name, &mut pb, &season, app, joint, 5));
    }
    Value::Object(out)
}
