//! PyO3 モジュール `pokenavi_engine`（R5）。境界は「対戦1回」単位なので marshalling は無視できる。
//!
//! 公開API:
//!   greedy_3v3(pa, sa, pb, sb, seed, season="M-3") -> u8
//!   mcts_3v3(pa, sa, pb, sb, seed, sims, season="M-3") -> u8
//!   mcts_vs_dist(pa, sa, pb, seed, sims, season="M-3") -> u8
//!   mu_analyze(spec_a, spec_b, season) -> str(JSON)  1v1の与ダメ・確定数・手順・記号判定
//!   mu_sym(score) -> str  スコア→記号（複数型の平均を集約するとき用）
//!   datapack_hash() -> str / version() -> str
//!
//! データパックは環境変数 POKENAVI_DATAPACK（既定 `_rust_engine/datapack.json`）から1度だけロードする。
use engine::net::NetW;
use engine::pack::Pack;
use pyo3::exceptions::{PyRuntimeError, PyValueError};
use pyo3::prelude::*;
use std::sync::{Mutex, OnceLock};

struct Eng {
    pack: Pack,
    net: NetW,
    hash: String,
    live: Option<engine::live::Live>,
    /// 学習選出の状態の符号化に使う（初回に作る）
    ft: Option<engine::features::FeatTables>,
}

static ENG: OnceLock<Mutex<Eng>> = OnceLock::new();

fn datapack_path() -> String {
    std::env::var("POKENAVI_DATAPACK").unwrap_or_else(|_| "_rust_engine/datapack.json".to_string())
}

/// ロックを取る。前の呼び出しがパニックで抜けて poison されていても中身を使い続ける
/// （エンジンの状態は呼び出しごとに作り直すので、壊れた途中状態は残らない。scenario は呼び出し側で既定に戻す）。
fn lock_eng(m: &'static Mutex<Eng>) -> std::sync::MutexGuard<'static, Eng> {
    let mut g = m.lock().unwrap_or_else(|e| e.into_inner());
    if m.is_poisoned() {
        g.pack.scenario = engine::pack::Scenario::default();
        m.clear_poison();
    }
    g
}

fn eng() -> PyResult<&'static Mutex<Eng>> {
    if let Some(e) = ENG.get() {
        return Ok(e);
    }
    let path = datapack_path();
    let txt = std::fs::read_to_string(&path)
        .map_err(|e| PyRuntimeError::new_err(format!("datapack 読み込み失敗 {}: {}", path, e)))?;
    let v: serde_json::Value = serde_json::from_str(&txt)
        .map_err(|e| PyRuntimeError::new_err(format!("datapack parse: {}", e)))?;
    let hash = Pack::content_hash(&v);
    let pack = Pack::from_value(&v);
    let net = pack
        .net
        .clone()
        .ok_or_else(|| PyRuntimeError::new_err("datapack に net が無い"))?;
    let _ = ENG.set(Mutex::new(Eng { pack, net, hash, live: None, ft: None }));
    Ok(ENG.get().unwrap())
}

/// 提案の採点の選出に使う学習選出のモデル（selector_m6b.json 等）を live に渡す（起動時に1回）。空文字で外す（ヒューリスティック）
#[pyfunction]
fn live_set_selector(path: &str) -> PyResult<bool> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { live, .. } = &mut *g;
    let live = live.as_mut().ok_or_else(|| PyRuntimeError::new_err("live_setup 未実行"))?;
    if path.is_empty() {
        live.selector = None;
        return Ok(false);
    }
    let sel = engine::selector::Selector::from_json(path)
        .ok_or_else(|| PyValueError::new_err(format!("{path}: 選出モデルとして読めない")))?;
    live.selector = Some(sel);
    Ok(true)
}

