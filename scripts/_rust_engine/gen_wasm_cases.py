"""wasm 版 1v1 の照合ケースを Python(正本)から生成する。

Rust パリティ(`cases/*.jsonl`)と同じ考え方で、Python の実行結果を記録して突き合わせる。
表示側(%・確率・記号)は含めない。ここで守りたいのはルール層＝
「HP・実効素早さ・各技の与ダメ・確定数」が Python と一致すること。

env: NCASE(300) / OUT(_rust_engine/cases/wasm_1v1.jsonl)
"""
import json
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("GA_SIMS", "1")
import feature1 as _f1

_f1._ensure_loaded("M-3", 8)
L = _f1._W["loader"]
import _explain as E
import _mu_engine as ME
from simulator.ai import _effective_speed

ME._LOADER[0] = L
NCASE = int(os.environ.get("NCASE", "300"))
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(__file__), "cases", "wasm_1v1.jsonl"))


def side(spec_x, spec_y, field, X):
    moves = []
    for i, mv in enumerate(X.moves):
        if mv is None or mv.category == "status" or not (mv.power or 0):
            moves.append({"n": mv.name_jp if mv is not None else None, "dmg": None})
            continue
        hl, rl = ME._run(spec_x, spec_y, mv.name_jp, L, 0.0)
        hh, rh = ME._run(spec_x, spec_y, mv.name_jp, L, 1.0)
        hp = X._opp_hp if False else None  # 未使用
        moves.append({
            "n": mv.name_jp,
            "ratioLo": rl, "ratioHi": rh,
            "hitsLo": hl, "hitsHi": hh,
        })
    return {"hp": X.max_hp, "speed": _effective_speed(X, field), "moves": moves}


def main():
    import random

    panel = json.load(open("m3_top119_valid.json"))
    seen = {}
    for t in panel:
        for s in t["party"]:
            seen.setdefault(s.split("@")[0], s)
    uniq = [E._build(s, L)._spec for s in seen.values()]
    rng = random.Random(20260905)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    n = 0
    with open(OUT, "w") as f:
        for _ in range(NCASE):
            sa, sb = rng.sample(uniq, 2)
            A = E._build(sa, L)
            B = E._build(sb, L)
            field, A2, B2 = E._enter(A, B)
            rec = {"a": sa, "b": sb,
                   "sa": side(sa, sb, field, A2), "sb": side(sb, sa, field, B2)}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
    print(f"{OUT}: {n}件")


if __name__ == "__main__":
    main()
