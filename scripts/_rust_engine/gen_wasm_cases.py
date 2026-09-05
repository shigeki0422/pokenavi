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
from simulator.battle import COUNTER_MOVES, _calc_hits
from simulator.damage import calc_damage

ME._LOADER[0] = L
NCASE = int(os.environ.get("NCASE", "300"))
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(__file__), "cases", "wasm_1v1.jsonl"))


def fixed_hits(mv, A):
    """分析での連続回数。engine の calc_hits(FixedRng) と対応。"""
    ME._enter_fixed(0.0)
    try:
        return max(1, _calc_hits(mv, A))
    finally:
        ME._exit_fixed()


def move_damage(A, B, mv, field, roll, n):
    """技1回ぶんの与ダメージ（連続技は全ヒット合計）。engine の analysis::move_damage と対応。

    「1ターンで減ったHP」ではないので、ばけのかわの身代わり分・砂の削り・
    たべのこしの回復は含まれない（それらは発数の方に効く）。

    連続技の途中では半減きのみの消費とHP減少を持ち越す。持ち越さないと
    「1発目も2発目も半減」になり、対戦本体と食い違う
    （ゲッコウガのみずしゅりけん→ゴウカザル@イトケのみ で 13+13=26 と出た。実際は 13+26=39）。
    呼び出し元のオブジェクトを汚さないよう、最後に元へ戻す。
    """
    ME._enter_fixed(roll)
    save = (B.item, B.hp, A.item, getattr(A, "charged", None), getattr(A, "_multi_hit_index", 0))
    try:
        total = 0
        for hit_i in range(max(1, n)):
            # トリプルアクセルのように「何発目か」で威力が変わる技があるので、
            # 対戦本体（battle.py の _multi_hit_index）と同じく毎ヒット更新する
            A._multi_hit_index = hit_i
            d = calc_damage(A, B, mv, field, False, roll)
            total += d
            B.hp = max(1, B.hp - d)
        return total
    finally:
        B.item, B.hp, A.item = save[0], save[1], save[2]
        if save[3] is not None:
            A.charged = save[3]
        A._multi_hit_index = save[4]
        ME._exit_fixed()


def side(spec_0, spec_1, att, field, X, Y):
    """並び (spec_0, spec_1) の対面における att 側の評価。
    場は対面ごとに1つなので、向きで並びを入れ替えない。"""
    moves = []
    for mv in X.moves:
        if (mv is None or mv.category == "status" or not (mv.power or 0)
                or mv.name_jp in COUNTER_MOVES):
            moves.append({"n": mv.name_jp if mv is not None else None, "dmg": None})
            continue
        hl, _ = ME._run(spec_0, spec_1, mv.name_jp, L, 0.0, att)
        hh, _ = ME._run(spec_0, spec_1, mv.name_jp, L, 1.0, att)
        n_hits = fixed_hits(mv, X)
        moves.append({
            "n": mv.name_jp,
            "dmgLo": move_damage(X, Y, mv, field, 0.0, n_hits),
            "dmgHi": move_damage(X, Y, mv, field, 1.0, n_hits),
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
                   "sa": side(sa, sb, 0, field, A2, B2), "sb": side(sa, sb, 1, field, B2, A2)}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
    print(f"{OUT}: {n}件")


if __name__ == "__main__":
    main()
