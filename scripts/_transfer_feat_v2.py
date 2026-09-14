"""特徴量v1(905次元) のネット重みを v2(965次元) へ転移する。

v2で増える10次元は末尾ではなく各個体ブロックの持ち物カテゴリ位置に挿入されるため、
W1 の列を「同じ意味の特徴が同じ列に来る」ように並べ替え、新規列は重み0で初期化する。
重み0＝初期状態では v1 と数値的に完全一致し、そこから再学習で新特徴を使い始める。

env: IN(az_net_np.json) OUT(az_net_v2.json)
"""
import os, json, subprocess, sys
import numpy as np

D = os.path.dirname(os.path.abspath(__file__))
IN = os.environ.get("IN", os.path.join(D, "az_net_np.json"))
OUT = os.environ.get("OUT", os.path.join(D, "az_net_v2.json"))

_PROBE = (
    "import json,sys;sys.path.insert(0,%r);"
    "import simulator.features as F;"
    "print(json.dumps({'poke':F._POKE,'side':F._PER_SIDE,'nitem':len(F._ITEM_FLAGS),"
    "'dim':F.feature_dim(),'ntypes':len(F.TYPES)}))" % D
)


def _layout(v2):
    env = dict(os.environ, FEAT_V2="1" if v2 else "0")
    out = subprocess.run([sys.executable, "-c", _PROBE], env=env, capture_output=True, text=True)
    if out.returncode: raise RuntimeError(out.stderr[-800:])
    return json.loads(out.stdout)


def index_map(a, b):
    """v1の各入力indexに対応する v2 の index。持ち物ブロック以降が個体ごとに +delta ずれる。"""
    delta = b["nitem"] - a["nitem"]
    item_off = 2 + a["ntypes"] + 5 + 6          # alive,hp + タイプ + 状態 + 実数値
    m = []
    for i in range(a["dim"]):
        j = i
        for s in (0, 1):                         # 2陣営
            base_a = s * a["side"]; base_b = s * b["side"]
            if not (base_a <= i < base_a + 3 * a["poke"]): continue
            k, r = divmod(i - base_a, a["poke"])  # k体目のr番目
            j = base_b + k * b["poke"] + r + (delta if r >= item_off + a["nitem"] else 0)
            break
        else:
            j = i + 2 * (b["side"] - a["side"]) if i >= 2 * a["side"] else i
        if i >= 2 * a["side"]:                   # 陣営ブロックより後ろ（行列/場）
            j = i + 2 * (b["side"] - a["side"])
        elif not any(s * a["side"] <= i < s * a["side"] + 3 * a["poke"] for s in (0, 1)):
            s = 0 if i < a["side"] else 1        # 陣営内の個体ブロック外（能力ランク等）
            j = s * b["side"] + (i - s * a["side"]) + 3 * (b["poke"] - a["poke"])
        m.append(j)
    return m


_ENC_PROBE = os.path.join(D, "_feat_v2_encprobe.py")


def _encode(v2):
    env = dict(os.environ, FEAT_V2="1" if v2 else "0")
    out = subprocess.run([sys.executable, _ENC_PROBE], env=env, capture_output=True, text=True)
    if out.returncode: raise RuntimeError(out.stderr[-800:])
    return json.loads(out.stdout)


def verify(m, b):
    """同一盤面を v1/v2 で符号化し、対応列が完全一致することを確認する。
    転移の正しさは「新規列が0」ではなく「既存列が同じ意味の位置に来ている」ことで決まる。"""
    v1, v2 = _encode(False), _encode(True)
    bad = [i for i in range(len(v1)) if abs(v1[i] - v2[m[i]]) > 1e-12]
    assert not bad, f"符号化が一致しない v1 index {bad[:5]}"
    extra = sorted(set(range(len(v2))) - set(m))
    live = [i for i in extra if v2[i] != 0]
    print(f"検証: v1の{len(v1)}列が全て一致 / v2新規{len(extra)}列のうち{len(live)}列が"
          f"このテスト盤面で実際に立っている（v1では不可視だった持ち物）", flush=True)


def main():
    a, b = _layout(False), _layout(True)
    print(f"v1 dim={a['dim']} poke={a['poke']} item={a['nitem']} / "
          f"v2 dim={b['dim']} poke={b['poke']} item={b['nitem']}", flush=True)
    m = index_map(a, b)
    assert len(m) == a["dim"] and len(set(m)) == a["dim"], "index_map が単射でない"
    assert max(m) < b["dim"], "index_map が v2 次元を超えた"
    verify(m, b)
    d = json.load(open(IN, encoding="utf-8"))
    assert d["dim"] == a["dim"], f"{IN} は {d['dim']}次元で v1({a['dim']}) と一致しない"
    W1 = np.array(d["W1"])                        # (hidden, dim)
    W1b = np.zeros((W1.shape[0], b["dim"]))
    W1b[:, m] = W1                                # 新規列は0のまま＝初期は v1 と完全一致
    d["W1"] = W1b.tolist(); d["dim"] = b["dim"]
    json.dump(d, open(OUT, "w", encoding="utf-8"))
    print(f"保存: {OUT}  W1 {W1.shape} → {W1b.shape}  新規列 {b['dim']-a['dim']}本を0初期化", flush=True)


if __name__ == "__main__":
    main()
