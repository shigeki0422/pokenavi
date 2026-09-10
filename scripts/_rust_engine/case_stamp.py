"""パリティ用ケースの「刻印」ツール。

ケースは Python(正本) が記録した期待値なので、記録後に simulator/**.py の仕様を変えると
エンジンが正しくてもゲートが赤くなる。実際 R4-G1 で、`_effective_speed` の
すなかき/ゆきかき 修正より前のコーパスが残り「エンジンの乖離」に見える事故が起きた。

そこで各ケースのヘッダ行に、ダンプ時点の simulator/** ダイジェスト(sim_hash)を刻む。
ゲート(Rust)は datapack の source_hashes.simulator_py と突き合わせ、古ければそう言う。

  venv/bin/python _rust_engine/case_stamp.py --check              # 全ケースの刻印を照合
  venv/bin/python _rust_engine/case_stamp.py --stamp [files...]   # 刻印を現在値で更新

--stamp は「そのケースでゲートが乖離0だった」ことを確認してから使うこと。
乖離があるまま刻印すると、古さの証拠を消してしまう。
"""
import argparse
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = os.path.join(HERE, "cases")
sys.path.insert(0, HERE)


def sim_hash() -> str:
    from datapack_export import source_hashes
    return source_hashes()["simulator_py"]


def header_of(path: str):
    with open(path, encoding="utf-8") as f:
        return json.loads(f.readline())


def stamp_file(path: str, h: str) -> str:
    """先頭行だけ書き換える。数百MBあるので本文は読まずに流し込む。"""
    hdr = header_of(path)
    if hdr.get("sim_hash") == h:
        return "既に最新"
    old = hdr.get("sim_hash")
    hdr["sim_hash"] = h
    tmp = path + ".stamp"
    with open(path, encoding="utf-8") as src, open(tmp, "w", encoding="utf-8") as dst:
        src.readline()
        dst.write(json.dumps(hdr, ensure_ascii=False, separators=(",", ":")) + "\n")
        while True:
            chunk = src.read(1 << 22)
            if not chunk:
                break
            dst.write(chunk)
    os.replace(tmp, path)
    return "刻印なし→付与" if old is None else f"更新 {old[:8]}→{h[:8]}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--stamp", action="store_true")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    files = a.files or sorted(glob.glob(os.path.join(CASES, "*.jsonl")))
    h = sim_hash()
    print(f"現在の simulator/** : {h}")
    stale = []
    for p in files:
        got = header_of(p).get("sim_hash")
        mark = "OK" if got == h else ("刻印なし" if got is None else f"古い({got[:8]})")
        if got != h:
            stale.append(p)
        if a.stamp:
            print(f"  {os.path.basename(p):22s} {mark:16s} -> {stamp_file(p, h)}")
        elif a.check or True:
            print(f"  {os.path.basename(p):22s} {mark}")
    if not a.stamp and stale:
        print(f"\n古い/未刻印: {len(stale)}件。ゲートを回して乖離0を確認してから --stamp すること。")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