/// 照合用: 採点のパネル各面で Rust が選んだ (自分の選出, パネル側の選出)
#[pyfunction]
fn live_panel_selections(specs: Vec<String>) -> PyResult<Vec<(Vec<usize>, Vec<usize>)>> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, live, .. } = &mut *g;
    let live = live.as_mut().ok_or_else(|| PyRuntimeError::new_err("live_setup 未実行"))?;
    Ok(live.panel_states_full(pack, &specs).1)
}

/// 学習選出（simulator/learned_selection.py）の候補・相手の仮定・状態ベクトル。推論と選択は Python 側。
/// state は random.getstate()[1]（624語＋位置）。戻り: (候補, 相手の仮定, 状態ベクトルのバイト列 f64 LE, 次元, 進めた乱数の状態)
#[pyfunction]
#[allow(clippy::type_complexity, clippy::too_many_arguments)]
fn learned_select_states(
    py: Python<'_>,
    specs_a: Vec<String>,
    specs_b: Vec<String>,
    season: &str,
    n: usize,
    min_mega: usize,
    max_mega: usize,
    state: Vec<u32>,
) -> PyResult<(Vec<Vec<usize>>, Vec<Vec<usize>>, PyObject, usize, Vec<u32>)> {
    if state.len() != 625 {
        return Err(PyValueError::new_err("state は 625 語（random.getstate()[1]）"));
    }
    let m = eng()?;
    let mut g = lock_eng(m);
    for sp in specs_a.iter().chain(specs_b.iter()) {
        if let Some(e) = engine::poke::spec_error(&g.pack, sp, season) {
            return Err(PyValueError::new_err(e));
        }
    }
    let Eng { pack, ft, .. } = &mut *g;
    if ft.is_none() {
        *ft = Some(engine::features::FeatTables::build(pack));
    }
    let ftr = ft.as_ref().unwrap();
    let (c, o, xs, dim, st) = engine::sim::learned_select_states(pack, ftr, &specs_a, &specs_b, season, n, min_mega, max_mega, &state);
    let mut buf = Vec::with_capacity(xs.len() * 8);
    for v in xs {
        buf.extend_from_slice(&v.to_le_bytes());
    }
    Ok((c, o, pyo3::types::PyBytes::new_bound(py, &buf).into(), dim, st))
}

/// 検証用: PREDICT_PROBE=1 で走らせた直前の対戦の各ターンの読み (ターン, side1 JSON, side2 JSON)
#[pyfunction]
fn predict_probe_take() -> PyResult<Vec<(i64, String, String)>> {
    Ok(engine::sim::predict_probe_take())
}

/// 検証用: BELIEF_PROBE=1 で走らせた直前の対戦の P1 の信念
/// [(種, 事後(EV/性格候補), 型プール重み, 判明技, 判明持ち物, 持ち物喪失, 発動しなかった持ち物)]
#[pyfunction]
#[allow(clippy::type_complexity)]
fn belief_probe_take() -> PyResult<Vec<(String, Vec<f64>, Vec<f64>, Vec<String>, Option<String>, bool, Vec<String>)>> {
    Ok(engine::sim::belief_probe_take())
}

#[pyfunction]
#[pyo3(signature = (pa, sa, pb, sb, seed, season="M-3"))]
fn greedy_3v3(
    pa: Vec<String>,
    sa: Vec<usize>,
    pb: Vec<String>,
    sb: Vec<usize>,
    seed: i128,
    season: &str,
) -> PyResult<u8> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, .. } = &mut *g;
    Ok(engine::sim::greedy_3v3(pack, &pa, &sa, &pb, &sb, season, seed) as u8)
}

#[pyfunction]
#[pyo3(signature = (pa, sa, pb, sb, seed, sims, season="M-3"))]
fn mcts_3v3(
    pa: Vec<String>,
    sa: Vec<usize>,
    pb: Vec<String>,
    sb: Vec<usize>,
    seed: i128,
    sims: usize,
    season: &str,
) -> PyResult<u8> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, net, .. } = &mut *g;
    let net = net.clone();
    let (r, _) =
        engine::sim::mcts_3v3(pack, &net, None, &pa, &sa, &pb, &sb, season, season, seed, sims, |_, _| {});
    Ok(r as u8)
}

