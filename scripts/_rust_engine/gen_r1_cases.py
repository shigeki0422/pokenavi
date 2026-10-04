"""R1 コーパス（cases/shard_0*.jsonl・synth_00.jsonl）の期待値を現在の Python で採り直す。

元の生成スクリプト（dump_damage_cases）はソースが消失している。入力（攻撃側・防御側・技・場・急所・ロール）はそのまま、
期待値（dmg と POST＝atk_charged / atk_electromorphosis_charged / def_item / def_stage_speed / field_weather_negated）だけを
現在の simulator/damage.py の calc_damage で計算し直す。仕様を変えたら採り直し、gate_r1 が乖離0になってから case_stamp.py --stamp。

usage: venv/bin/python _rust_engine/gen_r1_cases.py [files...]   env JOBS(12) DRY(1=書かない)
"""
import dataclasses
import glob
import json
import multiprocessing as mp
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
os.chdir(ROOT)
from simulator.data import DataLoader, MoveData  # noqa: E402
from simulator.pokemon import BattlePokemon  # noqa: E402
from simulator.battle import BattleField  # noqa: E402
import simulator.damage as D  # noqa: E402

_DL = []
PF = None


def dl():
    if not _DL:
        _DL.append(DataLoader())
    return _DL[0]


def poke(a):
    d = dict(zip(PF, a))
    p = BattlePokemon(name=d["name"], dex=0, type1=d["type1"], type2=d["type2"], max_hp=d["max_hp"], hp=d["hp"],
                      attack=d["attack"], defense=d["defense"], sp_attack=d["sp_attack"], sp_defense=d["sp_defense"],
                      speed=d["speed"], base_type1=d["type1"], base_type2=d["type2"], item=d["item"], ability=d["ability"])
    for k in PF[5:]:
        if k in ("hp", "max_hp", "attack", "defense", "sp_attack", "sp_defense", "speed"):
            continue
        setattr(p, k, d[k])
    return p


def move(m):
    base = dl().get_move(m[0])
    if base is None:
        return MoveData(name_jp=m[0], name_en="", type=m[1], category=m[2], power=m[3], accuracy=None, priority=0,
                        pp=None, effect_id=None)
    return dataclasses.replace(base, type=m[1], category=m[2], power=m[3])


def recompute(c):
    a, d, m, f = poke(c[0]), poke(c[1]), move(c[2]), BattleField()
    w, f.electric_terrain, f.psychic_terrain, f.misty_terrain, f.grassy_terrain, f.gravity = c[3]
    f.weather = w
    D._ROLL_OVERRIDE = c[6]
    try:
        v = D.calc_damage(a, d, m, f, c[4], c[5])
    finally:
        D._ROLL_OVERRIDE = None
    post = [bool(getattr(a, "charged", False)), bool(getattr(a, "_electromorphosis_charged", False)), d.item,
            d.stage_speed, bool(getattr(f, "_weather_negated", False))]
    return c[:7] + [v, post]


def work(args):
    global PF
    pf, lines = args
    PF = pf
    out, nchg = [], 0
    for ln in lines:
        c = json.loads(ln)
        n = recompute(c)
        nchg += n[7] != c[7] or n[8] != c[8]
        out.append(json.dumps(n, ensure_ascii=False, separators=(",", ":")))
    return out, nchg


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "cases", "shard_0*.jsonl"))) + \
        [os.path.join(HERE, "cases", "synth_00.jsonl")]
    jobs = int(os.environ.get("JOBS", "12"))
    for path in files:
        with open(path, encoding="utf-8") as fh:
            head = fh.readline()
            body = fh.read().splitlines()
        pf = json.loads(head)["schema"]["poke"]
        chunks = [(pf, body[i:i + 5000]) for i in range(0, len(body), 5000)]
        with mp.get_context("fork").Pool(jobs) as p:
            res = p.map(work, chunks)
        new = [x for o, _ in res for x in o]
        nchg = sum(n for _, n in res)
        print(f"{os.path.basename(path)}: {len(new)}件 / 期待値が変わった {nchg}件", flush=True)
        if os.environ.get("DRY") != "1":
            tmp = path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as fh:
                fh.write(head)
                fh.write("\n".join(new) + "\n")
            os.replace(tmp, path)


if __name__ == "__main__":
    main()
