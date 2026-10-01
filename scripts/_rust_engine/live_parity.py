"""提案の採点（_ensemble_surrogate）の Rust 経路（_live_rust.live_feats）と Python 経路が一致するか。
候補（既定: 3プールから300党）ごとに、採点の特徴量33次元・採点値、パネル20面の選出（学習選出を Rust 内で）と状態ベクトル（1037次元）を突き合わせる。候補1件あたりの採点時間も出す。
正は Python（採点モデルの学習に使う経路）。許容誤差 1e-9（Rust は中間量だけ返し集約は Python なので本来ビット一致）。
env: N(300) KMG(40) NSTATE(60) STAGE1(=1 で2段階採点の1段目) ENS_MODEL POOL_SEASON(M-6)"""
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
H1 = os.environ.get("STAGE1") == "1"     # 2段階採点の1段目（同じ採点モデル・選出だけヒューリスティック・Rust のスロット1）
e = (ES.EnsembleScorer(L, F._W["net"], PartyGen(), load_threats(L), heuristic=True, slot=1)
     if H1 else ES.EnsembleScorer(L, F._W["net"], PartyGen(), load_threats(L)))
if e._rust is None:
    sys.exit("Rust 経路が無効（ENGINE=rust と pokenavi_engine を確認）")
N = int(os.environ.get("N", "300"))
rng = random.Random(20261001)
C = []
for p in ("eval_evo_M-6.json", "eval_base_M-6.json", "ab_pool_new.json"):
    C += _m6_pool.load_parties(p)
C = [C[i] for i in rng.sample(range(len(C)), min(N, len(C)))]
# 乱数を消費する技（きまぐレーザー）の候補: 抽出した候補の1体を差し替えて作る（env KMG 件、既定40）
_KMG = ["カミツオロチ@たべのこし:ひかえめ:じこさいせい|まもる|きまぐレーザー|だいちのちから:2/0/0/32/32/0:さいせいりょく",
        "ブリジュラス@いのちのたま:ひかえめ:きまぐレーザー|りゅうせいぐん|ラスターカノン|10まんボルト:0/0/0/32/0/32:じきゅうりょく"]
for k in range(int(os.environ.get("KMG", "40"))):
    base = list(C[k % len(C)]); kmg = _KMG[k % 2]; sp = kmg.split("@")[0]
    if any(x.split("@")[0] == sp for x in base):
        continue
    base[k % 6] = kmg
    C.append(base)
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
NS = int(os.environ.get("NSTATE", "60"))
sel_bad = st_bad = st_n = 0
SC = C[:NS] + [c for c in C[NS:] if any("きまぐレーザー" in x for x in c)]   # 乱数を消費する技の候補は全部
for specs in SC:
    A = [build_from_spec(parse_pokemon_spec(s), L, season=os.environ["POOL_SEASON"], randomize=False) for s in specs]
    rs = [(list(a), list(b)) for a, b in E.live_panel_selections(list(specs), e.slot)]
    sb, mb, spd_a, hp_a, npanel, dim, na, nb = E.live_feats(list(specs), None, e.slot)
    X = np.frombuffer(sb, dtype="<f8").reshape(npanel, dim)
    for pi, B in enumerate(e.panel_built):
        ia, ib, x = P3._panel_eval(A, B, pi, heuristic=e.heuristic)
        st_n += 1
        sel_bad += (rs[pi] != (ia, ib))
        st_bad += float(np.abs(X[pi] - np.array(x)).max()) > 1e-9
nk = sum(1 for c in C if any("きまぐレーザー" in x for x in c))
print(("［1段目］" if H1 else "") + f"■ 採点の Rust/Python 一致 {len(C)}候補（うちきまぐレーザー {nk}）: 特徴量 {len(C)-bad_x}/{len(C)}・採点値 {len(C)-bad_s}/{len(C)}（最大差 {maxd:.2e}）"
      f"・パネルの選出 {st_n-sel_bad}/{st_n}・状態ベクトル {st_n-st_bad}/{st_n}（{len(SC)}候補）"
      + ("  ✓" if not (bad_x or bad_s or st_bad or sel_bad) else "  ✗")
      + f"（候補1件 Rust {tr/len(C)*1000:.0f}ms / Python {tp/len(C)*1000:.0f}ms）")
sys.exit(1 if (bad_x or bad_s or st_bad or sel_bad) else 0)
