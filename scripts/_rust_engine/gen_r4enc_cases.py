"""R4-G1/G2 コーパス（cases/enc_*.jsonl＝encode_state と逐次ネット forward のビット一致）の期待値を現在の Python で採り直す。

元の生成スクリプト（dump_encode_cases.py）はソースも pyc も消失している。gate_r4_enc.rs と同じ手順:
  gen_r3fb_cases.battle と同じフル対戦（g=GreedyAI / h=HeuristicAI ＋ certain_ko_override）を走らせ、毎ターン終わりに
  H: 正準状態ハッシュ、E: 状態を1回複製して first=0（side1 視点）→ first=1 の順に
     x = features.encode_state(自分, 相手, 場)・L = alphazero.legal_actions_indexed の添字（空なら [0]）・
     (p, v) = 逐次順オラクルのネット（seqnet.SeqNet＝az_np.PVNetNP.forward の左→右加算）.evaluate(x, L)
     を [f_hash(x), v のビット, [[添字, p のビット], …]] で記録（同じ複製で続けて評価するのは Rust と同じ）。
ネットは datapack と同じ az_net_np.json（env NET で別のネット）。seqnet は _rust_engine/__pycache__ の pyc から読む（ソース消失）。
入力（パーティ・シーズン・選出・シード・AI）は既存コーパスのまま。採り直したら gate_r4_enc で乖離0 → case_stamp.py --stamp。

usage: venv/bin/python _rust_engine/gen_r4enc_cases.py [files...]   env JOBS(12) DRY(1=書かない) NET
"""
import copy
import glob
import importlib.machinery
import importlib.util
import json
import multiprocessing as mp
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
os.chdir(ROOT)
os.environ.setdefault("OMP_NUM_THREADS", "1")
import gen_r3fb_cases as FB  # noqa: E402


def load_pyc(name):
    """ソースの消えたモジュールを __pycache__ の pyc から読む"""
    path = os.path.join(HERE, "__pycache__", f"{name}.cpython-312.pyc")
    loader = importlib.machinery.SourcelessFileLoader(name, path)
    spec = importlib.util.spec_from_loader(name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    sys.modules[name] = mod
    return mod


def bits(x):
    return struct.unpack("<Q", struct.pack("<d", float(x)))[0]


_N = {}


def _init(parties, seasons, net):
    FB._init(parties, seasons)
    sn = load_pyc("seqnet")
    assert sn.selftest()
    _N["net"] = sn.SeqNet.load(net)


def work(line):
    import state_codec as SC
    from simulator.features import encode_state
    from simulator.alphazero import legal_actions_indexed
    c = json.loads(line)
    P, S = FB._W["parties"], FB._W["seasons"]
    H, E = [], []

    def on_turn(bt):
        H.append(SC.sv_hash(SC.encode_battle(bt).vals))
        s1, s2, f = copy.deepcopy((bt.side1, bt.side2, bt.field))
        row = []
        for me, op in ((s1, s2), (s2, s1)):
            legal = [ix for _, ix in legal_actions_indexed(me, op, f)]
            x = encode_state(me, op, f)
            p, v = _N["net"].evaluate(x, legal or [0])
            pol = [[a, bits(p[a])] for a in legal] if legal else []   # evaluate は {添字: 確率}
            row.append([SC.f_hash(x), bits(v), pol])
        E.append(row)
    res, nturn = FB.battle(P[c["ia"]], c["sa"], P[c["ib"]], c["sb"], S[c["ia"]], S[c["ib"]], c["seed"], c["ai"],
                           on_turn=on_turn)
    changed = c["H"] != H or c["E"] != E or c["result"] != res or c["nturn"] != nturn
    c["H"], c["E"], c["result"], c["nturn"] = H, E, res, nturn
    return json.dumps(c, ensure_ascii=False, separators=(",", ":")), changed


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "cases", "enc_*.jsonl")))
    jobs = int(os.environ.get("JOBS", "12"))
    net = os.environ.get("NET") or os.path.join(ROOT, "az_net_np.json")
    for path in files:
        with open(path, encoding="utf-8") as fh:
            head = fh.readline()
            body = fh.read().splitlines()
        hdr = json.loads(head)
        with mp.get_context("fork").Pool(jobs, initializer=_init, initargs=(hdr["parties"], hdr["seasons"], net)) as p:
            res = p.map(work, body, chunksize=8)
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
