"""Rust エンジン（pokenavi_engine）へのディスパッチ shim（R5 / V4強化版）。

既定は Python（`ENGINE` 未設定 or `ENGINE=python`）＝従来挙動と完全に同一。
`ENGINE=rust` のときだけネイティブ実装を呼び、以下のいずれかで自動的に Python へフォールバックする:
  - モジュール未導入 / import 失敗
  - datapack のハッシュ不一致（datapack.json の header.content_hash と .so 内ロード結果の照合）
  - datapack の staleness（素材＝az_net_np.json / DB由来テーブル が datapack より新しい）
  - **未対応コンフィグ**（Rust移植が実装していない env が有効：下記 _GUARDS）
  - 呼び出し中の任意の例外（PyO3 PanicException を含む BaseException）

フォールバック警告は理由ごとに1度だけ stderr に出す（loudly-once）。

未対応コンフィグ（Rust版は実装していない）:
  MCTS_CACHE / MCTS_EARLY / MCTS_NEXTTURN_LAMBDA / MCTS_QSELECT* / MCTS_DOWNSIDE_* /
  MCTS_COLLAPSE_MEGA=0 / MCTS_EXPLAIN / HIDDEN_SELECTION=0 / SWITCH_BOOST / IMITATE_SWITCH /
  SELECT_MODE / LEARNED_SELECTION / SELECT_SIMS / SELECT_TOPK / MAX_MEGA / MIN_MEGA / MEGA_PENALTY
探索方式（exp3 / duct / tree_search）と solve_zero_sum / choose_faint_switch は env ではなく
呼び出し側の引数・オブジェクト構成で決まる。ディスパッチ済みの3経路は
`mcts_select="regret", mcts_fast=True, tree=False`・AIをlambdaで包む（＝choose_faint_switch 未設定）
に固定されているため到達しない。新たな経路を配線する場合はこの不変条件を必ず確認すること。

使い方:
    ENGINE=rust venv/bin/python _ev2_p50/run_pick.py
    POKENAVI_DATAPACK=/abs/path/datapack.json ENGINE=rust ...
    ENGINE_SKIP_SOURCE_CHECK=1 ... （素材ダイジェスト検査を省略／既定は検査する）
"""
import os
import re
import sys

# 既定は rust（オフラインバッチの高速化。2026-09-03 に python から切替）。
#   根拠: R0-R5 全パリティゲート乖離0＋V1統計等価（greedy n=24,000 完全一致 / MCTS n=10,400 Δ=-0.03pt p=0.95）。
#   Rust が使えない状況（モジュール未導入・datapack stale・未対応 env・panic）は自動で Python に落ちる。
#   Python 時代と厳密比較したい検証ジョブでは ENGINE=python を明示すること。
ENGINE = os.environ.get("ENGINE", "rust").lower()
_HERE = os.path.dirname(os.path.abspath(__file__))
_DATAPACK = os.environ.get(
    "POKENAVI_DATAPACK", os.path.join(_HERE, "_rust_engine", "datapack.json"))

RUST = None          # 有効時のみモジュール、無効なら None
_WARNED = set()
_INIT = False

