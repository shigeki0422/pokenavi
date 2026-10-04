"""R3 追加ゲート（cases/sel_00.jsonl＝ai.select_party のパリティ）の期待値を現在の Python で採り直す。

元の生成スクリプトは消失している。gate_r3_sel.rs と同じ手順:
  random.seed(seed)（対戦用のグローバル乱数）・random.Random(sseed)（select_party の rng）・
  6体ずつ build_from_spec(randomize=False)・env MEGA_PENALTY=mp で select_party(a, b, n, temp, rng)、
  期待値は選出の添字と、呼んだ後の12体の正準状態ハッシュ（state_codec.poke_fields → sv_hash。副作用が残らないことの確認）。
入力（パーティ・シーズン・n・温度・mp・シード）は既存コーパスのまま。採り直したら gate_r3_sel で乖離0 → case_stamp.py --stamp。

usage: venv/bin/python _rust_engine/gen_r3sel_cases.py [files...]   env JOBS(12) DRY(1=書かない)
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


def work(line):
    import state_codec as SC
    from simulator.pokemon import build_from_spec as bfs, parse_pokemon_spec as pps
    from simulator.ai import select_party
    c = json.loads(line)
    L, P, S = _W["L"], _W["parties"], _W["seasons"]
    random.seed(c["seed"])
    srng = random.Random(c["sseed"])
    a = [bfs(pps(s), L, season=S[c["ia"]], randomize=False) for s in P[c["ia"]]]
    b = [bfs(pps(s), L, season=S[c["ib"]], randomize=False) for s in P[c["ib"]]]
    os.environ["MEGA_PENALTY"] = repr(float(c["mp"]))
    sel = select_party(a, b, L, n=c["n"], temperature=c["temp"], rng=srng)
    idx = [next(i for i, p in enumerate(a) if p is m) for m in sel]
    e = SC.Enc()
    for p in a + b:
        SC.poke_fields(e, p, "")
    h = SC.sv_hash(e.vals)
    changed = c["idx"] != idx or c["H"] != h
    c["idx"], c["H"] = idx, h
    return json.dumps(c, ensure_ascii=False, separators=(",", ":")), changed


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "cases", "sel_*.jsonl")))
    jobs = int(os.environ.get("JOBS", "12"))
    for path in files:
        with open(path, encoding="utf-8") as fh:
            head = fh.readline()
            body = fh.read().splitlines()
        hdr = json.loads(head)
        with mp.get_context("fork").Pool(jobs, initializer=_init, initargs=(hdr["parties"], hdr["seasons"])) as p:
            res = p.map(work, body, chunksize=16)
        nchg = sum(ch for _, ch in res)
        print(f"{os.path.basename(path)}: {len(res)}件 / 期待値が変わった {nchg}件", flush=True)
        if os.environ.get("DRY") != "1":
            tmp = path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as fh:
                fh.write(head)
                fh.write("\n".join(x for x, _ in res) + "\n")
            os.replace(tmp, path)


if __name__ == "__main__":
    main()
