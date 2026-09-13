"""Product3 ローカル製品：コア入力→残り枠補完→サロゲート提案。
モデル常駐のHTTPサーバ＋簡易UI。 起動: venv/bin/python product3_server.py  → http://localhost:8899
"""
import os, numpy as np, json, random, html, glob, threading, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("GA_SIMS", os.environ.get("SIM_SIMS", "150"))   # ライブ実戦テストのMCTS探索数（軽め）
import multiprocessing as mp
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import feature1 as _f1
from gen_party_pool import PartyGen, _spec_mega, _item_of
from _threat_coverage import load_threats, team_coverage, team_depth
import _product3 as P3
from _product3_complete import complete_core, resolve_fixed, complete_core_free
from _ensemble_surrogate import EnsembleScorer
from simulator.pokemon import build_from_spec, parse_pokemon_spec
import _explain as EX

PORT = int(os.environ.get("PORT", "8899"))
EVK = ["H", "A", "B", "C", "D", "S"]

print("モデル読込中...", flush=True)
# シーズンは POOL_SEASON に追従（M-6移行時にM-3固定だと種テンプレート・アーキタイプが旧環境のままになる）
SEASON = os.environ.get("POOL_SEASON", "M-3")
_f1._ensure_loaded(SEASON, 8)
L = _f1._W["loader"]; NET = _f1._W["net"]
PG = PartyGen(); TH = load_threats(L)
ENS = EnsembleScorer(L, NET, PG, TH)   # アンサンブル(ネット+リッチ守備+構築, CV r≈0.69)
SPECIES = [p for p, _ in sorted(PG.rank.items(), key=lambda x: x[1]) if p in PG.pokes]

_CALIB = None
try:
    _cf = os.path.join(os.path.dirname(__file__), "calib_net.json")
    _cd = json.load(open(_cf, encoding="utf-8")); _CALIB = (_cd["x"], _cd["y"])
    print(f"較正ロード: {len(_CALIB[0])}点（生評価→実勝率）", flush=True)
except FileNotFoundError:
    pass

def calibrate(v):
    """価値ネットの生評価を総当たり実勝率にキャリブレーション（単調線形補間）。"""
    if not _CALIB: return v
    xs, ys = _CALIB
    if v <= xs[0]: return ys[0]
    if v >= xs[-1]: return ys[-1]
    for i in range(1, len(xs)):
        if v <= xs[i]:
            t = (v - xs[i - 1]) / (xs[i] - xs[i - 1] or 1)
            return ys[i - 1] + t * (ys[i] - ys[i - 1])
    return ys[-1]

_ARCH_FILE = os.path.join(os.path.dirname(__file__),
                          os.environ.get("ARCH_FILE",
                                         f"archetypes_{os.environ.get('POOL_SEASON','M-3').lower().replace('-','')}.json"))

def _scan_archetypes(n=8):
    """総当たり実勝率(5.5GB)から、メガ軸が重複しない代表アーキタイプをn個抽出（devのみ）。"""
    files = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "f1_cache_m3/*.json")))
    rows = []
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        w = sum(c.get("wins", 0) for c in d["cards"]); l = sum(c.get("losses", 0) for c in d["cards"])
        rows.append((w / max(1, w + l), d["subject_party"]))
    rows.sort(key=lambda x: -x[0])
    picked, sigs = [], set()
    for wr, p in rows:
        names = [s.split("@")[0] for s in p]
        megas = tuple(sorted(nm for nm, s in zip(names, p) if _spec_mega(s)))
        if megas in sigs: continue
        sigs.add(megas)
        label = ("＋".join(megas) + "軸") if megas else (names[0] + "軸")
        picked.append({"party": p, "names": names, "label": label, "wr": round(wr, 3)})
        if len(picked) >= n: break
    return picked

def _load_archetypes(n=8):
    """事前計算した小さなJSONを優先ロード。無ければ5.5GBを走査してキャッシュ生成（本番は前者のみ）。"""
    if os.path.exists(_ARCH_FILE):
        meta = json.load(open(_ARCH_FILE, encoding="utf-8"))[:n]
    elif SEASON == "M-3":
        meta = _scan_archetypes(n)
        json.dump(meta, open(_ARCH_FILE, "w", encoding="utf-8"), ensure_ascii=False)
        print(f"アーキタイプを {os.path.basename(_ARCH_FILE)} に事前計算保存", flush=True)
    else:
        # M-3以外は総当たり記録(f1_cache_m3)が無い。黙ってM-3盤面を使うと想定相手が
        # 旧環境のままになり、pick_rates(必然性リペアの基準)まで狂う。
        raise SystemExit(f"{os.path.basename(_ARCH_FILE)} が無い（{SEASON}用アーキタイプを先に作成）")
    for a in meta:
        a["built"] = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in a["party"]]
    return meta

ARCHES = _load_archetypes(8)
print(f"アーキタイプ盤面 {len(ARCHES)}個: {[a['label'] for a in ARCHES]}", flush=True)

def _xy_suffix(stone):
    if stone.endswith(("X", "Ｘ")): return "X"
    if stone.endswith(("Y", "Ｙ")): return "Y"
    return ""

def _variants(sp):
    """種の選べる型。メガは『メガ○○』(X/Y付き)、非メガ型があれば素の種名も。メガ前提種はメガのみ。
    低使用率メガ(実使用率<MIN_MEGA_USAGE%)はPartyGen側で既にpg.mega/pg.poolから除外済みなので、
    ここではpg.poolの中身をそのまま見ればよい。"""
    blds = PG.pool.get(sp) or []
    stones, has_nm = [], False
    for s in blds:
        if _spec_mega(s):
            st = _item_of(s)
            if st not in stones: stones.append(st)
        else:
            has_nm = True
    opts = [{"label": f"メガ{sp}{_xy_suffix(st)}", "sp": sp, "mega": st} for st in stones]
    if has_nm:
        opts.append({"label": sp, "sp": sp, "mega": ""})
    if not opts:
        opts.append({"label": sp, "sp": sp, "mega": None})
    return opts