# ─────────────────────────────────────────────────────────────
# 未対応コンフィグのガード。(env名, 許容値集合) … None=未設定を許容
_G_BASE = [
    ("HIDDEN_SELECTION", {None, "1"}),      # Rustは hidden=on 固定
    ("SWITCH_BOOST", {None, "0.0", "0", "0.00"}),
    ("IMITATE_SWITCH", {None, "0"}),
]
_G_MCTS = [
    ("MCTS_CACHE", {None, "0"}),
    ("MCTS_EARLY", {None, "0"}),
    ("MCTS_NEXTTURN_LAMBDA", {None, "0", "0.0"}),
    ("MCTS_COLLAPSE_MEGA", {None, "1"}),
    ("MCTS_QSELECT", {None, "1"}),
    ("MCTS_QSELECT_FRAC", {None, "0.1"}),
    ("MCTS_QSELECT_MIN", {None, "10"}),
    ("MCTS_DOWNSIDE_GUARD", {None, "1"}),
    ("MCTS_DOWNSIDE_K", {None, "8"}),
    ("MCTS_DOWNSIDE_MARGIN", {None, "0.20", "0.2"}),
    ("MCTS_EXPLAIN", {None, "0"}),
]
# 配線済み経路が内部で使う選出は simulator.ai.select_party（heuristic）であって
# learned_select_party ではない（_o1_policy.py:24 が simulator.ai から直接importしている）。
# ai.py が読む env は MEGA_PENALTY のみ（ai.py:663）で、LEARNED_SELECTION / SELECT_MODE /
# SELECT_SIMS / SELECT_TOPK / MAX_MEGA / MIN_MEGA はすべて learned_selection.py スコープ＝
# この経路の挙動を変えない。過剰にガードすると、_v3_final が import 時に
# LEARNED_SELECTION=1 を立てる副作用（_v3_final.py:6）だけで mcts_vs_dist が
# Python に落ちてしまい、11スクリプトが理由なく高速化を失う。
_G_SELECT = [
    ("MEGA_PENALTY", {None, "50", "50.0"}),
]
# 関数ごとの適用範囲。選出(select_party)を内部で行うのは mcts_vs_dist のみ。
_GUARDS = {
    "greedy_3v3":   _G_BASE,
    "mcts_3v3":     _G_BASE + _G_MCTS,
    "mcts_vs_dist": _G_BASE + _G_MCTS + _G_SELECT,
}


def unsupported_config(fn_name):
    """有効化されている未対応 env のリスト（空なら Rust 使用可）。"""
    bad = []
    for name, ok in _GUARDS.get(fn_name, _G_BASE + _G_MCTS + _G_SELECT):
        v = os.environ.get(name)
        if v not in ok:
            bad.append(f"{name}={v}")
    return bad
# ─────────────────────────────────────────────────────────────


def _warn(key, msg):
    """Rustを無効化してPython経路に落ちたことの通知（1事由につき1回）。
    ログ監視はこの接頭辞を拾う想定なので、無効化を伴わない注意喚起には _notice() を使うこと。"""
    if key in _WARNED:
        return
    _WARNED.add(key)
    print(f"[engine_dispatch] Rust無効→Pythonフォールバック: {msg}", file=sys.stderr, flush=True)


def _notice(key, msg):
    """Rustは使い続けるが運用者に確認を促す注意喚起（1事由につき1回）。
    _warn と接頭辞を分けないと「無効化された」と誤読され、逆に本物の無効化を見逃す。"""
    if key in _WARNED:
        return
    _WARNED.add(key)
    print(f"[engine_dispatch] 注意（Rustは有効のまま）: {msg}", file=sys.stderr, flush=True)


def _file_hash():
    """datapack.json の header.content_hash（先頭数百バイトだけ読む）。"""
    try:
        with open(_DATAPACK, "rb") as f:
            head = f.read(4096).decode("utf-8", "ignore")
        m = re.search(r'"content_hash"\s*:\s*"([0-9a-f]{64})"', head)
        return m.group(1) if m else None
    except Exception:
        return None


def _header_field(name):
    """datapack.json header の 1フィールド（先頭数KBだけ読む）。"""
    try:
        with open(_DATAPACK, "rb") as f:
            head = f.read(8192).decode("utf-8", "ignore")
        m = re.search(r'"%s":(\{[^}]*\}|\[[^\]]*\])' % name, head)
        if not m:
            return None
        import json as _j
        return _j.loads('{"x":' + m.group(1) + "}")["x"]
    except Exception:
        return None


def _file_source_hashes():
    return _header_field("source_hashes")


