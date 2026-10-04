"""R3-T2/T3 コーパス（cases/fb_*.jsonl）の期待値を現在の Python で採り直す。

元の生成スクリプトはソースも pyc も消失している（run_gates.sh のコメント）。gate_r3.rs（engine::sim::full_battle）の
Python 正本 `_v3_rollout._greedy_3v3` と同じ手順で対戦し、毎ターン終わりの正準状態ハッシュ（state_codec.sv_hash）・
勝敗・ターン数を書き直す。入力（パーティ・シーズン・選出・シード・AI）は既存コーパスのまま。
  1. random.seed(seed) → 6体ずつ build_from_spec(randomize=True)（A→B の順。Rust の CpyRandom と同じ乱数列）
  2. 選出3体を _effective_speed の最も速い個体を先頭に並べる（同速は先の個体）
  3. 見せ合いは6体（source6）。AI は GreedyAI（g）/ HeuristicAI（h）＋ certain_ko_override
  4. きまぐレーザー を含む党は両者に信念を付ける（_greedy_3v3 と同じ。信念の計算が乱数を消費するため）
採り直したら gate_r3 で乖離0を確かめてから case_stamp.py --stamp。

usage: venv/bin/python _rust_engine/gen_r3fb_cases.py [files...]   env JOBS(12) DRY(1=書かない)
"""
import glob
import json
import multiprocessing as mp
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
os.chdir(ROOT)
os.environ.setdefault("OMP_NUM_THREADS", "1")

_W = {}


def _init(parties, seasons):
    from simulator.simulate import get_loader
    _W["L"] = get_loader()
    _W["parties"], _W["seasons"] = parties, seasons


def battle(specs_a, sa, specs_b, sb, season_a, season_b, seed, ai, on_turn=None):
    """gate_r3（engine::sim::full_battle）の Python 正本。戻り値 (勝敗, ターン数)"""
    from simulator.pokemon import build_from_spec as bfs, parse_pokemon_spec as pps
    from simulator.ai import GreedyAI, HeuristicAI, certain_ko_override, _effective_speed as espd
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField as BF
    L = _W["L"]
    random.seed(seed)
    f = BF()
    A = [bfs(pps(s), L, season=season_a, randomize=True) for s in specs_a]
    B = [bfs(pps(s), L, season=season_b, randomize=True) for s in specs_b]

    def order(P, sub):
        mons = [P[i] for i in sub]
        ld = max(range(len(mons)), key=lambda j: espd(mons[j], f))
        return [mons[ld]] + [mons[j] for j in range(len(mons)) if j != ld]
    s1 = BattleSide(order(A, sa), viewer_label="P1", source6=A)
    s2 = BattleSide(order(B, sb), viewer_label="P2", source6=B)
    if any("きまぐレーザー" in s for s in list(specs_a) + list(specs_b)):
        s1.belief = OpponentBelief(L)
        s2.belief = OpponentBelief(L)
    mk = {"g": GreedyAI, "h": HeuristicAI}
    g1, g2 = mk[ai[0]](), mk[ai[1]]()

    def ai1(m, o, ff):
        return certain_ko_override(g1(m, o, ff), m, o, ff)

    def ai2(m, o, ff):
        return certain_ko_override(g2(m, o, ff), m, o, ff)
    b = Battle(s1, s2, BF())
    res = b.run(ai1, ai2, on_turn=on_turn)
    return res, b.turn


def work(line):
    import state_codec as SC
    c = json.loads(line)
    P, S = _W["parties"], _W["seasons"]
    sa_specs = c.get("specsA") or P[c["ia"]]
    sb_specs = c.get("specsB") or P[c["ib"]]
    H = []
    res, nturn = battle(sa_specs, c["sa"], sb_specs, c["sb"], S[c["ia"]], S[c["ib"]], c["seed"], c["ai"],
                        on_turn=lambda bt: H.append(SC.sv_hash(SC.encode_battle(bt).vals)))
    changed = (c["H"] != H or c["result"] != res or c["nturn"] != nturn)
    c["H"], c["result"], c["nturn"] = H, res, nturn
    return json.dumps(c, ensure_ascii=False, separators=(",", ":")), changed


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "cases", "fb_*.jsonl")))
    jobs = int(os.environ.get("JOBS", "12"))
    for path in files:
        with open(path, encoding="utf-8") as fh:
            head = fh.readline()
            body = fh.read().splitlines()
        hdr = json.loads(head)
        with mp.get_context("fork").Pool(jobs, initializer=_init, initargs=(hdr["parties"], hdr["seasons"])) as p:
            res = p.map(work, body, chunksize=16)
        nchg = sum(ch for _, ch in res)
        print(f"{os.path.basename(path)}: {len(res)}戦 / 期待値が変わった {nchg}戦", flush=True)
        if os.environ.get("DRY") != "1":
            tmp = path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as fh:
                fh.write(head)
                fh.write("\n".join(x for x, _ in res) + "\n")
            os.replace(tmp, path)


if __name__ == "__main__":
    main()