/// A/B用: 側1と側2で別のネットを使って mcts_3v3 を回す。net_b_path は JSON のパス（初回のみ読む）。
static NET_CACHE: std::sync::Mutex<Vec<(String, engine::net::NetW)>> =
    std::sync::Mutex::new(Vec::new());

fn load_net_cached(path: &str) -> PyResult<engine::net::NetW> {
    let mut c = NET_CACHE.lock().unwrap_or_else(|e| e.into_inner());
    if let Some((_, n)) = c.iter().find(|(p, _)| p == path) {
        return Ok(n.clone());
    }
    let txt = std::fs::read_to_string(path)
        .map_err(|e| PyRuntimeError::new_err(format!("{path}: {e}")))?;
    let v: serde_json::Value =
        serde_json::from_str(&txt).map_err(|e| PyRuntimeError::new_err(format!("{path}: {e}")))?;
    let n = engine::net::NetW::from_value(&v)
        .ok_or_else(|| PyRuntimeError::new_err(format!("{path}: ネットとして読めない")))?;
    c.push((path.to_string(), n.clone()));
    Ok(n)
}

#[pyfunction]
#[pyo3(signature = (pa, sa, pb, sb, seed, sims, net_a_path="", net_b_path="", season="M-6", sims_b=0))]
#[allow(clippy::too_many_arguments)]
fn mcts_3v3_ab(
    pa: Vec<String>,
    sa: Vec<usize>,
    pb: Vec<String>,
    sb: Vec<usize>,
    seed: i128,
    sims: usize,
    net_a_path: &str,
    net_b_path: &str,
    season: &str,
    sims_b: usize,
) -> PyResult<u8> {
    let na = if net_a_path.is_empty() { None } else { Some(load_net_cached(net_a_path)?) };
    let nb = if net_b_path.is_empty() { None } else { Some(load_net_cached(net_b_path)?) };
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, net, .. } = &mut *g;
    let base = net.clone();
    let side1 = na.as_ref().unwrap_or(&base);
    let side2 = nb.as_ref().unwrap_or(&base);
    let (r, _) = engine::sim::mcts_3v3_sims(
        pack, side1, Some(side2), &pa, &sa, &pb, &sb, season, season, seed, sims,
        if sims_b == 0 { sims } else { sims_b }, |_, _| {},
    );
    Ok(r as u8)
}

/// 終盤の厳密ソルバによる採点: mcts_3v3 を回し、終盤の各手番で
/// (手番側, 均衡値, [(手index, 期待勝率)], AIの手index, 残り体数, ノード数) を返す。
/// env SOLVE_DEPTH（深さ）/ SOLVE_MAX_ALIVE（対象とする残り体数の上限）で制御する。
#[pyfunction]
#[pyo3(signature = (pa, sa, pb, sb, seed, sims, season="M-6"))]
#[allow(clippy::type_complexity)]
fn mcts_3v3_solve(
    pa: Vec<String>,
    sa: Vec<usize>,
    pb: Vec<String>,
    sb: Vec<usize>,
    seed: i128,
    sims: usize,
    season: &str,
) -> PyResult<(u8, Vec<(usize, f64, Vec<(usize, f64)>, usize, usize, u64, u64, u64)>)> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, net, .. } = &mut *g;
    let net = net.clone();
    let _ = engine::sim::solve_trace_take();
    let (r, _) = engine::sim::mcts_3v3(pack, &net, None, &pa, &sa, &pb, &sb, season, season, seed, sims, |_, _| {});
    Ok((r as u8, engine::sim::solve_trace_take()))
}

/// 決定化の的中率を取り出してリセットする。
/// [試行数, 持ち物一致, 特性一致, 技の一致本数, 技4本完全一致, 全一致]
#[pyfunction]
fn det_slot_take() -> PyResult<Vec<u64>> {
    Ok(engine::sim::det_slot_take())
}

