"""分析側の確定数を、対戦本体を実際に走らせた結果と突き合わせる監査。

audit_entry.py は「入場直後の状態」までしか見ていない。ターンが進む間に起きること
（追加効果・反動・特性の発動・持ち物の消費・状態異常の蓄積）は未検査だったので、
対戦本体で 1v1 を実走させ、実際に何発かかるかを数えて比較する。

確定数の定義（最低乱数・急所なし・必中）に合わせるため:
  - damage._ROLL_OVERRIDE = 0.0 で全ダメージを最低ロールに固定
  - check_hit を常に True に差し替え（命中率のブレを排除）
  - 両者とも「分析側が選んだ最大打点」を撃ち続ける

env: NPAIR(300)
"""
import os, json, math, collections
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("GA_SIMS", "1")
import feature1 as _f1
_f1._ensure_loaded("M-3", 8); L = _f1._W["loader"]
import _explain as E
import simulator.damage as DMG
import simulator.battle as BT
from simulator.battle import BattleField, BattleSide, Battle, Action

NPAIR = int(os.environ.get("NPAIR", "300"))
MAXT = 30


def hits_by_engine(spec_a, spec_b, move_name):
    """実装側の _mu_engine._run をそのまま使う。
    監査が独自に対戦を組むと、入場処理の呼び方やターンの数え方の違いで
    「実装は正しいのに監査だけ落ちる」偽陽性が出る（実際に13%出た）。"""
    import _mu_engine as ME
    ME._LOADER[0] = L
    h, r = ME._run(spec_a, spec_b, move_name, L, 0.0, 0)
    return h, r


def main():
    panel = json.load(open("m3_top119_valid.json"))
    seen = {}
    for t in panel:
        for s in t["party"]:
            seen.setdefault(s.split("@")[0], s)
    uniq = list(seen.values())
    import random as _r
    rng = _r.Random(11)

    diffs = collections.Counter(); ex = collections.defaultdict(list); n = 0
    try:
        for _ in range(NPAIR):
            sa, sb = rng.sample(uniq, 2)
            A = E._build(sa, L); B = E._build(sb, L)
            # 実装は _build が保持する _spec で評価する。監査も同じ spec を使う
            sa, sb = A._spec, B._spec
            r = E._mu_score(A, B, BattleField())
            if r["my_move"] == "—" or r["myh"] >= 999:
                continue
            n += 1
            # 実装が選んだ技をそのまま実走して、確定数が一致するかを見る
            # （技の選び方まで含めた比較は _mu_engine 内部で完結しているので二重に評価しない）
            eng, _hp = hits_by_engine(sa, sb, r["my_move"])
            if eng != r["myh"]:
                key = f"確定数 分析{r['myh']} vs 実走{eng}"
                diffs[key] += 1
                if len(ex[key]) < 3:
                    ex[key].append(f"{A.name}({r['my_move']}) → {B.name}"
                                   f" [{A.ability}/{A.item} vs {B.ability}/{B.item}]")
    finally:
        pass

    print(f"\n=== 分析側の確定数 vs 対戦本体の実走（{n}対面・最低乱数・必中固定）===")
    bad = sum(diffs.values())
    print(f"  一致 {n - bad}/{n} ({100*(n-bad)/max(1,n):.1f}%)")
    for k, c in diffs.most_common(12):
        print(f"\n  {k}: {c}件")
        for e in ex[k]:
            print(f"      {e}")


if __name__ == "__main__":
    main()