VARIANTS = []
for sp in SPECIES:
    rk = PG.rank.get(sp, 9999)
    for v in _variants(sp):
        v["rank"] = rk
        VARIANTS.append(v)
print(f"準備完了。種{len(SPECIES)} 選択肢{len(VARIANTS)} / http://localhost:{PORT}", flush=True)

def _cpu_avail():
    try:
        return len(os.sched_getaffinity(0))   # cgroup/affinity準拠（コンテナのCPU割当を尊重）
    except (AttributeError, OSError):
        return os.cpu_count() or 2

# WORKERS env 優先。無ければ割当CPU-1（コンテナでは os.cpu_count がホスト全コアを返しがちなので affinity 基準）
_WORKERS = int(os.environ.get("WORKERS") or 0) or max(1, _cpu_avail() - 1)
print(f"並列ワーカー数 _WORKERS={_WORKERS} (cpu_avail={_cpu_avail()}, cpu_count={os.cpu_count()})", flush=True)
_POOL = None

def _get_pool():
    """永続forkプール（起動後モデル込みで1回だけfork→毎リクエストのfork overheadを回避）。
    重い処理は _HEAVY_LOCK で直列化されるため単一プールの共有で安全。"""
    global _POOL
    if _POOL is None:
        _POOL = mp.get_context("fork").Pool(_WORKERS)
    return _POOL

def _score_one(spec):
    return (ENS.score(spec), spec)

# 脅威カバーの「厚み」を選抜スコアに混ぜる仕組み。【実対戦A/Bで不採用・既定0のまま】
# 観察上の相関は本物: ガイド勝率との相関は 厚み+0.257 > ENS+0.180 > 二値の対応率+0.134、
# 同一軸5案内の順位相関でも 厚み+0.269 > ENS+0.166、両者の相関は+0.152で独立な情報だった。
# しかし実対戦A/Bは再現しない: 1回目(パネル20/シード900M帯/n=38) +3.38pt(z=+2.87) に対し、
# 2回目(パネル16/シード910M帯/n=30) は -0.26pt(z=-0.22)。「厚みのみ」で選ぶと -2.89pt(z=-2.10)と有意に悪化。
# 解釈: 相関は「強いパーティはたまたま厚みも高い」という共変関係で、直接最適化すると
# その外側（厚みは高いが弱い構成）を掴む。副作用として多様性も低下（異なり種数13.10→12.30）。
# メガ数較正(2026-07-12)と同型の失敗。DEPTH_W>0 にする場合は必ず実対戦A/Bを再取得すること。
DEPTH_W = float(os.environ.get("DEPTH_W", "0"))
_ENS_B, _DEP_B = 0.144, 0.235

def _mega_weak_shared(specs, fixnames=()):
    """パーティの『固定の主力』同士が揃って苦手とするタイプ数（型相性のみ・軽い）。

    当初はメガ2体同士の弱点重複だけを見ていたが、それだと
    「非メガの軸種（例: 素のセグレイブ）とメガ1体（例: メガガブリアスZ）」の
    ドラゴン被りを検出できなかった（両者ともドラゴンで弱点セットも大半が重なるのに、
    軸種はmegaフラグが立たないため比較対象から漏れる）。
    軸に固定された種はメガ以上に『動かせない枠』なので、主力＝mega=True の種 ∪
    軸固定(core)の種として、その中の最大ペア重複を見る。"""
    from _party_quality import mon_profile
    anchors = [s for s in specs if _spec_mega(s) or s.split("@", 1)[0] in fixnames]
    if len(anchors) < 2:
        return 0
    profs = [mon_profile(s, L)[1] for s in anchors]   # 弱点タイプ集合のみ
    best = 0
    for i in range(len(profs)):
        for j in range(i + 1, len(profs)):
            best = max(best, len(profs[i] & profs[j]))
    return best

# メガ2枚の弱点重複ペナルティ。共有弱点タイプ1つにつきENSスコアから引く。
# 既定0＝無効（従来と完全に同一挙動）。深さ加重・メガ数較正と同じ形の実験的ノブなので、
# 有効化する場合は必ず実対戦A/Bで確認してから既定を変える（このファイルの先例を踏襲）。
MEGA_OVERLAP_W = float(os.environ.get("MEGA_OVERLAP_W", "0"))

# 生成する候補パーティ数の下限。0＝無効（要求値をそのまま使う・従来と同一挙動）。
SUGGEST_NCAND = int(os.environ.get("SUGGEST_NCAND", "0"))


def _rerank(scored):
    """(ENSスコア, party) の列を、厚みを混ぜた順に並べ替える。DEPTH_W=0 なら元の順序のまま。"""
    if DEPTH_W <= 0 or len(scored) < 3:
        return sorted(scored, key=lambda x: -x[0])
    e = np.array([sc for sc, _ in scored], dtype=float)
    dp = np.array([team_depth(p, L, TH)[0] for _, p in scored], dtype=float)
    def _z(v):
        sd = v.std()
        return (v - v.mean()) / sd if sd > 1e-12 else np.zeros_like(v)
    comb = _ENS_B * _z(e) + DEPTH_W * _DEP_B * _z(dp)
    return [scored[i] for i in np.argsort(-comb)]


def _mega_adjusted(scored, fixnames=()):
    """{id(party): メガ弱点ペナルティ適用後スコア} を返す。表示用のスコアは生のまま保つ。

    _apply_mega_overlap_penalty は「並べ替える」だけでタプル内のスコアは書き換えないため、
    MMR選抜のように生スコアで再ランキングする経路ではペナルティが素通りしていた
    （MEGA_OVERLAP_W を0.05〜0.20で振っても提案が1件も変わらない、という形で表面化した）。
    順序ではなく値として渡す必要がある。"""
    if MEGA_OVERLAP_W <= 0:
        return {}
    return {id(p): sc - MEGA_OVERLAP_W * _mega_weak_shared(p, fixnames) for sc, p in scored}


