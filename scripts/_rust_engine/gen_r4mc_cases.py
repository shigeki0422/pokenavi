"""R4-G3 コーパス（cases/mc_*.jsonl＝MCTS フル対戦のパリティ）の期待値を現在の Python で採り直す。

元の dump_mcts_battles.py はソースが消失し pyc だけが残っている。その手順（pyc の逆アセンブルで確認）を写した:
  ・ネット = 逐次順オラクル（seqnet.SeqNet。pyc から読む）      … パリティ規約 #2
  ・belief.PokemonBelief.sample_moves の known_moves を sorted に正規化  … 規約 #3（Rust の belief.rs は sorted で保持）
  ・PYTHONHASHSEED=0（このスクリプトは子プロセスに設定して起動し直す）
  ・random.seed(seed) → 6体ずつ build_from_spec(randomize=True)、選出3体を最速先頭に並べ、見せ合いは6体
  ・両者に OpponentBelief、AI は train_az2._net_ai(net, L, 0, 12, seed[^0x5bd1e995], mcts=True, mcts_sims=sims,
    mcts_select="regret", mcts_fast=True) ＋ certain_ko_override
  ・毎ターン終わりの正準状態ハッシュ・勝敗・ターン数
入力（パーティ・シーズン・選出・シード・sims）は既存コーパスのまま。採り直したら gate_r4_mcts で乖離0 → case_stamp.py --stamp。

usage: venv/bin/python _rust_engine/gen_r4mc_cases.py [files...]   env JOBS(12) DRY(1=書かない) NET
"""
import glob
import json
import multiprocessing as mp
import os
import random
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
if os.environ.get("PYTHONHASHSEED") != "0":
    sys.exit(subprocess.run([sys.executable] + sys.argv, env=dict(os.environ, PYTHONHASHSEED="0")).returncode)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
os.chdir(ROOT)
os.environ.setdefault("OMP_NUM_THREADS", "1")
import gen_r4enc_cases as ENC  # noqa: E402

_W = {}


def patch_sorted_belief():
    from simulator.belief import PokemonBelief

    def sample_moves(self, rng, n: int = 4):
        chosen = list(dict.fromkeys(sorted(self.known_moves)))[:n]
        pool = [(m, r) for m, r in self.move_prior.items() if m not in chosen]
        while len(chosen) < n and pool:
            m = self._weighted(rng, pool)
            if m is None:
                return chosen
            chosen.append(m)
            pool = [(x, r) for x, r in pool if x != m]
        return chosen
    PokemonBelief.sample_moves = sample_moves


def _init(parties, seasons, net):
    from simulator.simulate import get_loader
    patch_sorted_belief()
    sn = ENC.load_pyc("seqnet")
    assert sn.selftest()
    _W["L"] = get_loader()
    _W["net"] = sn.SeqNet.load(net)
    _W["parties"], _W["seasons"] = parties, seasons


def work(line):
    import state_codec as SC
    from simulator.ai import certain_ko_override, _effective_speed as espd
    from simulator.pokemon import build_from_spec as bfs, parse_pokemon_spec as pps
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField as BF
    from train_az2 import _net_ai
    c = json.loads(line)
    L, net, P, S = _W["L"], _W["net"], _W["parties"], _W["seasons"]
    seed, sims = c["seed"], c["sims"]
    random.seed(seed)
    f = BF()
    A = [bfs(pps(s), L, season=S[c["ia"]], randomize=True) for s in P[c["ia"]]]
    B = [bfs(pps(s), L, season=S[c["ib"]], randomize=True) for s in P[c["ib"]]]

    def order(Pt, sub):
        mons = [Pt[i] for i in sub]
        ld = max(range(3), key=lambda j: espd(mons[j], f))
        return [mons[ld]] + [mons[j] for j in range(3) if j != ld]
    s1 = BattleSide(order(A, c["sa"]), viewer_label="P1", source6=A)
    s2 = BattleSide(order(B, c["sb"]), viewer_label="P2", source6=B)
    s1.belief = OpponentBelief(L)
    s2.belief = OpponentBelief(L)
    a1 = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=sims, mcts_select="regret", mcts_fast=True)
    a2 = _net_ai(net, L, 0, 12, seed ^ 1540483477, mcts=True, mcts_sims=sims, mcts_select="regret", mcts_fast=True)

    def ai1(m, o, ff):
        return certain_ko_override(a1(m, o, ff), m, o, ff)

    def ai2(m, o, ff):
        return certain_ko_override(a2(m, o, ff), m, o, ff)
    H = []
    b = Battle(s1, s2, BF())
    res = b.run(ai1, ai2, on_turn=lambda bt: H.append(SC.sv_hash(SC.encode_battle(bt).vals)))
    changed = c["H"] != H or c["result"] != res or c["nturn"] != b.turn
    c["H"], c["result"], c["nturn"] = H, res, b.turn
    return json.dumps(c, ensure_ascii=False, separators=(",", ":")), changed


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "cases", "mc_[0-9]*.jsonl")))
    jobs = int(os.environ.get("JOBS", "12"))
    net = os.environ.get("NET") or os.path.join(ROOT, "az_net_np.json")
    for path in files:
        with open(path, encoding="utf-8") as fh:
            head = fh.readline()
            body = fh.read().splitlines()
        hdr = json.loads(head)
        with mp.get_context("fork").Pool(jobs, initializer=_init, initargs=(hdr["parties"], hdr["seasons"], net)) as p:
            res = p.map(work, body, chunksize=1)
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
