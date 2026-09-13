"""R0ゲート: spec文字列 → BuiltPokemon の全派生フィールドが Python(正本) と Rust で一致するか。

対になる Rust 側は rust_engine/engine/src/bin/gate_r0.rs（spec→ビルド結果をJSONに吐く）。
ここでは同じ spec を Python で組み、フィールド単位で突き合わせる。
R1以降（ダメージ・1ターン・対戦）は「同じ個体が組めている」ことが前提なので、
ビルド差異をここで潰しておかないと上位ゲートの赤の原因切り分けができない。

使い方: scripts/ を cwd にして  venv/bin/python _rust_engine/gate_r0.py
env:
  R0_SEASON  対象シーズン（既定 POOL_SEASON、無ければ M-3）
  R0_N       検査する spec 数（既定 0 = 型プール全件）
  R0_CASES   spec を1行1件で書いたファイル。指定時は型プールではなくこれを使う
  R0_SHOW    不一致の表示件数（既定 20）
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

SEASON = os.environ.get("R0_SEASON") or os.environ.get("POOL_SEASON") or "M-3"
os.environ.setdefault("POOL_SEASON", SEASON)
os.environ.setdefault("OMP_NUM_THREADS", "1")

BIN = os.path.join(ROOT, "rust_engine", "target", "release", "gate_r0")
DATAPACK = os.path.join(HERE, "datapack.json")


def _specs():
    path = os.environ.get("R0_CASES")
    if path:
        with open(path, encoding="utf-8") as f:
            return [ln.strip() for ln in f if ln.strip()]
    from gen_party_pool import PartyGen
    pg = PartyGen()
    out = []
    for sp in sorted(pg.pool):
        out.extend(pg.pool[sp])
    n = int(os.environ.get("R0_N", "0"))
    return out[:n] if n else out


def _py_dump(spec_str, L):
    """Rust側 gate_r0.rs の dump() と同じキー・同じ値域で1個体を書き出す。"""
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    spec = parse_pokemon_spec(spec_str)
    p = build_from_spec(spec, L, season=SEASON, randomize=False)

    def dump(q, with_moves=True):
        d = {
            "name": q.name, "dex": q.dex,
            "type1": q.type1, "type2": q.type2,
            "max_hp": q.max_hp, "hp": q.hp,
            "attack": q.attack, "defense": q.defense,
            "sp_attack": q.sp_attack, "sp_defense": q.sp_defense, "speed": q.speed,
            "ability": q.ability, "item": q.item, "nature": q.nature,
            "weight_kg": getattr(q, "weight_kg", None),
            "evs": {k: q.evs.get(k, 0) for k in ("H", "A", "B", "C", "D", "S")},
        }
        if with_moves:
            d["moves"] = [None if m is None else {
                "name_jp": m.name_jp, "type": m.type, "category": m.category,
                "power": m.power, "accuracy": m.accuracy,
                "priority": m.priority, "pp": m.pp,
            } for m in q.moves]
            d["pp"] = list(q.pp)
        return d

    rec = dump(p)
    rec["spec"] = spec_str
    rec["season"] = SEASON
    rec["parsed"] = {
        "name": spec.get("name"), "item": spec.get("item"), "nature": spec.get("nature"),
        "moves": spec.get("moves"), "ability": spec.get("ability"),
        "evs": None if not spec.get("evs") else {k: spec["evs"].get(k, 0)
                                                 for k in ("H", "A", "B", "C", "D", "S")},
    }
    md = p.mega_data
    rec["mega"] = None if md is None else {
        "mega_name": md.mega_name, "mega_stone": md.mega_stone,
        "type1": md.type1, "type2": md.type2,
        "hp": md.hp, "attack": md.attack, "defense": md.defense,
        "sp_attack": md.sp_attack, "sp_defense": md.sp_defense, "speed": md.speed,
        "ability": md.ability, "weight_kg": md.weight_kg,
    }
    if md is None:
        rec["mega_applied"] = None
    else:
        p.do_mega_evolve()
        rec["mega_applied"] = dump(p, with_moves=False)
    return rec


def _diff(a, b, path=""):
    """Rust(a) と Python(b) の相違を (パス, rust値, python値) で列挙する。"""
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            out += _diff(a.get(k), b.get(k), f"{path}.{k}" if path else k)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append((path + ".len", len(a), len(b)))
        for i, (x, y) in enumerate(zip(a, b)):
            out += _diff(x, y, f"{path}[{i}]")
    else:
        if isinstance(a, float) or isinstance(b, float):
            if a is None or b is None or abs(float(a) - float(b)) > 1e-9:
                out.append((path, a, b))
        elif a != b:
            out.append((path, a, b))
    return out


def main():
    if not os.path.exists(BIN):
        sys.exit(f"gate_r0: Rust側バイナリが無い: {BIN}\n"
                 f"  (cd rust_engine && cargo build --release) を先に実行せよ")
    specs = _specs()
    print(f"gate_r0: season={SEASON} specs={len(specs)}", flush=True)

    in_path = os.path.join(HERE, "cases", "r0_in.json")
    out_path = os.path.join(HERE, "cases", "r0_rust.json")
    os.makedirs(os.path.dirname(in_path), exist_ok=True)
    with open(in_path, "w", encoding="utf-8") as f:
        json.dump([{"spec": s, "season": SEASON} for s in specs], f, ensure_ascii=False)
    subprocess.run([BIN, DATAPACK, in_path, out_path], check=True)
    with open(out_path, encoding="utf-8") as f:
        rust = json.load(f)
    if len(rust) != len(specs):
        sys.exit(f"gate_r0: Rustの出力件数が違う rust={len(rust)} specs={len(specs)}")

    import feature1 as _f1
    _f1._ensure_loaded(SEASON, 8)
    L = _f1._W["loader"]

    show = int(os.environ.get("R0_SHOW", "20"))
    bad = 0
    shown = 0
    for r, s in zip(rust, specs):
        try:
            p = _py_dump(s, L)
        except Exception as e:
            bad += 1
            if shown < show:
                shown += 1
                print(f"  ✗ {s}\n      Python側でビルド失敗: {e}")
            continue
        d = _diff(r, p)
        if d:
            bad += 1
            if shown < show:
                shown += 1
                print(f"  ✗ {s}")
                for path, rv, pv in d[:8]:
                    print(f"      {path}: rust={rv!r} python={pv!r}")
    if bad:
        sys.exit(f"gate_r0: 乖離 {bad}/{len(specs)} 件")
    print(f"gate_r0: OK 乖離0 ({len(specs)}件)")


if __name__ == "__main__":
    main()