def _apply_mega_overlap_penalty(scored, fixnames=()):
    """MEGA_OVERLAP_W>0 のときだけ、共有弱点タイプ数×係数をENSスコアから引いて並べ替える。
    _rerank の後・_cap_select の前に置く（並べ替え結果を最終選抜に反映させるため）。"""
    if MEGA_OVERLAP_W <= 0:
        return scored
    return sorted(scored, key=lambda x: -(x[0] - MEGA_OVERLAP_W * _mega_weak_shared(x[1], fixnames)))


def _par_score(cands):
    """候補のENSスコアをCPU並列で計算（fork継承でネットは共有・ピクル不要）。"""
    if len(cands) < 8:
        return [_score_one(p) for p in cands]
    return _get_pool().map(_score_one, cands, chunksize=4)

# メガ数較正は実測A/Bで不採用（2026-07-12）: 候補プールは実119構築の2メガ率84%とほぼ一致[82-91%]なのに
# ENS順位のtop5では約54%まで下がる。層化選出(2メガ84%へ強制)を実装し検証したが、
# 実対戦A/B 43.5%(20-26/48)で有意に敗北＝「実プレイヤーの構成比に寄せる」ことは強さの改善にならず、
# 総当たり実勝率データ(1メガ0.502/2メガ0.495・ほぼ拮抗)と整合。ENSのtop5選好は測定として正しい。
# 教訓: 母集団分布との一致は目的ではなく手段。効果は必ず実対戦A/Bで確認してから採用する。

def _proposal_detail(args):
    """1提案ぶんの詳細（役割・想定勝率・相性・統計）を組み立てる。fork並列用にモジュール関数化。"""
    sc, p, fixnames = args
    mons = []
    for s in p:
        hd, rest = s.split("@", 1); it, na, mv, ev, ab = rest.split(":")
        evs = " ".join(f"{k}{v}" for k, v in zip(EVK, ev.split("/")) if v != "0")
        mons.append({"name": hd, "item": it, "nature": na, "ability": ab, "ev": evs,
                     "moves": mv.split("|"), "mega": _spec_mega(s), "core": hd in fixnames,
                     "roles": EX.role_of(s, L)})
    arch = []
    for a in ARCHES:
        v, pick = P3.eval_vs_built(p, a["built"])
        arch.append({"label": a["label"], "opp": a["names"], "wr": a["wr"],
                     "adv": round(calibrate(v), 4), "pick": pick})
    return {"score": round(sc, 3), "coverage": round(team_coverage(p, L, TH)[0], 2),
            "specs": p, "mons": mons, "stats": EX.party_stats(p, L, PG, TH), "matchup": EX.matchup_grid(p, L),
            "details": EX.stat_details(p, L, TH), "archetypes": arch,
            "speed": EX.speed_info(p, L)}

_SCACHE = {}   # 提案は決定的（固定シード＋温度0の貪欲選出）なので軸ごとに結果をキャッシュ
_SCACHE_FILE = os.path.join(os.path.dirname(__file__), "suggest_cache.json")
try:
    for _k, _v in json.load(open(_SCACHE_FILE, encoding="utf-8")).items():
        _SCACHE[_k] = _v
    print(f"提案キャッシュ事前ロード: {len(_SCACHE)}件（人気軸）", flush=True)
except FileNotFoundError:
    pass

# 選出ガイド（バッチが焼き上げ済みのコアのみ・全240コア完了前でも計算済み分から段階的に同梱可）。
# ファイルが無ければ何もしない＝未焼成コアは従来通りguide/strategyキー無し（UIは「準備中」表示）。
_SGUIDE_FILE = os.path.join(os.path.dirname(__file__), "suggest_cache_guided_s.json")
try:
    _n_guided = 0
    for _k, _v in json.load(open(_SGUIDE_FILE, encoding="utf-8")).items():
        _SCACHE[_k] = _v; _n_guided += 1
    print(f"選出ガイドオーバーレイ: {_n_guided}件", flush=True)
except FileNotFoundError:
    pass

# 提案多様性キャップ: top選択時に「非コア種が SUGGEST_CAP 提案を超えて出現する案」を飛ばす。
# 既定0＝無効（従来と完全に同一挙動・キャッシュキーも不変）。1以上でキャップ有効＋キーに値を混ぜる
# （＝キャップ有無のエントリがキャッシュ内で混ざらない）。実対戦A/Bの根拠は _divdiag/gate_run*.log。
SUGGEST_CAP = int(os.environ.get("SUGGEST_CAP", "0"))

# 5提案内の多様性を「提案どうしの似かた」で直接制御する選抜。0＝無効（従来のキャップ方式）。
# キャップは種ごとの出現回数を数えるだけなので、上限に達した瞬間その種を含む候補を全部弾き、
# 良い候補を大量に捨てる。MMRは提案間のメンバー重複率を見るので、同じ種が入っていても
# 他が違えば許容でき、無駄に捨てない。
# 全21軸の実測（同一候補で比較・M-6）:
#   cap3(現行) 異なり13.6種/重複34%/score0.600
#   cap2       異なり14.8種/重複29%/score0.582
#   MMR 0.5    異なり16.7種/重複24%/score0.598  ← 多様性を上げてscoreはほぼ無傷
#   MMR 0.7    異なり17.7種/重複19%/score0.574
SUGGEST_MMR = float(os.environ.get("SUGGEST_MMR", "0"))
# MMRで多様性のために拾う候補の下限。トップ案のスコアからこの割合まで落ちる案は採らない。
# 下限なしだと、多様性を稼ぐために極端に弱い案（実測でトップ0.729に対し0.434）が混ざる。
SUGGEST_MMR_FLOOR = float(os.environ.get("SUGGEST_MMR_FLOOR", "0.80"))


