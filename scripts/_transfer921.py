"""現行ネット(905次元)を新エンコード(921次元・交代読み特徴16枠追加)へ重み移植。
新16枠は speedmat と disclose の間に挿入。前半(per-side+matrix+speedmat)は同一、
disclose+field は +16 シフト、switch16枠はゼロ初期化（挙動は現行とほぼ同一のまま学習で獲得）。
"""
import numpy as np, copy
from simulator.az_np import PVNetNP
import simulator.features as F

OLD = "az_net_np.json"; NEW = "/tmp/az921_base.json"
old = PVNetNP.load(OLD)
OLD_DIM = old.dim
X = 2 * F._PER_SIDE + F._MATRIX + F._SPEEDMAT     # speedmat末尾＝switchブロック挿入位置
SW = F._SWITCH
NEW_DIM = F.feature_dim()
assert NEW_DIM == OLD_DIM + SW, f"NEW={NEW_DIM} OLD={OLD_DIM} SW={SW}"

new = PVNetNP(NEW_DIM, hidden=old.hidden, hidden2=old.hidden2, hidden3=old.hidden3, seed=0)
new.b1 = old.b1.copy(); new.W2 = old.W2.copy(); new.b2 = old.b2.copy()
new.Wv = old.Wv.copy(); new.bv = float(old.bv); new.Wp = old.Wp.copy(); new.bp = old.bp.copy()
if old.hidden3:
    new.W3 = old.W3.copy(); new.b3 = old.b3.copy()
W1 = np.zeros((old.hidden, NEW_DIM))
W1[:, :X] = old.W1[:, :X]                          # 前半同一
W1[:, X + SW:NEW_DIM] = old.W1[:, X:OLD_DIM]       # disclose+field を+16シフト（switch16枠はゼロ）
new.W1 = W1
new.save(NEW)
print(f"移植完了 → {NEW} (dim {OLD_DIM}→{new.dim}, X={X}, SW={SW})")

# サニティ：新エンコードで評価が走るか
from simulator.simulate import get_loader
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, BattleField
from simulator.features import encode_state
import json, glob
L = get_loader()
p = json.load(open(sorted(glob.glob("f1_cache/*.json"))[0]))["subject_party"]
T = [build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False) for s in p[:3]]
feat = encode_state(BattleSide(T), BattleSide(T), BattleField())
print("encode_state dim:", len(feat), "評価=", round(new.evaluate(feat, [0])[1], 3))
