"""selector3 のA/Bのみ再実行（学習済み /tmp/selector3.pkl を再利用・ラベル再生成なし）。
53.2%/p0.066 を戦数拡大で有意確定するため。実MCTS@1600でヒューリスティック選出と対戦。
"""
import sys, os, math, random
from multiprocessing import Pool
import _pop_gen as G
import _selector3 as S

def main():
    abN = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    gpp = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    sims = int(sys.argv[3]) if len(sys.argv) > 3 else 1600
    workers = 12
    os.environ["SEL_SIMS"] = str(sims)
    import time
    D = G.load(season="M-2")
    ev = [G.gen_party(D, random.Random(9000)) for _ in range(abN + workers)]
    chunks = [ev[k::workers] for k in range(workers)]
    t1 = time.time()
    with Pool(workers, initializer=S._winit) as pool:
        res = pool.map(S._ab, [(8000 + k, ch, gpp, "/tmp/selector3.pkl") for k, ch in enumerate(chunks)])
    vw = sum(r[0] for r in res); vl = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = vw + vl; wr = vw / dec if dec else 0
    z = (vw - dec * .5) / math.sqrt(dec * .25) if dec else 0
    pv = math.erfc(abs(z) / math.sqrt(2)) if dec else 1
    verdict = ("有意に優位＝MCTS教師で選出学習が現行超え確定" if pv < 0.05 and wr > 0.5
               else ("有意に劣位" if pv < 0.05 else "有意差なし"))
    print(f"\n=== A/B拡大: 学習選出(MCTS@{sims}教師) vs ヒューリスティック（実MCTS・{dec+dr}戦・{time.time()-t1:.0f}秒）===", flush=True)
    print(f"学習選出: {vw}勝 {vl}敗 {dr}分 → 勝率{wr*100:.1f}%  z={z:+.2f} p={pv:.4f}  {verdict}", flush=True)

if __name__ == "__main__":
    main()