def _mmr_select(scored, fixnames, top, lam, base=None):
    """スコア −(λ×既選択との最大メンバー重複率) で貪欲に top 本選ぶ。
    重複率は非軸メンバー集合のJaccard的な比（|共通|/|候補の非軸数|）。
    base は {id(party): 補正済みスコア}（メガ弱点ペナルティ等）。省略時は生スコア。"""
    base = base or {}
    sel, sets, pool = [], [], list(scored)
    # 足切り: トップ案のスコア×SUGGEST_MMR_FLOOR を下回る候補は多様性目的でも採らない。
    # ただし足切り後に top 本に満たない場合は、足りない分だけ元の順で補充する。
    top_sc = max((sc for sc, _ in scored), default=0.0)
    floor = top_sc * SUGGEST_MMR_FLOOR if top_sc > 0 else float("-inf")
    pool_ok = [(sc, p) for sc, p in pool if sc >= floor]
    if len(pool_ok) >= top:
        pool = pool_ok
    while len(sel) < top and pool:
        best = None
        for i, (sc, p) in enumerate(pool):
            nm = {x.split("@", 1)[0] for x in p if x.split("@", 1)[0] not in fixnames}
            ov = max((len(nm & s) / max(1, len(nm)) for s in sets), default=0.0)
            adj = base.get(id(p), sc) - lam * ov
            if best is None or adj > best[0]:
                best = (adj, i, sc, p, nm)
        _, i, sc, p, nm = best
        sel.append((sc, p)); sets.append(nm); pool.pop(i)
    # 提示順はスコア降順に戻す。MMRの採用順のままだと「1位より下に高スコア案がある」
    # 見た目になり（実測 0.729→0.545→0.434→0.632→0.728）、利用者を混乱させる。
    return sorted(sel, key=lambda x: -x[0])

# メガ枠だけを対象にした多様性キャップ。0＝無効。
# 種キャップ(SUGGEST_CAP)/MMRはどちらも「取り巻き」の入れ替えに効いてしまい、
# 5提案の相棒メガが同じペアで固定される偏り（実測: Mグソクムシャ軸で5本中3本が同一ペア）は
# 崩せなかった。取り巻きの重複は許容してよいので、メガ種の出現回数だけを直接数える。
SUGGEST_MEGA_CAP = int(os.environ.get("SUGGEST_MEGA_CAP", "0"))


def _mega_cap_select(scored, fixnames, mcap, top):
    """ENS降順に貪欲採用。非コアのメガ種の採用回数が mcap を超える案はスキップ。
    top本に満たなければ制約を無視してスコア順に補充（必ず top 本返す）。"""
    sel, cnt = [], {}
    for sc, p in scored:
        mg = [x.split("@", 1)[0] for x in p
              if _spec_mega(x) and x.split("@", 1)[0] not in fixnames]
        if any(cnt.get(n, 0) >= mcap for n in mg):
            continue
        sel.append((sc, p))
        for n in mg:
            cnt[n] = cnt.get(n, 0) + 1
        if len(sel) == top:
            break
    if len(sel) < top:
        chosen = {id(p) for _, p in sel}
        for sc, p in scored:
            if len(sel) == top:
                break
            if id(p) not in chosen:
                sel.append((sc, p))
    return sel[:top]

# メガの「組み合わせ」キャップ。0＝無効。同一のメガ構成（非コアメガ種の集合）が
# この回数を超えて現れる案をスキップする。
# 種ごとの回数を数える SUGGEST_MEGA_CAP では、1提案がメガを2体消費する構造に対応できない。
# 実測（パーモット軸・megacap=1）: #1がMガブ+Mグソク、#2がMボーマンダ+Mルカリオで上位4種を使い切り、
# 残るMセグレイブを含む候補14件は全てMガブ/Mグソクと同居していたため全スキップ、
# 結果 Mピクシー+Mキラフロル(0.437) まで落ちた。在庫は20種あったのに、である。
# ペアで数えれば Mガブリアスが複数案に出てもよく、相方が毎回違えば要求を満たす。
SUGGEST_MEGA_PAIR = int(os.environ.get("SUGGEST_MEGA_PAIR", "0"))


# ペアキャップで多様性のために拾う候補の下限（トップ案のスコアに対する割合）。
# メガ軸は空きメガ枠が1つしかないため「5案＝相棒メガ5種」となり、在庫の質が落ちる帯まで
# 掘らされる（実測ボーマンダ軸: 上位3種0.61-0.64に対し4番手0.584・6番手Mライチュウ0.513）。
# 下限を割るくらいならペアの重複を許す。
SUGGEST_MEGA_PAIR_FLOOR = float(os.environ.get("SUGGEST_MEGA_PAIR_FLOOR", "0.90"))
# 下限の絶対値。相対下限と「低いほう」を採る。0＝無効（相対下限のみ・従来と同一挙動）。
# 相対下限だけだと、トップ1本が突出した軸で下限が跳ね上がり多様性が出せない
# （実測エースバーン軸: top0.704で floor0.599、2位以下は0.59前後に固まり2種しか通らず
#  メガ構成2/5。候補は600件82種あり生成の問題ではない）。
SUGGEST_MEGA_PAIR_ABS = float(os.environ.get("SUGGEST_MEGA_PAIR_ABS", "0"))
# メガ2体の共有弱点の上限。これを超える案は選抜から除外する（0＝無効）。
# MEGA_OVERLAP_W は「引いて並べ替える」ペナルティなので、下限を通れば共有2でも採られる。
# 共有2は「1つの技で両方に抜群」を意味し、メガ2枚を並べる意味が薄れるため上限で弾く。
SUGGEST_MEGA_SHARED_MAX = int(os.environ.get("SUGGEST_MEGA_SHARED_MAX", "0"))


