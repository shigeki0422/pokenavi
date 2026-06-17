"""ヒューリスティック選出 vs 学習選出(/tmp/selector3.pkl) が実際どう変わるかを可視化。
対戦はせず、両者が選ぶ3体(先頭=リード)を並べ、違うケースを抽出する。
"""
import sys, os, random, pickle
import _pop_gen as G
import _selector3 as S
from multiprocessing import Pool

def names(mons): return [p.name for p in mons]

def fmt(sel):
    return f"[{sel[0].name}] " + " / ".join(p.name for p in sel[1:])

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    os.environ["SEL_SIMS"] = "1"   # 選出だけなのでMCTSは使わない(軽量)
    S._winit()
    L = S._W["L"]
    from simulator.ai import select_party
    with open("/tmp/selector3.pkl", "rb") as fh: sel = pickle.load(fh)
    D = G.load(season="M-2"); rng = random.Random(4242)
    parties = [G.gen_party(D, rng) for _ in range(N + 1)]
    diffs = 0; shown = 0
    for i in range(N):
        a, b = parties[i], parties[i + 1]
        A = S._team(a); B = S._team(b)
        h = select_party(A, B, L, n=3, temperature=0.0, rng=random.Random(i))
        m = S._select_with(sel, A, B, random.Random(i))
        hset = set(names(h)); mset = set(names(m))
        same_members = hset == mset
        same_lead = h[0].name == m[0].name
        if same_members and same_lead:
            continue
        diffs += 1
        if shown >= 10:
            continue
        shown += 1
        opplead = select_party(B, A, L, n=3, temperature=0.0, rng=random.Random(i))[0].name
        print(f"\n--- ケース{i} (vs 相手リード見込み: {opplead}) ---")
        print(f"  手持ち6体: {' / '.join(names(A))}")
        print(f"  ヒューリスティック: {fmt(h)}")
        print(f"  学習選出        : {fmt(m)}")
        if not same_members:
            ho = hset - mset; mo = mset - hset
            print(f"   → 構成変更: 外した[{','.join(ho)}] 入れた[{','.join(mo)}]")
        elif not same_lead:
            print(f"   → 同じ3体だがリード変更: {h[0].name} → {m[0].name}")
    print(f"\n=== {N}マッチ中 {diffs}件で選出が相違（{diffs/N*100:.0f}%）===")

if __name__ == "__main__":
    main()
