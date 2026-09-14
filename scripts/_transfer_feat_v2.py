"""特徴量の次元拡張にともなうネット重みの転移。

v1(905) → v2(965) → v3(1037) と段階的に増えるが、いずれも新規列は個体ブロックの内部に
挿入される（末尾ではない）ので、W1 の列を並べ替えて「同じ意味の特徴が同じ列」に揃える。

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
    "'dim':F.feature_dim(),'ntypes':len(F.TYPES),'nm3':F._N_M3,'nabil':F._N_ABIL_CATS}))" % D
)


def _layout(v2, v3=None):
    """v2/v3 の ON/OFF を指定してレイアウトを取る。v3 省略時は v2 と同じ値にする。"""
    if v3 is None:
        v3 = v2
    env = dict(os.environ, FEAT_V2="1" if v2 else "0", FEAT_V3="1" if v3 else "0")
    out = subprocess.run([sys.executable, "-c", _PROBE], env=env, capture_output=True, text=True)
    if out.returncode: raise RuntimeError(out.stderr[-800:])
    return json.loads(out.stdout)


def index_map(a, b):
    """aの各入力indexに対応する b の index。個体ブロック内で2箇所ずれる:
      持ち物カテゴリ（v2で 8→18）と、技特徴の末尾（v3で +12）。
    どちらも個体ブロックの内部なので、単純な末尾追加では揃わない。"""
    d_item = b["nitem"] - a["nitem"]
    d_m3 = b["nm3"] - a["nm3"]
    item_off = 2 + a["ntypes"] + 5 + 6          # alive,hp + タイプ + 状態 + 実数値
    # 技特徴（タイプ網羅18＋クラス10＋v3の12）の直後 = 揮発ブロックの手前
    m3_end = (item_off + a["nitem"] + a["nabil"] + 1 + a["ntypes"] + 10 + a["nm3"])
    m = []
    for i in range(a["dim"]):
        j = i
        for s in (0, 1):                         # 2陣営
            base_a = s * a["side"]; base_b = s * b["side"]
            if not (base_a <= i < base_a + 3 * a["poke"]): continue
            k, r = divmod(i - base_a, a["poke"])  # k体目のr番目
            sh = 0
            if r >= item_off + a["nitem"]:
                sh += d_item
            if r >= m3_end:
                sh += d_m3
            j = base_b + k * b["poke"] + r + sh
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


def _encode(v2, v3=None):
    if v3 is None:
        v3 = v2
    env = dict(os.environ, FEAT_V2="1" if v2 else "0", FEAT_V3="1" if v3 else "0")
    out = subprocess.run([sys.executable, _ENC_PROBE], env=env, capture_output=True, text=True)
    if out.returncode: raise RuntimeError(out.stderr[-800:])
    return json.loads(out.stdout)


def verify(m, b, src):
    """同一盤面を v1/v2 で符号化し、対応列が完全一致することを確認する。
    転移の正しさは「新規列が0」ではなく「既存列が同じ意味の位置に来ている」ことで決まる。"""
    v1, v2 = _encode(*src), _encode(True, True)
    bad = [i for i in range(len(v1)) if abs(v1[i] - v2[m[i]]) > 1e-12]
    assert not bad, f"符号化が一致しない v1 index {bad[:5]}"
    extra = sorted(set(range(len(v2))) - set(m))
    live = [i for i in extra if v2[i] != 0]
    print(f"検証: v1の{len(v1)}列が全て一致 / v2新規{len(extra)}列のうち{len(live)}列が"
          f"このテスト盤面で実際に立っている（v1では不可視だった持ち物）", flush=True)


def main():
    # IN の次元からどのレイアウトかを判定する（905→1037 / 965→1037 の両方に対応）
    _d = json.load(open(IN, encoding="utf-8"))["dim"]
    src = (False, False) if _d == 905 else (True, False)
    a = _layout(*src)
    b = _layout(True, True)
    print(f"v1 dim={a['dim']} poke={a['poke']} item={a['nitem']} / "
          f"v2 dim={b['dim']} poke={b['poke']} item={b['nitem']}", flush=True)
    m = index_map(a, b)
    assert len(m) == a["dim"] and len(set(m)) == a["dim"], "index_map が単射でない"
    assert max(m) < b["dim"], "index_map が v2 次元を超えた"
    verify(m, b, src)
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