def _mega_pair_select(scored, fixnames, pcap, top, base=None):
    """ENS降順に貪欲採用。非コアのメガ種の集合が pcap 回を超える案はスキップ。
    SUGGEST_MEGA_CAP>0 なら「同一メガ種が何回出てよいか」も併せて制限する
    （ペアだけだと Mグソクムシャのように共有弱点0で誰とでも組める種が
    相方を替えながら5案中ほぼ全てに居座る。実測46%）。
    ただし下限を割る案しか残らないときは、どちらの制約も緩めて強い案を採る。"""
    # 補正済みスコアで下限判定・選抜する。_apply_mega_overlap_penalty は並べ替えるだけで
    # タプル内のスコアを書き換えないため、生スコアで選ぶとメガ弱点ペナルティが素通りする
    # （MEGA_OVERLAP_W を0.05〜0.20で振っても出力が1件も変わらない形で表面化。MMRと同じ不具合）。
    # しかもペア制約は「他と違うメガ構成」を積極的に探すので、共有弱点の多いペアはむしろ
    # 多様性要員として引き寄せられ、ペナルティが逆効果になっていた。
    base = base or {}
    def _adj(sc, p): return base.get(id(p), sc)
    # 種構成が同一の提案は1本まで。メガ構成が違えばペア制約は通ってしまうため、
    # 「6体が全く同じでガブリアスがメガか非メガかだけ違う」提案が並んでいた
    # （実測インテレオン軸#1/#2、アローラペルシアン軸#1/#4）。利用者からは同じパーティに見える。
    sel, cnt, scnt, used, spset = [], {}, {}, set(), set()
    top_sc = max((_adj(sc, p) for sc, p in scored), default=0.0)
    floor = top_sc * SUGGEST_MEGA_PAIR_FLOOR if top_sc > 0 else float("-inf")
    if SUGGEST_MEGA_PAIR_ABS > 0:
        floor = min(floor, SUGGEST_MEGA_PAIR_ABS)
    def _mg(p):
        return tuple(sorted(x.split("@", 1)[0] for x in p
                            if _spec_mega(x) and x.split("@", 1)[0] not in fixnames))
    def _sp(p):
        return frozenset(x.split("@", 1)[0] for x in p)
    while len(sel) < top:
        pick = None
        for sc, p in scored:                      # ペア制約を満たし、かつ下限以上
            if id(p) in used or _adj(sc, p) < floor:
                continue
            if _sp(p) in spset:
                continue
            if SUGGEST_MEGA_SHARED_MAX and _mega_weak_shared(p, fixnames) > SUGGEST_MEGA_SHARED_MAX:
                continue
            mg = _mg(p)
            if SUGGEST_MEGA_CAP and any(scnt.get(n, 0) >= SUGGEST_MEGA_CAP for n in mg):
                continue
            if cnt.get(mg, 0) < pcap:
                pick = (sc, p); break
        if pick is None:                          # 下限以上ならペア重複を許す
            for sc, p in scored:
                if id(p) not in used and _sp(p) not in spset and _adj(sc, p) >= floor:
                    pick = (sc, p); break
        if pick is None:                          # それも尽きたらスコア順に補充
            for sc, p in scored:
                if id(p) not in used and _sp(p) not in spset:
                    pick = (sc, p); break
        if pick is None:                          # 種構成の重複を許してでも top 本埋める
            for sc, p in scored:
                if id(p) not in used:
                    pick = (sc, p); break
        if pick is None:
            break
        sc, p = pick
        sel.append((sc, p)); used.add(id(p))
        mg = _mg(p)
        spset.add(_sp(p))
        cnt[mg] = cnt.get(mg, 0) + 1
        for n in mg:
            scnt[n] = scnt.get(n, 0) + 1
    return sel[:top]

def _cap_select(scored, fixnames, cap, top):
    """ENS降順に貪欲採用。各非コア種の採用回数が cap を超える案はスキップ。
    top本に満たなければ制約を無視してスコア順に補充（必ず top 本返す）。"""
    sel, cnt = [], {}
    for sc, p in scored:
        nm = [x.split("@", 1)[0] for x in p if x.split("@", 1)[0] not in fixnames]
        if any(cnt.get(n, 0) >= cap for n in nm):
            continue
        sel.append((sc, p))
        for n in nm:
            cnt[n] = cnt.get(n, 0) + 1
        if len(sel) == top:
            break
    if len(sel) < top:
        chosen = {id(p) for _, p in sel}
        for sc, p in scored:
            if len(sel) == top:
                break
            if id(p) not in chosen:
                sel.append((sc, p))
    return sel[:top]

