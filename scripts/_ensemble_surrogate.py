"""アンサンブル勝率サロゲート（ネットt0パネル＋リッチ守備＋構築）。
train()で総当たり300体から学習・保存。EnsembleScorerで候補を採点（Product3サーバ用）。
"""
import os, json, glob, random, statistics
import numpy as np
import feature1 as _f1
from simulator.battle import BattleField
from simulator.ai import _effective_speed
import _matchup_surrogate as M
import _product3 as P3
from _surrogate import features as confeat
from gen_party_pool import PartyGen
from _threat_coverage import load_threats
import _live_rust as _LR

# シーズン対応。M-6は総当たり記録が別ディレクトリになるので学習元とモデル出力を切り替える。
# 既定は従来どおり M-3 のコーパス・モデル（既存の呼び出しは無変更で動く）。
TRAIN_SEASON = os.environ.get("TRAIN_SEASON", "M-3")
CACHE_GLOB = os.environ.get("TRAIN_CACHE_GLOB",
                            "f1_cache_m3/*.json" if TRAIN_SEASON == "M-3"
                            else f"f1_cache_{TRAIN_SEASON.lower().replace('-','')}/*.json")
MODEL = os.path.join(os.path.dirname(__file__),
                     os.environ.get("ENS_MODEL", "ensemble_model.json"))

def _feats(specs, L, net, pg, th, field, panel_mons, spd):
    ns = P3.surrogate_score(specs)                 # ネットt0パネル（P3._W panel使用）
    A = M.build_party(specs, L)
    for mo in A: spd[id(mo)] = _effective_speed(mo, field)
    fs = [M.matchup_feats(A, B, field, spd) for B in panel_mons]
    rich = [statistics.mean(c) for c in zip(*fs)]
    con = confeat(specs, L, pg, th)
    return [ns] + list(rich) + list(con)

def _setup_panel(L, net, panel_specs, field):
    P3._score_setup(L, net, panel_specs)
    panel_mons = [M.build_party(sp, L) for sp in panel_specs]
    spd = {}
    for pm in panel_mons:
        for mo in pm: spd[id(mo)] = _effective_speed(mo, field)
    return panel_mons, spd

def train():
    _f1._ensure_loaded(TRAIN_SEASON, 8); L = _f1._W["loader"]; net = _f1._W["net"]
    pg = PartyGen(); th = load_threats(L); field = BattleField()
    files = sorted(glob.glob(os.path.join(os.path.dirname(__file__), CACHE_GLOB)))
    files = [f for f in files if not os.path.basename(f).startswith("_")]   # _state.json 等を除く
    extra = os.environ.get("EXTRA_CACHE_GLOB")   # 例: f1_cache_m3top/*.json（M-3実上位構築の総当たり）
    if extra:
        ef = sorted(glob.glob(os.path.join(os.path.dirname(__file__), extra)))
        files = files + ef
        print(f"追加学習データ: {len(ef)}件（{extra}）", flush=True)
    specs = []; y = []
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        w = sum(c.get("wins", 0) for c in d["cards"]); l = sum(c.get("losses", 0) for c in d["cards"])
        specs.append(d["subject_party"]); y.append(w / max(1, w + l))
    y = np.array(y)
    _pn = int(os.environ.get("PANEL_N", "20"))
    rng = random.Random(0); panel_specs = [specs[i] for i in rng.sample(range(len(specs)), _pn)]
    panel_mons, spd = _setup_panel(L, net, panel_specs, field)
    print(f"特徴計算 {len(specs)}体...", flush=True)
    X = np.array([_feats(sp, L, net, pg, th, field, panel_mons, spd) for sp in specs])
    mu = X.mean(0); sd = X.std(0) + 1e-9; Xs = np.hstack([np.ones((len(y), 1)), (X - mu) / sd])
    lam = 3.0
    w = np.linalg.solve(Xs.T @ Xs + lam * np.eye(Xs.shape[1]), Xs.T @ y)
    # 学習内相関(参考)
    r = np.corrcoef(Xs @ w, y)[0, 1]
    json.dump({"panel": panel_specs, "mu": mu.tolist(), "sd": sd.tolist(), "w": w.tolist(),
               "nfeat": int(X.shape[1])}, open(MODEL, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"保存: {MODEL}  特徴{X.shape[1]}次元  学習内r={r:.3f}")

class EnsembleScorer:
    def __init__(self, L, net, pg, th):
        self.L, self.net, self.pg, self.th = L, net, pg, th
        self.field = BattleField()
        m = json.load(open(MODEL, encoding="utf-8"))
        self.mu = np.array(m["mu"]); self.sd = np.array(m["sd"]); self.w = np.array(m["w"])
        self.panel_mons, self.spd = _setup_panel(L, net, m["panel"], self.field)
        # ENGINE=rust のときだけネイティブ経路（無効・失敗時は None＝従来の純Python経路）
        self._rust = _LR.setup(m["panel"])
        if self._rust is not None:
            self._pspd = [[self.spd[id(mo)] for mo in pm] for pm in self.panel_mons]
            self._php = [[mo.max_hp for mo in pm] for pm in self.panel_mons]

    def _x(self, specs):
        """33次元の生特徴。Rust経路が有効ならネット/リッチ部分だけネイティブ計算（集約はPython）。"""
        if self._rust is not None:
            try:
                nr = _LR.feats(self._rust, specs, self.net, self._pspd, self._php)
                return np.array(nr + list(confeat(specs, self.L, self.pg, self.th)))
            except _LR.NeedsPython:
                pass          # この候補だけ Python 経路（Rustは有効のまま）
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException as e:
                import engine_dispatch as _ED
                _LR.ERRORS.append((list(specs), repr(e)))
                _ED._warn("live:exc", f"live_feats 実行時例外: {e} → 以後Python経路")
                self._rust = None
        return np.array(_feats(specs, self.L, self.net, self.pg, self.th, self.field, self.panel_mons, self.spd))

    def score(self, specs):
        x = self._x(specs)
        xs = np.hstack([[1.0], (x - self.mu) / self.sd])
        return float(xs @ self.w)

    def breakdown(self, specs):
        """スコアを ネット / 火力(リッチ) / 構築 の寄与に分解。1(net)+12(rich)+20(con)=33次元。"""
        x = self._x(specs)
        contrib = self.w[1:] * ((x - self.mu) / self.sd)   # 各特徴の寄与（重み×標準化値）
        net = float(contrib[0]); rich = float(contrib[1:13].sum()); con = float(contrib[13:].sum())
        return {"total": round(float(self.w[0] + contrib.sum()), 3),
                "net": round(net, 3), "rich": round(rich, 3), "con": round(con, 3)}

if __name__ == "__main__":
    train()