#[pyfunction]
fn det_consist_take() -> PyResult<Vec<u64>> {
    Ok(engine::sim::det_consist_take())
}

#[pyfunction]
fn det_hit_take() -> PyResult<Vec<u64>> {
    Ok(engine::sim::det_hit_take())
}

/// 学習用: mcts_3v3 を回し、各手番の (手番側, 盤面1037次元, [(行動index, 訪問数)]) を返す。
#[pyfunction]
#[pyo3(signature = (pa, sa, pb, sb, seed, sims, season="M-6", net_b_path="", burn=0, net_a_path=""))]
#[allow(clippy::type_complexity)]
fn mcts_3v3_trace(
    pa: Vec<String>,
    sa: Vec<usize>,
    pb: Vec<String>,
    sb: Vec<usize>,
    seed: i128,
    sims: usize,
    season: &str,
    net_b_path: &str,
    burn: i64,
    net_a_path: &str,
) -> PyResult<(u8, Vec<(usize, Vec<f64>, Vec<(usize, i64)>, f64)>, Vec<(Vec<f64>, f64, Vec<(usize, i64)>)>)> {
    let nb = if net_b_path.is_empty() { None } else { Some(load_net_cached(net_b_path)?) };
    let na = if net_a_path.is_empty() { None } else { Some(load_net_cached(net_a_path)?) };
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, net, .. } = &mut *g;
    let net = na.unwrap_or_else(|| net.clone());
    let (r, recs, nodes) = engine::sim::mcts_3v3_trace(
        pack, &net, nb.as_ref(), &pa, &sa, &pb, &sb, season, season, seed, sims, burn,
    );
    Ok((r as u8, recs, nodes))
}

#[pyfunction]
#[pyo3(signature = (pa, sa, pb, seed, sims, season="M-3"))]
fn mcts_vs_dist(
    pa: Vec<String>,
    sa: Vec<usize>,
    pb: Vec<String>,
    seed: i128,
    sims: usize,
    season: &str,
) -> PyResult<u8> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, net, .. } = &mut *g;
    let net = net.clone();
    Ok(engine::sim::mcts_vs_dist(pack, &net, &pa, &sa, &pb, season, season, seed, sims) as u8)
}

/// mcts_vs_dist のパリティ調査用: (結果, 選出3匹の添字, 各ターンの状態ハッシュ)。
#[pyfunction]
#[pyo3(signature = (pa, sa, pb, seed, sims, season="M-3"))]
fn mcts_vs_dist_trace(
    pa: Vec<String>,
    sa: Vec<usize>,
    pb: Vec<String>,
    seed: i128,
    sims: usize,
    season: &str,
) -> PyResult<(u8, Vec<usize>, Vec<u64>, Vec<String>, Vec<String>, Vec<String>, Vec<String>, Vec<String>, Vec<String>, Vec<String>, Vec<f64>)> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, net, .. } = &mut *g;
    let net = net.clone();
    let (r, idx, hs, nm, vs, ac, rt, cf, ev, dt, xx) =
        engine::sim::mcts_vs_dist_trace(pack, &net, &pa, &sa, &pb, season, season, seed, sims);
    Ok((r as u8, idx, hs, nm, vs, ac, rt, cf, ev, dt, xx))
}

/// パリティ調査用: select_party 直後の共有RNG位置を見る。
#[pyfunction]
#[pyo3(signature = (pa, pb, seed, season="M-3"))]
fn select_party_rng_probe(
    pa: Vec<String>,
    pb: Vec<String>,
    seed: i128,
    season: &str,
) -> PyResult<(Vec<usize>, f64)> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, .. } = &mut *g;
    Ok(engine::sim::select_party_rng_probe(pack, &pa, &pb, season, seed))
}

