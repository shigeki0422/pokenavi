"""datapack.json エクスポータ（Rustエンジン用）

Python側の正本（simulator/data.py・damage.py・pokemon.py）が参照する静的データを
そのままRustへ渡すための単一ファイルを生成する。simulator/** は一切変更しない。

出力: scripts/_rust_engine/datapack.json
"""
import hashlib
import json
import os
import re
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

DB = os.path.join(ROOT, "pokenavi.db")
OUT = os.path.join(HERE, "datapack.json")

from simulator.data import NATURE_MODS, _chart_raw, _types, DataLoader  # noqa: E402
from simulator.damage import _is_secondary_effect  # noqa: E402
from simulator.ability_categories import CATEGORIES as _ABIL_CATS, ABILITY_CAT_BITS as _ABIL_CAT_BITS  # noqa: E402

SEASONS = os.environ.get("DATAPACK_SEASONS", "M-2,M-3,M-4,M-5,M-6").split(",")

TOPN = {"moves": 12, "items": 5, "abilities": 3, "natures": 3, "evs": 3}


def _stat1(path):
    try:
        st = os.stat(path)
        return [st.st_size, st.st_mtime_ns]
    except OSError:
        return None


def source_stat():
    """素材の安価な署名（size, mtime_ns）。一致していれば重いダイジェストを省略できる。
    ※ SQLite は WAL モードだと本体ファイルの stat を変えずに内容が変わるため、
       -wal / -shm も必ず署名に含める（これを外すと staleness を取り逃す）。"""
    return {"db": [_stat1(DB), _stat1(DB + "-wal"), _stat1(DB + "-shm")],
            "net": [_stat1(os.path.join(ROOT, "az_net_np.json"))]}


def source_hashes(con=None):
    """データパックの「素材」のダイジェスト。datapack.json 本体のハッシュは
    エクスポート結果しか守らないため、素材（ネット重み・DB由来テーブル・simulator/**）が
    変わったのに再エクスポートしていない状態（staleness）はこちらで検出する。
    engine_dispatch から呼ばれるので import 副作用なし・0.3秒以内で完了すること。"""
    own = con is None
    if own:
        con = sqlite3.connect(DB)
    d = hashlib.sha256()
    for tb in ("move_master", "pokemon_base_stats", "pokemon_mega_stats"):
        for r in con.execute(f"SELECT * FROM {tb} ORDER BY id"):
            d.update(repr(tuple(r)).encode())
    qs = ",".join("?" * len(SEASONS))
    for tb in ("pokemon_moves", "pokemon_items", "pokemon_abilities",
               "pokemon_natures", "pokemon_evs"):
        for r in con.execute(
                f"SELECT * FROM {tb} WHERE rule='single' AND season IN ({qs}) "
                f"ORDER BY season, pokemon, crawled_date, rank, rowid", SEASONS):
            d.update(repr(tuple(r)).encode())
    if own:
        con.close()
    npath = os.path.join(ROOT, "az_net_np.json")
    nh = hashlib.sha256(open(npath, "rb").read()).hexdigest() if os.path.exists(npath) else None
    sd = hashlib.sha256()
    simdir = os.path.join(ROOT, "simulator")
    for fn in sorted(os.listdir(simdir)):
        if fn.endswith(".py"):
            sd.update(fn.encode())
            sd.update(open(os.path.join(simdir, fn), "rb").read())
    return {"db_tables": d.hexdigest(), "az_net_np": nh, "simulator_py": sd.hexdigest()}