def _file_bytes_mismatch():
    """datapack.json 実体の sha256 とサイドカー（datapack.json.sha256）の照合。
    header.content_hash は「ヘッダに書かれた文字列」を Rust が echo するだけなので、
    本体を書き換えられた場合は検出できない。ファイルバイト列のハッシュで塞ぐ。"""
    side = _DATAPACK + ".sha256"
    if not os.path.exists(side):
        return f"サイドカー {os.path.basename(side)} が無い（datapack_export.py で再生成が必要）"
    import hashlib
    try:
        want = open(side).read().strip()
        with open(_DATAPACK, "rb") as f:
            got = hashlib.sha256(f.read()).hexdigest()
    except Exception as e:
        return f"datapack 読み取り失敗: {e}"
    if want != got:
        return (f"datapack.json が改変されている sha256={got[:12]} 期待={want[:12]}"
                " → _rust_engine/datapack_export.py で再生成せよ")
    return None


def _source_staleness():
    """素材が datapack より新しい場合に理由文字列、問題なければ None。
    az_net_np / DB由来テーブル = 致命（Rust無効化）。simulator/**.py = 警告のみ。"""
    if os.environ.get("ENGINE_SKIP_SOURCE_CHECK") == "1":
        return None
    want = _file_source_hashes()
    if not want:
        return "datapack に source_hashes が無い（datapack_export.py で再生成が必要）"
    # 速い経路: 素材の (size, mtime_ns) が記録と一致すれば重いダイジェストを省略（0.41s→0.001s）
    want_stat = _header_field("source_stat")
    if want_stat:
        try:
            sys.path.insert(0, os.path.join(_HERE, "_rust_engine"))
            from datapack_export import source_stat
            if source_stat() == want_stat:
                return None
        except BaseException:
            pass
    try:
        sys.path.insert(0, os.path.join(_HERE, "_rust_engine"))
        from datapack_export import source_hashes
        got = source_hashes()
    except BaseException as e:
        return f"素材ダイジェスト計算に失敗: {e}"
    for k in ("az_net_np", "db_tables"):
        if want.get(k) != got.get(k):
            return (f"datapack が stale: {k} が変化 "
                    f"(datapack={str(want.get(k))[:12]} 実体={str(got.get(k))[:12]})"
                    " → _rust_engine/datapack_export.py で再生成せよ")
    if want.get("simulator_py") != got.get("simulator_py"):
        _notice("simdrift",
                "simulator/**.py がパリティ検証時点から変化している。"
                "_rust_engine/verify_parity.sh（smoke 約5分）の再実行を強く推奨")
    return None


def _init():
    global RUST, _INIT
    if _INIT:
        return RUST
    _INIT = True
    if ENGINE != "rust":
        return None
    os.environ.setdefault("POKENAVI_DATAPACK", _DATAPACK)
    try:
        import pokenavi_engine as _pe
    except BaseException as e:        # 未ビルド環境
        _warn("import", f"import 失敗: {e}")
        return None
    try:
        got = _pe.datapack_hash()
    except BaseException as e:
        _warn("load", f"datapack ロード失敗: {e}")
        return None
    want = os.environ.get("POKENAVI_DATAPACK_EXPECT") or _file_hash()
    if want and got != want:
        _warn("hash", f"datapack ハッシュ不一致 rust={got[:12]} file={want[:12]}")
        return None
    bad = _file_bytes_mismatch()
    if bad:
        _warn("bytes", bad)
        return None
    stale = _source_staleness()
    if stale:
        _warn("stale", stale)
        return None
    RUST = _pe
    return RUST


def rust():
    """有効なら pokenavi_engine モジュール、無効なら None。"""
    return _init()


def call(fn_name, *args):
    """成功なら結果（int）、無効/失敗なら None（呼び出し側は Python 経路へ）。"""
    m = _init()
    if m is None:
        return None
    bad = unsupported_config(fn_name)
    if bad:
        _warn(f"cfg:{fn_name}:{','.join(bad)}",
              f"{fn_name}: 未対応コンフィグが有効 [{', '.join(bad)}]")
        return None
    try:
        return int(getattr(m, fn_name)(*args))
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException as e:
        # Rust の panic! は PyO3 では BaseException 派生の PanicException になるため
        # Exception では捕まらない。ここで確実に握って Python 経路へ落とす。
        global RUST
        RUST = None
        _warn(f"exc:{fn_name}", f"{fn_name} 実行時例外: {e}")
        return None