/// ライブ提案経路のパネル初期化（`_ensemble_surrogate._setup_panel` 相当）。
#[pyfunction]
#[pyo3(signature = (panel_specs, season="M-3"))]
fn live_setup(panel_specs: Vec<Vec<String>>, season: &str) -> PyResult<usize> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, live, .. } = &mut *g;
    let l = engine::live::Live::setup(pack, &panel_specs, season);
    let n = l.panel_net.len();
    *live = Some(l);
    Ok(n)
}

/// 1候補ぶんの中間量。集約(net forward / statistics.mean)は Python 側が行う。
/// 返り値: (states_bytes<f64 LE>, mats_bytes<i64 LE>, spd_a, hp_a, npanel, dim, na, nb)
#[pyfunction]
#[pyo3(signature = (specs, sels=None))]
fn live_feats(
    py: Python<'_>,
    specs: Vec<String>,
    sels: Option<Vec<(Vec<usize>, Vec<usize>)>>,
) -> PyResult<(PyObject, PyObject, Vec<i64>, Vec<i64>, usize, usize, usize, usize)> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let Eng { pack, live, .. } = &mut *g;
    let live = live.as_mut().ok_or_else(|| PyRuntimeError::new_err("live_setup 未実行"))?;
    // 既定（sels 無し）は選出まで Rust で完結（live_set_selector のモデルで学習選出、無ければヒューリスティック）。
    // sels（パネルごとの (自分の選出, パネル側の選出)）を渡すとその選出で符号化する（照合用）
    let states = match &sels {
        Some(s) => live.panel_states_sel(pack, &specs, s),
        None => live.panel_states_full(pack, &specs).0,
    };
    let (spd_a, hp_a, mats) = live.rich_matrices(pack, &specs);
    let npanel = states.len();
    let dim = states.first().map(|v| v.len()).unwrap_or(0);
    let mut sb: Vec<u8> = Vec::with_capacity(npanel * dim * 8);
    for row in &states {
        for v in row {
            sb.extend_from_slice(&v.to_le_bytes());
        }
    }
    let na = specs.len();
    let nb = live.panel_rich.first().map(|p| p.len()).unwrap_or(0);
    let mut mb: Vec<u8> = Vec::with_capacity(mats.len() * (na * nb + nb * na) * 8);
    for (dab, dba) in &mats {
        for v in dab {
            mb.extend_from_slice(&v.to_le_bytes());
        }
        for v in dba {
            mb.extend_from_slice(&v.to_le_bytes());
        }
    }
    Ok((
        pyo3::types::PyBytes::new_bound(py, &sb).into(),
        pyo3::types::PyBytes::new_bound(py, &mb).into(),
        spd_a,
        hp_a,
        npanel,
        dim,
        na,
        nb,
    ))
}

/// 1v1判定（各技の与ダメ・確定数・最短手順・記号）を JSON 文字列で返す。
///
/// 工房・ポケモン情報ページが使う wasm と同じ `analysis::analyze_json` を呼ぶ。
/// 提案API側に判定式を持たせると、記号の刻みや先制技の扱いが片方だけ古くなる
/// （実際に score の刻みが 0.5 と 1 で食い違い、同じ対面で結論が割れていた）。
#[pyfunction]
#[pyo3(signature = (spec_a, spec_b, season="M-3"))]
fn mu_analyze(spec_a: &str, spec_b: &str, season: &str) -> PyResult<String> {
    mu_analyze_scenario(spec_a, spec_b, season, 0, 0, 0, 0)
}