def export():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row

    # ---- move_master (501) ----
    moves = []
    secondary = []
    for r in con.execute("SELECT * FROM move_master ORDER BY id"):
        eff = r["effect_text"] or ""
        moves.append({
            "name_jp": r["name_jp"], "name_en": r["name_en"], "type": r["type"],
            "category": r["category"], "power": r["power"], "accuracy": r["accuracy"],
            "priority": r["priority"], "pp": r["pp"], "effect_id": r["effect_id"],
            "effect_text": eff,
        })
        if _is_secondary_effect(eff):
            secondary.append(r["name_jp"])

    # ---- pokemon_base_stats (237) : id順 = LIKEフォールバックの先頭一致順 ----
    base = []
    for r in con.execute("SELECT * FROM pokemon_base_stats ORDER BY id"):
        base.append({k: r[k] for k in r.keys()})

    # ---- pokemon_mega_stats (75) ----
    mega = []
    for r in con.execute("SELECT * FROM pokemon_mega_stats ORDER BY id"):
        mega.append({k: r[k] for k in r.keys()})

    # ---- usage: (season, usage_name) ごとの top-N（data.pyのSQLと同一意味論） ----
    names = set()
    for tbl, col in (("pokemon_moves", "move"), ("pokemon_items", "item"),
                     ("pokemon_abilities", "ability"), ("pokemon_natures", "nature"),
                     ("pokemon_evs", "ev_spread")):
        for (p,) in con.execute(f"SELECT DISTINCT pokemon FROM {tbl} WHERE rule='single'"):
            names.add(p)
    names = sorted(names)

    # 名前解決用: pokemon_moves(rule='single') に存在する名前（season無関係のEXISTS判定）
    moves_names = sorted({p for (p,) in con.execute(
        "SELECT DISTINCT pokemon FROM pokemon_moves WHERE rule='single'")})

    usage = {}
    for season in SEASONS:
        cd = ("(SELECT MAX(crawled_date) FROM pokemon_moves "
              "WHERE season=? AND rule='single' AND pokemon=?)")
        for name in names:
            args = (season, name, season, name)
            mv = con.execute(f"""
                SELECT move, usage_rate FROM pokemon_moves
                WHERE season=? AND rule='single' AND pokemon=? AND crawled_date={cd}
                ORDER BY rank LIMIT 12""", args).fetchall()
            it = con.execute(f"""
                SELECT item, usage_rate FROM pokemon_items
                WHERE season=? AND rule='single' AND pokemon=? AND crawled_date={cd}
                ORDER BY rank LIMIT 5""", args).fetchall()
            ab = con.execute(f"""
                SELECT ability, usage_rate FROM pokemon_abilities
                WHERE season=? AND rule='single' AND pokemon=? AND crawled_date={cd}
                ORDER BY rank LIMIT 3""", args).fetchall()
            na = con.execute(f"""
                SELECT nature, usage_rate FROM pokemon_natures
                WHERE season=? AND rule='single' AND pokemon=? AND crawled_date={cd}
                ORDER BY rank LIMIT 3""", args).fetchall()
            ev = con.execute(f"""
                SELECT ev_spread, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, usage_rate FROM pokemon_evs
                WHERE season=? AND rule='single' AND pokemon=? AND crawled_date={cd}
                ORDER BY rank LIMIT 3""", args).fetchall()
            if not (mv or it or ab or na or ev):
                continue
            usage[f"{season}\t{name}"] = {
                "moves": [[r[0], r[1]] for r in mv],
                "items": [[r[0], r[1]] for r in it],
                "abilities": [[r[0], r[1]] for r in ab],
                "natures": [[r[0], r[1]] for r in na],
                "evs": [{"H": r["ev_h"], "A": r["ev_a"], "B": r["ev_b"], "C": r["ev_c"],
                         "D": r["ev_d"], "S": r["ev_s"], "spread": r["ev_spread"],
                         "rate": r["usage_rate"]} for r in ev],
            }
    con.close()

    # ---- ネット重み ----
    net = None
    npath = os.path.join(ROOT, "az_net_np.json")
    if os.path.exists(npath):
        with open(npath) as f:
            nd = json.load(f)
        net = {k: nd[k] for k in nd if k in
               ("W1", "b1", "W2", "b2", "Wv", "bv", "Wp", "bp")}
        net["_meta"] = {k: nd[k] for k in nd if k not in
                        ("W1", "b1", "W2", "b2", "Wv", "bv", "Wp", "bp")}

    # ---- 特性効果カテゴリ（features.py の _ability_cats 用） ----
    abil_cats = {"names": list(_ABIL_CATS),
                 "bits": {k: [int(b) for b in v] for k, v in _ABIL_CAT_BITS.items()}}

    # ---- 登録テンプレートの実スプレッド（belief.registered_spreads_by_species） ----
    from simulator.belief import registered_spreads_by_species  # noqa: E402
    _ldr = DataLoader()
    reg = {k: [[{kk: ev[kk] for kk in "HABCDS"}, nat] for ev, nat in v]
           for k, v in registered_spreads_by_species(_ldr).items()}

    pack = {
        "header": {"version": 2, "seasons": SEASONS, "topn": TOPN, "content_hash": None},
        "types": _types,
        "type_chart": _chart_raw,
        "nature_mods": {k: list(v) for k, v in NATURE_MODS.items()},
        "form_aliases": DataLoader.FORM_ALIASES,
        "region_prefixes": ["ガラル", "アローラ", "ヒスイ", "パルデア"],
        "move_master": moves,
        "secondary_moves": sorted(secondary),
        "pokemon_base_stats": base,
        "pokemon_mega_stats": mega,
        "usage_names_in_moves": moves_names,
        "usage": usage,
        "net": net,
        "ability_cats": abil_cats,
        "registered_spreads": reg,
    }
    body = {k: v for k, v in pack.items() if k != "header"}
    blob = json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    pack["header"]["content_hash"] = hashlib.sha256(blob.encode()).hexdigest()
    pack["header"]["source_hashes"] = source_hashes()
    pack["header"]["source_stat"] = source_stat()

    with open(OUT, "w") as f:
        json.dump(pack, f, ensure_ascii=False, separators=(",", ":"))
    file_hash = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    with open(OUT + ".sha256", "w") as f:
        f.write(file_hash + "\n")
    size = os.path.getsize(OUT)
    print(f"wrote {OUT} bytes={size} hash={pack['header']['content_hash']}")
    print(f"file_sha256={file_hash}")
    print(f"source_hashes={pack['header']['source_hashes']}")
    print(f"abil_cats={len(abil_cats['bits'])}x{len(abil_cats['names'])} reg_species={len(reg)}")
    print(f"moves={len(moves)} secondary={len(secondary)} base={len(base)} "
          f"mega={len(mega)} usage_keys={len(usage)} net={'yes' if net else 'no'}")


if __name__ == "__main__":
    export()
