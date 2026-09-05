//! PyO3 モジュール `pokenavi_engine`（R5）。境界は「対戦1回」単位なので marshalling は無視できる。
//!
//! 公開API:
//!   greedy_3v3(pa, sa, pb, sb, seed, season="M-3") -> u8
//!   mcts_3v3(pa, sa, pb, sb, seed, sims, season="M-3") -> u8
//!   mcts_vs_dist(pa, sa, pb, seed, sims, season="M-3") -> u8
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
        engine::sim::mcts_3v3(pack, &net, &pa, &sa, &pb, &sb, season, season, seed, sims, |_, _| {});
    Ok(r as u8)
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
    m.add_function(wrap_pyfunction!(mcts_vs_dist, m)?)?;
    m.add_function(wrap_pyfunction!(live_setup, m)?)?;
    m.add_function(wrap_pyfunction!(live_feats, m)?)?;
    m.add_function(wrap_pyfunction!(datapack_hash, m)?)?;
    m.add_function(wrap_pyfunction!(version, m)?)?;
    Ok(())
}
