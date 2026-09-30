"""提案の採点（_ensemble_surrogate）の Rust 経路（_live_rust.live_feats）と Python 経路が一致するか。
候補（既定: 3プールから300党）ごとに、採点の特徴量33次元・採点値、パネル20面の状態ベクトル（1037次元、選出は学習選出）を突き合わせる。候補1件あたりの採点時間も出す。
正は Python（採点モデルの学習に使う経路）。許容誤差 1e-9（Rust は中間量だけ返し集約は Python なので本来ビット一致）。
env: N(300) ENS_MODEL POOL_SEASON(M-6)"""
import os, sys, random
os.environ.setdefault("POOL_SEASON", "M-6"); os.environ.setdefault("OMP_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
import feature1 as F
F._ensure_loaded(os.environ["POOL_SEASON"], 8)
from gen_party_pool import PartyGen
from _threat_coverage import load_threats
import _ensemble_surrogate as ES, _product3 as P3, _m6_pool
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.ai import select_party
from simulator.battle import BattleSide, BattleField
from simulator.belief import OpponentBelief
from simulator.features import encode_state

L = F._W["loader"]
e = ES.EnsembleScorer(L, F._W["net"], PartyGen(), load_threats(L))
if e._rust is None:
    sys.exit("Rust 経路が無効（ENGINE=rust と pokenavi_engine を確認）")
N = int(os.environ.get("N", "300"))
rng = random.Random(20261001)
C = []
for p in ("eval_evo_M-6.json", "eval_base_M-6.json", "ab_pool_new.json"):
    C += _m6_pool.load_parties(p)
C = [C[i] for i in rng.sample(range(len(C)), min(N, len(C)))]
bad_x = bad_s = bad_state = 0; maxd = 0.0
import time as _t
tr = tp = 0.0
for k, specs in enumerate(C):
    t0 = _t.perf_counter(); xr = e._x(specs); tr += _t.perf_counter() - t0
    r = e._rust; e._rust = None
    t0 = _t.perf_counter(); xp = e._x(specs); tp += _t.perf_counter() - t0
    e._rust = r
    d = float(np.abs(xr - xp).max()); maxd = max(maxd, d)
    bad_x += d > 1e-9
    bad_s += abs(float((np.hstack([[1.0], (xr - e.mu) / e.sd]) - np.hstack([[1.0], (xp - e.mu) / e.sd])) @ e.w)) > 1e-9
import pokenavi_engine as E
st_bad = 0; st_n = 0
for specs in C[:30]:
    A = [build_from_spec(parse_pokemon_spec(s), L, season=os.environ["POOL_SEASON"], randomize=False) for s in specs]
    sels = P3.panel_selections(A)                      # 採点の選出＝学習選出（2026-10-01〜）
    sb, mb, spd_a, hp_a, npanel, dim, na, nb = E.live_feats(list(specs), sels)
    X = np.frombuffer(sb, dtype="<f8").reshape(npanel, dim)
    for pi, B in enumerate(P3._W["panel"]):
        sa = [A[i] for i in sels[pi][0]]; sbb = [B[i] for i in sels[pi][1]]
        s1 = BattleSide(sa, source6=A); s2 = BattleSide(sbb, source6=B)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        st_n += 1
        st_bad += float(np.abs(X[pi] - np.array(encode_state(s1, s2, BattleField()))).max()) > 1e-9
print(f"■ 採点の Rust/Python 一致 {len(C)}候補: 特徴量 {len(C)-bad_x}/{len(C)}・採点値 {len(C)-bad_s}/{len(C)}（最大差 {maxd:.2e}）"
      f"・パネルの状態ベクトル {st_n-st_bad}/{st_n}" + ("  ✓" if not (bad_x or bad_s or st_bad) else "  ✗")
      + f"（候補1件 Rust {tr/len(C)*1000:.0f}ms / Python {tp/len(C)*1000:.0f}ms）")
sys.exit(1 if (bad_x or bad_s or st_bad) else 0)