/// 1v1判定の本体。不正な spec は組み立て前にエラーで返し、判定中のパニックも捕まえてエラーにする
/// （パニックのまま抜けるとロックが壊れ、以後の呼び出しが全部失敗する＝提案APIが止まる）。
fn analyze_guarded(g: &mut Eng, spec_a: &str, spec_b: &str, season: &str, sc: engine::pack::Scenario) -> PyResult<String> {
    for sp in [spec_a, spec_b] {
        if let Some(e) = engine::poke::spec_error(&g.pack, sp, season) {
            return Err(PyValueError::new_err(e));
        }
    }
    g.pack.scenario = sc;
    let r = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
        engine::analysis::analyze_json(&mut g.pack, spec_a, spec_b, season).to_string()
    }));
    g.pack.scenario = engine::pack::Scenario::default();
    r.map_err(|e| {
        let msg = e.downcast_ref::<String>().cloned()
            .or_else(|| e.downcast_ref::<&str>().map(|x| x.to_string()))
            .unwrap_or_else(|| "panic".into());
        PyRuntimeError::new_err(format!("mu_analyze: {}", msg))
    })
}

/// 「この状況なら」(天候・フィールド・自分/相手の積み回数)を指定した1v1判定。工房の仮想敵の前提と同じ。
/// 指定はこの呼び出しの間だけ効き、終わったら既定に戻す。weather/terrain の番号は wasm の set_scenario と同じ。
#[pyfunction]
#[pyo3(signature = (spec_a, spec_b, season="M-3", weather=0, terrain=0, boost=0, opp_boost=0))]
fn mu_analyze_scenario(spec_a: &str, spec_b: &str, season: &str, weather: i32, terrain: i32,
                       boost: i32, opp_boost: i32) -> PyResult<String> {
    let m = eng()?;
    let mut g = lock_eng(m);
    let sc = engine::pack::Scenario {
        weather: weather.clamp(0, 4) as u8, terrain: terrain.clamp(0, 4) as u8,
        boost: boost.clamp(0, 6), opp_boost: opp_boost.clamp(0, 6),
    };
    analyze_guarded(&mut g, spec_a, spec_b, season, sc)
}

/// スコアから記号（◎○△▲×）へ。複数型の平均スコアを集約するときに使う。
/// 閾値を Python 側に置くと、片方だけ刻みが古いまま残る。
#[pyfunction]
fn mu_sym(score: f64) -> String {
    engine::analysis::score_sym(score).to_string()
}

#[pyfunction]
fn datapack_hash() -> PyResult<String> {
    let m = eng()?;
    let g = lock_eng(m);
    Ok(g.hash.clone())
}

#[pyfunction]
fn version() -> String {
    format!("pokenavi_engine {} (R5)", env!("CARGO_PKG_VERSION"))
}

#[pymodule]
fn pokenavi_engine(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(greedy_3v3, m)?)?;
    m.add_function(wrap_pyfunction!(belief_probe_take, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_3v3, m)?)?;
    m.add_function(wrap_pyfunction!(det_hit_take, m)?)?;
    m.add_function(wrap_pyfunction!(det_consist_take, m)?)?;
    m.add_function(wrap_pyfunction!(det_slot_take, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_3v3_trace, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_3v3_ab, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_3v3_solve, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_vs_dist, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_vs_dist_trace, m)?)?;
    m.add_function(wrap_pyfunction!(select_party_rng_probe, m)?)?;
    m.add_function(wrap_pyfunction!(predict_probe_take, m)?)?;
    m.add_function(wrap_pyfunction!(learned_select_states, m)?)?;
    m.add_function(wrap_pyfunction!(live_set_selector, m)?)?;
    m.add_function(wrap_pyfunction!(live_panel_selections, m)?)?;
    m.add_function(wrap_pyfunction!(live_setup, m)?)?;
    m.add_function(wrap_pyfunction!(live_feats, m)?)?;
    m.add_function(wrap_pyfunction!(mu_analyze, m)?)?;
    m.add_function(wrap_pyfunction!(mu_analyze_scenario, m)?)?;
    m.add_function(wrap_pyfunction!(mu_sym, m)?)?;
    m.add_function(wrap_pyfunction!(datapack_hash, m)?)?;
    m.add_function(wrap_pyfunction!(version, m)?)?;
    Ok(())
}