def suggest(core_args, ncand, top):
    fixed = resolve_fixed(PG, core_args)
    key = [fixed, ncand, top] + ([SUGGEST_CAP] if SUGGEST_CAP else []) \
                                  + ([f"dw{DEPTH_W}"] if DEPTH_W else []) \
                                  + ([f"mo{MEGA_OVERLAP_W}"] if MEGA_OVERLAP_W else []) \
                                  + ([f"mmr{SUGGEST_MMR}"] if SUGGEST_MMR else []) \
                                  + ([f"mc{SUGGEST_MEGA_CAP}"] if SUGGEST_MEGA_CAP else []) \
                                  + ([f"mp{SUGGEST_MEGA_PAIR}_{SUGGEST_MEGA_PAIR_FLOOR}_{SUGGEST_MEGA_PAIR_ABS}"] if SUGGEST_MEGA_PAIR else []) \
                                  + ([f"ms{SUGGEST_MEGA_SHARED_MAX}"] if SUGGEST_MEGA_SHARED_MAX else []) \
                                  + ([f"ms{SUGGEST_MEGA_CAP}"] if SUGGEST_MEGA_PAIR and SUGGEST_MEGA_CAP else [])
    ck = json.dumps(key, ensure_ascii=False)   # 解決後specでキー化（入力形式に非依存）
    hit = _SCACHE.get(ck)
    if hit is not None:
        return hit                      # 同一軸は即時返却（重い計算をスキップ）
    # キャッシュミス＝事前計算済み241軸に無い組み合わせ（未収録種 or 複数コア指定等）。
    # 必然性修復はコスト上ライブ計算に組み込めないため、後日オフラインでキャッシュへ追加できるよう
    # Cloud Logging（標準stdout）に構造化ログを残すのみ（追加インフラ不要・$0）。
    print(f"CACHE_MISS {json.dumps({'fixed': fixed, 'ncand': ncand, 'top': top}, ensure_ascii=False)}", flush=True)
    rng = random.Random(0)
    # 候補生成数。キャッシュキーには入れない（本番フロントは ncand:100 固定送信のため、
    # キーに混ぜるとオフライン生成したキャッシュが永久にヒットしなくなる）。
    # ncand=100 では候補の8割が上位3メガに集中し、Mライチュウ/Mフラエッテのような
    # 弱点の被らないメガが1件も生成されなかった（実測ボーマンダ軸: 下限超えメガ2種→600で7種）。
    _nc = max(ncand, SUGGEST_NCAND)
    _t = time.time(); cands = complete_core(PG, L, TH, fixed, rng, _nc); tg = time.time() - _t
    fixnames = [f.split("@")[0] for f in fixed]
    _t = time.time()
    _all = _apply_mega_overlap_penalty(_rerank(_par_score(cands)), fixnames)
    if SUGGEST_MEGA_PAIR:
        scored = _mega_pair_select(_all, set(fixnames), SUGGEST_MEGA_PAIR, top,
                                   base=_mega_adjusted(_all, fixnames))
    elif SUGGEST_MEGA_CAP:
        scored = _mega_cap_select(_all, set(fixnames), SUGGEST_MEGA_CAP, top)
    elif SUGGEST_MMR > 0:
        scored = _mmr_select(_all, set(fixnames), top, SUGGEST_MMR,
                             base=_mega_adjusted(_all, fixnames))
    elif SUGGEST_CAP:
        scored = _cap_select(_all, set(fixnames), SUGGEST_CAP, top)
    else:
        scored = _all[:top]
    ts = time.time() - _t
    jobs = [(sc, p, fixnames) for sc, p in scored]
    _t = time.time(); out = _get_pool().map(_proposal_detail, jobs); td = time.time() - _t   # 提案ごとに並列（永続プール）
    print(f"[suggest] gen={tg:.2f}s score={ts:.2f}s detail={td:.2f}s workers={_WORKERS}", flush=True)
    res = {"fixed": fixnames, "results": out, "opps": [{"label": a["label"], "wr": a["wr"]} for a in ARCHES]}
    _SCACHE[ck] = res
    return res

COMPLETE_NCAND = int(os.environ.get("COMPLETE_NCAND", "50"))   # /complete の補完候補数（応答時間と品質のトレードオフ。fill=1/5実測: 総 4-9秒 <<20秒目標）

def complete(specs, fill, top, ncand=None):
    """型(spec)固定メンバー(specs、型プール非所属可)から残りfill体を補完し、上位topを返す。
    返却specsは追加分のみ（固定分は含まない）。決定的（固定シード）。
    追加分の種名集合(frozenset)が同一の候補は、並び順違いの重複案として1つに統合（最高スコアのみ残す）。"""
    ncand = ncand or COMPLETE_NCAND
    fixed = list(specs)
    for s in fixed:
        parse_pokemon_spec(s)   # 形式検証。不正なら例外→呼び出し側でエラー応答
    rng = random.Random(0)
    cands = complete_core_free(PG, L, TH, fixed, rng, ncand)
    if not cands:
        return {"results": []}
    scored = sorted(_par_score(cands), key=lambda x: -x[0])
    nfixed = len(fixed)
    best_by_set = {}   # 種名集合(frozenset) -> (score, party)。scoredは降順なので初出のみ採用すればよい
    for sc, p in scored:
        key = frozenset(s.split("@", 1)[0] for s in p[nfixed:nfixed + fill])
        if key not in best_by_set:
            best_by_set[key] = (sc, p)
        if len(best_by_set) >= top:
            break
    deduped = sorted(best_by_set.values(), key=lambda x: -x[0])[:top]
    out = [{"specs": p[nfixed:nfixed + fill], "score": round(sc, 3)} for sc, p in deduped]
    return {"results": out}

def simulate(specs, opp_idx, k):
    if not (0 <= opp_idx < len(ARCHES)): return {"error": "相手が不正"}
    opp = ARCHES[opp_idx]
    jobs = [(specs, opp["party"], (1234 + i * 97 + 13) & 0x7fffffff) for i in range(k)]
    workers = max(1, (os.cpu_count() or 2) - 2)
    with mp.get_context("fork").Pool(workers) as pool:
        res = pool.map(P3._play_winner, jobs, chunksize=1)
    w = sum(1 for r in res if r == 1); l = sum(1 for r in res if r == 2); dr = sum(1 for r in res if r == 0)
    dec = w + l
    return {"label": opp["label"], "wins": w, "losses": l, "draws": dr, "k": k,
            "wr": round(w / dec, 3) if dec else 0.5}

