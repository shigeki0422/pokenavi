"""MCTSが変化技（設置/状態異常/積み/壁/トリル等）を実戦で使えているか診断。
プールのパーティ同士を対戦させ、選出個体が持つ各変化技について「場に出ている間に1度でも選択したか」
を集計＝『使えるはずの変化技の発動率』。攻撃技偏重（脳筋）かどうかを定量化する。
"""
import os, sys, json, random, time, sqlite3
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "120"))                # 対戦数
NPROC = int(os.environ.get("NPROC", "12"))
_W = {}
KEY = ["ステルスロック", "どくびし", "まきびし", "おにび", "でんじは", "あくび", "ちょうはつ",
       "トリックルーム", "おいかぜ", "つるぎのまい", "りゅうのまい", "わるだくみ", "めいそう",
       "リフレクター", "ひかりのかべ", "オーロラベール", "なまける", "はねやすめ", "じこさいせい", "みがわり", "まもる"]

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader()
    _W["ai"] = _net_ai(PVNetNP.load(), _W["L"], 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _job(args):
    pa, pb, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    def AI(my, opp, f): return certain_ko_override(ai0(my, opp, f), my, opp, f)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    # 場に出た個体が持つ変化技の「保有(出場)」と「使用」を集計
    held = {}; used = {}
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        b = Battle(s1, s2)
        w = b.run(AI, AI)
        for side in (sa, sb):
            for mon in side:
                for mv in mon.moves:
                    if mv and mv.name_jp in KEY:
                        held[mv.name_jp] = held.get(mv.name_jp, 0) + 1
        for l in b.logs:                              # 使用マーカー: 技【X】を確認（初使用時に必ず出る・全技共通）
            for k in KEY:
                if ("【" + k + "】を確認") in l:
                    used[k] = used.get(k, 0) + 1
    except Exception:
        pass
    return held, used

def main():
    pool = [p["specs"] for p in json.load(open("func1_themed_M-3.json", encoding="utf-8"))["parties"]]
    n = len(pool); rng = random.Random(3)
    jobs = []
    for _ in range(N):
        i, j = rng.sample(range(n), 2)
        jobs.append((pool[i], pool[j], rng.randrange(10 ** 6)))
    print(f"{N}戦 / MCTS@{SIMS} で変化技の使用を診断", flush=True)
    held = {}; used = {}; t0 = time.time()
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for h, u in p.imap_unordered(_job, jobs, chunksize=4):
            for k, v in h.items(): held[k] = held.get(k, 0) + v
            for k, v in u.items(): used[k] = used.get(k, 0) + v
    print(f"完了 {time.time()-t0:.0f}s\n")
    print(f"{'変化技':<12}{'出場(選出)':>8}{'使用回数':>8}{'使用/出場':>10}")
    rows = sorted(KEY, key=lambda k: -held.get(k, 0))
    for k in rows:
        h = held.get(k, 0); u = used.get(k, 0)
        if h == 0: continue
        print(f"{k:<12}{h:>8}{u:>8}{(u/h):>9.2f}")
    th = sum(held.values()); tu = sum(used.values())
    print(f"\n合計: 出場{th} 使用{tu} 使用率{tu/max(1,th):.2f}")

if __name__ == "__main__":
    main()
