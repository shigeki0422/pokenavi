"""価値ヘッドをスカラー(sigmoid)から two-hot 分類へ差し替える転移。

W1/W2/W3 と方策ヘッドはそのまま引き継ぎ、価値ヘッドだけ作り直す。
初期化は「元のスカラー値を再現する分布」にはできない（表現が違う）ので、
ビン方向に定数＝一様分布から始める。価値の初期予測は 0.5 になるが、
表現層（W1/W2）は学習済みのものを使えるので、ゼロからよりはるかに速く立ち上がる。

env: IN(az_net_np.json) OUT(az_net_twohot.json) VALUE_BINS(32)
"""
import os, sys, json
import numpy as np

D = os.path.dirname(os.path.abspath(__file__))
IN = os.environ.get("IN", os.path.join(D, "az_net_np.json"))
OUT = os.environ.get("OUT", os.path.join(D, "az_net_twohot.json"))
BINS = int(os.environ.get("VALUE_BINS", "32"))


def main():
    d = json.loads(open(IN, encoding="utf-8").read())
    if d.get("vbins"):
        sys.exit(f"{IN} は既に two-hot（vbins={d['vbins']}）")
    top = d.get("hidden3") or d.get("hidden2") or d["hidden"]
    # 一様分布から始める＝価値予測0.5。表現層は学習済みを引き継ぐ。
    d["vbins"] = BINS
    d["Wv"] = np.zeros((BINS, top)).tolist()
    d["bv"] = np.zeros(BINS).tolist()
    json.dump(d, open(OUT, "w", encoding="utf-8"))
    print(f"保存: {OUT}  価値ヘッド {top} → {BINS}ビン（W1/W2/方策は引き継ぎ）", flush=True)


if __name__ == "__main__":
    main()