PAGE = """<!doctype html><html lang=ja><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>M-3 パーティ提案（Product3）</title><style>
body{font-family:system-ui,'Hiragino Kaku Gothic ProN',sans-serif;max-width:920px;margin:0 auto;padding:16px;background:#f6f7f9;color:#1f2937}
h1{font-size:1.25rem} .row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:12px 0}
input,select,button{font-size:1rem;padding:8px 10px;border:1px solid #cbd5e1;border-radius:8px}
button{background:#2563eb;color:#fff;border:0;cursor:pointer} button:disabled{opacity:.5}
.chip{background:#e0e7ff;border-radius:999px;padding:4px 10px;font-size:.85rem}
.card{background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:12px;margin:12px 0;box-shadow:0 1px 2px rgba(0,0,0,.04)}
.hd{display:flex;justify-content:space-between;align-items:center;font-weight:700}
table{width:100%;border-collapse:collapse;margin-top:8px;font-size:.82rem}
td,th{border-bottom:1px solid #eef2f7;padding:4px 6px;text-align:left;vertical-align:top}
.core{background:#fff7ed} .mega{color:#b45309;font-weight:700}
.muted{color:#6b7280;font-size:.85rem} .sc{color:#2563eb;font-weight:700}
.role{display:inline-block;background:#eef2ff;color:#3730a3;border-radius:6px;padding:1px 6px;font-size:.72rem;margin-right:3px}
.stats{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0;font-size:.8rem}
.stats span{background:#f1f5f9;border-radius:6px;padding:3px 8px}
.mg{font-size:.72rem;margin-top:6px;overflow-x:auto}
.mg table{min-width:640px} .mg td,.mg th{text-align:center;padding:2px 3px;border:1px solid #eef2f7}
.v◎{background:#bbf7d0} .vmark-good{background:#bbf7d0}
.cc{font-weight:700}
</style></head><body>
<h1>M-3 パーティ提案 <span class=muted>コアを固定→残り枠をAIが補完・強い順に提案</span></h1>
<div class=row>
 <input id=core placeholder="コア(カンマ区切り 例: サザンドラ,メタグロス)" style="flex:1;min-width:260px" list=splist>
 <datalist id=splist></datalist>
 <label class=muted>候補 <input id=nc type=number value=120 style="width:70px"></label>
 <label class=muted>提案数 <input id=tp type=number value=5 style="width:60px"></label>
 <button id=go onclick=run()>提案する</button>
</div>
<div id=status class=muted></div><div id=out></div>
<script>
fetch('/species').then(r=>r.json()).then(d=>{document.getElementById('splist').innerHTML=d.map(s=>`<option value="${s}">`).join('')});
async function run(){
 const core=document.getElementById('core').value.split(',').map(s=>s.trim()).filter(Boolean);
 if(!core.length){alert('コアを入力');return}
 const go=document.getElementById('go');go.disabled=true;
 document.getElementById('status').textContent='生成・評価中…（数〜十数秒）';document.getElementById('out').innerHTML='';
 try{
  const r=await fetch('/suggest',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({core,ncand:+document.getElementById('nc').value,top:+document.getElementById('tp').value})});
  const d=await r.json();
  if(d.error){document.getElementById('status').textContent='エラー: '+d.error;go.disabled=false;return}
  document.getElementById('status').textContent=`固定コア: ${d.fixed.join(' + ')} / ${d.results.length}件`;
  document.getElementById('out').innerHTML=d.results.map((res,i)=>{
   const rows=res.mons.map(m=>`<tr class="${m.core?'core':''}"><td>${m.core?'◆':(m.mega?'<span class=mega>★</span>':'')}${m.name}<br>${(m.roles||[]).map(r=>`<span class=role>${r}</span>`).join('')}</td><td>${m.item}</td><td>${m.nature}</td><td>${m.ability}</td><td>${m.ev}</td><td>${m.moves.join(' / ')}</td></tr>`).join('');
   const st=res.stats?('<div class=stats>'+Object.entries(res.stats).map(([k,v])=>`<span><b>${k}</b> ${v}</span>`).join('')+'</div>'):'';
   const col=c=>({'◎':'#16a34a','○':'#65a30d','△':'#6b7280','▲':'#ea580c','×':'#dc2626'}[c]||'#6b7280');
   let mg='';
   if(res.matchup){
     const th='<tr><th>自分＼相手</th>'+res.matchup.tops.map(t=>`<th>${t}</th>`).join('')+'</tr>';
     const mr=res.matchup.rows.map(r=>`<tr><td style="text-align:left">${r.mon}</td>`+r.cells.map(c=>`<td class=cc style="color:${col(c)}">${c}</td>`).join('')+'</tr>').join('');
     mg=`<div class=mg><div class=muted>1v1 相性（使用率上位）　◎有利 ○やや有利 △五分 ▲やや不利 ×不利</div><table>${th}${mr}</table></div>`;
   }
   return `<div class=card><div class=hd><span>提案 ${i+1}</span><span><span class=sc>スコア ${res.score}</span> ・ 脅威対応 ${Math.round(res.coverage*100)}%</span></div>
   ${st}<table><tr><th>ポケモン / 役割</th><th>持ち物</th><th>性格</th><th>特性</th><th>EV</th><th>技</th></tr>${rows}</table>${mg}</div>`;
  }).join('');
 }catch(e){document.getElementById('status').textContent='通信エラー: '+e}
 go.disabled=false;
}
</script></body></html>"""

ALLOW_ORIGIN = os.environ.get("ALLOW_ORIGIN", "*")   # 本番は https://pokenavi.jp を推奨
MIN_INTERVAL = float(os.environ.get("MIN_INTERVAL", "0"))  # 同一IPの重い処理の最短間隔(秒)。0で無効
_HEAVY_LOCK = threading.Lock()                       # 重い計算の同時実行を1本に直列化（CPU保護）
_LAST_HIT = {}                                       # ip -> 直近の重い処理時刻
_HEAVY = ("/suggest", "/simulate", "/complete")
MAX_BODY_BYTES = int(os.environ.get("MAX_BODY_BYTES", 16 * 1024))  # POSTボディ上限(既定16KB)。超過は413
MAX_SPEC_LEN = 500                                   # /complete の specs 1本あたりの文字数上限

