"""TS側(src/scripts/party-builder/damage.ts)とPython側(scripts/simulator/damage.py)の
ダメージ計算の数値パリティ検証。

TS実装はPython実装の「移植」なので、同じ入力(タイプ/実数値/特性/持ち物/技/乱数)に対して
1ダメージも違わないことを保証する。乖離が出たらどちらかにバグがある。

実行:
    cd scripts && venv/bin/python tests/test_ts_damage_parity.py

内部でTS側を esbuild でバンドルして node 実行し、そのケース(攻守のResolvedBuild・技・乱数・
TS側のダメージ)を受け取って、同じ条件のBattlePokemonをPython側で組み立てて calc_damage する。
天候は「両者が場に出た状態」＝TS側 fieldWeather() の結果を field.weather に設定して再現する
(Python側は entry_ability が同じ天候を張るため、これが実戦の1v1と同じ状態)。
"""
import json
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from simulator.battle import BattleField
from simulator.damage import calc_damage
from simulator.data import DataLoader, MoveData
from simulator.pokemon import BattlePokemon

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
N_CASES = int(os.environ.get("PARITY_N", "400"))
LOADER = DataLoader()


def _dump_ts_cases() -> list:
    out = os.path.join(tempfile.mkdtemp(), "tsdump.mjs")
    subprocess.run(
        ["npx", "esbuild", "scripts/tests/ts_damage_dump.ts", "--bundle",
         "--platform=node", "--format=esm", f"--outfile={out}", "--log-level=warning"],
        cwd=ROOT, check=True,
    )
    env = dict(os.environ, PARITY_N=str(N_CASES))
    res = subprocess.run(["node", out], cwd=ROOT, check=True, capture_output=True, env=env)
    return json.loads(res.stdout)


def _build(rb: dict) -> BattlePokemon:
    """TS側 ResolvedBuild と同じ実数値・タイプ・特性・持ち物を持つ BattlePokemon を組む。"""
    h, a, b, c, d, s = rb["stats"]
    moves = []
    for m in rb["moves"]:
        md = LOADER.get_move(m["n"])
        moves.append(md if md is not None else MoveData(
            name_jp=m["n"], name_en="", type=m["type"], category=m["cat"],
            power=m["power"], accuracy=100, priority=0, pp=10))
    p = BattlePokemon(
        name=rb["sp"], dex=0, type1=rb["t1"], type2=rb["t2"],
        max_hp=h, hp=h, attack=a, defense=b, sp_attack=c, sp_defense=d, speed=s,
        moves=moves, item=rb["item"] or None, ability=rb["ability"],
    )
    return p


def main() -> int:
    cases = _dump_ts_cases()
    fails = []
    for i, cs in enumerate(cases):
        atk = _build(cs["atk"])
        dfn = _build(cs["def"])
        mv = next((m for m in atk.moves if m.name_jp == cs["move"]), None)
        if mv is None:
            continue
        field = BattleField()
        field.weather = cs["weather"]
        if cs["weather"]:
            field.weather_count = 5
        # 連続技は battle.py execute_move のヒットループと同じく1発ずつ計算する
        # (_multi_hit_index はトリプルアクセルの威力20/40/60に使われる)。
        # 防御側の半減きのみは1発目で消費されるため item=None になる挙動もそのまま再現される。
        py_hits = []
        for hi in range(cs["nhits"]):
            atk._multi_hit_index = hi
            d = calc_damage(atk, dfn, mv, field, False, cs["roll"])
            if d <= 0:
                break
            py_hits.append(d)
        ts_hits = cs["hits"]
        if py_hits != ts_hits:
            fails.append((i, cs, py_hits, ts_hits))

    print(f"検証ケース: {len(cases)}件  乖離: {len(fails)}件")
    for i, cs, py, ts in fails[:30]:
        a, d = cs["atk"], cs["def"]
        print(f"  [{i}] {a['sp']}({a['ability']}/{a['item']}) -{cs['move']}-> "
              f"{d['sp']}({d['ability']}/{d['item']}) weather={cs['weather']} "
              f"roll={cs['roll']:.3f}  py={py} ts={ts}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
