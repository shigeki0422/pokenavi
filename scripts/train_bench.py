import os, time, sys
from simulator.az_loop import run_loop_parallel

if __name__ == "__main__":
    workers = max(1, (os.cpu_count() or 2) - 1)
    games = workers * 3
    t = time.time()
    net, hist = run_loop_parallel(iters=1, games_per=games, n_sims=24, hidden=128,
                                  workers=workers, seed=999, fresh=False, verbose=True)
    dt = time.time() - t
    g = hist[0]["games"]
    print(f"\n実測: {g}試合 / {dt:.1f}秒 = {g/dt:.2f} 試合/秒  (workers={workers})")
    print(f"目安: 10000試合 ≈ {10000/(g/dt)/60:.1f}分,  30000試合 ≈ {30000/(g/dt)/60:.1f}分")
