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
use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;
use std::sync::{Mutex, OnceLock};

struct Eng {
    pack: Pack,
    net: NetW,
    hash: String,
    live: Option<engine::live::Live>,
}

static ENG: OnceLock<Mutex<Eng>> = OnceLock::new();

fn datapack_path() -> String {
    std::env::var("POKENAVI_DATAPACK").unwrap_or_else(|_| "_rust_engine/datapack.json".to_string())
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
    let _ = ENG.set(Mutex::new(Eng { pack, net, hash, live: None }));
    Ok(ENG.get().unwrap())
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
    let mut g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
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
    let mut g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
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
    let mut c = NET_CACHE.lock().map_err(|_| PyRuntimeError::new_err("net cache lock"))?;
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
#[pyo3(signature = (pa, sa, pb, sb, seed, sims, net_a_path="", net_b_path="", season="M-6"))]
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
) -> PyResult<u8> {
    let na = if net_a_path.is_empty() { None } else { Some(load_net_cached(net_a_path)?) };
    let nb = if net_b_path.is_empty() { None } else { Some(load_net_cached(net_b_path)?) };
    let m = eng()?;
    let mut g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
    let Eng { pack, net, .. } = &mut *g;
    let base = net.clone();
    let side1 = na.as_ref().unwrap_or(&base);
    let side2 = nb.as_ref().unwrap_or(&base);
    let (r, _) = engine::sim::mcts_3v3(
        pack, side1, Some(side2), &pa, &sa, &pb, &sb, season, season, seed, sims, |_, _| {},
    );
    Ok(r as u8)
}

/// 学習用: mcts_3v3 を回し、各手番の (手番側, 盤面1037次元, [(行動index, 訪問数)]) を返す。
#[pyfunction]
#[pyo3(signature = (pa, sa, pb, sb, seed, sims, season="M-6"))]
#[allow(clippy::type_complexity)]
fn mcts_3v3_trace(
    pa: Vec<String>,
    sa: Vec<usize>,
    pb: Vec<String>,
    sb: Vec<usize>,
    seed: i128,
    sims: usize,
    season: &str,
) -> PyResult<(u8, Vec<(usize, Vec<f64>, Vec<(usize, i64)>, f64)>, Vec<(Vec<f64>, f64, Vec<(usize, i64)>)>)> {
    let m = eng()?;
    let mut g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
    let Eng { pack, net, .. } = &mut *g;
    let net = net.clone();
    let (r, recs, nodes) = engine::sim::mcts_3v3_trace(
        pack, &net, &pa, &sa, &pb, &sb, season, season, seed, sims,
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
    let mut g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
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
    let mut g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
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
    let mut g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
    let Eng { pack, .. } = &mut *g;
    Ok(engine::sim::select_party_rng_probe(pack, &pa, &pb, season, seed))
}

/// ライブ提案経路のパネル初期化（`_ensemble_surrogate._setup_panel` 相当）。
#[pyfunction]
#[pyo3(signature = (panel_specs, season="M-3"))]
fn live_setup(panel_specs: Vec<Vec<String>>, season: &str) -> PyResult<usize> {
    let m = eng()?;
    let mut g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
    let Eng { pack, live, .. } = &mut *g;
    let l = engine::live::Live::setup(pack, &panel_specs, season);
    let n = l.panel_net.len();
    *live = Some(l);
    Ok(n)
}

/// 1候補ぶんの中間量。集約(net forward / statistics.mean)は Python 側が行う。
/// 返り値: (states_bytes<f64 LE>, mats_bytes<i64 LE>, spd_a, hp_a, npanel, dim, na, nb)
#[pyfunction]
#[pyo3(signature = (specs))]
fn live_feats(
    py: Python<'_>,
    specs: Vec<String>,
) -> PyResult<(PyObject, PyObject, Vec<i64>, Vec<i64>, usize, usize, usize, usize)> {
    let m = eng()?;
    let mut g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
    let Eng { pack, live, .. } = &mut *g;
    let live = live.as_mut().ok_or_else(|| PyRuntimeError::new_err("live_setup 未実行"))?;
    let states = live.panel_states(pack, &specs);
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
    let m = eng()?;
    let mut g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
    let v = engine::analysis::analyze_json(&mut g.pack, spec_a, spec_b, season);
    Ok(v.to_string())
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
    let g = m.lock().map_err(|_| PyRuntimeError::new_err("engine lock"))?;
    Ok(g.hash.clone())
}

#[pyfunction]
fn version() -> String {
    format!("pokenavi_engine {} (R5)", env!("CARGO_PKG_VERSION"))
}

#[pymodule]
fn pokenavi_engine(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(greedy_3v3, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_3v3, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_3v3_trace, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_3v3_ab, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_vs_dist, m)?)?;
    m.add_function(wrap_pyfunction!(mcts_vs_dist_trace, m)?)?;
    m.add_function(wrap_pyfunction!(select_party_rng_probe, m)?)?;
    m.add_function(wrap_pyfunction!(live_setup, m)?)?;
    m.add_function(wrap_pyfunction!(live_feats, m)?)?;
    m.add_function(wrap_pyfunction!(mu_analyze, m)?)?;
    m.add_function(wrap_pyfunction!(mu_sym, m)?)?;
    m.add_function(wrap_pyfunction!(datapack_hash, m)?)?;
    m.add_function(wrap_pyfunction!(version, m)?)?;
    Ok(())
}