class H(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        b = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code); self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", ALLOW_ORIGIN)
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)

    def _client_ip(self):
        xff = self.headers.get("Fly-Client-IP") or self.headers.get("X-Forwarded-For", "")
        return (xff.split(",")[0].strip() if xff else self.client_address[0])

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", ALLOW_ORIGIN)
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.end_headers()

    def log_message(self, *a): pass

    def do_GET(self):
        if self.path == "/" or self.path == "/health":
            self._send(200, "ok" if self.path == "/health" else PAGE, "text/plain" if self.path == "/health" else "text/html")
        elif self.path == "/species":
            self._send(200, json.dumps(VARIANTS, ensure_ascii=False))
        else:
            self._send(404, "{}")

    def do_POST(self):
        if self.path not in ("/suggest", "/simulate", "/complete", "/fire_detail", "/speed_detail", "/matchup_detail", "/atk_detail", "/guide_request"):
            self._send(404, "{}"); return
        try:
            n = int(self.headers.get("Content-Length", 0) or 0)
        except ValueError:
            n = 0
        if n > MAX_BODY_BYTES:
            self._send(413, json.dumps({"error": f"リクエストボディが大きすぎます（上限{MAX_BODY_BYTES}バイト）"}, ensure_ascii=False)); return
        if MIN_INTERVAL and self.path in _HEAVY:
            ip = self._client_ip(); now = time.time()
            if now - _LAST_HIT.get(ip, 0) < MIN_INTERVAL:
                self._send(429, json.dumps({"error": "リクエストが多すぎます。少し待って再試行してください。"}, ensure_ascii=False)); return
            _LAST_HIT[ip] = now
        try:
            req = json.loads(self.rfile.read(n) or "{}")
            if self.path == "/guide_request":
                core = req.get("core") or []
                if not isinstance(core, list) or len(core) > 6:
                    self._send(200, json.dumps({"error": "invalid"}, ensure_ascii=False)); return
                safe = []
                for a in core[:6]:
                    if isinstance(a, dict):
                        safe.append({"sp": str(a.get("sp", ""))[:30], "mega": (None if a.get("mega") is None else str(a.get("mega"))[:30])})
                    else:
                        safe.append(str(a)[:120])
                print("[GUIDE_REQUEST] " + json.dumps({"core": safe, "ip": self._client_ip()}, ensure_ascii=False), flush=True)
                self._send(200, json.dumps({"ok": True}, ensure_ascii=False)); return
            if self.path == "/atk_detail":
                self._send(200, json.dumps(EX.atk_detail(req.get("specs") or [], req.get("mon", ""), req.get("type", ""), L), ensure_ascii=False)); return
            if self.path in ("/fire_detail", "/speed_detail", "/matchup_detail"):
                fn = {"/fire_detail": EX.fire_detail, "/speed_detail": EX.speed_detail, "/matchup_detail": EX.matchup_detail}[self.path]
                self._send(200, json.dumps(fn(req.get("specs") or [], req.get("mon", ""), req.get("opp", ""), L), ensure_ascii=False)); return
            if self.path == "/simulate":
                specs = req.get("specs") or []
                opp_idx = int(req.get("opp_idx", 0))
                k = min(20, max(2, int(req.get("k", 6))))
                with _HEAVY_LOCK:
                    self._send(200, json.dumps(simulate(specs, opp_idx, k), ensure_ascii=False))
                return
            if self.path == "/complete":
                specs = req.get("specs") or []
                if not isinstance(specs, list) or not all(isinstance(s, str) for s in specs) or len(specs) > 5:
                    self._send(200, json.dumps({"error": "specsは文字列配列（最大5件）で指定してください"}, ensure_ascii=False)); return
                if any(len(s) > MAX_SPEC_LEN for s in specs):
                    self._send(200, json.dumps({"error": f"specの文字数が上限（{MAX_SPEC_LEN}）を超えています"}, ensure_ascii=False)); return
                if any(("@" not in s or len(s.split("@", 1)[1].split(":")) != 5) for s in specs):
                    self._send(200, json.dumps({"error": "spec形式が不正です（種名@持ち物:性格:技1|技2|技3|技4:H/A/B/C/D/S:特性 の完全形式で指定してください）"}, ensure_ascii=False)); return
                fill = int(req.get("fill", 0))
                if not (1 <= fill <= 6 - len(specs)):
                    self._send(200, json.dumps({"error": "fillが不正です（1 <= fill <= 6-specs.length）"}, ensure_ascii=False)); return
                top = min(3, max(1, int(req.get("top", 3))))
                with _HEAVY_LOCK:
                    res = complete(specs, fill, top)
                self._send(200, json.dumps(res, ensure_ascii=False))
                return
            core = req.get("core") or []
            nc = min(300, max(20, int(req.get("ncand", 120))))
            top = min(10, max(1, int(req.get("top", 5))))
            with _HEAVY_LOCK:
                res = suggest(core, nc, top)
            self._send(200, json.dumps(res, ensure_ascii=False))
        except SystemExit as e:
            self._send(200, json.dumps({"error": str(e)}, ensure_ascii=False))
        except Exception as e:
            self._send(200, json.dumps({"error": repr(e)}, ensure_ascii=False))

if __name__ == "__main__":
    HOST = os.environ.get("HOST", "127.0.0.1")   # 本番(コンテナ)は 0.0.0.0
    _get_pool()   # 単スレッドのうちに永続プールをfork（マルチスレッド化後のfork回避）
    print(f"listen {HOST}:{PORT}  CORS={ALLOW_ORIGIN}  rate={MIN_INTERVAL}s", flush=True)
    ThreadingHTTPServer((HOST, PORT), H).serve_forever()
